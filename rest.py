from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("BILLING COUNTER")

f1=Frame(root, width=1600,relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(root,width=800,height=700,relief=SUNKEN)
f2.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(f1,font=('ALGERIAN',50,'bold'),text="RESTAURANT MANAGEMENT SYSTEM",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(f1,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#________________________________________________#
def Ref():
    x=random.randint(1,500)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())

    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())

    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())

    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())
                   
    CostofFries =CoFries * 140
    CostofDrinks=CoD * 65
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger* 260
    CostSandwich=CoSandwich * 300

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.05)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)
 
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def rates():
    r=Tk()
    r.geometry("300x300")
    r.title("Price List")
    

    r.mainloop()
    
    




    
    
def qExit():
    root.destroy()
    

lblInfo1=Label(f2,font=('helvetica',20,'bold'),text="Cost of Soup=140",fg="Black",bd=10,anchor='w')
lblInfo2=Label(f2,font=('helvetica',20,'bold'),text="Cost of Burger=260 ",fg="Black",bd=10,anchor='w')
lblInfo3=Label(f2,font=('helvetica',20,'bold'),text="Cost of Noodles=90 ",fg="Black",bd=10,anchor='w')
lblInfo4=Label(f2,font=('helvetica',20,'bold'),text="Cost of Drinks=65 ",fg="Black",bd=10,anchor='w')
lblInfo5=Label(f2,font=('helvetica',20,'bold'),text="Cost of Fries=140 ",fg="Black",bd=10,anchor='w')
lblInfo6=Label(f2,font=('helvetica',20,'bold'),text="Cost of Sandwich=300 ",fg="Black",bd=10,anchor='w')
def List():
    
    lblInfo1.grid(row=0,column=4)
   
    lblInfo2.grid(row=1,column=4)
  
    lblInfo3.grid(row=2,column=4)
    
    lblInfo4.grid(row=3,column=4)
    
    lblInfo5.grid(row=4,column=4)
 
    lblInfo6.grid(row=5,column=4)

def Dlt():
    #print("hide called")
    lblInfo1.grid_forget()
    lblInfo2.grid_forget()
    lblInfo3.grid_forget()
    lblInfo4.grid_forget()
    lblInfo5.grid_forget()
    lblInfo6.grid_forget()
   # print("Hide complete...:")
    
def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()



lblReference= Label(f2, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f2, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f2, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f2, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f2, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f2, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f2, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f2, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f2, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f2, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f2, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f2, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)


lblDrinks= Label(f2, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f2, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f2, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f2, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)



lblService= Label(f2, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f2, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f2, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f2, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f2, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f2, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f2, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f2, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

btnTotal=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=0)

btnReset=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=1)

btnExit=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=2)

btnList=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="PriceList",bg="powder blue",command=List).grid(row=7,column=3)

btnDlt=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Hide",bg="powder blue",command=Dlt).grid(row=7,column=4)
btnrate=Button(f2,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Rates",bg="powder blue",command=rates).grid(row=7,column=5)

root.mainloop()


