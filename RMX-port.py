import socket
import sys
from time import *
from datetime import datetime
#############################################
print ("====================================> welcome <====================================")
print("######                                                                      #######")
print("#######                                                                    ########")
print("########                                                                  #########")
print("•")
print("•")
print("•")
#############################################
ip = input("======> Enter your ip <======: ")
t1=datetime.now()
print ("Scanning.. %s please with.."%ip)
sleep(1)
#############################################
try:
	for port in range(1,6653):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if (s.connect_ex((ip,port))==0):
			try:
				serv=socket.getservbyport(port)
			except socket.error:
				serv="Unknown Service"
			print("port %s open service: %s "%(port,serv))
		t2=datetime.now()
		t3=t2-t1
	print("Scanning Completed on%s"%t3)
except KeyboardInterrupt:
		print("see your son...&")
		
