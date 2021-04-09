from priority_queue import PriorityQueue
from file_handling import *
import time
from random import seed
from random import random
from random import randint

symbols = ['abc','def','ghi','jkl','mno','pqr','tuv','xyz']
seed(42)
with open('times_artificial.csv', 'w') as fp:
    fp.write('')

for i in range(1,9):
    counts = 0
    for j in range(19):
        queue = PriorityQueue()
        num_inputs = 0
        start_time = time.time()
        counts = counts + 5 * 10 ** i
        for k in range(counts):
            item = {
                'symbol' : symbols[randint(0,len(symbols)-1)],
                'score' : random() * 500
                }
            queue.push(item)
            num_inputs = num_inputs + 1
        for k in range(3):
            queue.pop()
        total_time = time.time() - start_time
        write_csv_artificial(num_inputs, total_time)