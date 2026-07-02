Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#concatenation
a="sarvani"
b="singareddy"
print(a+b)
sarvanisingareddy
print(a+" "+b)
sarvani singareddy
a="code"
b="gnan"
print(a+b)
codegnan
fname=sarvani
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fname=sarvani
NameError: name 'sarvani' is not defined
fname="sarvani"
lname="singareddy"
print(fname+lname)
sarvanisingareddy
print(fname+" "+lname)
sarvani singareddy
print(fname.title()+" "+lname.title())
Sarvani Singareddy
print((fname+" "+lname).title())
Sarvani Singareddy
a=2
b=4
print(a+b)
6
print("the sum is",a+b)
the sum is 6
city="vja"
print("the city is",city)
the city is vja
a="motu"
b="pathulu"
print("hello {} {}".fprmat(a,b))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print("hello {} {}".fprmat(a,b))
AttributeError: 'str' object has no attribute 'fprmat'. Did you mean: 'format'?
print("hello {} {}".format(a,b))
hello motu pathulu
>>> print("hello {}  {}".format(a,b))
hello motu  pathulu
>>> print("hello {} hello {}.format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {} hello {}".format(a,b))
...       
hello motu hello pathulu
>>> a="sita"
...       
>>> b="ram"
...       
>>> print(f"hello {a} {b}")
...       
hello sita ram
>>> print(f"hello {a}{b}")
...       
hello sitaram
>>> print(f"hello {a} hello {b}")
...       
hello sita hello ram
>>> a=3
...       
>>> b=6
...       
>>> print("multiply {}{}".format(a,b))
...       
multiply 36
>>> print("a*b {}{}".format(a,b))
...       
a*b 36
>>> print("a*b {}{}.format(a*b)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> a*b
...       
18
>>> print(a*b {}{}.format(a,b))
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=4
...       
>>> b=5
...       
>>> a*b
...       
20
>>> c=a*b
...       
>>> print("the product is {}".format(c))
...       
the product is 20
>>> print("the product is {}".format(a*b))
...       
the product is 20
>>> print(f"the product is {c}")
...       
the product is 20
>>> print(f"the product is {a*b}")
...       
the product is 20
>>> print("the product is {}{}".format(c))
...       
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print("the product is {}{}".format(c))
IndexError: Replacement index 1 out of range for positional args tuple
