import sys,os,string,random,time


print("[\033[1;31;40mPassword Generator\033[1;36;40m]\n")
length = 13
chars = string.ascii_letters + string.digits + "!@$%^&*()" 
random.seed = (os.urandom(1024))

count = 0
while count != 5:
  print(''.join(random.choice(chars) for i in range(length)))
  time.sleep(1)
  count = count + 1
		  
if count == 5:
    print("{0} Passwords Generated".format(count))
input("Press Enter To Continue...")
sys.exit()
