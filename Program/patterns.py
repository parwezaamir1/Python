# Example 1
"""
*
**
***
****
*****

"""

# row = int(input("Enter the number of rows: "))

# for i in range(1, row+1):
#     for j in range(0, i):
#         print("*", end=' ')
#     print('\n')

# Example 2
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

# row = int(input("Enter the no. of rows: "))
# for i in range(1, row+1):
#     for j in range(1, row+1):
#         print("*", end=" ")
#     print()

# Example 3
'''
* * * * *
* * * *
* * * 
* *
*
'''

# row = int(input("Enter the no. of rows: "))
# for i in range(1, row+1):
#     for j in range(i, row+1):
#         print("*", end=" ")
#     print()


# Example 4
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
# row = int(input("Enter the no. of rows: "))
# for i in range(1, row+1):
#     for j in range(i, row+1):
#         print(" ", end=' ')
    
#     for j in range(i):
#         print("*", end=" ")
#     print()


# Example 5
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''

# row = int(input("Enter the no. of rows: "))
# for i in range(1, row+1):
#     for j in range(i):
#         print(" ", end=" ")
    
#     for j in range(i, row+1):
#         print("*", end=" ")
#     print()


# Example 6
'''
         *
       * * *
     * * * * * 
   * * * * * * *
 * * * * * * * * * 
'''

# row = int(input("Enter the no. of rows: "))
# for i in range(1, row+1):
#     for j in range(i,row+1):
#         print(" ", end=" ")
    
#     for j in range(i):
#         print("*", end=' ')
    
#     for j in range(i-1):
#         print("*", end=' ')
#     print()


# Example 7
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
'''

row = int(input("Enter the no. of rows: "))
for i in range(1, row+1):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(i, row+1):
        print("*", end=' ')
    
    for j in range(i, row):
        print("*", end=' ')
    print()