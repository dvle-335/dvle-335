import numpy as np
import pandas as pd
import sys
def new_file(name):
    if name == '':
        sys.exit('name file not exist')
    elif name.endwith('.csv' == True):
        data = pd.read_csv(name)
    elif name.endwith('.txt' == True):
        data = pd.read_txt(name)
    else: 
        sys.exit('file format not correct')