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

HOST                 = '10.22.0.15'  # The server's hostname or IP address
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
CMD_PULSE            = "PULSE"
CMD_AUTHORIZE        = "AUTH"

CMD_GET_OUTPUT       = "/usr/sbin/i2cget -y 1 0x21"
CMD_GET_INPUT        = "/usr/sbin/i2cget -y 1 0x24"
CMD_SET_OUTPUT       = "/usr/sbin/i2cset -y 1 0x21 "
CMD_SWITCH_OFF       =  "/usr/sbin/i2cset -y 1 0x21 0xFF "

MOBILE_APN = "3g.ge"

DEVICE_ID = 0x0 #read device id from text file

TICK_DELAY = 0.1
PULSE_DELAY = 1.0

#DEVICE STATES--------------
DEVICE_STATE_UNKNOWN = 0xFF
DEVICE_STATE_OK = 0
DEVICE_STATE_FAIL = 0
#---------------------------

RESPONCE_OK ="OK"
RESPONCE_ERR = "ERR"

#GPRS-----------------------
GPRS_APN ="3g.ge"
GPRS_SERVER_IP = "81.16.245.47"
GPRS_SERVER_PORT = 10004
#----------------------------