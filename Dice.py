import random
import matplotlib.pyplot as plt

random.seed()

tas = [0,0,0,0,0,0]
for i in range(0,100000):
    roll = random.randrange(1,7)
    tas[roll -1] += 1

plt.bar([1,2,3,4,5,6], tas)
plt.show()