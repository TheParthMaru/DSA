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

# Find Second largest element in an array

- Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array.

## Example

```
Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: Second largest = 34

Input: arr[] = {10, 5, 10}
Output: Second largest = 5

Input: arr[] = {10, 10, 10}
Output: Does not exists
```

## Explanation of algorithm

- First check if length of array < 2, then simply print "Invalid number of elements" and return.

- If length of array > 2, then largest = secondLargest = -ve infinity.

- Traverse through array and check if current element is greater than largest.

- If yes, then first add largest value to secondLargest and update largest with current element.

- Check if current element > secondLargest and currentElement != largest.

- If yes then update secondLargest with current element.

- If our secondLargest was updated, then only return its value else return does not exists because all the elements will be equal.

- SecondLargest would have been updated if all the elements are not equal.

## Complexity

- Time complexity: O(n)
- Space complexity: O(1)

## Solution

```python
def secondLargestElement(arr):
    if len(arr) < 2:
        print("Invalid number of eleents")
        return

    largest = float("-inf")
    secondLargest = float("-inf")

    for element in arr:
        if element > largest:
            secondLargest = largest
            largest = element
        elif element > secondLargest and element != largest:
            secondLargest = element

    if secondLargest == float("-inf"):
        print("Does not exists")
    else:
        return secondLargest
```

# 
