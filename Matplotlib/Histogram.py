import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
age_range = np.arange(10,110,10,dtype=int)
ages = np.random.randint(1,100,size=100)
plt.hist(ages,bins=age_range,edgecolor='black')
median_age = 52
plt.axvline(median_age,color='r',label='Median Age')
plt.title('My Test Survey')
plt.xlabel('Peoples')
plt.ylabel('Ages')
plt.tight_layout()
plt.legend()
plt.show()





