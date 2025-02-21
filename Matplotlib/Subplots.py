import matplotlib.pyplot as plt
age = [25,26,27,28,29,30]
dev = [2600,2200,2500,3600,2800,3500]
# fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(age,dev,color='g',linestyle='--',marker='.',label='Developer')
py_dev = [2000,1200,3200,2600,3800,4500]
ax2.plot(age,py_dev,color='r',linestyle=':',marker='*',label='Python Developer')
js_dev = [2100,2200,2300,2400,2500,2600]
ax1.plot(age,js_dev,color='y',linestyle='-',linewidth=3,marker='s',label='JavaScript Developer')
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Age')
ax1.set_ylabel('Median Salary (USD)')
ax1.legend() 
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Age')
ax2.set_ylabel('Median Salary (USD)')
ax2.legend() 
plt.tight_layout()
plt.show()
