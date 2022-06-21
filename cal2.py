v1=int(input("enter the valur1:-"))
v2=int(input("enter the value2:-"))
opr=input("enter the opr(+,-,*,/)")

if opr=="+":
    print(v1+v2)
if opr=="-":
    print(v1-v2)
if opr=="*":
    print(v1*v2)
if opr=="/":
    print(v1/v2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("invalid operation")
