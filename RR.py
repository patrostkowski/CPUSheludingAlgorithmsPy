from Algorithm import Algorithm
import copy
import os
import sys

class RR(Algorithm):
    def Calculate(self, processes):
        n = 0
        id = 0
        lowest_list = []
        queue = []
        done = []
        return processes