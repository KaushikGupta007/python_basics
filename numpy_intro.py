import numpy as np
import matplotlib.pyplot as plt

# Q1

gfg = np.matrix('[4,1,9;12,3,1;4,5,6]')
result = np.sum(gfg)
print(result)

sum_row = np.sum(gfg, axis=0)
print(sum_row)

sum_column = np.sum(gfg, axis=1)
print(sum_column)

# Q2 a)

array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)
print(sorted_array)
indices = np.argsort(array)
print(indices)
print(sorted_array[:4])
print(sorted_array[-5:])

# Q2 b)

array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
int_array = array[array == array.astype(int)]
print(int_array)
float_array = array[array != array.astype(int)]
print(float_array)

# Q3 a)

X = 65 + 66
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("sales dataset : ", sales)

# Q3 b)

tax_rate = ((X % 5) + 5)/100
sales_after_tax = sales*(1 + tax_rate)
print("sales after tax : ", sales_after_tax)

# Q3 c)

discounted_sale = np.where(sales < X + 100, sales*0.95, sales*0.9)
print("discounted sales : ", discounted_sale)

# Q3 d)

week_sale = np.tile(sales, (3, 1))
sale_increase = week_sale*(1 + 0.02)**np.arange(3).reshape(-1, 1)
print(sale_increase)

# Q4

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(abs(x) + 1)
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='x^2', color='red')
plt.plot(x, y2, label='sin(x)', color='blue')
plt.plot(x, y3, label='exp(x)', color='green')
plt.plot(x, y4, label='log(|x| + 1)', color='yellow')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of Functions')
plt.legend()
plt.grid(True)
plt.show()
