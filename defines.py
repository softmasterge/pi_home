# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:35:26 2021

@author: User
"""

STATE_UNKNOWN = 0xff
STATE_ON = 1
SATE_OFF = 0


VERSION_1_INPUTS =  8
VERSION_1_OUTPUTS = 8

HOST                 = '10.22.0.62'  # The server's hostname or IP address
PORT                 = 1234        # The port used by the server
SOCKET_TIMEOUT       = 30
SOCKET_BUFFER_SIZE   = 256
NEW_LINE             = '#'
MAX_RECV_LEN         = 128
SLEEP_DELAY          = 1
GREETING_MESSAGE     = "SoftMaster Home Device 01"
MAX_LAN_RETRIES      = 5
CMD_GET              = "GET"
CMD_SET              = "SET"
CMD_AUTHORIZE        = "AUTH"

CMD_GET_OUTPUT       = "i2cget -y 1 0x21"
CMD_GET_INPUT        = "i2cget -y 1 0x24"
CMD_SET_OUTPUT       = "i2cset -y 1 0x21 "



DEVICE_ID = 0x0 #read device id from text file

TICK_DELAY = 0.1

#DEVICE STATES--------------
DEVICE_STATE_UNKNOWN = 0xFF
DEVICE_STATE_OK = 0
DEVICE_STATE_FAIL = 0
#---------------------------

RESPONCE_OK ="OK"
RESPONCE_ERR = "ERR"