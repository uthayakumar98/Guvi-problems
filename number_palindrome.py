number=int(input())
temp=num
new=0
while num:
    rem=num%10
    new=new*10+rem
    number//=10
if temp==new:
    print("yes")
else:
    print("no")
