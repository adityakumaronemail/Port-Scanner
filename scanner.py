import sys
import socket
from datetime import datetime

if len(sys.argv) == 1:
    print("\n")
    print("-"*50)
    print("Welcome to Port Scanner!")
    print("To learn how to use the tool, type 'scanner.py help'")
    print("-"*50)
    print("\n")
    sys.exit()

if len(sys.argv) == 2:
    if sys.argv[1]=="help":
        print("\n")
        print("-"*50)
        print("Run the command as : 'scanner.py ip_address port_to_begin port_to_end'")
        print("Example : 'scanner.py 192.168.0.1 70 90'")
        print("The tool will scan the ip address 192.168.0.1 for open ports from port 70 to port 90")
        print("-"*50)
        print("\n")
        sys.exit()

    if sys.argv[1]=="about":
        print("\n")
        print("-"*50)
        print("Welcome to Network Port Scanner!")
        print("Made by Aditya Kumar.")
        print("github.com/ak8476")
        print("-"*50)
        print("\n")
        sys.exit()

if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    lim1=int(sys.argv[2])
    lim2=int(sys.argv[3])
    print("-"*50)
    print("Scanning from port:")
    print(lim1)
    print("Scanning to port:")
    print(lim2)
    print("-"*50)

else:
    print ("Invalid amount of arguments. Run the 'help' command for help.")
    sys.exit()
    
print("\n")
print("-"*50)
print("Scanning Target : "+target)
print("Time started : "+str(datetime.now()))
print("-"*50)
print("\n")

try:
    for port in range(lim1,lim2+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print ("Checking port {}".format(port))
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print ("\nExiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could't connect to server.")
    sys.exit()
