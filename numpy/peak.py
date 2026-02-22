import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
def new_file(name,headercheck = 0):
    if name == '':
        sys.exit('name file not exist')
    elif name.endswith('.csv'):
        data = pd.read_csv(name, header = headercheck).to_numpy()
    elif name.endswith('.txt'):
        data = pd.read_table(name, header = headercheck).to_numpy()
    else: 
        sys.exit('file format not correct')
    return data

def plot1(data,plottype = 'default'):
    plt.rcParams.update({
       'font.size':16, 
       'mathtext.fontset': 'stix',
       'font.family': 'STIXGeneral',
    })
    plt.plot(data[:,0],data[:,1])
    if plottype.lower() == 'default':
        plt.xlabel('x')
        plt.ylabel('y')
    elif plottype.lower() == 'rempi':
        plt.xlabel(r'Wavenumber(cm$^{-1}$)')
        plt.ylabel('Intensity(a.u.)')
        plt.title('REMPI')
    else:
        sys.exit('incorrect plottype')

