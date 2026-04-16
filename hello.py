import subprocess

items_is_cart: int = 6
amount: int = 4000

msg = 'Yuo have {} items in cart and total amount is Rs. {}.'.format(items_is_cart*2,amount)

print(msg.upper(),msg.count('ITEMS'))

print(msg.swapcase() + " "+ 'hello this is the new section')
msg += ' hello this is the new section                    '
print(msg.replace('e','a'))

print(msg.strip().replace('a','e'))

command = "powershell -command \"Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, Speed, @{Name='Capacity(GB)'; Expression={[math]::Round($_.Capacity / 1GB, 2)}}\""

print(subprocess.check_output(command, shell=True).decode())

