import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
age = [25,26,27,28,29,30]
x_index = np.arange(len(age))
width = 0.25
dev = [2600,2200,2500,3600,2800,3500]
plt.bar(x_index - width,dev,width=width,color='g',label='Developer')
py_dev = [2000,1200,3200,2600,3800,4500]
plt.bar(x_index,py_dev,width=width,color='r',label='Python Developer')
js_dev = [2100,2200,2300,2400,2500,2600]
plt.bar(x_index + width,js_dev,width=width,color='y',label='JavaScript Developer')
plt.xticks(ticks=x_index,labels=age)
plt.title('Developers and there Salaries in (USD)')
plt.xlabel('Ages')
plt.ylabel('Salaries in (USD)')
plt.tight_layout()
plt.legend()
plt.show()