price=0
def Homepage():
    global price
    print("Welcome")
    print("1.Borrow book")
    print("2.Print bill")
    print("3.Quit")
    print("What do you want to do?")
    tra_loi=input()
    if tra_loi=="1":
     print("What book?")
     Booktype()
     Selectbook()
     price=Payment()
    elif tra_loi=="2":
        if price>0:
            print("Bill:",str(price))
        else:
            print("Invalid")
    else:
        print("Quit")
        return 1
        
   
def Booktype():
    x=["A","B","C","D"]
    for i in range(4):
      for p in x[i]:
          print(p)

def Selectbook():       
   iwant=input()
   match iwant:
        case "A":
            print("How much do you want to pay?")
        case "B":
            print("How much do you want to pay?")
        case "C":
            print("How much do you want to pay?")
        case "D":
            print("How much do you want to pay?")
        case _:
            print("Invalid selection")

def Payment():
      bill=int(input())
      if bill>0:
       print("Payment successful!")
       return bill
      else:
       print("Invalid! Please pay more than 0")
       return 0
    

while True:
   print(price)
   a=Homepage()
   if a==1:
       break
