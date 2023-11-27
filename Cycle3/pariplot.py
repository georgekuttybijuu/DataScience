print("SJC22MCA-2027-Georgekutty Biju\nS3MCA")
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
iris_data=pd.read_csv('iris.csv')
sns.set(style="ticks")
sns.pairplot(iris_data,hue="variety",kind="scatter",markers=["o","s","D"])
plt.show()
sns.pairplot(iris_data,hue="variety",kind="kde")
plt.show()
sns.pairplot(iris_data,hue="variety",kind="hist")
plt.show()
sns.pairplot(iris_data,hue="variety",kind="reg")
plt.show()
