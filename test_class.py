# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:21:43 2018

@author: moth
"""
import abstractstate as abst
import abstractexecution as abex
import get_loop as gl

# content of test_sample.py
def test_test() :
    assert 3 == 3
    

def test_ae_simple_loop_simple_update():
    
    i_stack = (0)
    recorder = 1
    program_point = 0;
    abstract_store = [0,1,2,3,4]
    
    init_state = abst.AbstractState(i_stack, recorder, program_point, abstract_store)
  
    
    expression = lambda x: x+2
    condition = lambda x: x<10
    
    print("state 1")
    state_1 = abex.abstract_execution_for_simple_loop(init_state, expression, condition, True )
    assert len(state_1._abstract_store) == 5

    assert state_1._abstract_store[0] == 2
    assert state_1._abstract_store[1] == 3
    assert state_1._abstract_store[2] == 4
    assert state_1._abstract_store[3] == 5
    assert state_1._abstract_store[4] == 6
    
    assert state_1._recorder == 1;
    
    
    print("state 2")
    state_2 = abex.abstract_execution_for_simple_loop(state_1, expression, condition, False )
    
    assert len(state_2._abstract_store) == 5
    
    assert state_2._abstract_store[0] == 4
    assert state_2._abstract_store[1] == 5
    assert state_2._abstract_store[2] == 6
    assert state_2._abstract_store[3] == 7
    assert state_2._abstract_store[4] == 8
    
    assert state_1._recorder == 2;
    
    print("state 3")
    state_3 = abex.abstract_execution_for_simple_loop(state_2, expression, condition, False )
    assert len(state_3._abstract_store) == 4

    assert state_3._abstract_store[0] == 6
    assert state_3._abstract_store[1] == 7
    assert state_3._abstract_store[2] == 8
    assert state_3._abstract_store[3] == 9
    
    assert state_1._recorder == 3;
    
    print("state 4")
    state_4 = abex.abstract_execution_for_simple_loop(state_3, expression, condition, False )
    assert len(state_4._abstract_store) == 2

    assert state_4._abstract_store[0] == 8
    assert state_4._abstract_store[1] == 9

    
    assert state_1._recorder == 4;
    
    print("state 5")
    state_5 = abex.abstract_execution_for_simple_loop(state_4, expression, condition, False )
    assert len(state_4._abstract_store) == 0
   
    assert state_1._recorder == 5;
    
    
def test_ae_auto_update():
    
    
    i_stack = (0)
    recorder = 1
    program_point = 0;
    abstract_store = [0,1,2,3,4,6]
    
    expression = lambda x: x+2
    condition = lambda x: x<10
    
    state = abst.AbstractState(i_stack, recorder, program_point, abstract_store)
    flag = True
    i = 1
    while(len(state._abstract_store)):
        if(flag):
            flag = False
            state = abex.abstract_execution_for_simple_loop(state, expression, condition, True)
        else: 
            state = abex.abstract_execution_for_simple_loop(state, expression, condition, False)
        print(i)
        i += 1
    

    assert len(state._abstract_store) == 0
    assert state._recorder == 5
    

def test_expression_parsing_for_loop():
    
    meat = gl.get_simple_for_loop("cloops/assert_forloop.c")
    
    #print (meat)
    #expression = lambda x: x + 1
    #condition = lambda x: x>10000
    
    expression_str = "lambda {0}: {1}".format(meat[0], meat[2])
    condition_str = "lambda {0}: {1}".format(meat[0], meat[1])
    
    #print("exp: {0}, cond {1}".format(expression_str, condition_str))


    expression = eval(expression_str)
    condition = eval(condition_str)
    
    assert(expression(5)==20)
    assert(condition(100)==False)
    assert(condition(99)==True)

    
























   