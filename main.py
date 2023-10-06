import time
import random

f = open('out.txt', 'w')

def gen(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(0, 10))

    return lst

def test(count, size):
    lst = []
    start = time.time()
    for i in range(count):
        gen(size)

    end = round((time.time() - start) / count, 7)
    return end    

i = 1000
while i < 10000:
    endTime = test(100, i)
    f.write(f"{endTime} - {str(i)}\n")
    i += 100

f.close()
