from sorters import BCIS, QS, IS
from timeit import default_timer as timer
import numpy as np
import pandas as pd
import sys, os, csv, io


#############################################################
#                                                           #
#                   Algorithm Parameters                    #
#                                                           #
#############################################################

TEST_SIZE = 7000 # max distribution size = 10k
STEP = 10
REPORT_FILENAME = 'ratios.csv'
DISTRIBUTIONS_FILENAME = 'distributions.csv'

#############################################################
#                                                           #
#              Data Preparation and Setup                   #
#                                                           #
#############################################################

distributions = pd.read_csv(DISTRIBUTIONS_FILENAME)

uniform_dist = distributions['uniform']
binominal_dist = distributions['binominal']
poisson_dist = distributions['poisson']
normal_dist = distributions['normal']
real_dist = distributions['real']

bcis_sorter = BCIS()
#qs_sorter = QS()
is_sorter = IS()

final_results = []

# a workaround to avoid Python's recursion limit
sys.setrecursionlimit(TEST_SIZE+100)


def write_report(values):
    filename = REPORT_FILENAME
    fieldnames = ['array_size', 'uniform_bcis', 'uniform_qs', 'uniform_is', 'uniform_bcis/qs', 'uniform_bcis/is', 'binomial_bcis', 'binomial_qs', 'binomial_is', 'binomial_bcis/qs', 'binomial_bcis/is', 'poisson_bcis', 'poisson_qs', 'poisson_is', 'poisson_bcis/qs', 'poisson_bcis/is', 'normal_bcis', 'normal_qs', 'normal_is', 'normal_bcis/qs', 'normal_bcis/is','real_bcis', 'real_qs', 'real_is', 'real_bcis/qs', 'real_bcis/is']
    print('Writings report...')

    try:
        output_file = open(filename, 'w', newline='')
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in values:
            csv_writer.writerow(row)
            
    finally:
        output_file.close()

    
def calc_execution_elapsed_times(distribution, dist_name):  

    # measuring BCIS execution elapsed time

    start = timer()
    bcis_sorter.sort(distribution, 0, len(distribution)-1)
    end = timer()

    elapsed_time_bcis = end - start
    print("BCIS for size: {0} took {1} for {2}".format(len(distribution), elapsed_time_bcis, dist_name))

    # measuring QS execution elapsed time
    #start = timer()
    #qs_sorter.sort(distribution, 0, len(distribution)-1)
    #end = timer()
#
    #elapsed_time_qs = end - start
    #print("QS for size: {0} took {1} for {2}".format(len(distribution), elapsed_time_qs, dist_name))

    # measuring IS execution elapsed time
    start = timer()
    is_sorter.sort(distribution)
    end = timer()

    elapsed_time_is = end - start
    print("IS for size: {0} took {1} for {2}".format(len(distribution), elapsed_time_is, dist_name))

    return {
        'bcis' : elapsed_time_bcis,
        #'qs' : elapsed_time_qs,
        'is' : elapsed_time_is,
        #'bcis/qs' : (elapsed_time_bcis/elapsed_time_qs),
        'bcis/is' : (elapsed_time_bcis/elapsed_time_is)
    }



#############################################################
#                                                           #
#                  Measurement Execution                    #
#                                                           #
#############################################################

try:

    # executing comparisons throught N trials
    for i in range(STEP, TEST_SIZE, STEP):

        print("Array size: {0}".format(i))

        uniform_res = calc_execution_elapsed_times(uniform_dist[0:i], "uniform")
        binominal_res = calc_execution_elapsed_times(binominal_dist[0:i], "binominal")
        poisson_res = calc_execution_elapsed_times(poisson_dist[0:i], "poisson")
        normal_res = calc_execution_elapsed_times(normal_dist[0:i], "normal")
        real_res = calc_execution_elapsed_times(real_dist[0:i], "real")



        partial_result = {
            'array_size' : i,

            'uniform_bcis' : uniform_res['bcis'],
            'uniform_is' : uniform_res['is'],
            'uniform_bcis/is' : uniform_res['bcis/is'],

            'binomial_bcis' : binominal_res['bcis'],
            'binomial_is' : binominal_res['is'],
            'binomial_bcis/is' : binominal_res['bcis/is'],

            'poisson_bcis' : poisson_res['bcis'],
            'poisson_is' : poisson_res['is'],
            'poisson_bcis/is' : poisson_res['bcis/is'],

            'normal_bcis' : normal_res['bcis'],
            'normal_is' : normal_res['is'],
            'normal_bcis/is' : normal_res['bcis/is'],

            'real_bcis' : real_res['bcis'],
            'real_is' : real_res['is'],
            'real_bcis/is' : real_res['bcis/is']
        }


        final_results.append(partial_result)


except:
    print("An error has been occurred")
finally:
    write_report(final_results)


