a=int(input("Enter the no.\n"))
c=0
d=0
for i in range(a):
    r=a%10
    if r%2==0:
        c+=1
    else:
        d+=1
    a=a//10
    if a==0:
            break
print(c,"no of even no.\n")
print(d,"no of odd no.\n")
