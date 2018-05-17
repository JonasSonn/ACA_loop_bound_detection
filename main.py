# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:49:18 2018

@author: moth
"""

import test_class as tc
import examples as ex
import get_loop as gl
import scopegraph_simple as sg_s
import calc_bound as cb
import readcfg as rcfg

if __name__ == "__main__":
    
    
    sg_file = rcfg.createGraph("example2_cfg.cfg")
    sg = sg_s.init_graphs()
    
    assert type(sg) == nx.DiGraph
    bounds = cb.calc_bound_no_nest_handle(sg_file)
    print ("Loop bounds found: {0}".format(bounds))
    
    #tc.test_ae_auto_update()
    
    #meat = gl.get_simple_for_loop("cloops/forloop.c")
    
    #print (meat)
    #expression = lambda x: x + 1
    #condition = lambda x: x>10000
    
    #expression_str = "lambda {0}: {1}".format(meat[0], meat[2])
    #condition_str = "lambda {0}: {1}".format(meat[0], meat[1])
    
    #print("exp: {0}, cond {1}".format(expression_str, condition_str))


   ##expression = eval(expression_str)
    ##condition = eval(condition_str)
    
    #print("expression: {0}".format(expression(2)))
    #print("condition: {0}".format(condition(30)))
    #Get bounds 
        
    #bound = ex.example_get_bound(expression, condition)
    
    #print("max loop bound: {0}".format(bound))
    
    
    