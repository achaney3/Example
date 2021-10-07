# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countDown(num):
    for i in range(num,-1,-1):
        print(i)

countDown(10)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def returnNums(list):
    print(list[0])
    return(list[1])
mylist =[2,9]
print(returnNums(mylist))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in xthe list plus the list's length.
def firstSum(list):
    sum = list[0] + len(list)
    return sum
plus = [5,0,0,0,1,3,5]
print(firstSum(plus))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def biggerThanTwo(list):
    newlist =[]
    if (len(list)<2):
        return False
    for i in range(len(list)):
        if (i>list[1]):
            newlist.insert(0,i) 
    print(len(newlist)) 
    return newlist

examp = [5,2,3,2,1,4]
print(biggerThanTwo(examp))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def makeList(size,value):
    newOne = []
    for i in range(size):
        newOne.append(value)
    return newOne
print(makeList(3,9))