# **Exercise 2.8: Numpy Arrays**

## **Question:**
Suppose arrays a and b are defined as follows:

a = np.array([1,2,3,4], int)
b = np.array([2,4,6,8], int)

what will the computer print upon executing the following lines? 

a) print(b/a+1)
b) print(b/(a+1))
c) print(1/a)
## **Physics Solution**

ok so numpy when multiplying and dividing arrays does element by element operations

So for part a) order of operations tells us the it will do b/a with will result in [2, 2, 2, 2] so then it will add 1 to each element resulting in [3, 3, 3, 3]

for part b) we now need to add 1 to array a so [2, 3, 4, 5] and then divide b by that so [2/2, 4/3, 6/4, 8/5] since python is dynamically typed we will get a float which is [1, 1.333, 1.5, 1.6]

for part c) it is again element by element so [1/1, 1/2, 1/3, 1/4] or [1, 0.5, 0.333, 0.25]
