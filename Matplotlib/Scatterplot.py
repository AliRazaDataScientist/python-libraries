import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-talk')
# print(plt.style.available())
rec = pd.read_csv('2019-05-31-data.csv')
view_count = rec['view_count']
likes = rec['likes']
ratio = rec['ratio']
plt.scatter(view_count,likes,c=ratio,cmap='summer',edgecolors='black',linewidths=1,alpha=0.75)
cbar = plt.colorbar()
cbar.set_label('Like and Dislike Ratio')
plt.xscale('log')
plt.yscale('log')
plt.title('My Test Scatterplot')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
# plt.legend()
plt.show()






