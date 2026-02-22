import numpy as np
import pandas as pd
import sys

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


