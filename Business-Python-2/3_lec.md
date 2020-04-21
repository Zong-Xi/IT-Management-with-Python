## Data Structure in Python
- a data structure is a particular way of organizing data in a computer so that it can be used efficiently
- Python has many built-in data structure
    - list
    - tuple
    - dictionary
    - set
    - datetime (to handle date and time data)
    - ... and more

<br>

## Tuple
- same as lists, but:
    - immutable
    - enclosed in parentheses
    - a tuple with a single element **must** have a comma inside the parentheses: `a = (11,)`
```python
mytuple = (11, 22, 33)
mytuple[0]    # 11
mytuple[-1]   # 33
mytuple[0:1]  # (11,)  圓括號表示 tuple
```

## Why
- it is clear that `[11]` and `11` are different (list of one element and integer 11)
- but:
    - `(11)` is an acceptable expression
    - `(11)` **without the camma** is the integer 11
    - `(11,)` **with a comma** is a tuple containing the integer 11

## Tuples are immutable
```python
mytuple = (11, 22, 33)
save = mytuple
mytuple += (44,)
print(mytuple)  # -> (11, 22, 33, 44)
print(saved)    # -> (11, 22, 33)
```
```python
mytuple += 55
# 會報錯 -> 不允許此操作
```

## Sorting tuples
```python
atuple = (33, 22, 11)
atuple.sort()  # 會報錯 -> tuple 不能做更改
```
```python
atuple = sorted(atuple) 
print(atuple)  # [11, 22, 33]  return a list !!!
'''
用此種方法相當於對 tuple 內的數值做排序，因此output是 list
'''
```

## Converting Lists into Tuples
```python
alist = [11, 22, 33]
atuple = tuple(alist)
print(atuple)  # (11, 22, 33)
```
``` python
newtuple = tuple('hello world!')
print(newtuple)  # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!')
```

<br>

## Zipping two Variables
- zip: make an iterator that aggregates elements from each of the iterables
```python
newid = '10123456789'
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

for apair in zip(newid, weight):
    print(apair)
'''
會配對輸出:
('1', 1)
('0', 9)
('1', 8)
('2', 7)...
'''
```

## The Lambda Operator
- lambda is a way to define simple function
```python
def f1(x):
    return x**2
```
```python 
## use lambda
f2 = lambda x: x**2
print(f2(8))   # output: 64
```

## The Map Operator
- 在 `list` 或是 `tuple` 當中常常有很多元素，若這些元素都要執行相同的操作，常常會用 `map` 這個函數，一般會搭配 `lambda` 使用
- `map()` provides an easy way to apply an function to a list or tuples
- consider the situation when we want to square all numbers in a list
```python
list1 = [3, 5, 1.2, 4, 9]
out1 = map(f1, list1)  # f1 如上面的定義
print(out1)  # [9, 25, 1.44, 16, 81]
```
```python
out2 = map(lambda x: x**2, list1)
print(list(out2))   # [9, 25, 1.44, 16, 81]
```

<br>

## Dictionary Data Structure
- in Python, a dictionary is mapping between a set of indices(**keys**) and a set of **values**(the items in a dictionary are key-value pairs)
- keys can be any Python data type(because keys are used for indexing, they should be **immutable**)
- values can be any Python data(values can be **mutable or immutable**)

## Creating a Dictionary
```python
eng2cn = dict()
print(eng2cn)   ## {}

eng2cn['one'] = '一'
eng2cn['two'] = '二'
eng2cn['three'] = '三'
eng2cn['four'] = '四'
print(eng2cn)     ## {'one': '一', 'two': '二', 'three': '三', 'four': '四'}
```
```python
eng2cn = { 'two': '二', 'three': '三', 'four': '四'}
print(eng2cn)   ## {'two': '二', 'three': '三', 'four': '四'}
```
- in general, the order of items in a dictionary is unpredictable
- 字典的關鍵是 `key` 與 `value` 的對應，順序一般不重要
- Dictionaries are indexed by keys(including integers)

## Dictionary indexing
```python
print(eng2cn['one'])   ## 一
```
```python
if 'five' in eng2cn:
    print(eng2cn['five'])
## None
```

