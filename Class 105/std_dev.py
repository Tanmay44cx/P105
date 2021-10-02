import math
import csv

with open('sd-data.csv',newline='') as f:
    data=csv.reader(f)
    file_data=list(data) 
file_data=file_data[0]

n=len(file_data)
total=0
for x in file_data:
    total=total+int(x)
        
meam=total/n


squared_list=[]
for number in file_data:
    a=int(number)-meam
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum=sum+i

result=sum/(n-1)
std_dev=math.sqrt(result)
print(std_dev)
