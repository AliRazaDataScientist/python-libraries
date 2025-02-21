import matplotlib.pyplot as plt
lang = ['Python','SQL','JavaScript','PHP','HTML/CSS','Java']
Slices = [35,25,30,33,50,23]
color = ['red','gray','blue','yellow','green','pink']
explode = [0,0,0,0,0.1,0]
plt.pie(Slices,labels=lang,colors=color,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'})
plt.title('My Pie Chart')
plt.tight_layout()
plt.show()







