import time,os
sex = '\033[0;31m[\033[0;32m•\033[0;31m]\033[0;37m'
logo = (f"""

\033[0;37md8b   db d888888b d8b   db    d88b  .d8b.  
\033[0;37m888o  88   88'   888o  88    8P' d8' `8b 
\033[0;37m88V8o 88    88    88V8o 88     88  88ooo88 
\033[0;37m88 V8o88    88    88 V8o88     88  88~~~88 
\033[0;37m88  V888   .88.   88  V888 db. 88  88   88 
\033[0;37mVP   V8P Y888888P VP   V8P Y8888P  YP   YP 
\033[0;32m┌────────────────────────────────────────┐
\033[0;31m│ {sex}\033[0;37mAUTHOR       : \033[38;5;46mNINJA-XD             \033[0;31m│
\033[0;31m│ {sex}\033[0;37mGITHUB       : \033[38;5;46mX-NINJA-XD           \033[0;31m│
\033[0;31m│ {sex}\033[0;37mVERSION      : \033[38;5;46m0.0.1                \033[0;31m│
\033[0;31m│ {sex}\033[0;37mTOOL         : \033[38;5;46mSET-UP               \033[0;31m│       
\033[0;31m│ {sex}\033[0;37mSTUTUS       : \033[38;5;46mFREE                 \033[0;31m│       
\033[0;32m└────────────────────────────────────────┘
""")
print(logo)
print('  \033[0;37m©MAHDI HASAN')
input('\033[38;5;46m Do you Want Install Basic Command ; ')
os.system("pkg update -y")
os.system("pkg upgrade -y")
time.sleep(0.5)
print(f"{sex} -INSTALLING GIT....")
os.system("pkg install git -y")
print(f"{sex} -INSTALLING wget ")
os.system("pkg install wget -y")
print(f"{sex} -INSTALLING python ")
os.system("pkg install python -y")
print(f"{sex} -INSTALLING PYTHON 2")
os.system("pkg install python2 -y")
print(f"{sex} -INSTALLING requests")
os.system("pip install requests")
print(f"{sex} -INSTALLING Bs4")
os.system("pip install bs4")
print(f"{sex} -INSTALLING rich")
os.system("pip install rich")
print(f"{sex} -INSTALLING TIME")
os.system("pip install time")
print(f"{sex} - SET-UP DONE")
os.system("exit")
