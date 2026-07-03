Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,5.6,"pooja",8+9j,True,False)
print(a)
(4, 5.6, 'pooja', (8+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(8+9j)
3
a.count(True)
1
#sets
a=[3,6.7,"python",True,False}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a={3,6.7,"python",True,False}
print(a)
{False, True, 3, 'python', 6.7}
type(a)
<class 'set'>
b={6,9,12,6,5,20,8,9,5,6}
print(b)
{20, 5, 6, 8, 9, 12}
#types
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#superset
a={4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
#union
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection
a={3,4,5,6,7,8,9}
b=
SyntaxError: invalid syntax
b={7,8,9,10,11,12,13}
a.intersection(b)
{8, 9, 7}
b.intersection(a)
{8, 9, 7}
#differnce
a={10,11,12,13,14,15,16}
b={6,7,8,12,13,14,15,16,17}
a.difference(b)
{10, 11}
b.differnce(a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b.differnce(a)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
b.difference(a)
{8, 17, 6, 7}
#symmetric difference
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
b.symmetric_difference(a)
{2, 3, 4, 10, 11}
#update
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update
<built-in method update of set object at 0x10939a180>
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection_update
a={1,3,5,7,8,9,10}
b={2,4,6,7,10,11,12}
a.intersection.update(b)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.intersection.update(b)
AttributeError: 'builtin_function_or_method' object has no attribute 'update'
a.intersection_update(b)
a
{10, 7}
b.intersesction_update(a)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.intersesction_update(a)
AttributeError: 'set' object has no attribute 'intersesction_update'. Did you mean: 'intersection_update'?
b.intersection_update(a)
b
{10, 7}
#differnce_update
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
>>> b
{1, 5, 6, 7, 8, 9, 10}
>>> #symmetric difference update
>>> a={2,3,4,5,6,7,8,9}
>>> b={5,6,7,8,9,10,11}
>>> a.symmetric_difference_update(b)
>>> a
{2, 3, 4, 10, 11}
>>> b.symmetric_difference_update(a)
>>> b
{2, 3, 4, 5, 6, 7, 8, 9}
>>> #add,copy,clear
>>> a={3,4,5,6,7,8}
>>> a.add(10)
>>> a
{3, 4, 5, 6, 7, 8, 10}
>>> b=a.copy()
>>> b
{3, 4, 5, 6, 7, 8, 10}
>>> a.clear()
>>> a
set()
>>> c=set()
>>> c.add(30)
>>> c
{30}
>>> #pop
>>> a={5,6,7,8,9}
>>> a.pop()
5
>>> a.pop(1)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop(7)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(7)
>>> a
{6, 8, 9}
>>> #isdisjoint
>>> a={4,5,6,7}
>>> b=(8,9,10,11}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> b={8,9,10,11}
>>> c={8,9}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(c)
False
>>> #len
>>> a={3,4,5,6}
>>> len(a)
4
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
