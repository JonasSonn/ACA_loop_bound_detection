# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:22:21 2018

@author: moth
"""

class AbstractState:


    _i_stack = []
    _recorder = (0)
    _program_point = 0
    _abstract_store = {}
    def __init__(self, i_stack_, recorder_, program_point_, abstract_store_):
        self._i_stack = i_stack_
        self._recorder = recorder_
        self._program_point = program_point_
        self._abstract_store = abstract_store_

    def perform_step(self):
        
        self._i_stack = 1
        
        return self
    
    def new_scope():
        self.recorder = 1