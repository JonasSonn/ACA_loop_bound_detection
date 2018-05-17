# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:07:11 2018

@author: Monster
"""
import networkx as nx


def create_simple_loop() :
    G = nx.DiGraph(name='new loop')

    
    G.add_node("A", loopheader=True)
    
    G.add_node("B")
    
    G.add_node("C")
   
    G.add_path(["A","B","A", "C"])
    
    
   
    
    return G

def create_simple_loop_wo_entry_or_exit() :
    G = nx.DiGraph()

    #G.add_node("entry")
    
    G.add_node("loopheader")
    
    G.add_node("l1b1")
    
    #G.add_node("exit")
   
    G.add_path(["loopheader","l1b1","loopheader"])
    
    
   
    
    return G