# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:31:20 2018

@author: moth
"""
import networkx as nx
import abstractexecution as abex
def calc_bound_no_nest_handle(scopegraph):
    
    assert type(scopegraph) == nx.DiGraph
    
    bounds = {}
    
    #for node in scopegraph.nodes():
        #print (node)
        
   
    ex_scopes=nx.get_node_attributes(scopegraph, 'ex')
    cond_scopes=nx.get_node_attributes(scopegraph, 'cond')
    ab_scopes=nx.get_node_attributes(scopegraph, 'ab')

    #print(ex_scopes)
    
    for scope in scopegraph.nodes():
        if (ex_scopes[scope] != ""):
            ex = ex_scopes[scope]
            ab_state = ab_scopes[scope]
            cond = cond_scopes[scope]
            flag = True
            while(len(ab_state._abstract_store)):
                if(flag):
                    flag = False
                    ab_state = abex.abstract_execution_for_simple_loop(ab_state, ex, cond, True)
                else: 
                    ab_state = abex.abstract_execution_for_simple_loop(ab_state, ex, cond, False)
            #print(i)
            #i += 1
            ##run abs ex
            max_bound = ab_state._recorder
            bounds[scope] = max_bound
            

    return bounds
       #print('ex' in scope)
            
        
       # if scope == 'outer_loop':
          #  print(scopegraph[scope])
                    
                    #for scope in scopegraph.nodes(data = True):
       ## print(scope)
       # print(scopegraph.node[scope.name]['cond'])
            
            
    
    
    return bounds
