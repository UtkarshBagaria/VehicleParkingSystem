from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error
import os
try: 
    conn = mysql.connector.connect(host='localhost', database='477_vehicle_parking', user='root',password='') 
    if conn.is_connected():
        cursor=conn.cursor() 
        window = Tk()
        window.title("DBMS PROJECT")
        # window.geometry("1250x675")
        window.configure(bg='#ec5454')
        window.attributes('-fullscreen',True)

        frame = Frame(window)
        # frame.grid()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("download.png"))
        label = Label(frame, image = img)
        label.grid()
        lb1=Label(window,text="Vehicle Parking",bg='#e19ee6',font=("Comic Sans",50))
        lb1.grid(row=4,padx=425)

  
        def onClickUSER():
            sub1 = Tk()
            sub1.title("USER")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")

            lb1=Label(sub1,text="Please Enter details for new user and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)

            def add_data():
                uid = int(e1.get())
                fname = e2.get()
                lname = e4.get()
                status = int(e5.get())
                query="INSERT INTO `tbl_user` VALUES(%s,%s,%s,%s)"
                data=(uid,fname,lname,status)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_user` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_user` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter UserID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter FullName",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=10)

            lb3= Label(sub1,text="contact",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="status",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e5.grid(row=7,column=2)
            
            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg='#9edae6')  
            b1.grid(row=11,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_user` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=15,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=16,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg='#9edae6')  
            b1.grid(row=17, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_user` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=15,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=16,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg='#9edae6')  
            b2.grid(row=17,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Thank you for Registering",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Enter new user",font=("Arial",17),command= onClickUSER,bg="#9edae6" )
        bt1.grid(row=7,pady=10)

#function of Donating blood on first window    
        def onClickBooking():
            sub1 = Tk()
            sub1.title("Booking")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Pls enter details for your booking and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)

            #Data for the table 
            def add_data():
                did = int(e1.get())
                dod = int(e2.get())
                type = int(e3.get())
                amt = int(e4.get())
                bg = int(e5.get())
                fpid = int(e6.get())
                query="INSERT INTO `tbl_booking` VALUES(%s,%s,%s,%s,%s,%s,%s)"
                data=(did,dod,type,amt,bg,fpid)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_booking` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_booking` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter booking_id",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="customer_id",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=10)

            lb3= Label(sub1,text="vehicle_id",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="slot_id",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="booking_status",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e5.grid(row=7,column=2)

            lb3= Label(sub1,text="user_id",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6,column=3)
            e6= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e6.grid(row=7,column=3)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg='#9edae6')
            b1.grid(row=10,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_booking` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=13,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=14,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg='#9edae6')  
            b1.grid(row=16, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_booking` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=13,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=14,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg='#9edae6')  
            b2.grid(row=16,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Booking Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Enter booking details",font=("Arial",17),command= onClickBooking,bg="#9edae6" )
        bt1.grid(row=10,pady=10)

#function of Registering a person on first window    
        def onClickPayment():
            sub1 = Tk()
            sub1.title("Payment")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Enter the payment details and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = int(e1.get())
                dor = int(e2.get())
                typer = e3.get()
                amtr = int(e4.get())
                bgr = int(e5.get())
                query="INSERT INTO `tbl_payment` VALUES(%s,%s,%s,%s,%s)"
                data=(rid,dor,typer,bgr,amtr)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_payment` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_payment` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter paymentID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter bookingID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="paid by name",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="Amount paid",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            lb3= Label(sub1,text="userID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6,column=2)
            e5= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e5.grid(row=7,column=2)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg="#9edae6")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_payment` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg="#9edae6")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_payment` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg="#9edae6")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Payment Details Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Payment Details",font=("Arial",17),command= onClickPayment,bg="#9edae6")
        bt1.grid(row=13,pady=10)

        def onClickSlot():
            sub1 = Tk()
            sub1.title("Slot")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Enter the slot details and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = int(e1.get())
                dor = int(e2.get())
                typer = int(e3.get())
                amtr = int(e4.get())
                query="INSERT INTO `tbl_parking_slot` VALUES(%s,%s,%s,%s)"
                data=(rid,dor,typer,amtr)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_parking_slot` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_parking_slot` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter SlotID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="slot_number",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="slot_status",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="UserID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg="#9edae6")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_parking_slot` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg="#9edae6")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_parking_slot` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg="#9edae6")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Slot Details Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Parking Slot",font=("Arial",17),command= onClickSlot,bg="#9edae6")
        bt1.grid(row=16,pady=10)

        def onClickVeh():
            sub1 = Tk()
            sub1.title("Vehicle")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Enter the Vehicle details and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = int(e1.get())
                dor = int(e2.get())
                typer = e3.get()
                amtr = int(e4.get())
                query="INSERT INTO `tbl_vehicle` VALUES(%s,%s,%s,%s)"
                data=(rid,dor,typer,amtr)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_vehicle` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_vehicle` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter VehicleID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter CategoryID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="Plate_Number",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="OwnerID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg="#9edae6")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_vehicle` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg="#9edae6")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_vehicle` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg="#9edae6")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Vehicle Details Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Vehicle Details",font=("Arial",17),command= onClickVeh,bg="#9edae6")
        bt1.grid(row=19,pady=10)

        def onClickCat():
            sub1 = Tk()
            sub1.title("Category")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Enter the Vehicle Category details and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = int(e1.get())
                dor = e2.get()
                typer = int(e3.get())
                query="INSERT INTO `tbl_vehicle_category` VALUES(%s,%s,%s)"
                data=(rid,dor,typer)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_vehicle_category` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_vehicle_category` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter CategoryID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter Category Name",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="UserID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg="#9edae6")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_vehicle_category` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg="#9edae6")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_vehicle_category` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg="#9edae6")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Category Details Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Category Details",font=("Arial",17),command= onClickCat,bg="#9edae6")
        bt1.grid(row=22,pady=10)

        def onClickOwn():
            sub1 = Tk()
            sub1.title("Owner")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("2560x1444")
            lb1=Label(sub1,text="Enter the Vehicle Owner details and submit",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,columnspan=5)
            
            #Data for the table 
            def add_data():
                rid = int(e1.get())
                dor = e2.get()
                typer = int(e3.get())
                a = int(e4.get())
                query="INSERT INTO `tbl_vehicle_owner` VALUES(%s,%s,%s,%s)"
                data=(rid,dor,typer,a)
                print(query,data)
                cursor.execute(query,data)
                conn.commit()
                print("INSERTED SUCESSFULLY")
                
            def del_data():
                query="DELETE FROM `tbl_vehicle_owner` WHERE "
                data=(edel.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("DELETED SUCESSFULLY")

            def update_data():
                query="UPDATE `tbl_vehicle_owner` SET "
                data = (eup.get())
                print(query+data)
                cursor.execute(query+data)
                conn.commit()
                print("UPDATED SUCESSFULLY")

            #Data for the table 
            lb3= Label(sub1,text="Enter OwnerID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4)
            e1= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e1.grid(row=5,pady=10,padx=10)

            lb3= Label(sub1,text="Enter Owner Name",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=2)
            e2= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e2.grid(row=5,column=2,padx=53)

            lb3= Label(sub1,text="Owner Contact",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=4,column=3)
            e3= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e3.grid(row=5,column=3)

            lb3= Label(sub1,text="UserID",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=6)
            e4= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            e4.grid(row=7,pady=10)

            b1 = Button(sub1,  text='Add Record',font=("Arial",17) ,command=add_data,bg="#9edae6")  
            b1.grid(row=7,column=3)
            
            lb3= Label(sub1,text="DELETE FROM `tbl_vehicle_owner` WHERE",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10)
            edel= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            edel.grid(row=12,pady=10)
            b1 = Button(sub1,  text='Delete Record',font=("Arial",17) ,command=del_data,bg="#9edae6")  
            b1.grid(row=14, pady=10)

            lb3= Label(sub1,text="UPDATE `tbl_vehicle_owner` SET",bg='#e19ee6',font=("Arial",15))
            lb3.grid(row=11,pady=10,column=2)
            eup= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eup.grid(row=12,pady=10,column=2)
            b2 = Button(sub1,  text='Update Record', font=("Arial",17) , command=update_data,bg="#9edae6")  
            b2.grid(row=14,pady=10,column=2)

            #function of END on second window 
            def display_key():
                lb1=Label(window,text="Owner Details Added",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(pady=10,columnspan=5)
        bt1=Button(window,text="Owner Details",font=("Arial",17),command= onClickOwn,bg="#9edae6")
        bt1.grid(row=25,pady=10)
#function of running any Query on first window
        def QRes():
            def getres():
                ans = Tk()
                query = eq.get()
                cursor.execute(query)
                result=cursor.fetchall()
                # print(type(result))
                columns=[]
                for cd in cursor.description:
                    columns.append(cd[0])
                result.insert(0,columns)
                total_rows = len(result)
                total_columns = len(result[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        e = Entry(ans, width=14,bg='#9edae6', fg='black',font=('Comic Sans',12))
                        e.grid(row=i, column=j)
                        if(result[i][j]==None):
                            e.insert(END,"NULL")
                        else:
                            e.insert(END, result[i][j])
            sub1 = Tk()
            sub1.title("Query Results")
            sub1.configure(bg='#e19ee6')
            sub1.geometry("525x325")
            lb1=Label(sub1,text="Enter any Query below",bg='#e19ee6',font=("Comic Sans",17))
            lb1.grid(row=2,pady=7)
            eq= Entry(sub1,width=25,borderwidth=2,font=("Arial",15))
            eq.grid(row=3,pady=10,padx=10)
            bt=Button(sub1,text="Submit",font=("Arial",16),command= getres,bg="#9edae6" )
            bt.grid(row=5)
            def display_key():
                lb1=Label(window,text="Query Results displayed",bg='#e19ee6',font=("Arial",20))
                lb1.grid(pady=5)
            btn_2 = Button(sub1, text="CLOSE", font=("Arial",17) ,command=lambda:[sub1.destroy(),display_key()],bg="#9edae6")
            btn_2.grid(row=6,pady=10)
        bt1=Button(window,text="ANY QUERY",font=("Arial",17),command= QRes,bg="#9edae6" )
        bt1.grid(row=37,pady=10)

#Close the main window 
        bt1 = Button(window, text="EXIT", font=("Arial",17) ,command=window.destroy,bg="#9edae6")
        bt1.grid(row=47,pady=10)
        window.mainloop()
except Error as e: 
    print("Error while connecting to MySQL", e) 
finally: 
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")