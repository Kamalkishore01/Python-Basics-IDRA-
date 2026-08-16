import numpy as np
#print("NumPy version:", np.__version__)

arr_1D = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr_1D)

#2D-Array
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("2D Array:")
print(arr_2d)

#Creating 3D-Array
arr_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D Array:")
print(arr_3d)

#Checking Array Properties
print("Number of dimensions:", arr_2d.ndim)
print("Shape:", arr_2d.shape)
print("Total elements:", arr_2d.size)
print("Data type:", arr_2d.dtype)


#Indexing
numbers = np.array([10, 20, 30, 40, 50])

print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

#On 2D array
print("Element at row 1, column 2:", arr_2d[0, 1])
print("Element at row 3, column 1:", arr_2d[2, 0])

#Slicinggg-------------------------------

numbers = np.array([10, 20, 30, 40, 50])

print("First three elements:", numbers[:3])
print("Elements from index 2:", numbers[2:])
print("Elements from index 1 to 3:", numbers[1:4])
#2D-Array
print("First two rows:")
print(arr_2d[:2])

print("\nFirst two columns:")
print(arr_2d[:, :2])

#Reshapinggg
numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)

reshaped = numbers.reshape(3, 4)

print("\nReshaped Array:")
print(reshaped)

#10. Creating Arrays Using ones()
one_array = np.ones((2, 3))

print(one_array)

#Using arrange
arr = np.arange(1, 11)

print(arr)

#Linspace
arr = np.linspace(0, 10, 6)

print(arr)

#Operatuonss
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Scalar and Vectors oprns

numbers = np.array([10, 20, 30, 40])

print("Original:", numbers)
print("Add 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)
print("Divide by 2:", numbers / 2)


numbers = np.array([1, 2, 3, 4, 5])

squared = numbers ** 2

print("Original:", numbers)
print("Squared:", squared)

#Boolean masking
numbers = np.array([10, 25, 30, 45, 50, 65])

mask = numbers > 40

print("Boolean Mask:")
print(mask)

print("Values greater than 40:")
print(numbers[mask])

#Broadcasting
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

addition = numbers + 5

print(addition)

#Aggreagate fxn
numbers = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Median:", np.median(numbers))

#On 2D arr
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Total:", np.sum(data))
print("Mean:", np.mean(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Median:", np.median(data))
#Row-wise and Column-wise Operations
print("Row-wise sum:")
print(np.sum(data, axis=1))

print("\nColumn-wise sum:")
print(np.sum(data, axis=0))


#20. Practical Numerical Data Analysis Example
marks = np.array([
    78, 85, 92, 67, 88,
    76, 95, 81, 73, 89
])

print("Student Marks:")
print(marks)

print("\nTotal Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Median Marks:", np.median(marks))

#Find std above 80
above_80 = marks[marks > 80]

print("Marks above 80:")
print(above_80)

#Count std abpove 80
count = np.sum(marks > 80)

print("Number of students scoring above 80:", count)


#21. final summary
print("========== NumPy Summary ==========")
print("1. Created 1D, 2D and 3D arrays")
print("2. Checked dimensions, shape, size and data type")
print("3. Performed indexing and slicing")
print("4. Reshaped arrays")
print("5. Used zeros(), ones(), arange() and linspace()")
print("6. Performed mathematical operations")
print("7. Demonstrated vectorization")
print("8. Used boolean masking")
print("9. Demonstrated broadcasting")
print("10. Used aggregate functions")