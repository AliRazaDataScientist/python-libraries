import matplotlib.pyplot as plt
plt.xkcd() # Using to show the image as handmaded picture
# print(plt.style.available) # we can check the available style using this
plt.style.use('fivethirtyeight') # Here we are defining the specific style
age = [25,26,27,28,29,30]
dev = [2600,2200,2500,3600,2800,3500]
plt.plot(age,dev,color='g',linestyle='--',marker='.',label='Developer')
py_dev = [2000,1200,3200,2600,3800,4500]
plt.plot(age,py_dev,color='r',linestyle=':',marker='*',label='Python Developer')
js_dev = [2100,2200,2300,2400,2500,2600]
plt.plot(age,js_dev,color='y',linestyle='-',linewidth=3,marker='s',label='JavaScript Developer')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.legend() # It is used to show the lable like which line is for which record
plt.grid(True) # Using for grid view
plt.tight_layout() # For responsiveness
plt.savefig('demo.jpg')
plt.show()


