import array
import array as ar
from array import *

three_d = [
            [
            [1,2,3],
            [4,5,6]
            ],
            [
            [7,8,9],
            [10,11,12]
            ]
          ]

print(f"3-Demensional Array : {three_d}\n", )

for i in range(len(three_d)):           # Depth (Blocks)
    for j in range(len(three_d[i])):    # Rows
        for k in range(len(three_d[i][j])): # Columns (Individual numbers)
            print(f"three_d [{i}][{j}][{k}] = {three_d [i],[j],[k]} ")
    print() # Move to next line after completing a block
