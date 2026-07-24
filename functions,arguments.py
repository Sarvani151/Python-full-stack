'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                            1.add
                            2.sub
                            3.mul))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    cal()'''
#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
     print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="bhanu",mailid="b@gmail.com")
Details(id=30,name="nayana",mailid="n@gmailid.com")
Details(40,"chetana","c@gmail.com")
Details("h@gmail.com",50,"harika")'''

#default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %2.f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %2.f" %price)
Grocery("dhal")'''

'''def Grocery(price,item="ghee"):
#non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''
#arguments(* is used to unpack the elements)




