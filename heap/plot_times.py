import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    if len(sys.argv) < 2 or sys.argv[1][-4:] != '.csv':
        print('Usage: python plot_times.py [input_filename.csv]')
        exit()
    results = np.genfromtxt(sys.argv[1], delimiter=',')
    x, y = results[:,0],results[:,1]
    m, b = 0.0000028, 0
    plt.plot(x, y, 'o')
    plt.plot(x, m*x + b)
    plt.xlabel('Inputs (n)')
    plt.ylabel('Time (t)')
    plt.title('Time complexity for WSB Scraper - Heap Implementation')
    plt.show()

if __name__ == "__main__":
    main()