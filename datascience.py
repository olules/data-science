import pandas as pd
import numpy as np
import statistics as st


arr = np.array([
[1,2],
[3,4]
    
])
print(arr)
print(arr.shape)


student_marks = [78,45,67,23,45,90]
student_marks=np.array(student_marks)

#mean
mean = student_marks.mean()

#median
median = np.median(student_marks)

#mode 
mode = st.mode(student_marks)

print(f'Mode: {mode}, median: {median}, mean: {mean}')



davids_marks= np.array([
    [78,67,90],
    [34,55,23],
    [12,89,45]
])

mean2=davids_marks.mean()

print(mean2)

print(davids_marks[0][2])
print(davids_marks[2][1])


diagonal = [davids_marks[0][0], davids_marks[1][1], davids_marks[2][2]]
print(diagonal)

my_Arr = np.array([[i for i in range(4)] for _ in range(4) ])
print(my_Arr.ndim)



