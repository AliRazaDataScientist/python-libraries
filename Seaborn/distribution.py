import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
# print(tips)
# There are two step we can achieve this Figure level function and Axis level function
# Figure level Function -> displot
# Axis level Function -> histplot, rugplot, kdeplot

# We are moving with histplot
# sns.histplot(data=tips,x='total_bill',hue='sex',bins=10,element='step')#axis level function
# sns.displot(data=tips,x='total_bill',kind='hist',col='sex',row='day')#figure level function

# We are moving with kdeplot
# sns.kdeplot(data=tips,x='total_bill',hue='sex',fill=True)
# sns.displot(data=tips,x='total_bill',hue='sex',kind='kde')

#We are moving on rugplot
#Plot marginal distributions by drawing ticks along x and y axes.
#It is using with another plot not along 
# sns.kdeplot(data=tips,x='total_bill')
# sns.rugplot(data=tips,x='total_bill')

#Bivariate plot it consist of two colums where both are intersect eachother then showing in the form of grid 
# create 2d plot and dark color shows the majority of the point falls at that point
sns.histplot(data=tips,x='total_bill',y='tip')
sns.displot(data=tips,x='total_bill',y='tip',kind='kde')
plt.show()