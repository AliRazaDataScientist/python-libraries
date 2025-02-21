import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
# Regplot -> axes level function 
# sns.regplot(data=tips,x='total_bill',y='tip')
# lmplot -> figure level function 
# sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')



# Its tell us about the prediction error that we made
# Residplot -> axes level function 
sns.residplot(data=tips,x='total_bill',y='tip')
plt.show()