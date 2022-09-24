'''
Sqrt (or Square Root) Decomposition Technique is one of the most common query optimization technique 

The key concept of this technique is to decompose given array into small chunks specifically of size sqrt(n).

Time Complexity: In the worst case our range can be 0 to n-1(where n is the size of array and assuming n to be a perfect square). 
O(sqrt(n))
'''

from math import sqrt
MAXN = 10000
SQRSIZE = 100

arr = [0]*(MAXN) # original array
block = [0]*(SQRSIZE) # decomposed array
blk_sz = 0 #block size

def update(idx,val):
    blkno = idx // blk_sz
    block[blkno] += val - arr[idx]
    arr[idx] = val

def query(l,r):
    sum = 0
    while (l < r and l% blk_sz !=0 and l!=0):
        sum += arr[1]
        l += 1
    while (l + blk_sz -1 <= r):
        sum += block[l//blk_sz]
        l += blk_sz
    while (l <= r):
        sum += arr[l]
        l += 1
    return sum

def preprocess(input,n):
    blk_id = -1
    global blk_sz
    blk_sz = int(sqrt(n))
    for i in range(n):
        arr[i] = input[i]
        if (i % blk_sz == 0):
            blk_id += 1

        block[blk_id] += arr[i]

# Driver code
 
# We have used separate array for input because
# the purpose of this code is to explain SQRT

input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(input)
 
preprocess(input, n)
 
print("query(3,8) : ",query(3, 8))
print("query(1,6) : ",query(1, 6))
update(8, 0)
print("query(8,8) : ",query(8, 8))


