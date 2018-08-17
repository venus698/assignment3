#ques1
a=[]
b=int(input("enter the size of the list:"))
for i in range(0,b):
    c=input("")
    a.append(c)
print(a)

#ques2
a=[]
b=int(input("enter the size of the list:"))
for i in range(0,b):
    c=input("")
    a.append(c)
print(a)
d=["google","apple","facebook","microsoft","tesla"]
a.append(d)
print(a)

#ques3
a=["apple","banana","orange","apple","apple","hello","banana"]
b=input("enter the object : ")
print(b," ","occurs"," ",a.count(b)," times")

#ques4
a=[5,545,54,5,4,5448,54,564,4,64]
a.sort()
print(a)

#ques5
a=[5,44,80,84,9,41,98]
b=[1,6534,54,4564,40,74]
c=[]
c=a+b
c.sort()
print(c)

#ques6
a=[]
odd=0
even=0
size=int(input("enter the size ot the list: "))
for i in range(0,size):
    b=int(input(""))
    a.append(b)
    if b%2==0:
        even+=1
    else:
        odd+=1;
print("list is :",a)
print("list contains %d odd and %d even numbers."%(odd,even))

#ques7
a=(1,2,3,4,5,6,7)
b=slice(-1,-8,-1)
print(a[b])

#ques8
a=(64,6,4,78,87,91,897,178,43,76)
print("max element in tuple is ",max(a))
print("min element in tuple is ",min(a))

#ques9
a="Chitkara University,Punjab"
print(a.upper())

#ques10
a="13579"
print(a.isnumeric())

#ques11
a="Hello world"
print(a.replace("world","Venus"))

