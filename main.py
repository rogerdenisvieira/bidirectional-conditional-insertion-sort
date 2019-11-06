from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import numpy as np
import pandas as pd
import sys, os, csv, io


#############################################################
#                                                           #
#              Data Preparation and Setup                   #
#                                                           #
#############################################################

TEST_SIZE = 100 # max distribution size

uniform_dist = np.random.uniform(-1,1,TEST_SIZE),
binominal_dist = np.random.binomial(1000, .5, TEST_SIZE),
poisson_dist = np.random.poisson(1000, TEST_SIZE),
normal_dist = np.random.normal(0, .1, TEST_SIZE)

bcis_sorter = BCIS()
qs_sorter = QS()
is_sorter = IS()

final_results = []



# a workaround to avoid Python's recursion limit
sys.setrecursionlimit(6100)


def write_report(values):
    filename = 'ratios.csv'
    fieldnames = ['name', 'size', 'bcis', 'qs', 'is','bcis/qs','bcis/is']
    print('Writings report...')

    try:
        output_file = open(filename, 'w', newline='')
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in values:
            csv_writer.writerow(row)
            
    finally:
        output_file.close()

    
def calc_execution_elapsed_times(distribution):  

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

    # measuring IS execution elapsed time
    start = timer()
    is_sorter.sort(distribution)
    end = timer()

    elapsed_time_is = end - start

    return {
        'bcis' : elapsed_time_bcis,
        'qs' : elapsed_time_qs,
        'is' : elapsed_time_is
    }



#############################################################
#                                                           #
#                  Measurement Execution                    #
#                                                           #
#############################################################

# executing comparisons throught N trials
for i in range(0, TEST_SIZE, 1):

    #distributions = {
    #    'uniform_dist' : np.random.uniform(-1,1,i),
    #    'binominal_dist' : np.random.binomial(1000, .5, i),
    #    'poisson_dist' : np.random.poisson(1000, i),
    #    'normal_dist' : np.random.normal(0, .1, i)
    #}



    uniform_dist_partial_results = calc_execution_elapsed_times(uniform_dist[0:i])
    binominal_dist_partial_results = calc_execution_elapsed_times(uniform_dist[0:i])
    poisson_dist_partial_results = calc_execution_elapsed_times(uniform_dist[0:i])
    normal_dist_partial_results = calc_execution_elapsed_times(uniform_dist[0:i])

    print("Size: {0}".format(len(uniform_dist[0:i])))


    #print("{0} # {1} # {2} # {3}".format(
    #    uniform_dist_partial_results,
    #    binominal_dist_partial_results,
    #    poisson_dist_partial_results,
    #    normal_dist_partial_results
    #))



    
    if i%10 == 0:
        print("Array size: {0}".format(i))


#print(total_ratios)
write_report(final_results)


