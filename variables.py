Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#variables
print(3+8)
11
a=10
print(a)
10
b=20
print(b)
20
x=40
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
40
z=50
print(z)
50
3=80
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=80
print(a3)
80
6a=90
SyntaxError: invalid decimal literal
b123456789=300
print(b123456789)
300
@=60
SyntaxError: invalid syntax
print(@)
SyntaxError: invalid syntax
_=50
print(_)
50
_=100
print(_)
100
if=20
SyntaxError: invalid syntax
a=4;b=9
print(a+b)
13
a,b,c=3,4
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a,b,c=3,4
ValueError: not enough values to unpack (expected 3, got 2)
p
a,b=3,4
print(a,b)
3 4
>>> a,b,c=(2,3,4)
>>> print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a,b,c=2,3,4,5,6,7
ValueError: too many values to unpack (expected 3, got 6)
>>> first name="pooja"
SyntaxError: invalid syntax
>>> first_name=("pooja")
>>> print(first_name)
pooja
>>> firstname=("pooja")
>>> print(firstname)
pooja
>>> fname="pooja"
>>> lname="ch"
>>> print(fname+lname)
poojach
>>> print(fname+" "+lname)
pooja ch
>>> print(fname,lname)
pooja ch
>>> name="pooja"
>>> print("name)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("name")
...       
name
>>> print("name")
...       
name
>>> city="vja"
...       
>>> print(city)
...       
vja
>>> a=5
...       
>>> print(a)
...       
5
>>> del a
...       
>>> print(a)
...       
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name="sai"
...       
>>> print(name)
...       
sai
>>> NAME="pooja"
...       
>>> print(NAME)
...       
pooja
>>> Name="pooja"
...       
>>> print(Name)
...       
pooja
