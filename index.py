import os
import subprocess

os.system("netstat -nr | grep default | head -1")
ip = input(("Please insert your ip: "))
# user = input(("Please insert your user: "))
# passw = input(("Please insert your pass: "))
open_software = "telnet "+ip
os.system(open_software)

### stopped here
## missing login and commands
# may add options of what commands should be executed
time.sleep(5)
os.system(user)
os.system(passw)

#subprocess.run("netstat -nr")
