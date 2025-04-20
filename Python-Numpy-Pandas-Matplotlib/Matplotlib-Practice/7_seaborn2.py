
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel("weather_data.xlsx", sheet_name="Sheet1", parse_dates=["day"])
df.set_index("day", inplace=True)  # Optional: makes date-based plots easier
print(df.head())

sns.lineplot(data=df, x=df.index, y="temperature")
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





