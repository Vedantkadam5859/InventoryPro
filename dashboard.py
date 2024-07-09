
from tkinter import *
from catagory import catagoryClass
from coustomer import coustomerClass
from supplier import supplierClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
from billing import BillClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("InventoryPro | Developed by Vedant Kadam")
        self.root.config(bg="white")
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="InventoryPro",image=self.icon_title,compound=LEFT,
                       font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,
                                                                                                                   y=0,
                                                                                                                   relwidth=1,
                                                                                                                   height=70)

        btn_invoice_=Button(self.root,text="New Purchase",command=self.billing,font=("times new roman",15,"bold"), bg="#33bbf9",fg="white",
                            cursor="hand2").place(x=1050,y=400,height=50,width=150)
    
        self.lbl_clock=Label(self.root,
                                text="Welcome to InventoryPro\t\t Date:DD-mm-yyyy\t\t Time: HH:MM:SS",
                                font=("times new roman", 15),bg="#4d636d",fg="white", )
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu= Label(LeftMenu,text="MENU",font=("times new roman", 20,),bg="#009688",cursor="hand2").pack(
            side=TOP,fill=X)

        btn_coustomer=Button(LeftMenu, text="Customer",command=self.employee,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack (side=TOP, fill=X)
        btn_Supplier =Button(LeftMenu, text="Supplier",command=self.supplier,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack (side=TOP, fill=X)
        btn_Catagory =Button(LeftMenu, text="Category",command=self.catagory,image=self.icon_side, compound=LEFT,padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack (side=TOP, fill=X)
        btn_Product =Button(LeftMenu, text="Product",command=self.product,image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack (side=TOP,fill=X)
                                                                                                            
        btn_Sales =Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack (side=TOP,fill=X)
                                                                                                          
                           
        btn_Exit =Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack (side=TOP, fill=X)
                          
        self.lbl_coustomer =Label(self.root, text="Total Customers\n[ 0]", bd=5, relief=RIDGE, bg="#33bbf9",
                                    fg="white",font=("goudy old style",20,"bold"))
        self.lbl_coustomer.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier =Label(self.root, text="Total Suppliers\n[ 0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",
                                   font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_catagory=Label(self.root,text="Total Categories\n[ 0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",
                                   font=("goudy old style", 20, "bold"))
        self.lbl_catagory.place(x=1000, y=120, height=150, width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_product.place (x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",
                                font=("goudy old style",20,"bold"))
        self.lbl_sales.place (x=650,y=300,height=150,width=300)

        lbl_fotter=Label(self.root,
                            text="InventoryPro| Developed by Vedant Kadam\n for any technical Issue Contact: 9423579003",
                            font=("times new roman", 11), bg="#4d636d", fg="white", ).pack(side=BOTTOM,fill=X)
        self.update_content()

    def employee(self):
        self.new_win=Toplevel (self.root)
        self.new_obj=coustomerClass (self.new_win)

    def supplier(self):
        self.new_win=Toplevel (self.root)
        self.new_obj=supplierClass (self.new_win)

    def catagory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=catagoryClass(self.new_win)
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')


            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')
        
        
            cur.execute("select * from catagory")
            catagory=cur.fetchall()
            self.lbl_catagory.config(text=f'Total Categories\n[{str(len(catagory))}]')
   
            cur.execute("select * from coustomer")
            coustomer=cur.fetchall()
            self.lbl_coustomer.config(text=f'Total Customers\n[{str(len(coustomer))}]')
            
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m:%Y")
             
            self.lbl_clock.config(text=f"Welcome to InventoryPro\t\t Date:{str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parrent=self.root)
            
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
if __name__ == "__main__":
    root = Tk ()
    obj = IMS (root)
    root.mainloop ()
