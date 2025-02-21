import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# print(sns.get_dataset_names())
tips = sns.load_dataset('tips')
print(tips)
#same view with these two response
#scatterplot with axis level function
# sns.scatterplot(data=tips,x='total_bill',y='tip',hue='sex',style='time',size='size')
#relplot with figure level function
# sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='sex',style='time',size='size')

#Now start working on LinePlot
gap = px.data.gapminder()
# pk_gap = gap[gap['country'].isin(['Pakistan','France','Australia'])]
# print(pk_gap)
# lineplot with axies level function
# sns.lineplot(data=pk_gap,x='year',y='lifeExp',hue='country',style='continent',size='continent')
# relplot with figure level function
# sns.relplot(data=pk_gap,x='year',y='lifeExp',hue='country',kind='line',style='continent',size='continent')

#FacetPlot 
#Its work only figure level function #work only relplot # It will not work with scatter and line plot directly
# sns.relplot(data=tips,x='total_bill',y='tip',kind='line',col='sex',row='time')
#Now try the colwrap function
sns.relplot(data=gap,x='lifeExp',y='gdpPercap',kind='scatter',col='year',col_wrap=4)
plt.show()





