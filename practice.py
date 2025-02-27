import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Q1

roll_number = 102317265
np.random.seed(roll_number)

sales_data = np.random.randint(1000, 5001, size=(12, 4))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
columns = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']

sales_df = pd.DataFrame(sales_data, index=months, columns=columns)
sales_df.head()
sales_df.describe()

total_sales_per_category = sales_df.sum()
total_sales_per_month = sales_df.sum(axis=1)
sales_df['Total Sales'] = total_sales_per_month


sales_df.head()

sales_df['Growth Rate'] = sales_df['Total Sales'].pct_change() * 100

sales_df.head()

if roll_number % 2 == 0:

    sales_df['Electronics Discounted'] = sales_df['Electronics'] * 0.90
else:

    sales_df['Clothing Discounted'] = sales_df['Clothing'] * 0.85
sales_df.head()


plt.figure(figsize=(10, 6))
for column in sales_df.columns[:-2]:
    plt.plot(sales_df.index, sales_df[column], label=column)

plt.title('Monthly Sales Trends for Each Category')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=sales_df.drop(columns=['Total Sales', 'Growth Rate']), orient='v')
plt.title('Sales Distribution by Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Q2

array = np.array([[1, -2, 3], [-4, 5, -6]])
abs_array = np.abs(array)
print("Element-wise absolute value:")
print(abs_array)

flattened_array = array.flatten()

percentiles_flattened = np.percentile(flattened_array, [25, 50, 75])
print("\nPercentiles (25th, 50th, 75th) for flattened array:")
print(f"25th: {percentiles_flattened[0]}, 50th: {percentiles_flattened[1]}, 75th: {percentiles_flattened[2]}")

percentiles_columns = np.percentile(array, [25, 50, 75], axis=0)
print("\nPercentiles (25th, 50th, 75th) for each column:")
print(f"25th: {percentiles_columns[0]}")
print(f"50th: {percentiles_columns[1]}")
print(f"75th: {percentiles_columns[2]}")

percentiles_rows = np.percentile(array, [25, 50, 75], axis=1)
print("\nPercentiles (25th, 50th, 75th) for each row:")
print(f"25th: {percentiles_rows[0]}")
print(f"50th: {percentiles_rows[1]}")
print(f"75th: {percentiles_rows[2]}")

mean_flattened = np.mean(flattened_array)
median_flattened = np.median(flattened_array)
std_flattened = np.std(flattened_array)

print("\nMean, Median, and Standard Deviation for flattened array:")
print(f"Mean: {mean_flattened}, Median: {median_flattened}, Std Dev: {std_flattened}")

mean_columns = np.mean(array, axis=0)
median_columns = np.median(array, axis=0)
std_columns = np.std(array, axis=0)

print("\nMean, Median, and Standard Deviation for each column:")
print(f"Mean: {mean_columns}")
print(f"Median: {median_columns}")
print(f"Std Dev: {std_columns}")

mean_rows = np.mean(array, axis=1)
median_rows = np.median(array, axis=1)
std_rows = np.std(array, axis=1)

print("\nMean, Median, and Standard Deviation for each row:")
print(f"Mean: {mean_rows}")
print(f"Median: {median_rows}")
print(f"Std Dev: {std_rows}")

# Q3

a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

floor_values = np.floor(a)
ceiling_values = np.ceil(a)
truncated_values = np.trunc(a)
rounded_values = np.round(a)

print("Original Array:", a)
print("Floor Values:", floor_values)
print("Ceiling Values:", ceiling_values)
print("Truncated Values:", truncated_values)
print("Rounded Values:", rounded_values)

# Q4


def swap_elements(lst, index_1, index_2):
    if index_1 < len(lst) and index_2 < len(lst):
        temp = lst[index_1]
        lst[index_1] = lst[index_2]
        lst[index_2] = temp
        return lst
    else:
        return "Indices are out of range."


my_list = [10, 20, 30, 40, 50]

index1 = 1
index2 = 3
swapped_list = swap_elements(my_list, index1, index2)
print("List after swapping:", swapped_list)

# Q5

my_set = {10, 20, 30, 40, 50}
index1 = 1
index2 = 3
swapped_set = set(swap_elements(list(my_set), index1, index2))
print("Set after swapping:", swapped_set)


