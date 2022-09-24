def revers_arr(arr:list,start:int,end:int):
    while (start < end):
        t = arr[start]
        arr[start] = arr[end]
        arr[end] = t
        start +=1
        end = end -1

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
revers_arr(A, 0, 5)
print("Reversed list is")
print(A)


def reverse_l(A,start,end):
    if start >= end:
        return
    A[start],A[end] = A[end],A[start]
    reverse_l(A,start +1,end-1)

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_l(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer
