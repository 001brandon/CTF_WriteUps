# In a pickle

### Problem Description

Author: n00bmaster

We managed to intercept communication between und3rm4t3r and his hacker friends. However it is obfuscated using something.
We just can't figure out what it is. Maybe you can help us find the flag?

[data](https://play.duc.tf/files/5f85a352ae3eaf93f5adf9cb06074ea0/data?token=eyJ1c2VyX2lkIjoyNDc4LCJ0ZWFtX2lkIjoxMDI2LCJmaWxlX2lkIjozM30.X2dFng.hYWA6IafRlMg4Q5kKhue7CHKnik)

Category: misc. 200 Points

### data
``
(dp0
I1
S'D'
p1
sI2
S'UCTF'
p2
sI3
S'{'
p3
sI4
I112
sI5
I49
sI6
I99
sI7
I107
sI8
I108
sI9
I51
sI10
I95
sI11
I121
sI12
I48
sI13
I117
sI14
I82
sI15
I95
sI16
I109
sI17
I51
sI18
I53
sI19
I53
sI20
I52
sI21
I103
sI22
I51
sI23
S'}'
p4
sI24
S"I know that the intelligence agency's are onto me so now i'm using ways to evade them: I am just glad that you know how to use pickle. Anyway the flag is "
p5
s.
``

## Concepts Used:
[pickle](https://docs.python.org/3/library/pickle.html)
[ASCII](http://www.asciitable.com/)

## Solving the Challenge
Reading the title of the challenge, I was able to recognize that the data was being converted into a byte stream using the Python pickle library. 
Since the data has been pickled, we need to write a script to unpickle the data. The first step is to unpickle and save the contents of the `data` file into a
string called `flag`.
```
import pickle
flag=""
pickleFile=open(r"C:\Users\brook\Downloads\data","rb")
contents=pickle.load(pickleFile)
```
If we examine the variable `contents`
```
>>> print(contents)
{1: 'D', 2: 'UCTF', 3: '{', 4: 112, 5: 49, 6: 99, 7: 107, 8: 108, 9: 51, 10: 95,
 11: 121, 12: 48, 13: 117, 14: 82, 15: 95, 16: 109, 17: 51, 18: 53, 19: 53, 20: 52,
 21: 103, 22: 51, 23: '}', 24: "I know that the intelligence agency's are onto
 me so now i'm using ways to evade them: I am just glad that you know how to use
 pickle. Anyway the flag is "}

>>> type(contents)
<class 'dict'>
```
We can see that the contents are being saved as a dictionary, we can also take an educated guess and see that 
for the indices from 4-22 it seems to be a decimal value representing an ASCII value encased in the flag. The next step is to write code
in order to convert those values back to ASCII and concatenate them with the string variable `flag`.
```
for key, value in contents.items():
    if key<24:
        if key <4 or key==23:
            flag+=value
        else:
            flag+=chr(value)
```
If we now check the value of `flag` we get the final solution.
```
>>> print(flag)
DUCTF{p1ckl3_y0uR_m3554g3}
```

