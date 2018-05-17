# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:34:09 2018

@author: moth
"""

import networkx as nx
import abstractstate as abst

def init_graphs( ):
    
    scopegraph = nx.DiGraph()
    
    abstract_state_main = abst.AbstractState(-1, [1])

    scopegraph.add_node("main", cond="", ex="", ab = abstract_state_main, loopbound=1)
    cond_ol = lambda x: x<10
    ex_ol = lambda x : x+1
    abstract_state_outer = abst.AbstractState(1, list(range(1,2)))
    scopegraph.add_node("outer_loop", cond = cond_ol,  ex = ex_ol, ab = abstract_state_outer, loopbound=1)
    
    
    cond_il = lambda x: x<20
    ex_il = lambda x : x+2
    abstract_state_inner = abst.AbstractState(1, list(range(1,2)))
    scopegraph.add_node("inner_loop", cond = cond_il, ex = ex_il, ab = abstract_state_inner, loopbound=1)
    
    scopegraph.add_path(["main", "outer_loop", "inner_loop"])
    
    
    #print (scopegraph.nodes())
    
   # cond_scopes=nx.get_node_attributes(scopegraph,'ex')
    
   # for scope in cond_scopes:
       ## if scope == 'outer_loop':
            #print("arm wrestle")
   # for scope in scopegraph.nodes(data = True):
       ## print(scope)
       # print(scopegraph.node[scope.name]['cond'])
  
    return scopegraph
    