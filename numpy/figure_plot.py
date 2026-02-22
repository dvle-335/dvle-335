import matplotlib.pyplot as plt
import sys
#diffrent kind of plotting depending on the data set
def plot2D(data,data2 = None, plottype = 'default'):
    plt.rcParams.update({
       'font.size':16, 
       'mathtext.fontset': 'stix',
       'font.family': 'STIXGeneral',
    })
    plt.plot(data[:,0],data[:,1])
    if data2 is not None:
        plt.plot(data2[:,0],data2[:,1], 'o')
    if plottype.lower() == 'default':
        plt.xlabel('x')
        plt.ylabel('y')
    elif plottype.lower() == 'rempi':
        plt.xlabel(r'Wavenumber(cm$^{-1}$)')
        plt.ylabel('Intensity(a.u.)')
        plt.title('REMPI')
    else:
        sys.exit('incorrect plottype')
