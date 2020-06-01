#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    item = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        item.append(parts[0], parts[1])
    print(item)
    

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


    # prepare the solution in the specified output format
    # output_data = str(value) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, taken))
    # return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

