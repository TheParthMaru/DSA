def find_second_largest(arr: list):
    if len(arr) < 2:
        return -1
    
    # Initializing with -ve infinity 
    largest = float('-inf')
    second_largest = float('-inf')

    for number in arr:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    if second_largest == float('-inf'):
        return -1
    return second_largest



arr = [int(element) for element in input().split()]
print(find_second_largest(arr))