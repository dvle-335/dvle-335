import numpy as np
import pandas as pd
#pandas for simple reading input file in csv or txt, then convert to numpy array.
import sys
from scipy.signal import find_peaks 
from scipy.optimize import curve_fit
#scipy.signal libary for peak finding, fitting, etc..


def new_file(name,headercheck = 0):
#read data from either .csv or .txt file, return a 2D array.
    if name == '':
        sys.exit('name file not exist')
    elif name.endswith('.csv'):
        data = pd.read_csv(name, header = headercheck)
    elif name.endswith('.txt'):
        data = pd.read_table(name, header = headercheck)
    else: 
        sys.exit('file format not correct')
    for col in data.columns:
        if data[col].dtype == np.object_:
            data[col] = data[col].str.replace(',','.').str.strip().astype(float)
        elif data[col].dtype == np.float64:
            continue
    return data.to_numpy()
def peak_find(data,height = 0.1, distance = 5, prominence = 0.05):
#find all the peaks from 2D data based on peak characteristic restrictions.
    peak, _= find_peaks(data[:,1],
                            height = height,
                            distance = distance,
                            prominence = prominence)
    return data[peak]

def mass_convert(data, mass_list):
#convert a flight time spectrum to a mass spectrum based on the given mass list.
    peak_pos = peak_find(data, 35, 20, 0.3)
    print('number of peak found', peak_pos.shape[0])
    if len(mass_list) == 1 or peak_pos.shape[0] == 1:
        sys.exit('Not enough data for fitting')
    elif peak_pos.shape[0] is not len(mass_list):
        sys.exit('mismatch between data and possible mass')
    popt, _ = curve_fit(fit_func, mass_list, peak_pos[:,0])
    data[:,0] = np.power((data[:,0]-popt[1])/popt[0],2)
    return data


def fit_func(x, a, b):
    return a*np.sqrt(x) + b
