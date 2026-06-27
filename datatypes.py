Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''codegnan'''
>>> type(e)
<class 'str'>
>>> f=5+9j
>>> type(f)
<class 'complex'>
>>> g=4j+7
>>> type(g)
<class 'complex'>
>>> h=3j
>>> type(h)
<class 'complex'>
>>> a=3+7i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d="True"
>>> print(d)
True
