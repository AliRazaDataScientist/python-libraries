# jointplot,pairplot
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')
#Jointplot vs JointGrid
#Jointplot----->
#In jointplot we can create a plot with two columns and also we can see the plot with single single columns and we can use any plot for display
# sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist',hue='sex')
#JointGrid----->
#In jointgrid we can create both plots on our choices
g = sns.JointGrid(data=tips,x='total_bill',y='tip',hue='sex')
g.plot(sns.scatterplot,sns.histplot)

#Pairplot VS PairGrid
#Pairplot ----->
# In this plot pairs of numerical value will be created so it will create scatter plot but where they create pair with same colums so it is showing like histogram 
# sns.pairplot(iris,hue='species')

#Pairgrid -----> 
# In pairgrid we can use any plot in diagnal, upper-diagnal, lower-diagnal according to our need
# First Way --->
# g = sns.PairGrid(data=iris)
# g.map(sns.scatterplot)
# Second Way --->
# g = sns.PairGrid(data=iris,hue='species')
# g.map_diag(sns.histplot)
# g.map_upper(sns.kdeplot)
# g.map_lower(sns.scatterplot)
plt.show()