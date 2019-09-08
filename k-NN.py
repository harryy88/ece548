#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:23:02 2019

@author: harrisongroll
"""


class Node: 
    
    arrayofNodes = []
    numOfCorrect = 0
    totalCount = 0
    
    def __init__(self, w, a, b, cp, c=None):
        self.classify = c
        self.weight = w
        self.age = a
        self.bmi = b
        self.cpp = cp
        self.distance = None
        
    @staticmethod
    def createNode(line):
        pass
    
    @classmethod
    def findDistance():
        pass
    
    @staticmethod
    def sortDistances(arrayOfNodes):
        pass
    
    def getKNN(arrayOfNodes, k):
        pass
    
    def getErrorRate():
        pass

    def start(k): 
        """
        load file, create node, find distance, sort, vote, get error rate
        """
        pass
        
    

sample = ["no 3.5 7 22 yes","no 4.5 6 64 yes","yes 1.4 91 2 no"]


for line in sample:
   nodes.append(Node.createNode(line))
   
bob = Node(False, 3.5, 7, 22, True)
print(bob.age)

