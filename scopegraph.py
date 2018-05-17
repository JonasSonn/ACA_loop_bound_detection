import networkx as nx
import basicblock as bb


class ScopeGraph:
    _sg = nx.DiGraph()
    #lastnode = "hi"
    
    def __init__(self, name_):
        self._sg = nx.DiGraph(name = name_)
        #gaffa tape solution: since there is no basic block attribute to the start
        #node then there will be an AttributeError if trying to call basic block function
        #on code. Therefore, it will be solved by adding a basicblock to the start
        #node. Even though it's not useful otherwise
        #bblock = bb.BasicBlock("start", "start", 1)
        #self._sg.add_node("start", name= bblock)
        #self.lastnode="start"
        
    def add_scope(self, subgraph_, name_ ,b_block_):
        assert type(subgraph_) is nx.DiGraph
        assert type(b_block_) is bb.BasicBlock
        self._sg.add_node(subgraph_, name = b_block_)
        
    def add_nodes(self, nodes):
        # G.add_nodes_from([2,3])
        self._sg.add_nodes_from(nodes)
       
    def add_edges(self, edges):
        # G.add_edges_from([(1,2),(1,3)])
        self._sg.add_edge_from(edges)
        
    def add_path(self, nodes):
        #add_path([0,1,2,3,4,5,6,7,8,9])
        self._sg.add_path(nodes)

    def add_edge(self, subgraph_s_, subgraph_e_) :
        self._sg.add_edge(subgraph_s_, subgraph_e_)
    
    def add_node(self, node):
        self._sg.add_node(node)
        
    #def add_bb_scope(self, scope_, b_block_): #unfinished
        #raise NotImplementedError
        #assert type(scope) is nx.DiGraph
        #assert type(b_block) is bb.BasicBlock
        #scope.graph['bb']=b_block_
        
    def add_exit(self):
        self._sg.add_node("exit", name='exit' )

    def report(self):  
        print("\n")
        print('number of nodes: {0}'.format(self._sg.number_of_nodes()))
        
        print("Basic Blocks:")

        all_nodes = self._sg.nodes(data=True)
        for node in all_nodes:
           #print(node[1]["name"]) #for some reason using any other keyword than name will create a keyerror
           if('bb' in node):
               bblock = node[1]['name']
               bblock.report() 
        print("\n")
        print('number of edges: {0}'.format(self._sg.number_of_edges()))
        print("Edges:")
        print('{0}'.format(self._sg.edges()))
        
            
            