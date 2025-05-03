import sys

def add(a,b):
    sum=a+b
    return sum

def sub(a,b):
    subs=a-b
    return subs

a= float(sys.argv[1])
operation = sys.argv[2]
b= float(sys.argv[3])

if operation == "add":

    output = add(a,b)
    print (output)

if operation == "sub":

    output = sub(a,b)
    print (output)
   