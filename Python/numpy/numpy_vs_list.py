# importing required packages
import numpy
import time

# size of arrays and lists
size = 1000000

# declaring lists
list1 = [i for i in range(size)]
list2 = [i for i in range(size)]

# declaring arrays
array1 = numpy.arange(size)
array2 = numpy.arange(size)

# Concatenation
print("\nConcatenation:")

# list
initialTime = time.time()
list1 = list1 + list2

# calculating execution time
print("Time taken by Lists :",
      (time.time() - initialTime),
      "seconds")

# NumPy array
initialTime = time.time()
array = numpy.concatenate((array1, array2),
                          axis=0)

# calculating execution time
print("Time taken by NumPy Arrays :",
      (time.time() - initialTime),
      "seconds")

# Dot Product
dot = 0
print("\nDot Product:")

# list
initialTime = time.time()
for a, b in zip(list1, list2):
    dot = dot + (a * b)

# calculating execution time
print("Time taken by Lists :",
      (time.time() - initialTime),
      "seconds")

# NumPy array
initialTime = time.time()
array = numpy.dot(array1, array2)

# calculating execution time
print("Time taken by NumPy Arrays :",
      (time.time() - initialTime),
      "seconds")

# Scalar Addition
print("\nScalar Addition:")

# list
initialTime = time.time()
list1 = [i + 2 for i in range(size)]

# calculating execution time
print("Time taken by Lists :",
      (time.time() - initialTime),
      "seconds")

# NumPy array
initialTime = time.time()
array1 = array1 + 2

# calculating execution time
print("Time taken by NumPy Arrays :",
      (time.time() - initialTime),
      "seconds")

# Deletion
print("\nDeletion: ")

# list
initialTime = time.time()
del (list1)

# calculating execution time
print("Time taken by Lists :",
      (time.time() - initialTime),
      "seconds")

# NumPy array
initialTime = time.time()
del (array1)

# calculating execution time
print("Time taken by NumPy Arrays :",
      (time.time() - initialTime),
      "seconds")