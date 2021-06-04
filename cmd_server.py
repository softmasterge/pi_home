#!/usr/bin/env python3

import socket
import time
import logging
import sys
import subprocess
from subprocess import check_output
from defines import  CMD_GET,CMD_SET,SOCKET_TIMEOUT,HOST,PORT, GREETING_MESSAGE
from defines import  MAX_RECV_LEN, MAX_LAN_RETRIES,SLEEP_DELAY, NEW_LINE, SOCKET_BUFFER_SIZE
from device import Device
from defines import *


devices = []
current_device = Device(0xAEF1, VERSION_1_INPUTS, VERSION_1_OUTPUTS)

def execute_cmd(cmd):
      print("Executing ")
      print(cmd)
      print('\n')

def process_command(cmd):
    if   cmd == CMD_GET:
        execute_cmd(cmd)
    elif cmd == CMD_SET:
        execute_cmd(cmd)
    else:
        print("Unexpected command")


def init_server(file):
    current_device = Device(0xAEF1, VERSION_1_INPUTS, VERSION_1_OUTPUTS)
    devices.append(current_device)


def start_server():
    recv_buffer = bytearray()

    while True:
        print("Accessing LAN\n")
        lan_retries = 0;
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.settimeout(SOCKET_TIMEOUT)
                    logging.info(f"Connecting to {HOST}:{PORT}")
                    s.connect((HOST, PORT))
                    s.sendall(bytes(GREETING_MESSAGE, 'utf-8'))
                    s.settimeout(SOCKET_TIMEOUT)
                    while True:
                        recv_buffer+=s.recv(SOCKET_BUFFER_SIZE)
                        buffer_length = len(recv_buffer)
                        print("RCV>")
                        print(recv_buffer.decode())
                        if len(recv_buffer) > MAX_RECV_LEN:
                            break;
                        else:
                            if chr(recv_buffer[buffer_length - 1]) == NEW_LINE:
                                print ("command received\n")
                                print(str(recv_buffer))
                                recv_buffer = recv_buffer[:-1]
                                command_string = recv_buffer.decode()
                                tokens = command_string.split()
                                if tokens[0] == CMD_AUTHORIZE:
                                    response = ' '.join([CMD_AUTHORIZE, current_device.device_id])
                                    print(response)
                                    s.sendall(bytes(response, 'utf-8'));
                                    recv_buffer.clear()
                                elif tokens[0] == CMD_SET:
                                    if len(tokens) > 1:
                                        logging.info(f"CMD_SET {tokens[1]}")
                                        command_string = f"{CMD_SET_OUTPUT} {tokens[1]}"
                                        logging.info(f"Executing> {command_string}")
                                        response = check_output(command_string, shell=True).decode()
                                        if len(response) == 0:
                                            s.send(b'OK')
                                        else:
                                            s.sendall(bytes(response, 'utf-8'));

                                    else:
                                        logging.error("CMD_SET arguments not found")
                                    recv_buffer.clear()

                                elif tokens[0] == CMD_GET:
                                    logging.info("GET")

                                    response = check_output(CMD_GET_OUTPUT, shell=True).decode().rstrip()
                                    response2 = check_output(CMD_GET_INPUT, shell=True).decode().rstrip()
                                    response = ' '.join([RESPONCE_OK, response, response2])
                                    s.sendall(bytes(response, 'utf-8'));
                                    recv_buffer.clear()
                                elif tokens[0] == CMD_PULSE:

                                    if len(tokens) > 1:

                                        response = check_output( CMD_GET_INPUT, shell=True).decode().rstrip()
                                        state = int(response, 16);
                                        index = int(tokens[1])
                                        output = str((~(1 << index))&0xFF);
                                        logging.info(f"PULSE {output}")
                                        switch_cmd = f"{CMD_SET_OUTPUT} {output}"
                                        logging.info(f"Executing> {switch_cmd}")
                                        response = check_output(switch_cmd, shell=True).decode()
                                        time.sleep(PULSE_DELAY)
                                        response = check_output(CMD_SWITCH_OFF, shell=True).decode()

                                    else:
                                        logging.error("CMD_PULSE arguments not found")

                                else:
                                    logging.warning(f"unknown command {tokens[0]}")
                                    recv_buffer.clear()
                            else:
                                print ("chunk received\n")
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    if(lan_retries >= MAX_LAN_RETRIES):
                        break;
                    recv_buffer.clear()
                    lan_retries = lan_retries + 1
                    print(f"sleeping for a while {lan_retries}");
                    time.sleep(SLEEP_DELAY)
        print("Accessing GPRS")
    print('Loop exit')

init_server("test")
start_server()