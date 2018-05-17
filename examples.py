# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:46:49 2018

@author: moth
"""

import abstractstate as abst
import abstractexecution as abex


def example_get_bound(expression_, condition_):
        
        
        i_stack = (0)
        recorder = 1
        program_point = 0;
        abstract_store = list(range(1, 5000))     
        
        
        state = abst.AbstractState(i_stack, recorder, program_point, abstract_store)
        flag = True
        #i = 1
        while(len(state._abstract_store)):
            if(flag):
                flag = False
                state = abex.abstract_execution_for_simple_loop(state, expression_, condition_, True)
            else: 
                state = abex.abstract_execution_for_simple_loop(state, expression_, condition_, False)
            #print(i)
            #i += 1
        
        max_bound = state._recorder
        
        return max_bound
        