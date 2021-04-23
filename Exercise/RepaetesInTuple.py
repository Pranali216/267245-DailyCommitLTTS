t=(1,5,6,9,8,2,1,9,6,10,1)
lst=[]
for i in t:
    a=t.count(i)
    if(a>1 and i not in lst):
        lst.append(i)
        print(i,"is repeated ", a,"times")