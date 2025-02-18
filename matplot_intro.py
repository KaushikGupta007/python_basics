import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Q1

M = int(input("enter value:"))
x = np.linspace(-10, 10, 100)
y1 = M*(x**2)
y2 = M*np.sin(x)
plt.plot(x, y1, label="y=mx^2")
plt.plot(x, y2, label="y=mxsin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# Q2

data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Scores': [88, 92, 85, 78, 90]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
bar_plot = sns.barplot(x='Subject', y='Scores', data=df, palette='muted')

for index, row in df.iterrows():
    bar_plot.text(row.name, row.Scores, round(row.Scores, 2), color='black', ha="center")

plt.title('Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

# Q3

roll_number = int(input('enter roll number: '))
np.random.seed(roll_number)
dataset = np.random.randn(50)
print(dataset)

fig, axs = plt.subplots(1,2)
axs[0].plot(dataset)
axs[0].set_title('cumulative sum')
axs[0].set_xlabel('x-axis')
axs[0].set_ylabel('y-axis')
axs[0].grid()

axs[1].scatter(np.random.rand(30), np.random.rand(30))
axs[1].set_title('scatter plot')
axs[1].set_xlabel('x-axis')
axs[1].set_ylabel('y-axis')
axs[1].grid()

plt.show()

# Q4

url = "https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv"
data = pd.read_csv(url)
data.head()

sns.lineplot(x="month_number", y="total_profit", data=data)
plt.show()

for col in data.columns[1:6]:
  sns.lineplot(x="month_number", y=data[col],label = col, data=data)

plt.show()

for col in data.columns[1:6]:
  sns.barplot(x="month_number", y=data[col],label = col, data=data, alpha = 0.3)

plt.show()
