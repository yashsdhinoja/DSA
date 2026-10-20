import array
import array as arr
from array import *

two_D = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# Use this method when you just want to read or print the numbers without needing their row and column index numbers.
print(f"3_Demensional Array : {two_D}")
for row in two_D: # Outer Loop
    for item in row: #Inner Loop
        print(item, end=" ") 
    print() 


# Use this method in DSA when you need to know the exact row index (i) and column index (j) of an item.
print("")
for i in range(len(two_D)): # Outer Loop print with Index Number
    for j in range(len(two_D[i])): # # Inner Loop print with Index Number
        print(f"two_D[{i}][{j}] = {two_D[i][j]}")
    print()