from peak import new_file, plot
import matplotlib.pyplot as plt

def main():
    data = new_file('rempi.txt')
    plot(data)
    plt.show()

if __name__ == '__main__':
    main()