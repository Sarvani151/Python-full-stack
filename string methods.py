Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python course"
len(a)
13
b=""
len(b)
0
b=" "
len(b)
1
#count()
a="twinkle twinkle little star"
count("twinkle")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    count("twinkle")
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("i")
3
a.count("t")
5
#find a string
a="python"
a.find("t")
2
a.find("n")
5
b="hello"
b.find("1")
-1
b.find("l")
2
b[2:4]
'll'
#escape sequences
#/n-
#\n ->new line
#\t ->tab space
a="name\nmobilenumber\nmailid\ncollege\nbranch
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobilenumber\nmailid\ncollege\nbranch"
a
'name\nmobilenumber\nmailid\ncollege\nbranch'
print(a)
name
mobilenumber
mailid
college
branch
b="name:sarvani\nmobilenumber:8045678931\nemailid:sarvani@gmail.com\ncollege:crrcoe\nbranch:cse"
print(b)
name:sarvani
mobilenumber:8045678931
emailid:sarvani@gmail.com
college:crrcoe
branch:cse
#replace
a="wait until you suceed"
a.replace("wait","work")
'work until you suceed'
#upper()
a="python"
a.upper()
'PYTHON'
b="HAI"
b.lower()
'hai'
a="python"
a.captalize
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.captalize
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a.captalize()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'
a="sarvani"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False
a.isalnum()
True
>>> a="1234"
>>> a.isdigit()
True
>>> a.isalpha()
False
>>> a="sarvani123"
>>> a.isalum()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.isalum()
AttributeError: 'str' object has no attribute 'isalum'. Did you mean: 'isalnum'?
>>> a.isalnum()
True
>>> a="sai_123"
>>> a.isalnum()
False
>>> a.isdigit()
False
>>> a.isalpha()
False
>>> a="java"
>>> a.startswitch("j")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.startswitch("j")
AttributeError: 'str' object has no attribute 'startswitch'. Did you mean: 'startswith'?
>>> a.startswith("j")
True
>>> a.endsswith("a")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.endsswith("a")
AttributeError: 'str' object has no attribute 'endsswith'. Did you mean: 'endswith'?
>>> a.endswith("a")
True
>>> #strip(
>>> #strip()
>>> a="     sri      "
>>> a.strip()
'sri'
>>> a.lstrip()
'sri      '
>>> a.lstrip()
'sri      '
>>> a.rstrip()
'     sri'
>>> #split
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am in class room"
>>> b.split()
['i', 'am', 'in', 'class', 'room']
>>> #join()
>>> b="vja","hyd","vzg"
>>> "".join(b)
'vjahydvzg'
>>> " ".join(b)
'vja hyd vzg'
>>> "k".join(b)
'vjakhydkvzg'
>>> a="python"
>>> "a".join(a)
'payatahaoan'
>>> " ".join(a)
'p y t h o n'
