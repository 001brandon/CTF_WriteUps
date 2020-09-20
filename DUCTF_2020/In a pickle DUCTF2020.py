import pickle
import string
flag=""

pickleFile=open(r"C:\Users\brook\Downloads\data","rb")
contents=pickle.load(pickleFile)
for key, value in contents.items():
    if key<24:
        if key <4 or key==23:
            flag+=value
        else:
            flag+=chr(value)

print(flag)

