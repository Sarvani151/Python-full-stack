Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#arithmetic
a=5
b=4
print(a+b)
9
print(a-b)
1
print(a*b)
20
print(a//b)
1
print(a/b)
1.25
print(a**b)
625
print(a%b)
1
#assignment
a=6
b=3
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
9
a-=2
a
7
a*=b
b
3
a
21
a//=3
a
7
b
3
b//=3
b
1
b/=2
b
0.5
b**=5
b
0.03125
a**=b
a
1.0626966554348731
a%=b
a
0.00019665543487312753
b
0.03125
a=10
a%=b
a
0.0
#comparision
a=6
b=4
a<b
False
a>b
True
b<a
True
b>a
False
a=b
a==b
True
a>=b
True
a<=b
True
b>=a
True
b<=a
True
b
4

.
b>=a
True
b<=a
True
b!=a
False
a!=b
False
b>a
False
b<a
False
b>=a
True
b
4
<
#logical
a=8
b=5
a<b and b>a
False
a<b and a>b
False
a<b and b>A
False
a><b
SyntaxError: invalid syntax
a<b
False
a<=b and b>=a
False
a>=b or a<b
True
a<=b or a>=b
True
a!=b or a==b
True
a>b and b>a
False
not True
False
not False
True
#identity
a=6
type(a) is int
True
type (a) is float
False
type(a) is dtr
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type(a) is dtr
NameError: name 'dtr' is not defined. Did you mean: 'dir'?
type(a) is str
False
a=5.6
type (a) id float
SyntaxError: invalid syntax
type (a) is float
True
a="sai"
type(a) is dtr
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    type(a) is dtr
NameError: name 'dtr' is not defined. Did you mean: 'dir'?
type(a) is str
True
type(a) is float
False
type(a) is boolean
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    type(a) is boolean
NameError: name 'boolean' is not defined
type(a) is bool
False
a=3+4j

type(a) is complex
True
type(a) is bool
False
a=5
type(a) is bool
False
a=True
type (a) is bool
True
a=false
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a=false
NameError: name 'false' is not defined. Did you mean: 'False'?
a=False
type(a) is bool
True
#membership
a=3,4,5,6,7,8,9,10
8 in a
True
2 in a
False
b=5
5 in b
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    5 in b
TypeError: argument of type 'int' is not a container or iterable
#BITWISE
a=2
b=4
a&b
0
a=5
b=7
a&b
5
bin
<built-in function bin>
(
bin(2)
'0b10'
>>> bin(3)
'0b11'
>>> bin
<built-in function bin>
(
>>> bin(4)
'0b100'
>>> bin(5)
'0b101'
>>> a=3
>>> b=5
>>> a|b
7
>>> a=4
>>> b=8
>>> a|b
12
>>> #not
>>> a=2
>>> -(a+1)
-3
>>> ~a
-3
>>> a=5
>>> ~a
-6
>>> a=9
>>> ~a
-10
>>> b=-11
>>> ~b
10
>>> c=-15
>>> ~c
14
>>> #^
>>> a=6
>>> b=9
>>> a^b
15
>>> #^=opposites=1
>>> a=5
>>> b=7
>>> a^b
2
>>> #shift
>>> a<<2
20
>>> a=3
>>> a<<2
12
>>> a<<3
24
>>> a=4
>>> a>>2
1
>>> bin(4)
'0b100'
>>> a=9
>>> a>>3
1
>>> a<<3
72
>>> a=2
>>> a<<3
16
