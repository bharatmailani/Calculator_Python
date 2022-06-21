b1=int(input("total Attanced calls:-"))
b2=int(input("total assigned calls:-"))
opr=input("enter the opr:-")

if opr=="+":
    print(b1+b2)
if opr=="-":
    print(b1-b2)
if opr=="*":
    print(b1*b2/100)
if opr=="/":
    print(b1/b2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":

    print("invalid operation..")

