## String Data Type
processing text data is an important task for PC users.
- think about the time you spent on using word processors such as MS words
- a large portion of online interaction are posting text messages

In Python, text is represented in by the *string data type*

A string is a sequence of characters enclosed within quotation marks(**"**) or qpostrophes(**'**)
```python
>>> str1 = 'Hello'
>>> str2 = 'ntu'
>>> print(str1, str2)
Hello ntu

>>> type(str1)
<class 'str'>

>>> type(str2)
<class 'str'>
```

## The String Data Type
- we hace encountered the `input()` function before
- `input()` takes user input string and return it to the caller
- a string is a sequence of characters
- access the individual characters in a string through indexing
    - from left to right
    - starting from 0

|b|u|l|i|m|i|a|
|:---|:---|:---|:---|:---|:---|:---|
|0|1|2|3|4|5|6|
```python
>>> str1 = 'bulimia'
>>> str1[0]
'b'

>>> str1[1]
'u'

>>> str1[2]
'l'
```
- in a string of n characters, the last character is at position **n-1**
- index from the right to left using negative indexes
```python
>>> str1[-1]
'a'

>>> str1[-2]
'i'

>>> str1[-3]
'm'
```

## Slicing String
- slicing: access a contiguous sequence of characters from a string
- Syntax: `<string>[<start>:<end>]`
    - both start and end are ints
- beginning at position start and runs up to **but doesn't include** the position end

|b|u|l|i|m|i|a|
|:---|:---|:---|:---|:---|:---|:---|
|0|1|2|3|4|5|6|
```python
>>> str1[3:5]
'im'

>>> str1[2:6]
'limi'

>>> str1[2:8]
'limia'

>>> str1[2:10]
'limia'

>>> str1[:5]
'bulim'
```

<br>

## Some string operation
- can we put two strings together into a longer string?
- **concatenation** 'glues' two strings together(+)
- **repetition** builds up a string by multiple concatenations of a string with itself(*)
```python
>>> 'spam' + 'eggs'
'spameggs'

>>> 'spam' + 'And' + 'Eggs'
'spamAndEggs'

>>> 3 * 'spam'
'spamspamspam'

>>> (3*'spam') + (5*'eggs')
'spamspamspameggseggseggseggseggs'
```

- the function `len()` will return length of a string
```python
a1 = 'career'
print(len(a1))

for ch in a1:
    print("get a character:', ch)

[output]: 
6
get a character: c
get a character: a
get a character: r
get a character: e
get a character: e
get a character: r
```

## String Operation
|operator|meaning|
|--------|-------|
|+|concatenation|
|*|repetition|
|`<string>[]`|indexing|
|`<string[:]>`|slicing|
|`len(<string>)`|length|

## String, ;ists, and Sequences
- string and list are quite similar
- both are a special kind of *sequence*
- there are some common operations that can be applied to both types
```python
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]

>>> [1, 2] * 3
[1, 2, 1, 2, 1, 2]

>>> grades = ['A', 'B', 'C', 'D']
>>> grades[0]
'A'

>>> grades[2:4]
['C', 'D']

>>> len(grades)
5
```
- string are always sequences of characters, but `list` can be sequences of arbitrary values
- `list` can have numbers, strings, or both!!!
- `list` are **mutable** -> they can be changed
- `string` cannot be changed

### example
two commonly used data format is **yyyymmdd** and **ddmmyyyy**
- yyyymmdd: 20141203, 19990212
- ddmmyyyy: 02122014, 12021999
```python
def ymd2dmy(dstr):
    '''
    convert date format from ymd to dmy
    ex: 20150312 -> 12032015
    '''
    y1 = dstr[0:4]
    m1 = dstr[4:6]
    d1 = dstr[6:8]
    return d1 + m1 + y1
```

<br>

### Example: Validating Taiwan ID String
- Taiwan ID number of a string of length 10
- first digit must be a upper case letter (A~Z)
- second digit must be 1 or 2
- the remaining digits are numbers
- example ID string: A123456789

<br>

- use a simple checksum rule to validate whether an ID is valid or not
- according to this rule, A123456789 is valid, but A123456788 is not
- we are going to see how to validate Taiwan ID

### Length and the first digit
- use `len()` to check length
```python
>>> str1 = 'A123456789'
>>> len(str1)
10
```
- how to validate the first digit?
- as mentioned before, a string is a sequence of characters
- each character is stored using some sort of internal encoding
- Traditional, English characters are stored using the **ASCII** system
- the others are punctuation and control codes used to coordinate the sending and receiving of information
- the `ord()` function return the numeric (ordinal) code of a single character
- che `chr()` function converts a numeric code to the corresponding character
- note that the internal codes are arranged so that upper case letters are occupied in a continuous chunk of code range
- A -> 65,  B -> 66,  ...., Z -> 90
- we can use this characteristic to validate the first digit
- the first internal encoding of the first digit need to be **between 65 and 90**
```python
>>> idstr = 'A123456789'
>>> code1 = ord(idstr[0])
>>> if (code1 < 65 or code1 > 90):
        print("not valid")
    else:
        print("valid")

[output]:
valid
```

1. map the first digit to a two-digit number
    - ex: A -> 10,  B -> 11,  C -> 12,... Z -> 33
    - note: not in order of A to Z
2. attach the two-digit number to the remaining 9-digit ID
3. compute a checksum by multiplying the digit at each position to a weight: [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
4. sum over all results, devide the sum by 10 and compute the remainder
5. if the remainder is 0, then it is valid. otherwise, this is a invalid ID

Example: 
- ID: A123456789
- convert 'A' into '10'
- new ID: **10**123456789
- apply the weight: [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
- 1*1 + 0*9 + 1*8 + 2*7 + 3*6 + 4*5 + 5*4 + 6*3 + 7*2 + 8*1 + 9*1 = 130
- 130/10 = 13, remainder = 0
- -> valid

mapping the first letter to a two-digit number
```python
>>> idstr = 'A123456789'
>>> code1 = ord(idstr[0])
>>> cmap = [10, 11, 12, 13, 14, 15, 16, 17, \
            34, 18, 19, 20, 21, 22, 35, 23, 24, \
            25, 26, 27, 28, 29, 32, 30, 31, 33]
    ''' 
    cmap: A~Z 對應的數字
    code1 是身分證第一個字母的 ASCII code 
    '''
>>> num1 = cmap[code1 - 65]   ## num1 is 0 for A, 1 for B, and so on(A 的 ASCII 從 65 開始)
>>> newid = str(num1) + idstr[1:]
>>> print("newid=", newid)
newid= 10123456789
```
```python
>>> weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
>>> checksum = 0
>>> for i in range(0, 11):
        checksum += weight[i] * int(newid[i])
>>> remainder = checksum % 10
>>> print("checksum=", checksum)
checksum= 130

>>> print("remainder=", remainder)
remainder= 0
```

### putting everythin together:
```python
def verify_twid(idstr):
    # check length
    if len(idstr) != 10:
        return False
    
    # check the first letter
    code1 = ord(idstr[0])
    if (ocde1 < 65 or code1 > 90):
        return False
    
    # check the remaining letters
    for i in range(1, 10):
        code2 = ord(idstr[i])
        if (code2 < 48 or code2 > 57):
            return False

    # check the second character
    code2 = ord(idstr[1])
    if (code2 < 49 or code2 > 50):
        return False

    # convert first English character to two-digit number
    cmap = [10, 11, 12, 13, 14, 15, 16, 17, \
            34, 18, 19, 20, 21, 22, 35, 23, 24, \
            25, 26, 27, 28, 29, 32, 30, 31, 33]
    num1 = cmap[code1 - 65]
    newid = str(num1) + idstr[1:]
    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    checksum = 0
    for i in range(0, 11):
        checksum += weight[i] * int(newid[i])
    if checksum % 10 == 0:
        return True
    else: 
        return False
```

<br>

## Python 講中文
- 各家電腦廠商(台灣、香港)有自己的編碼法，檔案無法流通
- 簡體與繁體問題
- 日文漢字問題
1983年，資訊工業策進會為五大中文套裝軟體所設計共通內碼，稱為**Big-5**，在軟體市場大廈一片天地，也成為中文編碼的業界標準

<br>

- 其實 ASCII 只處理英文在世界各地都是個問題
- Unicode為了解決這問題，開始發展世界統一的編碼
- 目前的作業系統幾乎都支援 Unicode
- UTF-8(Linux 預設): one, two, or three bytes for a character
- UTF-16(Microsoft Windows 預設): one or two bytes for a character

## Python Speak Unicode
- Python string support Unicode
- How to use Unicode (Chinese characters) in your Python scripts
- 告訴 Python 你的程式是甚麼編碼
    - `# -*- coding: utf8 -*-`
    - or 
    - `#!/usr/bin/python`
    - `# -*- coding: utf8 -*-` 在第二行

    ## 中文訊息
    msg=u`中文測試`
    - 字串前面加 u 表示這是 Unicode 字串
    - Python 3.x 可以不用加u，但是 Python 2.x 不加的話，後面要再 encoding 處理

<br>

## Formatting String
- we often need to provide output in a specific format
- give "pretty print"
- for example, output gasoline price using a specific format($23.4)
- output stock price with two decimal place(ex: 32.12)
- add extra "0" upfront(ex: ID: 000325)
- Generating reports following a specific format

- consider this example: we have a variable that store the price of a product, and we want to output the price with only two decimal place:
```python
prc = 13.87612
print("current price: %0.2f" % prc)

[output]: current price: 13.88
```
- the formatting specifier has the form:
    `%<width>.<precision><type-char>`
- type char can be decimal, float, string (decimal is base-10 ints)
- `<width>` and `<precision>` are optimal
- `<width>` tells us how many spaces to use to display the value. 0 means to use as much space as necessary
- if the given `<width>` is not enough, Python will expand the space until the result fits.
- `<precision>`: number of places to display after the decimal (for floating point numbers only)

<br>

- output values are right-justified by default (if the width is wider than needed)
- to left-justify use a negative width(ex: `%-10.3f`)
- you may see random digits if showing a float with long decimal places. This is caused by internal representation for float
