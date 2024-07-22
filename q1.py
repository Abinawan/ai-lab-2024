# min and max
a = [2,5,4,5,4,3,87,53,0,67]
temp=a[0]
for i in a:
    if i>temp:
        temp=i
print(f'Greatest Number: {temp}')
for i in a:
    if i<temp:
        temp=i
print(f'Smallest Number: {temp}')
