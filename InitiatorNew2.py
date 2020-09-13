import numpy as np
import random
import itertools
from collections import Counter
import operator
import matplotlib.pyplot as plt 


class Initiator:
    #choice = [1, 2, 3, 4, 5]
    
    def __init__(self):
        iterable = [1, 2, 3, 4, 5]
        pool = []
        for i in range(1, len(iterable) + 1):
            for j in itertools.permutations(iterable, i):
                pool.append(j)
        self.pool = pool
    
    # create a pool with total number of combinations 
    def getPool(self):
        return self.pool
    
    # returns MC random sample as a list 
    def getMonteCarlo(self, iterable = None, trials = int()):
        picked = []
        for i in range(1, trials):
            randin = random.choice(iterable)
            picked.append(randin)
        return picked
    
    # returns Counter that unique values are counted as one 
    def getCounter(self, iterable):
        return Counter(iterable)
    
    # returns sum of all values for normaling distribution 
    def getSum(self, dictionary):
        sum = 0
        count = 0
        for keys, values in dictionary.items():
            sum += values
            count += 1
        return sum
    
    # returns probability values of all observed data sets
    def getNormalized(self, dictionary, sum):
        weighted = {}
        for keys, values in dictionary.items():
            each = round(values / sum, 4)
            weighted[keys] = weighted.get(keys, each)
        return weighted
    # return reversed sorted list of all items in the list 
    def getReversed(self, dictionary):
        sorted_d = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
        return sorted_d
    
    # convert dict to list
    def makeList(self, dictionary):
        l1 = []
        for keys, values in mcc3.items():
            l1.append((keys, values))
        return l1

    