##Problem -Book Store

books=("python TRC","carl hamacher","Foss","murach mysql","soft skills")
price=(500,600,300,800,250)
def sell(booknm,quantity):
    global books
    global price
    i=0
    flag=False
    while i!= len(books):
        if books[i]==booknm:
            print("bookname:",booknm)
            amount=quantity*price[i] 
            print("amount: ",amount)
            vat=(4*amount)/100
            print("VAT: ",vat)
            print("Bill: ",amount+vat)
            flag=True
        i+=1
    if not flag:
        print("NA")
bkname=input("Which book: ")
quant=int(input("how many books do yo want: "))
sell(bkname,quant)



