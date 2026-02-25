from peak import new_file, peak_find, mass_convert, fit_func
from figure_plot import plot2D
import matplotlib.pyplot as plt

def main():
    data = new_file('rempi.txt')
    peakvalue = peak_find(data)
    plot2D(data, peakvalue, plottype = 'REMPI')
    plt.savefig('myplot.png', dpi = 300)


    massdata = new_file('collisionbg3(20022026)(1).txt')
    newmass = mass_convert(massdata,[16,17,18])
    plot2D(newmass,plottype = 'ms', xlim = [14, 25])
    plt.savefig('massplot.png',dpi = 300)


if __name__ == '__main__':
    main()
