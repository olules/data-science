import numpy as np
import statistics as st
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)



zero_array = np.array([0 for i in range (10)])
print(zero_array)

zero_array=zero_array.reshape(2,5)
print(zero_array)


data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

#mean
mean = data.mean()

#median
median = np.median(data)

#mode
mode = st.mode(data)

print(f'Mode: {mode}, median: {median}, mean: {mean}')

x = np.random.random((6,6))
print('Original Array: ')
print(x)

xmin, xmax=x.min(), x.max()

print('Minimun and maximum values: ')
print(xmin, xmax)

three_dims_array = np.array([[[5,  4],
                              [6,  9]],

                             [[1,  0],
                              [9,  5]],

                             [[4,  9],
                              [13, 19]],

                             [[8, 10],
                              [1, 5]]])

reshaped_array = three_dims_array.reshape(4, 4)

print(reshaped_array)



data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

reshaped_data = np.reshape(data, (-1, 1))
print(reshaped_data)




