## Computer programming

what are computer programs?
* elements working in computers
* also known as software
* a structure combination of data and instructuions used to operate a computer to produce a specific result

Strength: high-speed computing, large memory, etc

Weakness: people(programmers) need to tell them what to do

How may a programmer tell a computer what to do?
* programmers use **programming languages** to write codes line by line and construct "computer programs"

**Running a program** means executing the instructions line by line and achieve the programmer's goal

<br>

## Programming languages
* people and computers talk in programming languages.
* a programming language may be a **machine language(機器語言)**, an **assembly language(組合語言)**, or a **high-level language**
    - machine and assembly language: control the hardware directly, and but hard to read and program
    - high-level language: easy to read and program, but need a "translator"
* Most application software are developed in **high-level-languages**
    - the language we study in this course, Python, is a high-level language.
    - some others: C++, C, Basic, Quick Basic, Visual Basic, Fortran, COBOL, Pascal, Perl, Java, C#, PHP, Matlab, Objective C, R, etc

<br>

## Python
* Python was invented by Guido van Rossum around 1996:
    - was just something to do during the Christmas week
* Python is very good for beginners
    - it is simple
    - it is easy to start
    - it is powerful

<br>

## Interpreting a Program
* an **interpreter** translates programs into assembly programs.
    - for other high-level programs, a **compiler(編譯器)** is used
    - Python uses an interpreter(直譯器)
* compiler: 必須寫一個完整的程式才能被編譯
* interpreter: 一個 statement 就可以被執行
* an interpreter interpret a program line by line
* we may write Python in the **interactive mode**
    * input one line of program, then see the result
    * input the next line, then see the next result
    * the statements should be entered after **prompt** 

<br>

* we may also write Python in the **script mode**
    - write several lines in a file, and then interpret all the lines one by one at a single execution.
* A programming language using an interpreter is also called a **scripting language**. ex: R

<br>

## How to Run Python
* to state Python online:
    - https://www.python.org/ or other similar websites.
    - go to https://www.python.org/downloads/, download, double click, and then click and then click... and then you are done.
* to try interactive mode:
    - open your **console(the command line environment)** and type **python** to initiate the interactive mode.
    - you may need to set up your "PATH" variables
* to run Python on IDLE(Python GUI)
    - clicks its icon and then play with the prompt
    - do 'File -> new File' to write and execute a script
* to write Python on an **editor** and interpret a script with the interpreter:
    - open a good text editor, write a script, save it(.py)
    - open a **console**, locate your script file(.py), interpret it with the instruction **python**, and see the result

<br>

環境變數: 設定環境變數 -> 設定我的電腦，讓我不論在任何地方輸入某個指令(ex: python)，他都會去找找看那個資料夾下有沒有那個程式，沒有的話就會去設定環境變數的地方一個一個找

<br>

-----------------------------

## Program
### First program
```python
print("hello world!")
```
- `print` is a **function**: print out whatever after it on the screen
- `hello world!` is an **operand**: a message to be printed out
- in Python, each statement must be put in **a single line** in your editor

<br>

## A newline character
inside a computer, everything is **encoded**
- in particular, each character has a corresponding number representing it.
- "creating a new line" actually means "printing out **a newline character**"
- ex: 
```python 
print("長跪讀素書，書中竟何如。\n上言加餐食，下言長相憶。")
```
- that `\n` is a newline character

<br>

## Basic arithmetic
* computer are good at doing **computation**
* we may use operators `+, -, *, / and //` to do addition, subtraction, multiplication, floating-point division, floor division

<br>

## Second program
### input()
- a function `input` accept data input(by user or other programs) from the console input
- in order to get input, we need to first prepare a "**container**" for the input data. the thing we need is a **variable**
- when we use a single variable to receive the data, the syntax is:
`variable = input()`

## Variable and data types
a variable is a container that stores a value
- once we declare a variable, the system allocates a **memory space** for it 
- a value may then be stored in that space

a variable has its **data type**
- int, float, string
- three major attributes of a variable:
    - Type
    - Name
    - Value

before we use a variable, we must first **declare** it
- we need to specify its name
- we need to specify its data type, initial value, or both

```python
a = 689
b = 8.7
c = "hi everyone"
print(type(a))
print(type(b))
print(type(c))
```
a variable may be overwritten:
```python
a = 689
a = 8.7
print(type(a))
```

python 不需要事先指定資料型態，所以每次執行都要看一次變數內的值的資料型態，再去改變 type，這也導致 python 執行起來速度較慢的原因

sometime we have no idea about an initial value
```python
a = int()
b = float()
c = "" ## 空字串
```

this is our second program
```python
num1 = int()
num2 = int()
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```
- we allow user to enter two number
- we declare two variables to receive the inputs
- we then use the input function to read input values into the variables
- we then sum them up and print out the sum
- `input()` 預設的 return 值是字串，所以再用`int()`強制轉成 int-type

-----------------------------

## Debugging
### Syntax errors vs. logic errors
* syntax errors: occors when the program does not follow the standard of the programming language
* logic error: occor when the program does not run as the programmer expect
    - programmers must detect logic errors by themselves
    - the progress is called debugging















