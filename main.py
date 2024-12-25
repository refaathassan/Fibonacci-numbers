in_number=int(input("please enter your number:   "))
if in_number>0:
    fibo=[0]*in_number
    fibo[1]=1
    print(fibo[0])
    print(fibo[1])
    for i in range(2,in_number):
       fibo[i]=fibo[i-1]+fibo[i-2]
       print(fibo[i])
else: print("please enter valid count")