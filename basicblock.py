# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:36:25 2018

@author: Monster
"""

#import networkx as nx

class BasicBlock: 
    'Basic Block: Initialize as <str, str, int>'
    _scope = 'na' #name of the function or loop
    _headers = 'na' #entry node that starts the loop and were the loops exits
    _loopbound = 1 #Max no. of iterations of the loop
    _children = [] 
    
    def __init__(self, scope, headers, loopbound):
        assert type(scope) is str
        assert type(headers) is str
        assert type(loopbound) is int

        self._scope = scope
        self._headers = headers
        self._loopbound = loopbound
        
    def get_scope(self):
        return self._scope
    
    def get_headers(self):
        return self._headers
    
    def get_loopbound(self):
        return self._loopbound
    
    def add_children(self, children):
        self._children = children
    
    def report(self):
        print('basicblock | scope: {0}; headers: {1}; loopbound: {2}'.format(self._scope, self._headers, self._loopbound))