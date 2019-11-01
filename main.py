from sorters import BCIS, QS
from random import randrange
from timeit import default_timer as timer
import numpy as np
import sys, os, csv, io


#############################################################
#                                                           #
#              Data Preparation and Setup                   #
#                                                           #
#############################################################

binominal_dist = np.random.binomial(1000, .5, 10000)
poisson_dist = np.random.poisson(1000, 10000)
normal_dist = np.random.normal(0, .1, 10000)
uniform_dist1 = np.random.uniform(-1,1,10000)

bcis_sorter = BCIS()
qs_sorter = QS()

total_ratios = []



# a workaround to avoid Python's recursion limit
sys.setrecursionlimit(6100)


def write_report(values):
    # output file with a list of ratios
    output_file = open('ratios.csv', 'w')

    try:
        #csv_writer = file.writer(output_file)

        for value in values:
            output_file.write(str(value) + "\n")
    finally:
        output_file.close()


def get_ratio_bcis_qs(distribution):
    # measuring BCIS execution elapsed time
    start = timer()
    bcis_sorter.sort(distribution, 0, len(distribution)-1)
    end = timer()

    elapsed_time_bcis = end - start

    # measuring QS execution elapsed time
    start = timer()
    qs_sorter.sort(distribution, 0, len(distribution)-1)
    end = timer()

    elapsed_time_qs = end - start
    ratio = elapsed_time_bcis/elapsed_time_qs

    return "{0};{1};{2};".format(
        elapsed_time_bcis, 
        elapsed_time_qs, 
        ratio)

#############################################################
#                                                           #
#                  Measurement Execution                    #
#                                                           #
#############################################################

# executing comparisons throught N trials
for i in range(0, 6000, 100):
    uniform_dist = np.random.uniform(-1,1,i)

    partial_ratio = get_ratio_bcis_qs(uniform_dist)  
    total_ratios.append(partial_ratio)

    if i%10 == 0:
        print("Array size: {0} Ratio BCIS/QS: {1}".format(i, partial_ratio))


write_report(total_ratios)


