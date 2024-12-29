import seaborn as sns
import matplotlib.pyplot as plt
#load dataset
phool = sns.load_dataset('iris')
#change figure
plt.figure(figsize=(8,6))

#draw a line plot
sns.barplot(x="species", y="sepal_length",data=phool)
plt.title("Phoolon ka Plot")
sns.set_style("dark")
plt.show()