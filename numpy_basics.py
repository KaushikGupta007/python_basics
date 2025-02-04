import numpy as np

# Q1

arr = np.array([10, 20, 30, 40, 50])

arr_add = arr + 2
print("After addition:", arr_add)

arr_mul = arr * 3
print("After multiplication:", arr_mul)

arr_div = arr / 2
print("After division:", arr_div)

# Q2

arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)


def most_frequent(array):
    unique, counts = np.unique(array, return_counts=True)
    max_count_idx = np.argmax(counts)
    most_frequent_value = unique[max_count_idx]
    indices = np.where(array == most_frequent_value)
    return most_frequent_value, indices[0]


x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
value_x, indices_x = most_frequent(x)
print(f"Most frequent value in x: {value_x}, Indices: {indices_x}")

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
value_y, indices_y = most_frequent(y)
print(f"Most frequent value in y: {value_y}, Indices: {indices_y}")


# Q3

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr[0, 1])
print(arr[2, 0])

# Q4

kaushik = np.linspace(10, 100, 25)
print(kaushik)
print("dimensions: ", kaushik.ndim)
print("shape: ", kaushik.shape)
print("Total Elements: ", kaushik.size)
print("Data types: ", kaushik.dtype)
print("Total bytes consumed: ", kaushik.nbytes)

reshaped_array = kaushik.reshape(kaushik.shape[0], 1)

transposed_array = kaushik.T

print("transpose: ", reshaped_array)
print("transpose without shape: ", transposed_array)

# Q5

ucs420_kaushik = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])

mean_value = np.mean(ucs420_kaushik)
median_value = np.median(ucs420_kaushik)
max_value = np.max(ucs420_kaushik)
min_value = np.min(ucs420_kaushik)
unique_values = np.unique(ucs420_kaushik)

reshaped_ucs420_kaushik = ucs420_kaushik.reshape(4, 3)

resized_ucs420_kaushik = np.resize(ucs420_kaushik, (2, 3))

print("Original 2D Array (3x4):\n", ucs420_kaushik)
print("\nMean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_values)

print("\nReshaped Array (4x3):\n", reshaped_ucs420_kaushik)
print("\nResized Array (2x3):\n", resized_ucs420_kaushik)
