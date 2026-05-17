import paramiko
import time


# CLUSTER CONFIG

CLUSTER_IP = "172.31.7.231"

CLUSTER_USERNAME = "admin"
CLUSTER_PASSWORD = "clusterpassword"


# SP/BMC CONFIG

SP_USERNAME = "admin"
SP_PASSWORD = "sppassword"


# COMMANDS

HALT_CMD = (
    "system node halt "
    "-node BDB_NAS-01,BDB_NAS-02 "
    "-skip-lif-migration-before-shutdown true "
    "-ignore-quorum-warnings true "
    "-inhibit-takeover true "
    "-ignore-strict-sync-warnings true"
)

AUTOSUPPORT_CMD = (
    'system node autosupport invoke '
    '-node * -type all '
    '-message "MAINT=2h Planned Maintenance"'
)


# GENERIC SSH CONNECTION

def create_ssh_connection(host, username, password):

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )

    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        timeout=10
    )

    return ssh


# SEND COMMAND

def send(shell, command, wait=3):

    print(f"\n>>> {command}")

    shell.send(command + "\n")

    time.sleep(wait)

    output = shell.recv(65535).decode()

    print(output)

    return output


# CONNECT TO CLUSTER

print(f"\nConnecting to cluster {CLUSTER_IP}...")

cluster_ssh = create_ssh_connection(
    CLUSTER_IP,
    CLUSTER_USERNAME,
    CLUSTER_PASSWORD
)

cluster_shell = cluster_ssh.invoke_shell()

time.sleep(2)

cluster_shell.recv(65535)

print("\nConnected to cluster.")


# HEALTH CHECKS

cluster_output = send(cluster_shell, "cluster show")

if (
    "health false" in cluster_output.lower()
    or
    "eligibility false" in cluster_output.lower()
):

    print("\nERROR: Cluster is not healthy.")

    cluster_ssh.close()

    exit()

print("\nCluster health validation passed.")

send(cluster_shell, "storage failover show")

send(cluster_shell, "system health alert show")

send(cluster_shell, "job show")



# ENABLE AUTOSUPPORT MAINTENANCE MODE


print("\nEnabling AutoSupport maintenance mode...")

send(cluster_shell, AUTOSUPPORT_CMD)


# GET SP/BMC INFORMATION

print("\nRetrieving SP/BMC addresses...")

sp_output = send(
    cluster_shell,
    "system service-processor show -node * -fields address"
)


# PARSE NODE NAME + SP IP

sp_data = {}

lines = sp_output.splitlines()

for line in lines:

    parts = line.split()

    if len(parts) >= 2:

        node_name = parts[0]

        ip_address = parts[-1]

        if "." in ip_address:

            sp_data[node_name] = ip_address

print("*"*50)
print("\nDetected SP Information:")

for node_name, sp_ip in sp_data.items():
    print("-"*50)
    print(f"{node_name} -> {sp_ip}")


# FINAL CONFIRMATION

confirm = input(
    "\nProceed with FULL CHASSIS SHUTDOWN? (yes/no): "
)

if confirm.lower() != "yes":

    print("Operation cancelled.")

    cluster_ssh.close()

    exit()


# SHUTDOWN CLUSTER

print("-"*50)
print("\nSending halt command...")

cluster_shell.send(HALT_CMD + "\n")

time.sleep(2)

# Auto-confirm halt prompt
cluster_shell.send("y\n")

time.sleep(5)

try:

    output = cluster_shell.recv(65535).decode()
    print("="*50)
    print(output)
    print("="*50)

except:
    pass

print("\nCluster shutdown initiated.")

cluster_ssh.close()


# WAIT BEFORE SP CONNECTION

print("="*50)
print("\nWaiting 60 seconds before connecting to SPs...")
print("="*50)
time.sleep(60)


# CONNECT TO EACH SP

for node_name, sp_ip in sp_data.items():

    print(
        f"\nConnecting to "
        f"{node_name} SP: {sp_ip}"
    )

    try:

        sp_ssh = create_ssh_connection(
            sp_ip,
            SP_USERNAME,
            SP_PASSWORD
        )

        sp_shell = sp_ssh.invoke_shell()

        time.sleep(2)

        sp_shell.recv(65535)

        # Open SP console
        sp_shell.send("system console\n")

        print(
            f"\nMonitoring console output "
            f"for {node_name}..."
        )

        loader_detected = False

        timeout = time.time() + 600

        while time.time() < timeout:

            if sp_shell.recv_ready():

                output = sp_shell.recv(
                    65535
                ).decode()

                print(output)

                # Detect LOADER prompt
                if (
                    "LOADER-A>" in output
                    or
                    "LOADER-B>" in output
                ):

                    print(
                        f"\nSUCCESS: "
                        f"{node_name} reached "
                        f"LOADER prompt"
                    )

                    loader_detected = True

                    break

            time.sleep(2)

        if not loader_detected:

            print(
                f"\nWARNING: "
                f"LOADER prompt not detected "
                f"on {node_name}"
            )

        sp_ssh.close()

    except Exception as e:

        print(
            f"\nERROR: "
            f"{node_name} ({sp_ip}) -> {e}"
        )


# COMPLETE

print("="*50)
print("\nMaintenance shutdown verification completed.")
print("="*50)