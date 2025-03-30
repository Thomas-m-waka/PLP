import pandas as pd
import matplotlib.pyplot as plt

# 📥 Load dataset (Replace 'data.csv' with your actual file)
df = pd.read_csv("data.csv")

# 🔍 Display first few rows
print("🔹 First 5 Rows of Data:")
print(df.head())

# 📊 Get basic statistics
print("\n🔹 Dataset Summary Statistics:")
print(df.describe())

# 🔍 Check for missing values
print("\n🔹 Missing Values in Each Column:")
print(df.isnull().sum())

# 📈 Perform Data Analysis (Example: Group by category and get the average)
average_values = df.groupby("Category")["Value"].mean()
print("\n🔹 Average Value per Category:")
print(average_values)

# 🔍 Filter Data (Example: Select rows where Value > 50)
filtered_df = df[df["Value"] > 50]
print("\n🔹 Filtered Data (Value > 50):")
print(filtered_df)

# 📊 Visualization 1: Bar Chart - Average Value per Category
plt.figure(figsize=(8, 5))
average_values.plot(kind="bar", color="skyblue")
plt.xlabel("Category")
plt.ylabel("Average Value")
plt.title("Average Value per Category")
plt.show()

# 📈 Visualization 2: Line Plot - Value Over Time
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Value"], marker="o", linestyle="-", color="red")
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Trend Over Time")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.show()

# 🔵 Visualization 3: Scatter Plot - Feature1 vs Feature2
plt.figure(figsize=(8, 5))
plt.scatter(df["Feature1"], df["Feature2"], color="green", alpha=0.5)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Scatter Plot of Feature1 vs Feature2")
plt.show()
