# Array

- Collection of items of same data types stored at contiguous memory locations.
- Each element of an array is accessed with index starting from 0.
- Location of the next element depends on the type of data we use.

## Arrays in C/C++

- Fixed size which means we neither shrink or expand the array
- We cannot shrink an array, it is statically allocated and only the compiler can destroy that allocated memory.
- We cannot expand the array because we don't know whether the next memory location is free to allocate the new element and maintain the continuity of the elements.

## Arrays in Java

- Group of like-typed variables referred by a common name.
- Arrays in Java is different from C/C++.
- All arrays are dynamically allocated.
- Since arrays are objects, we can find their name using the `length` method which was not available in C/C++.
- The size of the array must be specified by `int` or `short` value and not `long` value.
- The size of the array cannot be altered however any array reference can be made to point to another array.
- Array can contain primitives (actual memory stored in contiguous memory locations) and non primitives (objects stored in heap).

## Advantages

- Random access to elements.
- Have better cache locality which improves performance.
- Used to implement other data structure like linked lists, stack, queues, etc.

## Disadvantages

- Fixed sized.
- Homogeneous in nature.
- Since data is stored in contiguous memory locations, insertion and deletions becomes difficult to implement.

## One dimensional array

### Declaration of Arrays

#### Syntax

```java
dataType[] referenceName;

OR

dataType referenceName[];
```

#### Examples

```java
// Array declarations
// Array of primitives
int[] intArray;
byte[] byteArray;
short[] shortArray;
long[] longArray;
float[] floatArray;
double[] doubleArray;
char[] charArray;
boolean[] boolArray;

// Array of objects
MyClass[] classArray;
Student[] aStudent;
```

- We are just declaring array variables or references above, which means that no actual array exists as of now.
- To link an array variable which the actual, physical array of integers, we must allocate the array using `new` and assign it to our reference variable.

### Instantiating/ Initialising an array

- When we declare an array, only its reference variable is created.
- We need to create and give it memory as follows:

```java
// General syntax
dataType[] referrence = new dataType[size];

// Examples
int[] intArray;
intArray = new int[5];

// Combining in one line
int[] intArray = new int[5];
```

- The above example states that we are creating a new integer array of size 5 which means it can store 5 elements whose index starts from 0 to 4.
- By default, array elements are initialsed to their default values.
- For `boolean` array, all elements will be false, for `int` array all elements will be 0, for `double` all elements will be 0.0, for `String` and `user-defined` types all elements will be null.

### Array literal

- When size and elements of the array are already know, we can use array literal as follows:

```java
int[] intArray = new int[]{1,2,3,4,5};

// new int[] is optional in latest versions
int[] intArray = {1,2,3,4,5};
```

### Accessing array elements

- Elements are accessed using index which starts from 0 to `array.length-1`.

```java
int[] intArray = {1,2,3,4,5};

System.out.println(intArray[0]); // 1
System.out.println(intArray[1]); // 2
System.out.println(intArray[2]); // 3
System.out.println(intArray[3]); // 4
System.out.println(intArray[4]); // 5
System.out.println(intArray[5]); // Error, ArrayIndexOutOfBoundsException
```
