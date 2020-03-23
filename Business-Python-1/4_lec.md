## The ternary if operator
- in many cases, what to do after an **if-else** selection is simple
- the **ternary if operator** can be helpful in this case
```python
operation_A if condition else operation_B
```

<br>

if, elif, while, 這些已經會了

<br>

## Case study: single-product pricing
- we shell a product to a small town
- the demand of this product is q = a - bp
    - a is the base demand
    - b measures the price sensitivity of the product
    - p is the unit price to be determined
- let c be the unit production cost
- given a, b, c, how to solve
    
    $\max_p(a - bp)(p - c)$

to find an optimal (profit-maximizing) price p*?

<br>

- where there is an analytical solution p* = (a + bc) / 2b
- let's assume that the price can only be an integer
```python
a = int(input("base demand = "))
b = int(input("price sensitivity = "))
c = int(input("unit cost = "))

maxProfit = 0
optimalPrice = 0
for p in range(c+1, a//b):
    profit = (a - b*p) * (p - c)
    # print(p, profit)

    if profit > maxProfit:
        maxProfit = profit
        optimalPrice = p
    else:
        break

print("optimal price = " + str(optimalPrice))
print("maximized profit = " + str(maxProfit))
```
- note that the profit as a function of price is first increasing and then decreasing
    - once a price results in a profit that is lower than the maximum profit, all further prices cannot be optimal
    - we may revise our program accordingly

## Precision can be a big issue
```python
import math

bad = 0
for i in range(100):
    f = pow(i, 1/2)
    print(i, f * f, end = " ")
    if f * f != i:
        print("!!!")
        bad += 1
    else:
        print()

print("bad precision:", bad)
```
- precision can be a big issue when we use floating-point values
- as modern computers store values in bits, most **decimal fractional numbers** can only be **approximated**
- therefore, that `f = pow(i, 1/2)` does not make **f** storing the **exact value** of square root of **i**. There must be some error

<br>

- remedy: 'imprecise' comparisons
```python
if abs(f * f - i) > 0.0001:
    print("!!!")
    bad +=1
else:
    print()
```
- the error tolerance can be neither too large nor too small, it should be set according to the property of your own problem



