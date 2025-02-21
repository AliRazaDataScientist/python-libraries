"""Categorical Plots
1) Categoraical Scatter Plot
      Stripplot
      Swarmplot
2) Categoraical Distribution Plot
      Boxplot
      Violinplot
3) Categoraical Estimate Plot -> for central  tendency
      Barplot
      Pointplot
      Countplot
Figure level function -> catplot """
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# Stripplot -> axes level function
# We can use jitter for more spacing in the columns
# sns.stripplot(data=tips,x='day',y='total_bill',hue='sex')
# Stripplot -> Figure level function
# sns.catplot(data=tips,x='day',y='total_bill',kind='strip',jitter=0.3,hue='sex')

# Swarmplot -> axes level function
# sns.swarmplot(data=tips,x='day',y='total_bill')
# Swarmplot -> figure level function
# sns.catplot(data=tips,x='day',y='total_bill',kind='swarm',hue='sex')

# Boxplot -> axes level function
# sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
# Boxplot -> figure level function
# sns.catplot(data=tips,x='day',y='total_bill',kind='box',hue='sex')
# Boxplot -> only single colums show
# sns.catplot(data=tips,y='total_bill',kind='box',hue='sex')

# Violinplot -> axes level function
# sns.violinplot(data=tips,x='day',y='total_bill',hue='sex')
# Violinplot -> figure level function
# sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex')
# sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split=True)

# Barplot -> axes level function
# sns.barplot(data=tips,x='sex',y='total_bill',hue='smoker')
# Barplot -> figure level function
# sns.catplot(data=tips,x='sex',y='total_bill',kind='bar',hue='smoker')

# Pointplot -> axes level function
# sns.pointplot(data=tips,x='sex',y='total_bill',hue='smoker')
# Pointplot -> figure level function
# sns.catplot(data=tips,x='sex',y='total_bill',kind='point',hue='smoker')

# Countplot -> axes level function
# sns.countplot(data=tips,x='sex',hue='day')


# Faceting -> figure level function
sns.catplot(data=tips,x='sex',y='total_bill',kind='bar',col='smoker',row='day')

plt.show()