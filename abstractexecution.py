# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:07:07 2018

@author: moth
"""

def abstract_execution(abs_state):
    
    abstract_state._recorder = 1
    abstract_state._program_point = abstract_state_._program_point + 1
    
def abstract_execution_for_simple_loop(abs_state, update_expression, condition, new_scope_flag):
    if(new_scope_flag) :
        abs_state._recorder = 1
    else :
        abs_state._recorder += 1
    
    #update_icon(abs_state._recorder)
                     
    
    # abs_state._i_stack[top]
    # expression : i = 1 + x * 2
    
    # update abstract stores
    j = 0 #gaffa solution
    for i in abs_state._abstract_store:
        abs_state._abstract_store[j] = update_expression(i)
        j += 1
        
    # trim impossible iterations
    new_list = []

    for i in abs_state._abstract_store :
        #print("is {0} more than 10?".format(i))
        #print(condition( i))
        if(condition(i) == True):
            #print ("no, {0} is not more than 10".format(i))
            new_list.append(i)
            
        
    print(new_list)
    abs_state._abstract_store = new_list
    #print(abs_state._abstract_store)
    #print(abs_state._recorder)
    #print("Total loop iterations: {0}".format(abs_state._recorder))

    return abs_state    

def update_icon(argument):
    
    n = argument%4
    
    switcher = {
        0: "\\",
        1: "|",
        2: "/",
        3: "--",
    }
    
    print (switcher.get(n))
            
        
    
        