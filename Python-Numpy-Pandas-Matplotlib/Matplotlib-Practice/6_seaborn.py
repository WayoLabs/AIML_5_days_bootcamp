import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
df = sns.load_dataset("tips")  # built-in dataset

# Basic plot: Scatter plot of total_bill vs tip
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

# Correlation heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

