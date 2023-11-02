import socket
# number of functions in any module or object or anythin
# print(dir(socket)) #directory
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #by default tcp protocol will be used if no argument is passes
#                ip_address ,   protocol(udp)
# finally s is having capability to create UDP socket
# target system address
target_ip="127.0.0.1"
target_port=9999
final_target=(target_ip,target_port)
while True:
    # Taking input from user
    msg=input("Please enter your message:")
    if msg!="":
        # Since python3 is supporting minimum encoding
        new_msg=msg.encode('ascii')
        # finally lets send data
        s.sendto(new_msg,final_target)
    else:
        break
