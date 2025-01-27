import pandas as pd

# Q1

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "REFUND": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married",
                       "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K",
                       "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)

# Q2

print(df.loc[[0, 4, 7, 8]])

# Q3

print(df.loc[3:7])
print(df.iloc[4:9, 2:5])
print(df.iloc[:, 1:4])

# Q4

df = pd.read_csv('Iris.csv')
print(df.head())

# Q5

df_modified = df.drop(index=3, columns=df.columns[2])
print(df_modified)

# Q6

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4, 3.8, 4.7, 3.5]
}
df = pd.DataFrame(employees)
df.to_csv('employees.csv', index=False)
shape = df.shape
print(f"The DataFrame has {shape[0]} rows and {shape[1]} columns.")
print(df.info())
print(df.describe())
print(df.head())
print(df.tail(3))
average_salary = df['Salary'].mean()
total_bonus = df['Bonus'].sum()
youngest_age = df['Age'].min()
highest_performance_rating = df['Rating'].max()
print(f"i. The average salary of employees: {average_salary}")
print(f"ii. The total bonus paid to all employees: {total_bonus}")
print(f"iii. The youngest employee's age: {youngest_age}")
print(f"iv. The highest performance rating: {highest_performance_rating}")
sorted_employees_df = df.sort_values(by='Salary', ascending=False)
print(sorted_employees_df)


def categorize_performance(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else:
        return 'Average'


df['Performance_Category'] = df['Rating'].apply(categorize_performance)

missing_values = df.isnull()
print(missing_values)
df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print(df)

experienced_employee = df[df["Years_of_Experience"] > 5]
it_employee = df[df["Department"] == "IT"]
print(experienced_employee)
print(it_employee)
df['Tax'] = df['Salary'] * 0.10
print(df)
df.to_csv('modified_employees.csv', index=False)


