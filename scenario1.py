# arr[]=[1,2,3,2,2,2,4]
# n=input("enter a")
# if
# while arr[i]<7:
#     for i in range(0,n-1):
#         if arr[i]==x:
#             count=count+1
#         print(count)


# given sorted array arr of size n and a number x,you need to find the number of occurances of x in arr
# n=int(input("enter n"))
# x=int(input("enter x"))
# count=0
# for i in range(n):
#     a=int(input(" "))
#     for i in range(0, n - 1):
#         if a[i]==x:
#             count=count+1
#         print(count)


# Addition of two no's without using +,sum()
# a=45
# b=12
# c=(-a-b)*-1
# print(c)

#find modulus of 2 no's without using modulus operter
# a=-10
# b=4
# q=a//b
# if q<0:
#     q==1
#
# m=a*b+

def divide(dividend, divisor):
    # if divisor == 0:
    #     return "Error: Divisor cannot be zero"
    negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if negative:
        quotient = -quotient

    return quotient

dividend = -11
divisor = 2
result = divide(dividend, divisor)
print(result)

# Given a number N,the task is to find the largest priime  factor of that number

#Given an array of size n-1 such that it only conatains  distinct integers in the range of  1 to n, and find the missing no. in an array



#
# def find_missing_number(arr, n):
#     total_sum = n * (n + 1) // 2
#     array_sum = sum(arr)
#     missing_number = total_sum - array_sum
#     return missing_number
# # Example usage
# arr = [1, 2, 4, 5, 6]
# n=int(input("enter a no."))
# missing_number = find_missing_number(arr, n)
# print(f"The missing number is: {missing_number}")


# def missingvalues():
#     a = [0,1, 2, 3, 5]
#     for i in a:
#         if(i!=a[i]):
#             return i
# a = [1, 2, 3, 5]
# n = int(input("enter a no."))
# print("missing value",missingvalues())

# arr=[]
# n=int(input("enter the size of array"))
# for i in range(0,n-1):
#     element=int(input("Enter element of array "))
#     arr.append(element)
#     arr.sort()
# print(" array: ",arr)
#
#
# for i in range(1,len(arr)+1):
#     if i not in arr:
#         print("missing element is",i)


# contains elements in range from 0 to n-1, you need to find all the element occurances more than once  in the given array
#example:
# input:arr[]={0,3,1,2}
# n=4 output:-1
# Therefore there is no repeating element in the array

#given an array arr of size N, print the second largest distict element frm the array. If second eleemet doest exists then return -1
# def second_largest(arr):
#     if len(arr) < 2:
#         return None
#     largest = second_largest = float('-inf')
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num!= largest:
#             second_largest = num
#     if second_largest == float('-inf'):
#         return None
#     return second_largest
#
# # Test the function
# arr = [12, 35, 1, 10, 34, 1]
# print("Second largest element is", second_largest(arr))


# given an arr[] of size n of non-ve  integers  each element represents  the maximum length
# of the jumps that can be made forword from that element,This means if arr[]=x,then we can jump any distance y such that
# y=<x.

