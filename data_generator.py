import numpy as np
import pandas as pd
import sys, os, csv, io

#############################################################
#                                                           #
#                   Algorith Parameters                     #
#                                                           #
#############################################################


TEST_SIZE = 7000 # max distribution size = 7k
STEP = 1
DATA_FILENAME = 'distributions.csv'


def write_data(values):
    filename = DATA_FILENAME
    fieldnames = ['uniform', 'binominal', 'poisson', 'normal']
    print('Writings data...')

    try:
        output_file = open(filename, 'w', newline='')
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

#        for row in values:
#            csv_writer.writerow(row)

        csv_writer.writerows(values)
            
    finally:
        output_file.close()


#############################################################
#                                                           #
#              Data Preparation and Setup                   #
#                                                           #
#############################################################



uniform_dist = np.random.uniform(-1,1,TEST_SIZE)
binominal_dist = np.random.binomial(1000, .5, TEST_SIZE)
poisson_dist = np.random.poisson(1000, TEST_SIZE)
normal_dist = np.random.normal(0, .1, TEST_SIZE)


distributions_list = []

for i in range(0, TEST_SIZE-1, STEP):

    distributions = {
        'uniform': uniform_dist[i],
        'binominal': binominal_dist[i],
        'poisson': poisson_dist[i],
        'normal': normal_dist[i]
    }

    distributions_list.append(distributions)


write_data(distributions_list)






