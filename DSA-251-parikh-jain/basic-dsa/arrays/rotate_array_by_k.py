'''
Time complexity: O(n)
Space complexity: O(1)

Note: We are rotating array by k towards left
'''

def rotate_by_k(array, k):
    if k > len(array):
        k = k % len(array)

    reverse(array, 0, k-1) # Reverse first k elements
    reverse(array, k, len(array)-1) # Reverse remaining elements
    reverse(array, 0, len(array)-1) # Reverse the entire array

    
def reverse(array,start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

array = [int(element) for element in input().split()]
k = int(input())

rotate_by_k(array,k)

print(*array)