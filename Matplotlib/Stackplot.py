import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 4, 2, 2, 1, 1, 0]
player2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
player3 = [0, 1, 1, 1, 2, 1, 1, 0, 0]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
plt.title('My Stack Plot')
plt.tight_layout()
plt.legend(loc=(0.05,0.07))
plt.show()