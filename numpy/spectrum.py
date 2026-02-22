from peak import new_file, peak_find
from figure_plot import plot2D
import matplotlib.pyplot as plt

def main():
    data = new_file('rempi.txt')
    peakvalue = peak_find(data)
    plot2D(data, peakvalue, plottype = 'REMPI')
    plt.savefig('myplot.png', dpi = 300)

if __name__ == '__main__':
    main()
