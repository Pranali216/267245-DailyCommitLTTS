lst=[10,60,40,90,90,20,50]
lst.sort()
n=lst[-1]
for i in range(len(lst),-1,-1):
    if(n!=lst[i-1]):
        print(lst[i-1])
        break

