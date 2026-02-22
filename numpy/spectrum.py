from peak import new_file
from figure_plot import plot2D
import matplotlib.pyplot as plt

def main():
    data = new_file('rempi.txt')
    plot2D(data,'REMPI')
    plt.savefig('myplot.png', dpi = 300)

if __name__ == '__main__':
    main()
