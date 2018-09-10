'''
Module written to parse outfiles from ConSurf queries.
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def load_grades(filename):
    '''
    a function used to load consurf .grades files into a pandas DataFrame
    '''
    # get absolute path of res file
    path = os.path.dirname(os.getcwd()) + '/res/consurf/'
    # read into DataFrame with pandas functionality
    return pd.read_csv(path+filename, delimiter=':')

if __name__ == '__main__':
    print(load_grades('b_gal_grades.csv'))
