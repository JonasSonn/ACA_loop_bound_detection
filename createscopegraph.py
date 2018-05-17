# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:27:44 2018

@author: Monster
"""

import networkx as nx
import basicblock as babl
import scopegraph as sg

def create_small_scope_graph() :
    #created after page 74 of "A modular tool architecure..."
    
    main=sg.ScopeGraph("main")
    foo = sg.ScopeGraph("foo")
    
    outer = sg.ScopeGraph('outer')
    
    inner = sg.ScopeGraph('inner')
    
    loop = sg.ScopeGraph('loop')
    
    #Create loop
    
    #Create basic blocks and add children
    main_bb = babl.BasicBlock("main", "H", 1)
    main_bb.add_children(["outer","foo"])
    outer_bb = babl.BasicBlock("outer", "I", 10)
    outer_bb.add_children(["inner"])
    inner_bb = babl.BasicBlock("inner", "J", 20)
    foo_bb = babl.BasicBlock("foo", "A", 1)
    foo_bb.add_children(["loop"])
    loop_bb = babl.BasicBlock("loop", "C", 10)
  
    
    #Create loop
    loop.add_nodes(["start","B", "C","D", "E","F", "exit"])
    loop.add_path(["B", "C","D", "E","F", "B"])   
    loop.add_edge("start", "C")
    loop.add_edge("C", "exit")
    loop.add_edge("D", "F")
    loop.add_edge("F", "exit")
    loop.report()
    
    #Create foo
    foo.add_nodes(["start","A", loop, "G", "exit"])
    foo.add_path(["start","A", loop,"G", "exit"])    
    #foo.report()
     
    #Create inner
    inner.add_nodes(["start", "J", "K", "L", "M", "N", "O", "P", "Q", "exit"])
    inner.add_path(["start", "J", "K", "M", "N", "P", "Q", "J"])
    inner.add_edge("J", "exit")
    inner.add_edge("K", "L")
    inner.add_edge("N", "O")
    inner.report()
    
    #Creating main 
    main.add_node("start")
    main.add_node("H",)
    
  

    main.add_scope(outer,"name", )
    main.add_node("S")
    main.add_scope(foo)
    main.add_node("T")
    main.add_node("end")
    main.add_path([start,H,outer,S,foo,T,end])
    
    
    
    loop = lg.create_simple_loop()
    #loop2 = lg.create_simple_loop()

    #simplebb = babl.BasicBlock("loop", "C", 10)
    #simplebb2 = babl.BasicBlock("foo", "A", 1)
    
    
    #simplebb.report()
    #SG.add_scope(loop, loop.name, simplebb)
    #SG.add_scope(loop2, loop2.name, simplebb2)
    
    #SG.add_edge(loop, loop2)

    #SG.add_bb_scope(loop, simplebb) #not sure if needed
    
    return SG


