from peak import new_file, peak_find, mass_convert, fit_func
from figure_plot import plot2D
import matplotlib.pyplot as plt

def main():
    rawdata1 = 'rempi.txt'
    rawdata2 = 'collisionbg3(20022026)(1).txt'



    rempidata = new_file(rawdata1)
    rempipeak = peak_find(rempidata)
    plot2D(rempidata, rempipeak, plottype = 'REMPI')
    plt.savefig('myplot.png', dpi = 300)


    massdata = new_file(rawdata2)

    newmass = mass_convert(massdata.copy(),[16,17,18])
    plot2D(newmass,plottype = 'ms', xlim = [14, 20])
    plt.savefig('massplot.png',dpi = 300)
 

    plot2D(massdata, plottype = 'flighttime')
    plt.savefig('flighttime.png', dpi = 300)
if __name__ == '__main__':
    main()
