import requests
from time import sleep
import os, sys
import paramiko
from paramiko import SSHClient
from tqdm import tqdm
from getpass import getpass

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)
os.system('clear')

red_color = "\033[1;31m"
info_color = "\033[1;33m"
detect_color = "\033[1;34m"
end_banner_color = "\33[00m"


print (end_banner_color + '''
==============================================
[developer] => FaLaH - 0xfff0800 [developer_email] => flaaah777@gmail.com ) 
[developer_snapchat] => flaah999
==============================================

''')

falah = input (end_banner_color + '''
1 - Browse stored application files
2 - Install Python dependencies when there is an error
-> ''')
os.system('clear')


if falah == "2":

  print (end_banner_color+"""

➜  (Main) ✗ pip install tqdm
➜  (Main) ✗ pip install paramiko"


─────────────────────────────────────────────────────────────────
│ ver/root/0x.py                                              │
├──────────┼─────────────────────────────────────────────────────┤
│ name     │ wep                                                 │
├──────────┼─────────────────────────────────────────────────────┤
│ OpenSSH  │ https://www.openssh.com                             │
│ tqdm     │ https://pypi.org/project/tqdm                       │
│ requests │ https://pypi.org/project/requests                   │
│ paramiko │ https://pypi.org/project/paramiko                   │
└──────────┴─────────────────────────────────────────────────────┘
""")
  os.system('pip3 install tqdm')
  os.system('pip3 install requests')
  os.system('pip3 install paramiko')
  os.system('pip3 install ssh')
  exit()
if falah == "1":

    print(red_color+'''
     Connect your phone to the same Wi-Fi network as the computer
     The default password root ( alpine ) -> If changed, write it in the required field
         
         - password default : alpine
         - ip iphone : Go to the phone's Wi-Fi and type ip
    
    ''')
    falah3 = input (end_banner_color+'ip Iphone -> ')
    falah2 = getpass("password root -> ")
    if len(falah2) > 0:
        print (' ')
        ketik (
            "\033[1;33m Please jailbreak the phone to access all the root features....\033[1;33m")
        sleep (0.5)

    else:
        print('')
        print("It cannot be left blank")
    print('==============================================')
    RPORT = 22
    password = ""+falah2+""

    ssh = paramiko.SSHClient ()
    ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy ())
    print ("Initiating SSH connection")
    while True:
        try:
            ssh.connect (''+falah3+'', username='root', password=password)
            break
        except:
            print ("Failed, retrying")
            continue
    print ("Connection established")
    ketik (
            "\033[1;33m ok....\033[1;33m")
    stdin, stdout, stderr = ssh.exec_command('python -m 0x', get_pty=True)
    for line in iter(stdout.readline, ""):
        print(line, end="")
        print(info_color+"")
        for i in tqdm (range (5)):
            sleep(0)





