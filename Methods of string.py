a='string'
type(a)
<class 'str'>
str()
''
a='i love python'
a.upper()
'I LOVE PYTHON'
a='I LOVE PYTHON'
a.lower()
'i love python'
a='python is good'
a.capitalize()
'Python is good'
a.title()
'Python Is Good'
a.count('o')
3
a='i love python'
a.islower()
True
a=a='I LOVE PYTHON 123 415'
a.isupper()
True
a='I LOVE PYTHON 123 415'
a.islower()
False
a='i love python'
a.isupper()
False
a.endswith('n')
True
a.startswith('i')
True
a.find('o')
3
a.index('o')
3
a.rfind('o')
11
a.find('x')
-1
a.index('x')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.index('x')
ValueError: substring not found
a.rfind('x')
-1
a='i LOVe pyhton'
a.swapcase()
'I lovE PYHTON'
a.isalpha()
False
a='python'
a.isalpha()
True
a='1234586'
a.isdigit()
True
a='i','love','python'
' '.join(a)
'i love python'
a='p','y','t','h','o','n'
''.join(a)
'python'
a='I-love-python'
a.split('-')
['I', 'love', 'python']
a.split('-',0)
['I-love-python']
a.split('-',1)
['I', 'love-python']
a.rsplit('-')
['I', 'love', 'python']
a.rsplit('-',2)
['I', 'love', 'python']
a.rsplit('-',1)
['I-love', 'python']
a='#####helloo####'
a.rstrip('#')
'#####helloo'
a.lstrip('#')
'helloo####'
a.strip('#')
'helloo'
a='hellow world'
a.replace('hello','bye')
'byew world'
