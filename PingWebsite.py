import sys,os,time

hostname = input("Website >> ") 
print("Loading...")
response = os.system("ping -c 1 " + hostname)
if response == 0:
    time.sleep(1)
    print("\n")
    print("\033[1;35;40mThe Website,[\033\033[0;37;46m",hostname,'\033[1;35;40m] is \033[1;32;40mup!\033')
    input("\033[1;36;40mPress Enter To Continue...")
    sys.exit()
        
else:
    time.sleep(1)
    print("\n")
    print("\033[1;35;40mThe Website,[\033\033[0;37;46m",hostname,'\033[1;35;40m] is\033\033[1;31;40m down!\033')
    input("\033[1;36;40mPress Enter To Continue...")
    sys.exit()
  
