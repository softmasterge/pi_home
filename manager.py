# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:43:50 2021

@author: User
"""
from device import Device
import logging


class Manager:
    
    def __init__(self, file):
        
        self.devices = []
        self.file = file;
        
    
    def load(self, file):
        logging.info("loading file");
        
    def run(self):
        logging.info("starting manager loop")
        while True:
            for d in self.devices:
                d.tick();