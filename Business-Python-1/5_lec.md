## Reading many values in a line
- in many cases we need to read a lot of values into our program
- an easy way to express an input is:
    - values will be **put in a line, separated by** white space(or commas or other **delimiters**)
    - for example, five student grades may be put in these ways:
    
    1. `98 65 57 48 80` 
    
    2. `98, 65, 57, 48, 80`
- one type of plan-text file, **CSV(comma-separated values)**, uses commas to separate each row into multiple columns
    - this is why it can be opened by MS Excel (or something similar)
- how to read this datas into your program

<br>

## Reading many values as a string
- Python is very good at string processing
- to read in a line of data, simply invoke `input()`
```python
gradeStr = input()
print(gradeStr)
```
- but gradeStr is a **string**, not five numbers!!!!
- we need to do three things:
    - **Splitting** the string into five pieces(substrings)
    - converting the five substrings into five numbers
    - put the five numbers into a **list**

<br>

## String splitting
- a string can be split by invoking `split()`
```python
gradeStr = input()   ## 1 2 3 4 5
grades = gradeStr.split()
print(grades)        ## ['1', '2', '3', '4', '5']
```

- we may choose the delimiter when invoking `split()`
```python
gradeStr = input()   ## 1, 2, 3, 4, 5
grades = gradeStr.split(',')
print(grades)        ## ['1', '2', '3', '4', '5']
```

- what is `grades`

<br>

## List

the outcome of invoking `split()` is a list

- a list is an **ordered container** that stores items
- an itemmay be an integer, a float, a string, or of other types
- Each item can be accessed by the **indexing operator []**
- the first item is indexed at **0**
```python
gradeStr = input()   ## 1 2 3 4 5
grades = gradeStr.split()
print(grades[0], grades[2] * 2)  ## 0 33
```

- the length of a list can be optained by invoking `len()`

-----------------

## List declaration
- we may **declare an empty list** as follows:
``` python
aList = []
print(aList, len(aList)) ## [] 0
```

- we may **declare a list of three 0s** as follows:
```python
aList = [0] * 3
print(aList, len(aList))  ## [0, 0, 0] 3
```

<br>

## Putting items into a list
- we may add into a list by invoking `append()`
```python
gradeStr = input()   ## 1, 2, 3, 4, 5
grades = gradeStr.split(',')
grades.append(-1)
print(grades)        ## ['1', '2', '3', '4', '5', '-1']
```
- note that the last item is an integer, not a string

<br>

## Traversing a list in a loop
```python
gradeStr = input()   ## 1 2 3 4 5
gradeList = gradeStr.split()
print(gradeList)     ## ['1', '2', '3', '4', '5']
grades = []

for g in gradeList:
    grades.append(int(g))

print(grades)        ## [1, 2, 3, 4, 5]
```

## Tic-Tac-Toe
let write a program to detect the winner of a tic-tac-toe game

```python
game = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]  ## 2-dim list

for i in range(3):
    if game[i][0] == game[i][1] and game[i][1] == game[i][2]:
        print("winner: ", game[i][0])
        break
```

--------------

## List operation

| Method | Meaning |
| ---    | ---     |
| `<list>.append(x)` | add element **x** to end of list|
|`<list>.sort()` | sort the list |
|`<list>.reverse()`|reverse the list|
|`<list>.index(x)`|return the index of first occur x|
|`<list>.insert(i, x)`|insert x into an index i|
|`<list>.count(x)`|return the number of occurrences of x index|
|`<list>.remove(x)`|deletes the first occurrences of x in list|
|`<list>.pop(x)`|delete the ith element of the list and returns its value|

<br>

## List copying
```python
aList = [1, 2, 3]
anotherList = aList

anotherList[0] = 5
print(aList)   ## [5, 2, 3]
```

- why `aList` is modified?
- in Python, a list variable is a 'reference' referring to a set of values
    - copying a list is just **copying the reference**, not those values
    - modifying the values through different references has the same effect

![lis](picture/list.png)

- 要避免這種事發生，要另外開一個空的list，然後用迴圈 aList 的 element append 到 bList

