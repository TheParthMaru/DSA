# Find the largest three distinct elements in an array

- Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1).

## Example

```
Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
```

## Explanation of algorithm

- Initialize largest, secondLargest and thirdLargest to Integer.MIN_VALUE.
- If elements are less that 3, then return with "invalid input".
- If elements are greater than 3, iterate over the array and check if current element is greater than largest.
- If yes, then store secondLargest value to thirdLargest, largest to secondLargest and finally current element to largest.
- If current element is greater than secondLargest, then add current secondLargest value to thirdLargest and update secondLargest value with current element.
- If current element is greater than thirdLargest, simply update thirdLargest with current element.

## Complexity

- Time complexity: O(n)
- Space complexity: O(1)

## Solution

```python
def largest_three_distinct_elements(array):
    largest = float("-inf")
    second_largest = float("-inf")
    third_largest = float("-inf")

    if len(array) < 3:
        print("Invalid number of elements")
        return

    for element in array:
        if element > largest:
            third_largest = second_largest
            second_largest = largest
            largest = element
        elif element > second_largest and element != largest:
            third_largest = second_largest
            second_largest = largest
        elif element > third_largest and element != largest and element != second_largest:
            third_largest = element

    if largest == float("-inf") or second_largest == float("-inf") or third_largest == float("-inf"):
        print("Does not exists")
    else:
        print(largest, second_largest, third_largest)
```

# 
