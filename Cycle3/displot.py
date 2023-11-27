print("SJC22MCA-2027-Georgekutty Biju\nS3MCA")
import seaborn as sns
import matplotlib.pyplot as plt
iris_data = sns.load_dataset("iris")
sns.displot(data=iris_data, x="sepal_length", kde=True)
plt.show()
sns.relplot(data=iris_data, x="sepal_length", y="petal_length", hue="species")
plt.show()
sns.histplot(data=iris_data, x="petal_length", bins=10, kde=True)
plt.show()