## the `in` operator
- note that the `in` operator works differently for dictionaries than for other sequences
- for **strings**, **lists**, and **tuples**, `x in y` means whether x is an item in the sequence
- for **dictionary**, `x in y` checks whether x is a `key` in the dictionary

## Keys and Values
- the `keys` method returns a list of the keys in a dictionary
- the `values` method return a list of the values
```python
print(eng2cn.keys())   ## dict_keys(['two', 'three', 'four'])
print(eng2cn.values)   ## dict_values(['二', '三', '四'])
```
- the `items` method return a list of tuple pairs of the key-value pairs in a dictionary
```python
print(eng2cn.items())
## dict_items([('two', '二'), ('three', '三'), ('four', '四')])
```
### example
```python
def histogram(seq):
    d = dict{}
    for element in seq:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d

h = histogram('brontosaurus')
print(h)
'''
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
'''
```
another way to output the result
```python
def print_hist(hist):
    for key in hist:
        print(key, hist[key])

h = histogram('brontosaurus')
print_hist(h)
```

change the print_hist function:
```python
def print_hist2(hist):
    for key, value in hist.items():
        print(key, value)

h = histogram('brontosaurus')
print_hist2(h)
```

sorting the keys
```python
def print_hist3(hist):
    keys = hist.keys()
    for key in sorted(keys):
        print(key, hist[key])

h = histogram('brontosaurus')
print_hist3(h)
```
### Using lists as values
- inverting the mapping: what are the letters with a given count?
```python
def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv
```

<br>

## Set
- identified by **curly braces**
    - {'Marry', 'Bob', 'John'}
    - {'Dean'} is a **singleton**
- set can only contain **unique element**
    - duplicates are eliminated
- **Immutable** like tuples and strings
```python
aset = {11, 22, 33}
bset = aset   ## 此時 aset, bset 都是指向{11, 22, 33} 這塊記憶體

aset = aset | {55}  ## 此時 python 會建立一塊新的記憶體，為{11, 22, 33, 55}，再將aset 指向該記憶體
## 這時 aset 與 bset 就分別指向不同的記憶體了
```
- set不能取第幾個，在set裡面順序是沒有意義的
```python
myset = {'大象', '長頸鹿', '蝸牛'}
myset[0]  ## 會報錯
```

```python
alist = ['大象', '長頸鹿', '蝸牛', '大象', '猴子']
aset = set(alist)
print(aset)  ## {'猴子', '大象', '長頸鹿', '蝸牛'} 會將重複的東西拿掉
```
- set does not support '+' operation

### Boolean operation on Sets
```python
aset = {11, 22, 33}
bset = {12, 23, 33}

## union
aset | bset

## intersetion
aset & bset

## difference
aset - bset

## symmetric difference  (在a，但不在b中)
aset ^ bset
```

<br>

## DateTime
### Handling date and time in Python
- Python has a build-in library 'datetime' that can process date and time data (neet to do `import datetime`)
```python
import datetime
d1 = datetime.datetime(2005, 5, 3)
```

```python
d2 = datetime.datetime(2017, 2, 5, 8, 5, 20)  ## 包含到幾分幾秒
d2.date()  # 輸出日期
d2.time()
d2.date().weekday    # 輸出那天是星期幾
datetime.date.today  # 輸出今天的日期
```
### difference of datetime
```python
d3 = datetime.datetime(1998, 2, 5, 8, 5, 20)
d4 = datetime.datetime(1999, 2, 1, 22, 4, 15)
diff = d4 - d3
print(diff)  ## 361 days, 13:58:55
diff.days     # 361
diff.seconds  # 50335
```

### time shifting by timedelta
```python
diff2 = datetime.timedelta(days=3, seconds=4)
d5 = datetime.datetime(2000, 1, 1, 0, 0, 0)
d6 = d5 + diff2
print(d6)  ## 2000-01-04 00:00:04
```

### datetime - string
```python
d7 = datetime.datetime(2002, 5, 2, 13, 15, 45)
print(str(d7))
print(d7.strftime('%Y-%m-%d'))   ## 2002-05-02
print(d7.strftime('%B %d, %Y'))  ## May 02, 2002
print(d7.strftime('%Y-%m-%d %H:%M:%S'))  ## 2002-05-02 13:15:45
print(d7.strftime('%Y-%m-%d %I:%M:%S %p, %A'))  ## 2002-05-02 01:15:45 PM, Thursday
```

