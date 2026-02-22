import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
def new_file(name):
    if name == '':
        sys.exit('name file not exist')
    elif name.endwith('.csv' == True):
        data = pd.read_csv(name, header = 0).to_numpy()
    elif name.endwith('.txt' == True):
        data = pd.read_table(name, header = 0).to_numpy()
    else: 
        sys.exit('file format not correct')
    return data

def plot(data):
    plt.plot(data[:,0], data[:,1])
    plt.show()