# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:55:22 2018

@author: moth
"""
import os 
import sys
import networkx as nx

import abstractstate as abst

def createGraph(file):
    
    sg = nx.DiGraph()
      
    
    
    if not os.path.isfile(file):
       print("File path {} does not exist. Exiting...".format(file))
       sys.exit()
    CFG = None
    nodes = []
    edges = []
    nodes_info = {}
    n = []
    
    with open(file) as fp:
       cnt = 0
       for line in fp:
           #print("line {} contents {}".format(cnt, line))
           if "Nodes:" in line:
               s = line.find("{")+1
               e = line.find("}")
               nodeline = line[s:e]
               nodes = nodeline.split(",")
               sg.add_nodes_from(nodes)
           if "Edges:" in line:
               s = line.find("{")+1
               e = line.find("}")
               edgeline = line[s:e]
               edges = edgeline.split(",")
              # sg.add_edges_from(edges)
           for node in nodes:
               if '|'+node+'|' in line:
                    #print (line)
                    s = line.find("{")+1
                    e = line.find("}")
                    nodeinfoline = line[s:e]
                    node_info = nodeinfoline.split(",")
                    ab_state = get_ab_state(node_info[0])
                    ex_str = get_function(node_info[1])
                    cond_str = get_function(node_info[2])
                    ex_f = ""
                    cond_f = "" 
                    if ex_str != "":
                        ex_f = eval(ex_str)
                        cond_f = eval(cond_str)
                    sg.add_node(node, cond=cond_f, ex=ex_f, ab = ab_state, loopbound=1)
                
    
                   
            
    return sg           
             
               #print("foudn var {0}; condition{1}; expression{2}".format(var, condition, expression))
               
      # cnt += 1
        
    
#def getNodes(line):
    
#def getEdges(line):
def get_ab_state(abstring) :
     #print(abstring)
     s = abstring.find("(")+1
     e = abstring.find(")")
     data = abstring[s:e]
     #print (data)
     split_data = data.split(";")
     recorder = split_data[0]
     #print(recorder)
     s = split_data[1].find("[")+1
     e = split_data[1].find("]")
     #print(split_data[1])
     ranges = split_data[1][s:e]
     ranges = ranges.split("-")
     #print(ranges)
     range_s = ranges[0]
     range_e = ranges[1]
     if range_e == range_s : #just to make humans feel comfortable
         range_e = int(range_e) + 1
     abstract_store = list(range(int(range_s), int(range_e)))
    
     abstract_state = abst.AbstractState(recorder, abstract_store)
     
     #print (abstract_state._abstract_store)
     #print (abstract_state._recorder)
     
     return abstract_state
def get_function(f_string):
    
    
   # ex = "x : x+1 if x%3 else x+3"
   # cond = "x<200"
    
    exp = f_string.split('\"')
    
    if exp[1] == "" :
        return ""
    lambda_f = "lambda " + exp[1]
    #print(lambda_f)
    
    return lambda_f
    
def getRules(line):
    
    
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
    
    