Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> a="python course"
>>> a[-1:-11:-3]
'eu h'
>>> a[-2:-12:-4]
'sch'
>>> a[-5:-13:-5]
'oh'
>>> a[8:4:2]
''
>>> #in positive striding :lower to higher
>>> a[-9:-3:-1]
''
>>> #in negtaive striding :hiher to lower number
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
