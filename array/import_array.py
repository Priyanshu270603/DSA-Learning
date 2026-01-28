from array import *

# val = array('i', [10, 20, 30, 40, 50])
#
# for i in val:
#     print(i, end = " ")

arr = array('i', [10, 11, 12, 13, 15, 19])

arr.insert(4, 14)
arr.append(20)
for i in range(0, len(arr)):
    print(arr[i], end = " ")