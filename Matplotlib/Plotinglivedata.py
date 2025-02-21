import matplotlib.pyplot as plt
import pandas as pd
import random
from itertools import count
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
x = []
y1 = []
y2 = []
indexcount = count()
def animate(i):
    x.append(next(indexcount))
    y1.append(random.randint(0,5))
    y2.append(random.randint(0,5))
    # plt.cla()
    plt.plot(x,y1,label='Channel 1')
    plt.plot(x,y2,label='Channel 2')
ani = FuncAnimation(plt.gcf(),animate,interval=1000)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()