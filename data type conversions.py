Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int()
>>> int(3)
3
>>> int(4.0)
4
>>> int("sai")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("sai")
ValueError: invalid literal for int() with base 10: 'sai'
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(5)
5.0
>>> float(4.0)
4.0
>>> float(3+4j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(3+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float("sai")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("sai")
ValueError: could not convert string to float: 'sai'
>>> flaot(True)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    flaot(True)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float(True)
1.0
>>> float(False)
0.0
>>> #string
>>> str(4)
'4'
>>> str(5.0)
'5.0'
>>> str('sai')
'sai'
>>> str(3+4j)
'(3+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(3)
(3+0j)
>>> complex(4.0)
(4+0j)
>>> complex("sai")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("sai")
ValueError: complex() arg is a malformed string
complex(3+4j)
(3+4j)
complex("True")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("True")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
