#Receiver ip--IP for every system(either internet connected or not): 127.0.0.1
# change recv and sender ip to 127.0.0.1
# file handling-- save msgs to file

import  socket 
import  time 
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="127.0.0.1"
# -- 52.2.116.225 -- jecrc.delvex.io 
my_port=9999
my_address=(my_ip,my_port)
# let me start above defined address 
s.bind(my_address)
#  socket --  IP:PORT  --  52.2.116.225:9999 
#   facebook ---          www.facebook.com:443 
# --                       157.240.239.35:443 
# port -- 0-65535
# lets recv text data
while True :
    data=s.recvfrom(100)
    # only filetring message 
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    # print(data[1])
    # print(new_data)
    # print(final_msg)
    # implement file handing print 
    time.sleep(2)
    if not os.path.exists(f"E:\Python-jecrc\RCE Project\Messages\{data[1][0]}"):
        os.mkdir(f"E:\Python-jecrc\RCE Project\Messages\{data[1][0]}")
    
    path=os.path.join(f"E:\Python-jecrc\RCE Project\Messages\{data[1][0]}","msg.txt")
    file=open(path,"a")
    file.write(f"{final_msg}\n")
    file.close()    
    # print(os.getcwd())
