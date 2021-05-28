# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:25:05 2021

@author: User
"""

from defines import *
import subprocess
from subprocess import check_output
from auxillary import array_to_byte



class Device:
    
    def reset_states(self):
        self.input_state  = [0xFF]*inputs
        self.output_state = [0xFF]*outputs
        self.state = STATE_UNKNOWN;
    
    def __init__(self, id, inputs, outputs):
        self.device_id = id
        self.num_inputs = inputs
        self.num_outputs =outputs
        self.reset_states(output_state)
    
   
    def tick(self):
        result = True;
        self.i2c_set(array_to_byte)
        sleep(TICK_DELAY)
        self.i2c_get()
        result = self.input_state == self.input_state
        if(result):
            self.state = DEVICE_STATE_OK
        else:
            self.state = DEVICE_STATE_FAIL
        return  result
    
    def fill_states(self,states):
        for i in range (0,VERSION_1_INPUTS):
            if( (1 << i) & states[0]):
                self.output_state[i] = 1
            else:
                self.output_state[i] = 0
                
            if( (1 << i) & states[1]):
                self.input_state[i] = 1
            else:
                self.input_state[i] = 0
    
    def i2c_get(self):
        states = [0]*2
        responce = check_output(CMD_GET_OUTPUT.split()).decode()
        states[0] = int(responce, 16)
        responce = check_output(CMD_GET_INPUT.split()).decode()
        states[1] = int(responce, 16)
        
        self.reset_states()
        self.fill_states(states);
                       
        return states
    
    def i2c_set(self, state):
        command = CMD_SET_OUTPUT+str(state)
        print(f"Executing {command}")
        responce = check_output(command.split())
        
    def save_state(self, filename):
        print("Saving state")
    
    def load_state(self, filename):
        print("Loading state")
        
        
        
    def load_device():
        print("loading device")
        

        
        
