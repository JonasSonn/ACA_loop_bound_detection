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
    
   
   # recursive_f(scopegraph, nodes[0])
    
    ex_scopes=nx.get_node_attributes(scopegraph, 'ex')
    cond_scopes=nx.get_node_attributes(scopegraph, 'cond')
    ab_scopes=nx.get_node_attributes(scopegraph, 'ab')

    #print(ex_scopes)
    
    for scope in scopegraph.nodes():
        #for child in scopegraph.successors(scope):
            
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
        else : 
            bounds[scope] = 1
            

    return bounds

    
def recursive_f (scopegraph, scope):
    #no need to calc this every scope, find another solution 
    ex_scopes=nx.get_node_attributes(scopegraph, 'ex')
    cond_scopes=nx.get_node_attributes(scopegraph, 'cond')
    ab_scopes=nx.get_node_attributes(scopegraph, 'ab')
    
    print ("new scope {0}".format(scope))
    ex = ex_scopes[scope]
    print
    ab_state = ab_scopes[scope]
    cond = cond_scopes[scope]
    #print ("ex: {0}, cond{1}".format(ex, cond))
    flag = True
    while(len(ab_state._abstract_store) != 0):
        if(flag):
            flag = False
            ab_state = abex.abstract_execution_for_simple_loop(ab_state, ex, cond, True)
            if len(scopegraph.successors(scope)) != 0: #multi edges not supported
                print ("scopegraph succesors {0}".format(scopegraph.successors(scope)[0]))
                recursive_f(scopegraph, scopegraph.successors(scope)[0])

                #scopegraph.remove_node(scopegraph.succesors(node))
        else: 
            ab_state = abex.abstract_execution_for_simple_loop(ab_state, ex, cond, False)
            if len(scopegraph.successors(scope)) != 0: #multi edges not supported
                print ("scopegraph succesors {0}".format(scopegraph.successors(scope)[0]))
                recursive_f(scopegraph, scopegraph.successors(scope)[0])
       #print('ex' in scope)
            
       # scope['loop'] = ab_state._recorder
       # print( ab_state._recorder)
       # if scope == 'outer_loop':
          #  print(scopegraph[scope])
                    
                    #for scope in scopegraph.nodes(data = True):
       ## print(scope)
       # print(scopegraph.node[scope.name]['cond'])
            
            
    
    
   
