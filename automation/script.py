import paramiko
host = "10.122.151.220"
username = "ubuntuserver"
password = "text123"
commands = [
    
    "lscpu",
    "uname -a",
    "hostnamectl",
    "df -h"
]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("connecting .....")
client.connect(hostname=host,username=username,password=password)

for cmd in commands:
    print(f'\nRunning {cmd}')
    stdin,stdout,stderr = client.exec_command(cmd, get_pty=True)

    # stdin.write(password + "\n")
    stdin.flush()

    print(stdout.read().decode())
    print(stderr.read().decode())
client.close()
print('\nDone')