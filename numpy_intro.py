import numpy as np 
array = np.array([1,2,3,4,5,6,7,8,9])
array1 = np.array([9,8,7,6,5,4,3,2,1])
print("the size of arrray is = ",np.size(array))
print("the size of arrray is = ",np.size(array1))

print("the shape of arrray is = ",np.shape(array))
print("the shape of arrray is = ",np.shape(array1))

print("the type of arrray is = ",array.dtype)
print("the type of arrray is = ",array1.dtype)

#mathamatical operations

# Addition of two arrays 
print("the sum of array is = ",array+array1)
print("the sub of array is = ",array-array1)
print("the div of array is = ",array/array1)
print("the mul of array is = ",array*array1)
# inter operation within the array
print("the sum of array1 is =",np.sum(array))
print("the mean of array1 is =",np.mean(array))
print("the standard deviation of array1 is =",np.std(array))


print("the sum of array1 is =",np.sum(array1))
print("the mean of array1 is =",np.mean(array1))
print("the standard deviation of array1 is =",np.std(array1))

#other operations
#adding some values in individual array

print("Adding 2 in all element of array",array+2)
print("Adding 1 in all element of array1",array1+1)

#subtracting some values in individual array

print("subtrating 1 in all element of array1",array1-1)

#slicing

print("slicing the array ",array[0:5])
print("slicing the array1 ",array1[0:5])
