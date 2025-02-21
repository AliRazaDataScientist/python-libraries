import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
gap = px.data.gapminder()
# We are creating pivot table plot so 
# gap_df = gap.pivot(index='country',columns='year',values='lifeExp')
# print(gap_df)
#I am creating headplot and it is axes function and there is no figure level function for heatmap
# sns.heatmap(gap_df)
#Trying for Europe countries data view
# europe_countries = gap[gap['continent'] == 'Europe']
# europe_df = europe_countries.pivot(index='country',columns='year',values='lifeExp')
# sns.heatmap(data=europe_df,annot=True,linewidths=0.5)#annot is showing numbers in the graph


#Clustermap
iris = px.data.iris()
sns.clustermap(iris.iloc[:,[0,1,2,3]])



plt.show()