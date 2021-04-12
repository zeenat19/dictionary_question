dict={"first":1, 
     "second": 2, 
     "third": 1, 
     "four": 5, 
     "five":5, 
     "six":9,
     "seven":7}
a=[]
for i in dict:
    if dict[i] not in a:
        a.append(dict[i])
print(a)