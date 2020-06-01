#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = [] 
    item = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
        item.append((items[i-1].value, items[i-1].weight))
    
    # optimal solution for feasible k
    if capacity*item_count <= 25000000:
        print('hello')
        # fill in table of optimal values for k capacity with items 0-j
        value_table = [['x' for i in range(item_count+1)] for i in range(capacity+1) ]

        for j in range(item_count + 1):
            for k in range(capacity + 1):
                #import ipdb; ipdb.set_trace()
                if j == 0 or k == 0:
                    value_table[k][j] = 0
                elif k < item[j-1][1]:
                    value_table[k][j] = value_table[k][j-1]
                else:
                    previous = value_table[k][j-1]
                    with_j = item[j-1][0] + value_table[k - item[j-1][1]][j - 1]
                    value_table[k][j] = max(previous, with_j)
        
        # backtrack to find optimal solution  
        elem_to_add = []
        j = item_count 
        k = capacity 
        while j!=0 and k!=0:
            if value_table[k][j-1] == value_table[k][j]:
                j-=1
            else:
                elem_to_add.append(j)
                k -= item[j-1][1]

        # format whether to take the item or not as a string
        output = ''
        for i in range(item_count):
            if i+1 in elem_to_add:
                output += '1 '
            else:
                output += '0 '

        # add value and optimal flag to the beginning and remove trailing space
        output = str(value_table[capacity][item_count]) + ' ' + '1' + '\n' + output[:-1]

        return output 

    # greedy algorithm for large k
    else:
        value = 0
        weight = 0
        taken = [0]*len(items)

        items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)

        for item in items:
            if weight + item.weight <= capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight

        output = str(value)+' '+str(0)+'\n'
        output += ' '.join(map(str, taken))

        return output






if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

