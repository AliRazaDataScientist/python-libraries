import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('fivethirtyeight')
all_data = pd.read_csv('data2.csv')
ages = np.arange(18,56,1,dtype=int)
Python = all_data['Python']
All_Devs = all_data['All_Devs']
plt.plot(ages,All_Devs,linestyle=':',color='r',label='All_Devs')
plt.fill_between(ages,All_Devs,Python,where=(All_Devs>=Python),interpolate=True,color='r',alpha=0.25,label='Below Average')
plt.plot(ages,Python,linestyle='--',color='g',label='Python')
plt.fill_between(ages,Python,All_Devs,where=(Python>All_Devs),interpolate=True,color = 'g',alpha = 0.25,label='Above Average')
JavaScript = all_data['JavaScript']
plt.plot(ages,JavaScript,linestyle='-',color='b',label='JavaScript')
plt.fill_between(ages,JavaScript,All_Devs,where=(JavaScript>=All_Devs),color='black',interpolate=True)
plt.title('My First Chart created about ages and salaries')
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.legend()
plt.tight_layout()
plt.show()








