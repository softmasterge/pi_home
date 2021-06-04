from blinker import *
from defines import *




class GPRS:
    def __init__(self):
        self.sequence_index = 0
        self.current_retries = 0;
        self.commands = []
        self.send_byte = 0x1a;

        commands.append(["AT+CPIN?", "+CPIN: READY", "", "0,1"])
        commands.append(["AT+CREG?","+CREG: 0,1", "", "OK"])
        commands.append(["AT+CGATT?", "+CGATT: 1", "", "OK"])
        commands.append([f"AT+CSTT=\"{GPRS_APN}\"","OK"])
        commands.append([f"AT + CIPSTART =\"TCP\", \"{GPRS_SERVER_IP}\", \"{GPRS_SERVER_PORT}\"", "OK", "CONNECT OK"])
        commands.append(["AT+CIICR", ">"])

