1.
Open the file with try and except
In [39]:
try:
    f=open('example2.txt')
    print(f.read())
except:
    print('no file exist')
hello world
my name is ravi chandra
In [15]:
f.close()

2.
Split the data in the file
In [12]:
f=open('example3.txt')
a=f.read()
print(a)
print(a.split())
good morning to all
i am going to say wounderful topic 
to day
['good', 'morning', 'to', 'all', 'i', 'am', 'going', 'to', 'say', 'wounderful', 'topic', 'to', 'day']
In [13]:
f.close()

3.
To read the contents in file using the with statement
In [16]:
with open('example2.txt') as f:
    a=f.read()
    print(a)
hello world
my name is mahesh reddy

4.
To remove the file and Director
In [18]:
import os
os.getcwd()
Out[18]:
'C:\\Users\\Siva Krishna\\Documents'
In [32]:
import os   
file = 'example3.txt' 
location = 'C:\\Users\\Siva Krishna\\Documents'
path = os.path.join(location, file)   
os.remove(path)

5.
TO access elements in the list
In [38]:
l=[1,3,4,2]
print(len(l))
print(l[1])
l[3]='k'
print(l)
4
3
[1, 3, 4, 'k']
In [ ]: