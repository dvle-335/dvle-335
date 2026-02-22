from peak import new_file, plot1
import matplotlib.pyplot as plt

def main():
    data = new_file('rempi.txt')
    plot1(data,'REMPI')
    plt.savefig('myplot.png', dpi = 300)

if __name__ == '__main__':
    main()
