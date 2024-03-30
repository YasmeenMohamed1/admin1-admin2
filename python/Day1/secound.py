num=int(input("Enter the number : "))
list=[]
for i in range(1,num+1):
    data=[]
    for j in range(1,i+1):
        data.append(i*j)
    list.append(data)
print(list)    
        