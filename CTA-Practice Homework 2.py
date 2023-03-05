##############################################################################
# CTA-Practice Homework 2.py
# Questions should be solved using recursion
# Author David
##############################################################################
import time

print("##############################################################################")
print("# 1. Write an algorithm that returns the reverse of a given string.")
print("##############################################################################")

def reverse(string):
    # Test lenght of string is zero return string
    if len(string) == 0:
        return string
    else:
        LastEl = reverse(string[1:])
        AddEl = string[0]
        print("Beginning of string {} added {}.".format(LastEl, AddEl))
        recurstring = LastEl + AddEl
        print("Output: {}.".format(recurstring))
        return recurstring
        

# Request input from user
string = input("Enter string to be reversed: ")
print("\nString reversed: " + reverse(string))


time.sleep(5)

print("\n\n##############################################################################")
print("# 2. Write an algorithm that reverses an array in-place (i.e changes ")
print("# what is stored at each # index), assume the input array contains numbers.")
print("##############################################################################")

def reverse_array(array):
    # Test lenght of array is zero return array
    if len(array) == 0: 
        return array
    # Variables for Slices on array
    # Select the first element of the array   
    SelectEl = [array[len(array) - 1]]
    # Add to left of the array
    AddEl = reverse_array(array[:len(array) - 1])
    # Print to screen expalnation to screen
    print("Add {} add to left of {} array.".format(SelectEl, AddEl))
    recur_array = SelectEl + AddEl
    # print output of recurive function to screen
    print("Recursive output: {} ".format(recur_array))
    # Return the reversed array
    return recur_array

# Input Array
array = [1, 2, 3, 4]
print("The input is {}. \n".format(array))

# Output array
ReversedArray = reverse_array(array)
print("\nFinal array reversed: {}".format(ReversedArray))

time.sleep(5)

print("\n\n##############################################################################")
print("# 3. Write an algorithm that checks whether an element occurs in an array, ")
print("# assume unsorted.")
print("##############################################################################")


def search(Q3array, num, lenarray):
    if Q3array[lenarray] == num:
        return True
    elif lenarray == 0:
        return False
    else:

        find = search(Q3array, num, lenarray - 1)
        return find
    
# Input array
Q3array = [9,2,4,3,7,10]
# Request input from user
num = int(input("Enter Number between 1 and 10: "))
# index of array is lenght minus 1
lenarray= len(Q3array) - 1

Output = search(Q3array, num, lenarray)
print("\nYour input is: {}".format(Output))

time.sleep(5)

print("\n\n##############################################################################")
print("# 4. Write an algorithm that computes the sum of an array of numbers")
print("##############################################################################")

def sumarray(Q4array,Q4lenarray):
   if (Q4lenarray == 0):
     return 0
   else:
    SelectEl = Q4array[Q4lenarray-1]
    # Add to left of the array
    AddEl = sumarray(Q4array, Q4lenarray -1)
    # Print to screen expalnation to screen
    print("Select number {} and add to {}.".format(SelectEl, AddEl))
    sum_array = SelectEl + AddEl
    # print output of recurive function to screen
    print("Recursive output: {}\n".format(sum_array))
    return sum_array


# Input array
Q4array = [5,10,3,12,30]
# Len of array
Q4lenarray= len(Q4array)
print("Input array is {}\n".format(Q4array))

print("\nThe sum of the array is {}".format(sumarray(Q4array,Q4lenarray)))

time.sleep(5)
print("\n\n##############################################################################")
print("# 5.Write an algorithm to produce calculate the Nth number in the Fibonacci sequence.")
print("# Assume the sequence begins 0,1,1,2....")
print("##############################################################################")


def fibonacci_of(n):
    if n in {0, 1}:  
        return n
    inputMinus1 = fibonacci_of(n - 1)
    # Add to left of the array
    inputMinus2 = fibonacci_of(n - 2) 
    # Print to screen expalnation to screen
    # print("n - 1 = {} add n - 2 = {}.".format(inputMinus1, inputMinus2))
    sum_Feb = inputMinus1 + inputMinus2
    # print output of recurive function to screen
    # print("Recursive output: {}\n".format(sum_Feb))
    return sum_Feb


# Request input from user
num = int(input("Enter Number between 1 and 20: "))

for n in range(num):
    febprint = fibonacci_of(n)
    print(febprint)

time.sleep(5)
print("\n\n##############################################################################")
print("# 6. Write a recursive function that checks whether a string is a palindrome (a palindrome")
print("# is a string that’s the same when reads forwards and backwards.)")
print("##############################################################################")

def palindrome(Q6string):
    if len(Q6string) < 2:  
        return True
    else:
        SelectEl = Q6string[0]
        AddEl = Q6string[-1]
        Palin = palindrome(Q6string[1:-1])
        # Print to screen expalnation to screen
        # print("SelectEl {}, AddEl {} and other {}".format(SelectEl, AddEl, other))
        sum_array = SelectEl == AddEl and Palin
        # print output of recurive function to screen
        # print("Recursive output: {}\n".format(sum_array))
        return sum_array


# Request input from user
Q6string = input("Input word to check if palindrome: ")
Q6 = palindrome(Q6string)

if Q6:
    print ("{} is a palindrome".format(Q6string))
else :
    print ("{} is not a palindrome".format(Q6string))

time.sleep(5)
print("\n\n##############################################################################")
print("# 7. Given a number and a power, compute the result of the number raised to that power.")
print("# For example 23 = 8.")
print("##############################################################################")


def power(num, exponent):
  # Exponent if equal to 1
  if exponent == 0 :
    return 1
    
  else :
    # Recursion   
    print("num {} * power(num {}, exponent {} - 1)".format(num, num, exponent))
    return num * power(num, exponent - 1)

num = int(input("Enter Number: "))
exponent =  int(input("Enter Power of the number: "))


Q7 = power(num, exponent)
print ("\nThe number {} to the power of {} is equal to {}".format(num, exponent, Q7))

time.sleep(5)
print("\n\n##############################################################################")
print("# 8. Given a string and a substring, compute how many times that substring appears in")
print("# the string. For example “he” appears twice in the string “her and herself”.")
print("##############################################################################")

def SubstrCount(str1, str2):
    # Get lenghts of strings 
    n1 = len(str1)
    n2 = len(str2)
    # Verify if string 1 is empty  
    # Or is smaller that the substring
    if (n1 == 0 or n1 < n2):
        return False
 
    if (str1[0 : n2] == str2):
        print("Part 1 SubstrCount({} [{} - 1:], {}), ".format(str1, n2, str2))
        return SubstrCount(str1[n2 - 1:], str2) + 1 
    print("Part 2 SubstrCount({} [{} - 1:], {}), ".format(str1, n2, str2))
    return SubstrCount(str1[n2 - 1:], str2)
 
     
# str1 = "her and herself"
# str2 = "he"

str1 = input("Enter a string: ")
str2 =  input("Enter a substring: ")


Q8 = SubstrCount(str1, str2)
print ("\nThe substring '{}' appears '{}' in the string '{}'".format(str2, Q8, str1))