# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:13:44 2016

@author: Best
"""
import datetime

from operator import itemgetter


class DisjointSet(dict):
    def add(self, item):
        self[item] = item
 
    def find(self, item):
        parent = self[item]
 
        while self[parent] != parent:
            parent = self[parent]
 
        self[item] = parent
        return parent
 
    def union(self, item1, item2):
        self[item2] = self[item1]
        
def kruskal( nodes, edges ):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add( n )
 
    sz = len(nodes) - 1
    cost = 0
    for e in sorted( edges, key=itemgetter( 2 ) ):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            cost += _
            sz -= 1
            if sz == 0:
                return mst, cost
            forest.union(t1, t2)
 
from collections import defaultdict
from heapq import *
 
def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )
 
    mst = []
    used = set( [nodes[ 0 ]] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )
 
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
 
            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst


 
nodes = list( "123456789" )
edges = [   ("1", "5",1),
            ("1", "3",1),
            ("5", "8",1),
            ("9", "7",1),
            ("5", "6",2),
            ("1", "2",2),
            ("2", "5",2),
            ("5", "7",2),
            ("5", "6",2),
            ("2", "4",3),
            ("5", "9",3),
            ("6", "8",3),
            ("8", "9",4),
            ("4", "7",4)
        ]
start = datetime.datetime.now()
k_result = kruskal(nodes, edges)
stop = datetime.datetime.now()


t_result = stop - start
print (kruskal( nodes, edges ))
print ("Kruskal time result:",t_result)

start = datetime.datetime.now()
p_result = prim(nodes, edges)
stop = datetime.datetime.now()


t_result = stop - start
print (prim( nodes, edges ))
print ("Prim time result:",p_result)


