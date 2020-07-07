# The Introduction to Python

---

## 1. Variables

### 1.1 numbers

a. int: `int()`
b. float: `float()`
c. complex numbers: `3+5j (j means i)`
d. bool: `True` `False`  

### 1.2 operators

| Operators             | Description                    |
| --------------------- | ------------------------------ |
| `[]` `[:]`            | 下标，切片                      |
| `**`                  | 指数                           |
| `~` `+` `-`           | 按位取反, 正负号               |
| `*` `/` `%` `//`      | 乘，除，模，整除               |
| `+` `-`               | 加，减                         |
| `>>` `<<`             | 右移，左移                     |
| `&`                   | 按位与                         |
| `^` `\|`              | 按位异或，按位或               |
| `<=` `<` `>` `>=`     | 小于等于，小于，大于，大于等于 |
| `==` `!=`             | 等于，不等于                   |
| `is` `is not`         | 身份运算符                     |
| `in` `not in`         | 成员运算符                     |
| `not` `or` `and`      | 逻辑运算符                     |
| `=` `+=` `-=`         | （复合）赋值运算符             |
| `*=` `/=` `%=`        | （复合）赋值运算符             |
| `//=` `**=` `&=` `|=` | （复合）赋值运算符             |
| `^=` `>>=` `<<=`      | （复合）赋值运算符             |

- multiple assignment:  

```python
a, b = 0, 1
a, b = b, a+b
```

- 注: 取整函数`round()`: 四舍六入五取偶

### 1.3 string  

- `'string1'`
- `"string2"`
- special characters can be escaped by \ : `"don\'t"` = don't
- `print(r'C:\some\name')` = C:\some\name
- strings are indexed and can be sliced
- immutable
- `len()`

---

## 2. Control Flow  

### 2.1 `if`  `elif`  `else`

### 2.2 `for`

```python
for x in list:
print(x)
```

### 2.3 `range()` function: iterable

### 2.4 `break` and `continue`

### 2.5 `pass`: do nothing

---

## 3. Data Structures

### 3.1 list

- index

```python
list1 = ['apple', 'banana', 'watermelon', 'sss', 'ghjslj'] #Definition

list1 = ['apple', 'banana', 'watermelon', 'sss', 'ghjslj']

list1[0] = 'apple'

list1[1:3] = ['banana', 'watermelon']

list1[0:] =  ['apple', 'banana', 'watermelon', 'sss', 'ghjslj']

list1[-1] = 'ghjslj'
```

- operations

```python
numbers = [3, 1, 7, 4, 90, 10]

numbers.append(17) # numbers = [3, 1, 7, 4, 90, 10, 17]  

numbers.insert(1, 20) # numbers = [3, 20, 1, 7, 4, 90, 10]

numbers.remove(7) # numbers = [3, 1, 4, 90, 10]

numbers.clear() # numbers = []

numbers.hop() # numbers = [3, 1, 7, 4, 90]

numbers.index(4) # return 3

numbers.count(1) # return 1, this function returns how many numbers do we have in the list  

numbers.sort() # numbers = [1, 3, 4, 7, 10, 90]

numbers.reverse() # numbers = [10, 90, 4, 7, 1, 3]

numbers.copy()
```

### 3.2 tuples  

- Tuples are **immutable**

```python
numbrs = (1, 2 ,3)
numbers[0]
numners.count()
numbers.index()

```

- **Unpacking**

```python
coordinates = (4, 5, 6)
x, y, z = coordinates
#this is also available in sets
```

### 3.3 dictionaries

- how to use

```python
dic_mapping = {
    'name' = 'liukuan',
    'age' = 25,
    'email' = 'liukuan0317@live.com'
}

dic_mapping['name'] #get 'liukuan'

dic_mapping.get('address', 'Xi\'an') #by using get() function, the return can be None or a default value.

d = dict() #function dict() can create a dictionary.

f = sorted(d) #the built-in function sorted() returns a list which contains the sorted keys that come from the parameter.

```

- rewrite the fibonacci function

```python
# This time we use a dictionary to store what we have computed during the computing
basic = {0: 0, 1: 1}

def fibonacci(n):
    if n in basic:
        return basic[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)
    basic[n] = result
    return result

```

- **global variables**

Global variables can be accessed from any function. But if you want to modify one global variable in a function, you have to declare it first.

```python
been_called = False

def example():
    been_called = True
```

If we run it we will see the value of been_called does not change. Because the function create a new **local variable** named *been_called*, and it goes away when the function ends.

If we want to use the global variable, we need to declare it first.

```python
been_called = False

def example():
    global been_called
    been_called = True
# now the value of been_called has been changed.
```

If a global variable refers to a **mutable value**, you can modify the value without declaring the variable:

```python
known = {0:0, 1:1}

def example4():
    known[2] = 1
```

---

## 4. Functions

```python
def function(parameters):
    pass
```

### 4.1 parameters

```python
def cheeseshop(kind, *arguments, **keywords):
pass
```

### 4.2 special parameters

```python
def func(pos1, pos2, /, pos_or_keyword, *, kw1, kw2):
def normal_arg(arg):
def pos_only_arg(arg, /):
def kwd_only_arg(*, arg):
def combined_example(pos_only, /, )
```

- keyword arguments can **only** be put after the position arguments.

### 4.3 return

If there is no return statement in a function, this function will return None as default value.

### 4.4 try except

```python
try:
    pass
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Number cannot be 0')
```

---

## 5. Classes

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def play():
        print('%s is playing with the ball' % self.name )

    def sleep():
        print('%s is sleepping' % self.name)

ZhuJiao = Gog('猪脚', '0.5')
ZhuJiao.play()
ZhuJiao.sleep()

```

- Inheritance

```python
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def play(self):
        print('%s is playing with the ball' % self.name )

    def sleep(self):
        print('%s is sleepping' % self.name)

class Dog(Pet):
    def bark(self):
        print('%s is barking' % self.name)
```

---

## 5. modules

### 5.1 import

### 5.2 packages

---

## 6. I/O

---

## 7. errors and exceptions
  
---
  
## 8. standard library  