```python
# string to datetime
dstr = "2007-03-04 21:08:12"
d9 = datetime.datetime.strptime(dstr, "%Y-%m-%d %H:%M:%S")
d9  ## datetime.datetime(2007, 3, 4, 21, 8, 12)
```

<br>

## Reading and Writing Files
- reading and writing files are useful operations for software
- read data files -> process -> write output to files
- read in configure files on starting an application 
- write/update configure files on exit
- caching data that is too big for memory

### File Processing
- typical file manipulation routine:
    - open a file
    - read or write contents from/to the file
    - close the file
- when done with the file, it needs to be closed. closing the file causes any outstanding operations and other bookkeeping for the file to be completed
- in some cases, not properly closing a file could result in data loss
- working with files in Python
    - associate a file with a variable using the open function
    - `<filevar> = open(<name>, <mode>, encoding=<encoding>)`
    - name is a string with the actual file name on the disk
    - `<filevar>` is often called 'file handler'
    - for text file, the mode is either **'r'** of **'w'** depending on whether we are reading or writing the file
    - for non-text files, the mode is **'rb'** or **'wb'** for reading or writing the file
    - `<encoding>` is the encoding to be used, default to system setting
    - example: `infile = open("numbers.dat", "rb")`

### File name and Path
- you need to specigy the full path(absolute path: 絕對路徑) so that Python can always access the file correctly
- absolute path can be found by opening the containing the file, and clicking the folder name.
- in this example, the absolute path is:`F:\ptt module 2 2018\py23\risk.txt`
- for windows users: because of historical reason, Windows System use backslash '\' in file path. Other operating systems use slack '/'
- backslash has a special meaning in string representation
- backslash is "escape character"
- the character following escape character are interpreted differently
- for example, if you are using double quote, and you need to define a string with double quote, then you can use backslash to achieve this
- in Python, you cannot use Windows absolute path directly. insteadm you need to change backslash to double backslash
- ex: `F:\\ptt moudle 2 2018\\py23\\risk.txt`

```python
fn1 = 'F:\\ptt moudle 2 2018\\py23\\risk.txt'
fh1 = open(fn1, 'r', encoding = 'utf-8')
```
- to read a file, use the `open()` function
- set mode to 'r' for reading text file, 'w' for writing, 'r+' for both reading and writing
- set mode to 'a' for appending
- set file encoding by: `encoding='utf-8'`
- for binary file, use rb, wb
- to close a file, use `fh1.close()`
- to read a line, use for loop directly, or `fh1.readline()`
```python
fh1 = open(fn1, 'r', encoding='utf-8')
linecount = 0
for aline in fh1:
    linecount += 1
    if len(aline) < 75:
        print("%02d:%s" % (linecount, aline.strip()))
    else:
        print("%02d:%s...(truncated" % (linecount, aline[0:75]))
fh1.close()
```

### Writing to a File
use the `write()` function of a file handler to write data
```python
name = input("Enter your name: ")
dob = input("Enter your birthday: ")

fn2 = "F:\\ptt module 2 2018\\py23\\arec.txt"
fh2 = open(fn2, "w", encoding='utf-8')

fh2.write(name + "\n")
fh2.write(dob + "\n")
fh2.close()
```

<br>

## Expecting and Handling Exception
- errors detected during execution are called **exceptions**
- if we do nothing, a script will stop executing on the first error encountered
- this may not be our intention. we may want to:
    - display useful information and terminate gracefully
    - try something different
    - silently terminate the script
- to achieve this, we need to handle errors as it happens

### Try-Except Blocks
- put codes that may raise exceptions to a try block
- put codes that handle exceptions to an except block
- if nothing went wrong, only the try block will be excuted
- if an exception occurs during execution of the try clause, the rest of the clause is skipped. Instead, the except clause is executed
```python
x = 0
try:
    inv = 1 / x
except Exception as inst:
    inv = 0
    print("!Exception encountered!")
    print(type(inst))
    print(inst)
print("\n===\n inv = %f" % inv)
```
```python
while True:
    try:
        x = int(input("請輸入數字: "))
    except ValueError:
        print("輸入非數字，請重新輸入")
print("得到數字:%d" % x)