'''
FIZZ BUZZ PROBLEM:
Write a program that prints the numbers in a list,
for multiples of ‘3’ print “fizz” instead of the number,
for the multiples of ‘5’ print “buzz” and 
for multiplies of both 3 and 5 it prints “fizzbuzz”.
'''
'''STEP-1: enumerate() enumerate method adds a counter to an iterable and returns it in a form of enumerate object.
'''

numbers=[10,20,30,40,60,30,42,28,33,44,15]
for i,num in enumerate(numbers):
    if num%3==0 and num%5==0:
        numbers[i]='fizzbuzz';
    elif num%3==0:
        numbers[i]='fizz'
    elif num%5==0:
        numbers[i]='buzz'

print(numbers)