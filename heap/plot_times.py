import numpy as np
import matplotlib.pyplot as plt

results = np.genfromtxt('times.csv', delimiter=',')
x, y = results[:,0],results[:,1]
m, b = 0.1, 0
plt.plot(x, y, 'o')
plt.plot(x, m*x + b)
plt.xlabel('Inputs (n)')
plt.ylabel('Time (t)')
plt.title('Time complexity for WSB Scraper - Heap Implementation')
plt.show()