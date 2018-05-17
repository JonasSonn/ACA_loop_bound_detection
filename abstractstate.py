# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:22:21 2018

@author: moth
"""

class AbstractState:
   
    _recorder = (0)
    _abstract_store = {}
    def __init__(self, recorder_, abstract_store_):
        self._recorder = recorder_
        self._abstract_store = abstract_store_

    def perform_step(self):
        
        self._i_stack = 1
        
        return self
    
    def new_scope():
        self.recorder = 1