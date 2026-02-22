import numpy as np
import pandas as pd
import sys
from scipy.signal import find_peaks

def new_file(name,headercheck = 0):
#read data from either .csv or .txt file, return a 2D array.
    if name == '':
        sys.exit('name file not exist')
    elif name.endswith('.csv'):
        data = pd.read_csv(name, header = headercheck).to_numpy()
    elif name.endswith('.txt'):
        data = pd.read_table(name, header = headercheck).to_numpy()
    else: 
        sys.exit('file format not correct')
    return data

def peak_find(data):
#find all the peaks from 2D data based on peak characteristic restrictions.
    peak, _= find_peaks(data[:,1],
                            height = 0.1,
                            distance = 5,
                            prominence = 0.05)
    return data[peak]

def mass_find(data, mass_list):
#convert a flight time spectrum to a mass spectrum based on the given mass list.
    