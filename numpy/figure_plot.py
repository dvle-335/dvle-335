import matplotlib.pyplot as plt
#basically a matlab plot like function.
import sys
#diffrent kind of plotting depending on the data set
def plot2D(data,data2 = None, plottype = 'default', xlim = None, ylim = None):
#plot a 2D data, and data2 is the peak value based on peak_find function.
#strictly no data modification to avoid data corruption.
    plt.figure()
    plt.rcParams.update({
       'font.size':16, 
       'mathtext.fontset': 'stix',
       'font.family': 'STIXGeneral',
    })
    if xlim is not None:
            plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    if plottype.lower() == 'flighttime':
        plt.plot(data[:,0],data[:,1])
        plt.xlabel('Flight time ($\mu$s)')
        plt.ylabel('Ion counts(a.u.)')
        plt.title('Flight time spectrum')   
    else:
        plt.plot(data[:,0],data[:,1])
        if plottype.lower() == 'default':
            plt.xlabel('x')
            plt.ylabel('y')
        elif plottype.lower() == 'rempi':
            plt.xlabel(r'Wavenumber(cm$^{-1}$)')
            plt.ylabel('Intensity(a.u.)')
            plt.title('REMPI')
        elif plottype.lower() == 'ms':
            plt.xlabel('m/z')
            plt.ylabel('Ion counts(a.u.)')
            plt.title('Mass spectrum')
        else:
            sys.exit('incorrect plottype')
#annotate peak position on top of peak in the graph.
    if data2 is not None:
        for i in range(len(data2[:,0])):
            plt.annotate(f'{data2[i,0]:.3f}', xy = (data2[i,0], data2[i,1]), xytext = [data2[i,0], data2[i,1]+data2[:,1].max()*0.05], ha = 'center')

def plotmulti(data1, data2 = None, data3 = None):
    plt.figure()
    plt.rcParams.update({
       'font.size':16, 
       'mathtext.fontset': 'stix',
       'font.family': 'STIXGeneral',
    })
    plt.plot(data1[:,0],data1[:,1])
    if data2 is not None:
        plt.plot(data2[:,0],data2[:,1])
    if data3 is not None:
        plt.plot(data3[:,0],data3[:,1])


#plot multiple data in one graph.
    pass      