from tkinter import *
from tkinter import messagebox
from functools import partial
import re
import tkinter
import customtkinter as ctk
import color as cs
import database as db

import pymysql as py

from datetime import datetime


# database conctivity
host_1=db.host_1
user_1=db.user_1
password_1=db.password_1
database_1=db.database_1


#colors

col_1=cs.col_1
col_2=cs.col_2                       
col_3=cs.col_3
col_4=cs.col_4
col_5=cs.col_5
col_6=cs.col_6
col_7=cs.col_7
BG_GRAY =cs.BG_GRAY
BG_COLOR =cs.BG_COLOR
TEXT_COLOR =cs.TEXT_COLOR

FONT = cs.FONT
FONT_BOLD =cs.FONT_BOLD

window=Tk()
window.title("IT_management")
window.maxsize(width=1000,height=800)
window.minsize(width=1000,height=800)
  

     #frame_1
f=Frame(window,bg=col_2)
f.place(x=0,y=0,height=80,width=1000)

     #frame_2
f1=Frame(window,bg=col_1)
f1.place(x=0,y=80,height=620,width=1000)

     #frame_3
f3=Frame(window,bg=col_3)
f3.place(x=0,y=700,height=100,width=1000)





def trainee_id():

     #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
            
    tittle=Label(f3,text="TRAINEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)   
    
    b=Button(f3,text="SIGN_UP",command=trainee)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="LOGIN",command=trainee_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="UPDATE",command=trainee_update)
    b2.place(x=430,y=45,width=100)
    
    b3=Button(f3,text="BACK",command=trainee_main)
    b3.place(x=620,y=45,width=100)


    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)




def employee_id():

      #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
           
    tittle=Label(f3,text="EMPLOYEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)
    
    b=Button(f3,text="SIGN_UP",command=employee)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="LOGIN",command=employee_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="UPDATE",command=employee_update)
    b2.place(x=430,y=45,width=100)
    
    b3=Button(f3,text="BACK",command=employee_main)
    b3.place(x=620,y=45,width=100)
    
    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)





def trainee_main():

     #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
            
    tittle=Label(f3,text="TRAINEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)   
    
    b=Button(f3,text="REGISTER",command=trainee_id)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="TASK",command=task)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="FEEDBACK",command=T_feedback)
    b2.place(x=430,y=45,width=100)
    
    b3=Button(f3,text="CHAT",command=trainee_chat_login)
    b3.place(x=620,y=45,width=100)


    b4=Button(f3,text="NOTICEBOARD",command=notice_feedback)
    b4.place(x=820,y=45,width=100)








def employee_main():

     #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
            
    tittle=Label(f3,text="EMPLOYEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)   
    
    b=Button(f3,text="E_REGISTER",command=employee_id)
    b.place(x=20,y=45,width=105)

    b1=Button(f3,text="CHAT",command=employee_chat_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="FEEDBACK",command=employee_feed)
    b2.place(x=430,y=45,width=100)
    
    b3=Button(f3,text="NOTICEBOARD",command=notice_feedback)
    b3.place(x=620,y=45,width=100)


    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)










def trainee():
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18
    
    tittle=Label(f1,text="TRAINEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    t1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t1.place(x=200,y=55,width=190,height=25)

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=130)
    t2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t2.place(x=200,y=135,width=190,height=25)
    

    a3=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=210)
    t3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t3.place(x=200,y=215,width=190,height=25)
    
    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=290)
    t4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t4.place(x=200,y=295,width=190,height=25)
    
    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=370)
    t5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t5.place(x=200,y=375,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=450)
    t6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t6.place(x=200,y=455,width=190,height=25)


    a7=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=550,y=50)
    t7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t7.place(x=700,y=55,width=190,height=25)

    a8=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=130)
    t8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t8.place(x=700,y=135,width=190,height=25)
    
    a9=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=210)
    t9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t9.place(x=700,y=215,width=190,height=25)

    a10=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=290)
    t10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t10.place(x=700,y=295,width=190,height=25)

     
    a11=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=370)
    t11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t11.place(x=700,y=375,width=190,height=25)
    
    a12=Button(f1,text="submit",bg="#8CC0DE",command=trainee_submit)
    a12.place(x=440,y=570,width=100)








def trainee_submit():
    print(t6.get())
    if t1.get()=="" or t2.get()=="" or t3.get()=="" or t4.get()=="" or t5.get()=="" or t6.get()=="" or t7.get()=="" or t8.get()=="" or t9.get()=="" or t10.get()=="" or t11.get()=="":
        messagebox.showwarning("Warning","all fields are required")
    
    
    else:
        #try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from trainee where contact=%s",t6.get())
             j=my.fetchone()
             print(j)
             print(t6.get())
             
             
             
            
            #date
             
             date=datetime.today()
             year=date.year
             
       

             if j!=None:
                 messagebox.showwarning("Warning","contact number already exists")
             
             else:
         #name_validation

                 if re.findall(r'\W',(t1.get())):
                     
                     messagebox.showwarning("Warning","invalid name please remove unnecessary special characters")
                     
                 elif re.findall("[0-9]",(t1.get())):
                     
                     messagebox.showwarning("Warning","invalid name please remove unnecessary numbers")
    
                 

            #lname_validation

                 elif re.findall(r'\W',(t2.get())):
                     messagebox.showwarning("Warning","invalid l_name please remove unnecessary special characters")
                     
                 elif re.findall("[0-9]",(t2.get())):
                     messagebox.showwarning("Warning","invalid l_name please remove unnecessary numbers")

                         
            #age validation
                 
                 elif re.findall("[a-zA-Z]",(t3.get())):
                    messagebox.showwarning("Warning","please check your age")
                    
                 elif re.findall(r'\W',(t3.get())):
                         messagebox.showwarning("Warning","please check your age")

                 elif int(t3.get())<18 or int(t3.get())>100:
                         messagebox.showwarning("Warning","please check your age")

            #dob
             
                 elif re.findall("[a-zA-Z]",(t4.get())):
                     messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

                 elif  re.findall('[ @_!#$^%&*(.)<>?/|}{;:"`,]',(t4.get())):
                     messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

                 elif len(t4.get())<10 or len(t4.get())>10:
                     messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

                     
                 elif (int(t4.get()[:2]))>31 or (int(t4.get()[:2]))==0 :
                     messagebox.showwarning("Warning","invaild D.O.B please check the date")

                 elif  (int(t4.get()[3:5]))==0 or  (int(t4.get()[3:5]))>12 :
                     messagebox.showwarning("Warning","invaild D.O.B  please check the month")

                 elif  ((t4.get()[:5]))=='30-02' or  ((t4.get()[:5]))=='31-02' :
                     messagebox.showwarning("Warning","invaild D.O.B  please check the date")                    
                     

                 elif int(t4.get()[6:])<1970 or int(t4.get()[6:])>(year-19) :
                     messagebox.showwarning("Warning","invaild D.O.B please check the year")

                 elif year-int(t4.get()[6:])< int(t3.get()) or year-int(t4.get()[6:]) >int(t3.get()):
                     messagebox.showwarning("Warning","invaild D.O.B not match to age please check")
                     
                     
                 
                         
            #email validation
                 
                 elif (re.findall("[A-Z]",(t5.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please romove uppercase")
                
                 elif (re.findall('[ _!#$^%&*()<>?/|}{;:"`,]',(t5.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")

                 elif not t5.get().endswith("@gmail.com"):
                 
                     messagebox.showwarning("Warning","invalid Email please endswith @gmail.com")
                     
             #mobile number validation
                    
                 elif not( (t6.get()[0])=="6" or (t6.get()[0])=="7" or (t6.get()[0])=="8" or (t6.get()[0])=="9" ):
                    messagebox.showwarning("Warning","invalid contact please check your contact")
                    
                 elif not (len(t6.get())==10):
                        messagebox.showwarning("Warning","invalid contact please check your contact")

                 elif re.findall("[a-zA-Z]",(t6.get())):
                     messagebox.showwarning("Warning","invalid l_name please remove unnecessary letters")

            #c_name_validation

                 elif re.findall(r'\W',(t7.get())):
                     messagebox.showwarning("Warning","invalid l_name please remove unnecessary special characters")
                     
                 elif re.findall("[0-9]",(t7.get())):
                     messagebox.showwarning("Warning","invalid l_name please remove unnecessary numbers")
            #qualification validation


                 elif re.findall(r'\W',(t8.get())):
                         messagebox.showwarning("Warning","invalid qualification please remove unnecessary special characters")

                 elif re.findall("[0-9]",(t8.get())):
                         messagebox.showwarning("Warning","invalid qualification please remove unnecessary numbers")





             #percentage validation


                 elif re.findall("[a-zA-Z]",(t9.get())):
                    messagebox.showwarning("Warning","please checkpercentage")
                    
                 elif re.findall('[ @_!#$^%&*()<>?/|}{;:"`,]',(t9.get())):
                         messagebox.showwarning("Warning","please check percentage")

                 elif float(t9.get())<35 or float(t9.get())>100:
                         messagebox.showwarning("Warning","please check percentage")

             #date validation
                         
                 elif re.findall("[a-zA-Z]",(t10.get())):
                     messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")

                 elif  re.findall('[ @_!#$^%&*(.)<>?/|}{~;:"`~,]',(t10.get())):
                     messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")
                 elif len(t10.get())<10 or len(t10.get())>10:
                     messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")
                 elif (int(t10.get()[:2]))>date.day or (int(t10.get()[:2]))<date.day :
                     messagebox.showwarning("Warning","invaild date please check the date")

                 elif  (int(t10.get()[3:5]))< date.month or  (int(t10.get()[3:5]))>date.month :
                     messagebox.showwarning("Warning","invaild  please check the month")
                     
                 
                 elif  (int(t10.get()[6:]))<date.year or  (int(t10.get()[6:]))>date.year :

                     messagebox.showwarning("Warning","invaild  please check the year")

                #salary
                         
                 elif re.findall("[a-zA-Z]",t11.get()):
                         messagebox.showwarning("warning","invalid salary please remove unnecessary letters")  
                 
                 elif re.findall('[ @_!#$^%&*()<>?/|}{;:"`.]',t11.get()):
                         messagebox.showwarning("warning","invalid salary please remove unnecessary special characters") 
                    
      
                 else:
                     
                     c="insert into trainee(name ,last_name,age ,dob ,email,contact ,c_name ,qualification,percentage,date,salary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                     d=(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t7.get(),t8.get(),t9.get(),t10.get(),t11.get())
                     my.execute(c,d)
                     db.commit()

                     messagebox.showinfo("success","data submitted")
                     for widgets in f1.winfo_children():
                         widgets.destroy()
                     
                
                 
                
     



        
                 

def trainee_login():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="TRAINEE_LOGIN_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=400,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=trainee_login_page).place(x=445,y=350,height=25,width=100)

def trainee_login_page():
   
    if t1.get()=="":
        messagebox.showwarning("Warning","all field are requried")


    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor() 
             my.execute("select *from trainee where contact=%s",t1.get())
             j=my.fetchone()
             print(j)

             if j == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
             else:
                 
                 trainee_show(j)
                 db.close()
        
        except:
            print("hlo")


def trainee_show(j):
    
    for widgets in f1.winfo_children():
      widgets.destroy()
         
    
    tittle=Label(f1,text="TRAINEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    t1=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[0])
    t1.place(x=200,y=55,width=190,height=25)

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=130)
    t2=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[1])
    t2.place(x=200,y=135,width=190,height=25)
    

    a3=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=210)
    t3=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[2])
    t3.place(x=200,y=215,width=190,height=25)
    
    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=290)
    t4=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[3])
    t4.place(x=200,y=295,width=190,height=25)
    
    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=370)
    t5=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[5])
    t5.place(x=200,y=375,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=450)
    t6=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[4])
    t6.place(x=200,y=455,width=190,height=25)


    a7=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=550,y=50)
    t7=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[6])
    t7.place(x=700,y=55,width=190,height=25)

    a8=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=130)
    t8=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[7])
    t8.place(x=700,y=135,width=190,height=25)
    
    a9=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=210)
    t9=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[8])
    t9.place(x=700,y=215,width=190,height=25)

    a10=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=290)
    t10=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[9])
    t10.place(x=700,y=295,width=190,height=25)

     
    a11=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=370)
    t11=Label(f1,bg="white",fg="black",font=("calibri",14),text=j[10])
    t11.place(x=700,y=375,width=190,height=25)
    
def trainee_update():
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global t1
    tittle=Label(f1,text="TRAINEE_UPDATE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=trainee_update_details).place(x=445,y=350,height=25,width=100)


def trainee_update_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid l_name please remove unnecessary letters")        

    else:
        try:         
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from trainee where contact=%s",t1.get())
            row=my.fetchone()
            print(t1.get())
            print(row)
            
            if row == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
            else:
                trainee_user_update(row)
                db.close()
        
         

      
        except:
            print("hlo")


def trainee_user_update(row):
    
    for widgets in f1.winfo_children():
      widgets.destroy()
         
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11
    
    tittle=Label(f1,text="TRAINEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    t1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t1.insert(0,row[0])
    t1.place(x=200,y=55,width=190,height=25)

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=130)
    t2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t2.insert(0,row[1])
    t2.place(x=200,y=135,width=190,height=25)
    

    a3=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=210)
    t3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t3.insert(0,row[2])
    
    t3.place(x=200,y=215,width=190,height=25)
    
    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=290)
    t4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t4.insert(0,row[3])

    t4.place(x=200,y=295,width=190,height=25)
    
    a5=Label(f1,text="Contact",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=370)
    t5=Label(f1,bg="white",fg="black",font=("calibri",14),text=row[4])    
    t5.place(x=200,y=375,width=190,height=25)

    a6=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=450)
    t6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t6.insert(0,row[5])
    t6.place(x=200,y=455,width=190,height=25)


    a7=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=550,y=50)
    t7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t7.insert(0,row[6])
    t7.place(x=700,y=55,width=190,height=25)

    a8=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=130)
    t8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t8.insert(0,row[7])
    t8.place(x=700,y=135,width=190,height=25)
    
    a9=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=210)
    t9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t9.insert(0,row[8])
    t9.place(x=700,y=215,width=190,height=25)

    a10=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=290)
    t10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t10.insert(0,row[9])
    t10.place(x=700,y=295,width=190,height=25)

     
    a11=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=370)
    t11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t11.insert(0,row[10])
    t11.place(x=700,y=375,width=190,height=25)
 
    a19=Button(f1,text="submit",bg="#8CC0DE",command=partial(show_trainee_update,row))
    a19.place(x=460,y=570,width=100)




def show_trainee_update(row):
    if t1.get()=="" or t2.get()=="" or t3.get()=="" or t4.get()==""  or t6.get()=="" or t7.get()=="" or t8.get()=="" or t9.get()=="" or t10.get()=="" or t11.get()=="":
        messagebox.showwarning("Warning","all field are requried")
 
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from trainee where contact=%s",row[4])
             j=my.fetchone()
            

             if j==None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                
             else:
                 
                 c="update trainee set name=%s ,last_name=%s,age=%s ,dob=%s ,email=%s,c_name=%s ,qualification=%s,percentage=%s,date=%s,salary=%s  where contact=%s"
                 d=(t1.get(),t2.get(),t3.get(),t4.get(),t6.get(),t7.get(),t8.get(),t9.get(),t10.get(),t11.get(),row[4])
                 print(d)
                 my.execute(c,d)
                 my.execute("select *from trainee where contact=%s",row[4])
                 jk=my.fetchone()
                 print(jk)                 
                 db.commit()
                 db.close()
                 messagebox.showinfo("success","Update completed")
                 for widgets in f1.winfo_children():
                    widgets.destroy()               
                 
                
                                                                                                                                                                                    
        except:

                print("hlo")
 









                                                                                      #employee





def employee():
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17
    
    tittle=Label(f1,text="EMPLOYEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    e1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e1.place(x=200,y=55,width=190,height=25)

    

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=120)
    e2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e2.place(x=200,y=125,width=190,height=25)
    
    
    a3=Label(f1,text="Age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=190)
    e3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e3.place(x=200,y=195,width=190,height=25)
    

    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=260)
    e4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e4.place(x=200,y=265,width=190,height=25)
    

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=330)
    e5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e5.place(x=200,y=335,width=190,height=25)
    

    a6=Label(f1,text="Contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=400)
    e6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e6.place(x=200,y=405,width=190,height=25)
    

    a7=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=470)
    e7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e7.place(x=200,y=475,width=190,height=25)

    a8=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=50)
    e8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e8.place(x=700,y=55,width=190,height=25)

    a9=Label(f1,text="Job_roll",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=120)
    e9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e9.place(x=700,y=125,width=190,height=25)

    a10=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=190)
    e10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e10.place(x=700,y=195,width=190,height=25)

    a11=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=260)
    a111=Label(f1,text="(in letters)",font=("calibri",12),bg=col_1,fg="black")
    a111.place(x=562,y=290)
    e11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e11.place(x=700,y=265,width=190,height=25)
    
    a12=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=330)
    e12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e12.place(x=700,y=335,width=190,height=25)
    

    
    a13=Label(f1,text="Salary",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=400)
    e13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e13.place(x=700,y=405,width=190,height=25)

    a14=Button(f1,bg="#8CC0DE",text="SUBMIT",fg="black",command=employee_submit)
    a14.place(x=450,y=555,width=100,height=25)




    
def employee_submit():
    

    date=datetime.today()
    year=date.year
    
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()=="" or e8.get()==""  or e10.get()=="" or e11.get()=="" or e12.get()=="" or e13.get()=="":
        messagebox.showwarning("Warning","all field are requried")

    #name_validation

    elif re.findall(r'\W',(e1.get())):

       messagebox.showwarning("Warning","invalid name please remove unnecessary special characters")

    elif re.findall("[0-9]",(e1.get())):

        messagebox.showwarning("Warning","invalid name please remove unnecessary numbers")



    #lname_validation

    elif re.findall(r'\W',(e2.get())):
        messagebox.showwarning("Warning","invalid l_name please remove unnecessary special characters")

    elif re.findall("[0-9]",(e2.get())):
        messagebox.showwarning("Warning","invalid l_name please remove unnecessary numbers")
    


    #age validation

    elif re.findall("[a-zA-Z]",(e3.get())):
        messagebox.showwarning("Warning","please check your age")

    elif re.findall(r'\W',(e3.get())):
        messagebox.showwarning("Warning","please check your age")

    elif int(e3.get())<18 or int(e3.get())>100:
        messagebox.showwarning("Warning","please check your age")

    #dob

    elif re.findall("[a-zA-Z]",(e4.get())):
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

    elif  re.findall('[ @_!#$^%&*(.)<>?/|}{;:"`,]',(e4.get())):
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

    elif len(e4.get())<10 or len(e4.get())>10:
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")


    elif (int(e4.get()[:2]))>31 or (int(e4.get()[:2]))==0 :
        messagebox.showwarning("Warning","invaild D.O.B please check the date")

    elif  (int(e4.get()[3:5]))==0 or  (int(e4.get()[3:5]))>12 :
        messagebox.showwarning("Warning","invaild D.O.B  please check the month")
        
    elif  ((e4.get()[:5]))=='30-02' or  ((e4.get()[:5]))=='31-02' :
        messagebox.showwarning("Warning","invaild D.O.B  please check the date")

    elif int(e4.get()[6:])<1990 or int(e4.get()[6:])>(year-19) :
        messagebox.showwarning("Warning","invaild D.O.B please check the year")

    elif year-int(e4.get()[6:])< int(e3.get()) or year-int(e4.get()[6:]) >int(e3.get()):
        messagebox.showwarning("Warning","invaild D.O.B not match to age please check")


             
    #email validation
     
    elif (re.findall("[A-Z]",(e5.get()))):
                  
         messagebox.showwarning("Warning","invalid Email please romove uppercase")

    elif (re.findall('[ _!#$^%&*()<>?/|}{;:"`,]',(e5.get()))):
                  
         messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")

    elif not e5.get().endswith("@gmail.com"):
     
         messagebox.showwarning("Warning","invalid Email please endswith @gmail.com")
         
    #mobile number validation
        
    elif not( (e6.get()[0])=="6" or (e6.get()[0])=="7" or (e6.get()[0])=="8" or (e6.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(e6.get())==10):
            messagebox.showwarning("Warning","invalid contact please enter 10 digit contact")


    #qualification validation


    elif re.findall(r'\W',(e7.get())):
             messagebox.showwarning("Warning","invalid qualification please remove unnecessary special characters")

    elif re.findall("[0-9]",(e7.get())):
             messagebox.showwarning("Warning","invalid qualification please remove unnecessary numbers")

    #city_validation

    elif re.findall(r'\W',(e8.get())):
         messagebox.showwarning("Warning","invalid city please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e8.get())):
         messagebox.showwarning("Warning","invalid city please remove unnecessary numbers")

    #job_roll_validation

    elif re.findall(r'\W',(e9.get())):
         messagebox.showwarning("Warning","invalid job_roll please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e9.get())):
         messagebox.showwarning("Warning","invalid job_roll please remove unnecessary numbers")

    #pre company_validation

    elif re.findall(r'\W',(e10.get())):
         messagebox.showwarning("Warning","invalid pre_company please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e10.get())):
         messagebox.showwarning("Warning","invalid pre_company please remove unnecessary numbers")

    #experience_validation

    elif re.findall('[@_!#$^%&*(.)<>?/|}{~;:"`~,]',(e11.get())):
         messagebox.showwarning("Warning","invalid experience please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e11.get())):
         messagebox.showwarning("Warning","invalid experience please remove unnecessary numbers")



    #date validation
             
    elif re.findall("[a-zA-Z]",(e12.get())):
         messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")

    elif  re.findall('[ @_!#$^%&*(.)<>?/|}{~;:"`~,]',(e10.get())):
         messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")
    elif len(e12.get())<10 or len(e12.get())>10:
         messagebox.showwarning("Warning","invaild date please enter the same format(dd-mm-yyyy)")
    elif (int(e12.get()[:2]))>date.day or (int(e12.get()[:2]))<date.day :
         messagebox.showwarning("Warning","invaild date please check the day")

    elif  (int(e12.get()[3:5]))< date.month or  (int(e12.get()[3:5]))>date.month :
         messagebox.showwarning("Warning","invaild  please check the month")
         
     
    elif  (int(e12.get()[6:]))<date.year or  (int(e12.get()[6:]))>date.year :

         messagebox.showwarning("Warning","invaild  please check the year")

    #salary
             
    elif re.findall("[a-zA-Z]",e13.get()):
             messagebox.showwarning("warning","invalid salary please remove unnecessary letters")  
     
    elif re.findall('[ @_!#$^%&*()<>?/|}{;:"`.]',e13.get()):
             messagebox.showwarning("warning","invalid salary please remove unnecessary special characters") 
        
    elif int(e13.get())<4999:
            messagebox.showwarning("warning","invalid salary minimun salary is 5000")

    else:
         db=py.connect(host=host_1,user=user_1,password=password_1,database='pravin')
         my=db.cursor()
         my.execute("select *from employee where contact=%s",e6.get())
         j=my.fetchone()
 
         if j!=None:
             messagebox.showwarning("Warning","contact number already exists")
         else:
             e="insert into employee(name,last_name,age,dob,email,contact,qualification,city,job_roll,pre_company,experience,date,salary_package) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             d=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get())

             
             my.execute(e,d)
             
             db.commit()   
             db.close()
             
             messagebox.showinfo("success","data submitted")
             for widgets in f1.winfo_children():
                 widgets.destroy()
                 
                
                 



def employee_login():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="EMPLOYEE_LOGIN_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=400,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=employee_login_page).place(x=445,y=350,height=25,width=100)



def employee_login_page():
    
    if t1.get()=="":
        messagebox.showwarning("Warning","all field are requried")

    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid l_name please remove unnecessary letters")
         
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database="pravin")
             my=db.cursor()
             my.execute("select *from employee where contact=%s",t1.get())
             k=my.fetchone()

             if k == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
             else:
                 
                 employee_show(k)
                 db.close()
        
        except:
            print("hlo")



                              #frame_1 func 
 

def employee_show(k):
    for widgets in f1.winfo_children():
      widgets.destroy()
      
   
    
    tittle=Label(f1,text="EMPLOYEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    e1=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[0])
    e1.place(x=200,y=55,width=190,height=25)

    

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=120)
    e2=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[1])
    e2.place(x=200,y=125,width=190,height=25)
    
    
    a3=Label(f1,text="Age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=190)
    e3=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[2])
    e3.place(x=200,y=195,width=190,height=25)
    

    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=260)
    e4=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[3])
    e4.place(x=200,y=265,width=190,height=25)
    

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=330)
    e5=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[4])
    e5.place(x=200,y=335,width=190,height=25)
    

    a6=Label(f1,text="Contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=400)
    e6=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[5])
    e6.place(x=200,y=405,width=190,height=25)
    

    a7=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=470)
    e7=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[6])
    e7.place(x=200,y=475,width=190,height=25)

    a8=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=50)
    e8=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[7])
    e8.place(x=700,y=55,width=190,height=25)

    a9=Label(f1,text="Job_roll",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=120)
    e9=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[8])
    e9.place(x=700,y=125,width=190,height=25)

    a10=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=190)
    e10=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[9])
    e10.place(x=700,y=195,width=190,height=25)

    a11=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=260)
    a111=Label(f1,text="(in letters)",font=("calibri",12),bg=col_1,fg="black")
    a111.place(x=562,y=290)
    e11=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[10])
    e11.place(x=700,y=265,width=190,height=25)
    
    a12=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=330)
    e12=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[11])
    e12.place(x=700,y=335,width=190,height=25)
   
    a13=Label(f1,text="Salary",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=400)
    e13=Label(f1,bg="white",fg="black",font=("calibri",14),text=k[12])
    e13.place(x=700,y=405,width=190,height=25)



    a61=Label(f1,text="(**********)",font=("calibri",10),bg=col_1,fg="black")
    a61.place(x=20,y=425)

    a121=Label(f1,text="(dd-mm-yyyy)",font=("calibri",12),bg=col_1,fg="black")
    a121.place(x=559,y=360)

    a41=Label(f1,text="(dd-mm-yyyy)",font=("calibri",12),bg=col_1,fg="black")
    a41.place(x=20,y=285)




def employee_update():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="EMPLOYEE_UPDATE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=employee_update_details).place(x=445,y=350,height=25,width=100)








def employee_update_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please enter 10 digit contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid contact please remove unnecessary letters")

    else:
        try:         
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from employee where contact=%s",t1.get())
            row=my.fetchone()
            
            if row == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
            else:
                employee_user_update(row)
                db.close()
        
         

      
        except:
            print("hlo")



def employee_user_update(row):
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14
    
    tittle=Label(f1,text="EMPLOYEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    e1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e1.place(x=200,y=55,width=190,height=25)

    

    a2=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=120)
    e2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e2.place(x=200,y=125,width=190,height=25)
    
    
    a3=Label(f1,text="Age",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=190)
    e3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e3.place(x=200,y=195,width=190,height=25)
    

    a4=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=260)
    e4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e4.place(x=200,y=265,width=190,height=25)
    

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=330)
    e5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e5.place(x=200,y=335,width=190,height=25)
    

    a6=Label(f1,text="Contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=400)
    e6=Label(f1,bg="white",fg="black",font=("calibri",14),text=row[5])
    e6.place(x=200,y=405,width=190,height=25)
    

    a7=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=470)
    e7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e7.place(x=200,y=475,width=190,height=25)

    a8=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=550,y=50)
    e8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e8.place(x=700,y=55,width=190,height=25)

    a9=Label(f1,text="Job_roll",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=550,y=120)
    e9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e9.place(x=700,y=125,width=190,height=25)

    a10=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=190)
    e10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e10.place(x=700,y=195,width=190,height=25)

    a11=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=260)
    a111=Label(f1,text="(in letters)",font=("calibri",12),bg=col_1,fg="black")
    a111.place(x=562,y=290)
    e11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e11.place(x=700,y=265,width=190,height=25)
    
    a12=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=330)
    e12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e12.place(x=700,y=335,width=190,height=25)
   
    a13=Label(f1,text="Salary",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=400)
    e13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e13.place(x=700,y=405,width=190,height=25)



    a61=Label(f1,text="(**********)",font=("calibri",10),bg=col_1,fg="black")
    a61.place(x=20,y=425)

    a121=Label(f1,text="(dd-mm-yyyy)",font=("calibri",12),bg=col_1,fg="black")
    a121.place(x=559,y=360)

    a41=Label(f1,text="(dd-mm-yyyy)",font=("calibri",12),bg=col_1,fg="black")
    a41.place(x=20,y=285)


    a14=Button(f1,bg="#8CC0DE",text="SUBMIT",fg="black",command=partial(employee_update_data, row))
    a14.place(x=450,y=555,width=100,height=25)


    e1.insert(0,row[0])
    e2.insert(0,row[1])
    e3.insert(0,row[2])
    e4.insert(0,row[3])
    e5.insert(0,row[4])
    #e6.insert(0,row[5])
    e7.insert(0,row[6])
    e8.insert(0,row[7])
    e9.insert(0,row[8])
    e10.insert(0,row[9])
    e11.insert(0,row[10])
    e12.insert(0,row[11])
    e13.insert(0,row[12])
  


def employee_update_data(row):
    
    date=datetime.today()
    year=date.year
    
    
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()==""  or e7.get()=="" or e8.get()=="" or e10.get()=="" or e11.get()=="" or e12.get()=="" or e13.get()=="":
        messagebox.showwarning("Warning","all field are requried")



 #name_validation

    elif re.findall(r'\W',(e1.get())):

       messagebox.showwarning("Warning","invalid name please remove unnecessary special characters")

    elif re.findall("[0-9]",(e1.get())):

        messagebox.showwarning("Warning","invalid name please remove unnecessary numbers")



    #lname_validation

    elif re.findall(r'\W',(e2.get())):
        messagebox.showwarning("Warning","invalid l_name please remove unnecessary special characters")

    elif re.findall("[0-9]",(e2.get())):
        messagebox.showwarning("Warning","invalid l_name please remove unnecessary numbers")


    #age validation

    elif re.findall("[a-zA-Z]",(e3.get())):
        messagebox.showwarning("Warning","please check your age")

    elif re.findall(r'\W',(e3.get())):
        messagebox.showwarning("Warning","please check your age")

    elif int(e3.get())<18 or int(e3.get())>100:
        messagebox.showwarning("Warning","please check your age")

    #dob

    elif re.findall("[a-zA-Z]",(e4.get())):
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

    elif  re.findall('[ @_!#$^%&*(.)<>?/|}{;:"`,]',(e4.get())):
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")

    elif len(e4.get())<10 or len(e4.get())>10:
        messagebox.showwarning("Warning","invaild D.O.B please enter the same format(dd-mm-yyyy)")


    elif (int(e4.get()[:2]))>31 or (int(e4.get()[:2]))==0 :
        messagebox.showwarning("Warning","invaild D.O.B please check the date")

    elif  (int(e4.get()[3:5]))==0 or  (int(e4.get()[3:5]))>12 :
        messagebox.showwarning("Warning","invaild D.O.B  please check the month")


    elif int(e4.get()[6:])<1990 or int(e4.get()[6:])>(year-19) :
        messagebox.showwarning("Warning","invaild D.O.B please check the year")

    elif year-int(e4.get()[6:])< int(e3.get()) or year-int(e4.get()[6:]) >int(e3.get()):
        messagebox.showwarning("Warning","invaild D.O.B not match to age please check")


             
    #email validation
     
    elif (re.findall("[A-Z]",(e5.get()))):
                  
         messagebox.showwarning("Warning","invalid Email please romove uppercase")

    elif (re.findall('[ _!#$^%&*()<>?/|}{;:"`,]',(e5.get()))):
                  
         messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")

    elif not e5.get().endswith("@gmail.com"):
     
         messagebox.showwarning("Warning","invalid Email please endswith @gmail.com")
         

    #qualification validation


    elif re.findall(r'\W',(e7.get())):
             messagebox.showwarning("Warning","invalid qualification please remove unnecessary special characters")

    elif re.findall("[0-9]",(e7.get())):
             messagebox.showwarning("Warning","invalid qualification please remove unnecessary numbers")

    #city_validation

    elif re.findall(r'\W',(e8.get())):
         messagebox.showwarning("Warning","invalid city please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e8.get())):
         messagebox.showwarning("Warning","invalid city please remove unnecessary numbers")

    #job_roll_validation

    elif re.findall(r'\W',(e9.get())):
         messagebox.showwarning("Warning","invalid job_roll please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e9.get())):
         messagebox.showwarning("Warning","invalid job_roll please remove unnecessary numbers")

    #pre company_validation

    elif re.findall(r'\W',(e10.get())):
         messagebox.showwarning("Warning","invalid pre_company please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e10.get())):
         messagebox.showwarning("Warning","invalid pre_company please remove unnecessary numbers")

    #experience_validation

    elif re.findall('[@_!#$^%&*(.)<>?/|}{~;:"`~,]',(e11.get())):
         messagebox.showwarning("Warning","invalid experience please remove unnecessary special characters")
         
    elif re.findall("[0-9]",(e11.get())):
         messagebox.showwarning("Warning","invalid experience please remove unnecessary numbers")



    #salary
             
    elif re.findall("[a-zA-Z]",e13.get()):
             messagebox.showwarning("warning","invalid salary please remove unnecessary letters")  
     
    elif re.findall('[ @_!#$^%&*()<>?/|}{;:"`.]',e13.get()):
             messagebox.showwarning("warning","invalid salary please remove unnecessary special characters")
    
    elif int(e13.get())<4999:
            messagebox.showwarning("warning","invalid salary minimun salary is 5000")

        


    else:
        
             db=py.connect(host=host_1,user=user_1,password=password_1,database="pravin")
             my=db.cursor()
             my.execute("select *from employee where contact=%s",row[5])
             row=my.fetchone()
             print(row[5])
             print(row)

             if row==None:
                 messagebox.showwarning("Warning","contact number dosn't exists")
                
             else:
                 
                 c="update employee set name=%s ,last_name=%s,age=%s,dob=%s,email=%s,qualification=%s,city=%s,job_roll=%s,pre_company=%s,experience=%s,date=%s,salary_package=%s where contact=%s"
                 d=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),row[5])
                 print(d)
                 my.execute(c,d)
                 my.execute("select *from employee where contact=%s",row[5])
                 row=my.fetchone()
                 print(row)
                 db.commit()
                 db.close()
                 messagebox.showinfo("success","Update completed")
                 for widgets in f1.winfo_children():
                     widgets.destroy()






            


def employee_del():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="EMPLOYEE_ID_DELETE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=employee_del_details).place(x=445,y=350,height=25,width=100)


def employee_del_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please enter 10 digit")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid contact please remove unnecessary letters")
         
    else:
        try:
            
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            b="select *from employee where contact=%s"
            d=t1.get()

            my.execute(b,d)
            i=my.fetchone()
            if i==None:
                messagebox.showwarning("Warning","contact number doesn't exists")
        
            else:
                
                db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                my=db.cursor()
                b="delete from employee where contact=%s"
                d=t1.get()

                my.execute(b,d)
                db.commit()
                db.close()
                messagebox.showinfo("success","data deleted")
                for widgets in f1.winfo_children():
                     widgets.destroy()

        except:
              print("hlo")



def trainee_del():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="TRAINEE_ID_DELETE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=trainee_del_details).place(x=445,y=350,height=25,width=100)



def trainee_del_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid l_name please remove unnecessary letters")
         
    else:
        try:
            
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            b="select *from trainee where contact=%s"
            d=t1.get()

            my.execute(b,d)
            i=my.fetchone()
            if i==None:
                messagebox.showwarning("Warning","contact number doesn't exists")
        
            else:
                
                db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                my=db.cursor()
                b="delete from trainee where contact=%s"
                d=t1.get()

                my.execute(b,d)
                db.commit()
                db.close()
                messagebox.showinfo("success","data deleted")
                for widgets in f1.winfo_children():
                     widgets.destroy()

        except:
              print("hlo")
               
        

def employee_clear():
   for widgets in f1.winfo_children():
      widgets.destroy()



def clear():
    
    for widgets in f1.winfo_children():
      widgets.destroy()
    for widgets in f3.winfo_children():
      widgets.destroy()






def admin():

        #frame_2 frame_3 clear
    
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
            
    tittle=Label(f3,text="TRAINEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)   
    
    b=Button(f3,text="TRAINEE_REGISTER",command=trainee_id_admin)
    b.place(x=20,y=45,width=125)

    b1=Button(f3,text="EMPLOYEE_REGISTER",command=employee_id_admin)
    b1.place(x=220,y=45,width=125)

    b2=Button(f3,text="NOTICEBOARD",command=NOTICEBOARD)
    b2.place(x=430,y=45,width=100)





def trainee_id_admin():

     #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
            
    tittle=Label(f3,text="TRAINEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)   
    
    b=Button(f3,text="SIGN_UP",command=trainee)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="LOGIN",command=trainee_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="UPDATE",command=trainee_update)
    b2.place(x=430,y=45,width=100)
    
    b3=Button(f3,text="DELETE",command=trainee_del)
    b3.place(x=620,y=45,width=100)


    b4=Button(f3,text="BACK",command=admin)
    b4.place(x=820,y=45,width=100)



def employee_id_admin():

      #frame_2 frame_3 clear
    
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
           
    tittle=Label(f3,text="EMPLOYEE",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=450,y=5)
    
    b=Button(f3,text="SIGN_UP",command=employee)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="LOGIN",command=employee_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="UPDATE",command=employee_update)
    b2.place(x=430,y=45,width=100)
    
    
    b3=Button(f3,text="DELETE",command=employee_del)
    b3.place(x=620,y=45,width=100)


    b4=Button(f3,text="BACK",command=admin)
    b4.place(x=820,y=45,width=100)

    





def sign():
    
    for widget in f1.winfo_children():
        widget.destroy()
     
  
    window.configure(background=col_1)
    global s1,s2,s3,s4
    tittle=Label(f1,text="SIGN_UP",font=("calibri",30,"bold"),bg=col_1,fg="#F8EDFF")
    tittle.place(x=465,y=10)

    a1=Label(f1,text="Name",font=("calibri",20),bg=col_1,fg="#BFCFE7")
    a1.place(x=300,y=130)
    s1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    s1.place(x=460,y=135,width=250,height=32)

    a2=Label(f1,text="Mobile_no",font=("calibri",20),bg=col_1,fg="#BFCFE7")
    a2.place(x=300,y=200)
    s2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    s2.place(x=460,y=205,width=250,height=32)
        

    a3=Label(f1,text="Email",font=("calibri",20),bg=col_1,fg="#BFCFE7")
    a3.place(x=300,y=270)
    s3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    s3.place(x=460,y=275,width=250,height=32)

    a4=Label(f1,text="Password",font=("calibri",20),bg=col_1,fg="#BFCFE7")
    a4.place(x=300,y=340)
    s4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    s4.place(x=460,y=345,width=250,height=32)


    s=Button(f1,text="submit",bg="#8CC0DE",command=sign_submit).place(x=485,y=420,width=150,height=30)



def sign_submit():
    if s1.get()=="" or s2.get()=="" or s3.get()=="" or s4.get()=="" :
        messagebox.showwarning("Warning","all fields are required")
    
    
    else:
        #try:
             
                 db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                 my=db.cursor()
             
  
      
         

                     
             #name_validation
                 if re.findall(r'\W',(s1.get())):
                     
                     messagebox.showwarning("Warning","invalid name please remove unnecessary special characters")
                     
                 elif re.findall("[0-9]",(s1.get())):
                     
                     messagebox.showwarning("Warning","invalid name please remove unnecessary numbers")
    
                 
                     
             #mobile number validation
                    
                 elif not( (s2.get()[0])=="6" or (s2.get()[0])=="7" or (s2.get()[0])=="8" or (s2.get()[0])=="9" ):
                    messagebox.showwarning("Warning","invalid contact please check your contact")
                    
                 elif not (len(s2.get())==10):
                        messagebox.showwarning("Warning","invalid contact please enter 10 digit contact")



                     
                 
                         
            #email validation
                 
                 elif (re.findall("[A-Z]",(s3.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please romove uppercase")
                
                 elif (re.findall('[ _!#$^%&*()<>?/|}{;:"`,]',(s3.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")
                     
                 elif (s3.get()).count("@")>1:                              
                     messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")

                 elif not s3.get().endswith("@gmail.com"):                 
                     messagebox.showwarning("Warning","invalid Email please endswith @gmail.com")
                     
            #password
         
                 elif  int((len(s4.get()))<8 or int(len(s4.get()))>15):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 8 char")

                 elif not(re.findall(r'\W',s4.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 special characters")
                     
                 elif not(re.findall("[a-z]",s4.get())): 
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 letter lower")

                 elif  not(re.findall("[A-Z]",s4.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 letters upper ")
                     
                 elif not(re.findall("[0-9]",s4.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 number")
                
                     
                 else:

                     db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                     my=db.cursor()
                     my.execute("select email from login where email=%s",s3.get())
                     row=my.fetchone()
                     print(row)
                                          

                     if row != None:
                         messagebox.showwarning("Warning","email id alredy exists")                     

                     else:
                                                                          
                         c="insert into login(name,contact ,email,password) values (%s,%s,%s,%s)"
                         d=(s1.get(),s2.get(),s3.get(),s4.get())
                         my.execute(c,d)
                         db.commit()

                         messagebox.showinfo("success","data submitted")
                         for widgets in f1.winfo_children():
                             widgets.destroy()
                         
                
            








def a_login():
    
    for widget in f1.winfo_children():
        widget.destroy()

      
    global L1,L2
    
    tittle=Label(f1,text="LOGIN",font=("calibri",30,"bold"),bg=col_1,fg="#3D3B40")
    tittle.place(x=490,y=120)

    a1=Label(f1,text="Email",font=("calibri",20),bg=col_1,fg="#3D3B40")
    a1.place(x=300,y=230)
    L1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    L1.place(x=460,y=240,width=250,height=32)
        

    a2=Label(f1,text="Password",font=("calibri",20),bg=col_1,fg="#3D3B40")
    a2.place(x=300,y=310)
    L2=Entry(f1,bg="white",fg="black",font=("calibri",14),show="*")
    L2.place(x=460,y=315,width=250,height=32)


    f=Button(f1,text="submit",bg="#8CC0DE",command=a_login_submit).place(x=500,y=380,width=150,height=30)






def a_login_submit():


    


    if  L1.get()=="" or L2.get()=="":
        messagebox.showwarning("Warning","all fields are required")


    else:
        #try:
             
                 db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                 my=db.cursor()
             
              
            #email validation
                 
                 if (re.findall("[A-Z]",(L1.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please romove uppercase")
                
                 elif (re.findall('[ _!#$^%&*()<>?/|}{;:"`,]',(L1.get()))):
                              
                     messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")
                     
                 elif (L1.get()).count("@")>1:                              
                     messagebox.showwarning("Warning","invalid Email please remove unnecessary special characters")

                 elif not L1.get().endswith("@gmail.com"):                 
                     messagebox.showwarning("Warning","invalid Email please endswith @gmail.com")
                     
            #password
         
                 elif  int((len(L2.get()))<8 or int(len(L2.get()))>15):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 8 char")

                 elif not(re.findall(r'\W',L2.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 special characters")
                     
                 elif not(re.findall("[a-z]",L2.get())): 
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 letter lower")

                 elif  not(re.findall("[A-Z]",L2.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 letters upper ")
                     
                 elif not(re.findall("[0-9]",L2.get())):
                     messagebox.showwarning("Warning","invalid Password please enter minimum 1 number")
                


            
                 else:
                             
                        db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                        my=db.cursor()
                        my.execute("select email,password from login where email=%s",L1.get())
                        row=my.fetchone()
                        print(row)

                             
                        if row == None:
                             messagebox.showwarning("Warning","email id doesn't match")
                             
                        elif row[1] != str(L2.get()):
                             messagebox.showwarning("Warning","invalid Password")
                             
                        else:
                            admin()
                            for widget in f1.winfo_children():
                                widget.destroy()
                            
                            db.close()
                
                     

                  
                   











def hello():
    
    
    for widget in f1.winfo_children():
        widget.destroy()

    for widget in f3.winfo_children():
        widget.destroy()
        
    f=Button(f3,text="SIGNUP",bg="#8CC0DE",command=sign).place(x=250,y=30,width=150,height=30)
 
    f=Button(f3,text="LOGIN",bg="#8CC0DE",command=a_login).place(x=570,y=30,width=150,height=30)

    

                                                           #task file


def add_todo():

    
    # Get today's date
    today = datetime.today()
    # Format the date in day, month, year format
    today_str = today.strftime("%d-%m-%Y")
    print(today_str) # Output: "23-02-2023" (day-month-year)
    day=str(today_str)
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    print(entry.get())
    db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
    my=db.cursor()
    c=("insert into task(name,time) values (%s,%s)")
    d=(entry.get(),day)
    my.execute(c,d)
    db.commit()
    db.close()
    entry.delete(0, ctk.END)
    




def task():


    


    for widget in f1.winfo_children():
        widget.destroy()    
    
    global entry,scrollable_frame
    title_label = ctk.CTkLabel(f1, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(padx=10, pady=(40, 20))

    scrollable_frame = ctk.CTkScrollableFrame(f1, width=800, height=400)
    scrollable_frame.pack()

    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add task")
    entry.pack(fill="x")

    add_button = ctk.CTkButton(f1, text="Add", width=500, command=add_todo)
    add_button.pack(pady=10)
    
    add_button = ctk.CTkButton(f1, text="PRE_TASK", width=500,command=task_show)
    add_button.pack(pady=10)







def task_submit():
    

    if entry.get()=="":
        messagebox.showwarning("Warning","please fill the date ")

        
    elif re.findall("[a-zA-Z]",(entry.get())):
        messagebox.showwarning("Warning","invaild DATE please enter the same format(dd-mm-yyyy)")

    elif  re.findall('[ @_!#$^%&*(.)<>?/|}{;:"`=,]',(entry.get())):
        messagebox.showwarning("Warning","invaild DATE please enter the same format(dd-mm-yyyy)")

    elif len(entry.get())<10 or len(entry.get())>10:
        messagebox.showwarning("Warning","invaild DATE please enter the same format(dd-mm-yyyy)")


    elif (int(entry.get()[:2]))>31 or (int(entry.get()[:2]))==0 :
        messagebox.showwarning("Warning","invaild DATE please check the date")

    elif  (int(entry.get()[3:5]))==0 or  (int(entry.get()[3:5]))>12 :
        messagebox.showwarning("Warning","invaild DATE  please check the month")


    elif int(entry.get()[6:])<2020:
        messagebox.showwarning("Warning","invaild DATE please check the year")





    else:
        
        
        db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
        my=db.cursor()
        c=("select * from task where time=(%s)")
        d=(entry.get())
        my.execute(c,d)
   
        row=my.fetchall()
        print(row)
        print("---------------------------------")
        if row == None:
            messagebox.showwarning("Warning","Data not found in this date ")

        else:
            
            global app
    
            app=[]
            for i in range(len(row)):
                if not row[i][0]=="":
                    if not row[i][0]==None:
                        show=row[i][0]
                        print(show)
                        app.append(show)

            print(app)
            data(app)
 
                        
        
        db.commit()
        db.close()





def task_show():
    global entry


    for widget in f1.winfo_children():
        widget.destroy() 
    
    scrollable_frame = ctk.CTkScrollableFrame(master=f1, width=500, height=50, label_text="Previous Task")
    scrollable_frame.pack(pady=50)


    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="enter the date",width=250)
    entry.pack(pady=40)



    

    add_button = ctk.CTkButton(f1, text="SHOW", width=500, command=task_submit)
    add_button.pack(pady=10)
    
    add_button = ctk.CTkButton(f1, text="BACK", width=500,command=task)
    add_button.pack(pady=10)
    
    






def data(app):
    for widget in f1.winfo_children():
        widget.destroy()
    

    scrollable_frame = ctk.CTkScrollableFrame(master=f1, width=500, height=300, label_text="PREVIOUS TASK")
    scrollable_frame.pack(pady=50)


    for j in range(len(app)):
        label = tkinter.Label(scrollable_frame, text=app[j],height=0,width=100)
        label.pack()

    add_button = ctk.CTkButton(f1, text="BACK", width=500,command=task_show)
    add_button.pack(pady=10)











def T_submit():
    
    # Get today's date
    today = datetime.today()
    # Format the date in day, month, year format
    today_str = today.strftime("%d-%m-%Y")
    print(today_str) # Output: "23-02-2023" (day-month-year)
    day=str(today_str)
    contact=t_entry.get()
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    print(entry.get())


    db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
    my=db.cursor()
    my.execute("select *from employee where contact=%s",t_entry.get())
    row=my.fetchone()
    
    if row == None:
         messagebox.showwarning("Warning","contact number doesn't match")
    else:
        
        db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
        my=db.cursor()
        c=("insert into feedback(contant,contact,date) values (%s,%s,%s)")
        d=(entry.get(),contact,day)
        my.execute(c,d)
        db.commit()
        db.close()
        entry.delete(0, ctk.END)
    


   


def T_feedback():

    


    for widget in f1.winfo_children():
        widget.destroy()    
    
    global t_entry,entry,scrollable_frame
    title_label = ctk.CTkLabel(f1, text="FEED BACK", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(padx=10, pady=(40, 20))

    scrollable_frame = ctk.CTkScrollableFrame(f1, width=800, height=400)
    scrollable_frame.pack()

    t_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Employee_contact",width=300)
    t_entry.pack()    

    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="add_feedback")
    entry.pack(fill="x",pady=10)

    add_button = ctk.CTkButton(f1, text="Add", width=500, command=T_submit)
    add_button.pack(pady=10)
    


	



def employee_feed():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="EMPLOYEE_FEEDBACK",font=("calibri",20),bg=col_1,fg="black")
    tittle.place(x=375,y=148)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=employee_check).place(x=445,y=350,height=25,width=100)







def employee_check():
    global d
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid l_name please remove unnecessary letters")

    else:
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from feedback where contact=%s",t1.get())
            hlo=my.fetchone()
            row=my.fetchall()
            print(row)
            
            if hlo == None:
                 messagebox.showwarning("Warning","NO FEEDBACK")
                 
            else:
                if row!=None:
                    
                    d=[]
                    for i in range(len(row)):
                        c=row[i][2]
                        b=row[i][0]
                        if c not in d:
                            d.append(c)
                            d.append(b)        
                        else:
                            d.append(b)
                    employee_feedback()
                    

                                    
                    
                    db.close()
            







def employee_feedback():
    global txt
    
    for widget in f1.winfo_children():
        widget.destroy()   

       
   
    lable1 = Label(f1, bg=col_1, fg=TEXT_COLOR, text="FEEDBACK", font=FONT_BOLD, pady=10, width=20, height=1).pack(padx=200)

    txt = Text(f1, bg=col_1, fg=TEXT_COLOR, font=FONT, width=90)
    txt.pack()

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.980)

    send = Button(f1, text="SHOW", bg=BG_GRAY,width=10,command=employee_feedback_read).place(x=480,y=580)




def employee_feedback_read():
    global send
    
    for j in d:
        t=str(j)
        send =t
        txt.insert(END, "\n\n" + send)
        

                
           
def send():
    global don,con
    txt.delete(1.0, END)
    t_number=t1.get()
    e_number=t2.get()
    db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
    my=db.cursor()
    a="insert into t_chat (contant,t_contact,e_contact) values (%s,%s,%s)"
    b="Trainee ->"+e.get(),t_number,e_number
    #print(b)
    my.execute(a,b)
    c="select * from t_chat where t_contact=%s and e_contact=%s"
    d=t_number,e_number
    my.execute(c,d)
    con=my.fetchall()
    #print(con)
    db.commit()
    db.close()
    send_t()
    e.delete(0, tkinter.END)


def send_t():
    global send
    
    for i in range(len(con)):
            c=con[i][0]
            print(c)
            send =c
            txt.insert(END, "\n\n" + send)
    

	
  
		
def send_1():
    global don,con
    
    txt.delete(1.0, END) 
    e_number=t1.get()
    print(e_number)
    
    t_number=t2.get()
    
    db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
    my=db.cursor()
    a="insert into t_chat (contant,t_contact,e_contact) values (%s,%s,%s)"
    b="Employee ->"+e1.get(),t_number,e_number
   # print(b)
    my.execute(a,b)
    c="select * from t_chat where t_contact=%s and e_contact=%s"
    d=t_number,e_number
    my.execute(c,d)
    con=my.fetchall()
    #print(con)
    db.commit()
    db.close()
    send_t()
    e1.delete(0, tkinter.END)
    



def trainee_Chat():
    global e,e1,txt,send
        
    lable1 = Label(f1, bg=col_1, fg=TEXT_COLOR, text="CHAT", font=FONT_BOLD, pady=10, width=20, height=1).pack(padx=200)

    txt = Text(f1, bg=col_1, fg=TEXT_COLOR, font=FONT, width=90,height=20)
    txt.pack()


    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.980)

    e = Entry(f1, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=80)
    e.place(x=15,y=520)

    send = Button(f1, text="Send", bg=BG_GRAY,width=10,command=send).place(x=915,y=520)
            






def employee_chat():
    
    global e,e1,txt,send
        
    lable1 = Label(f1, bg=col_1, fg=TEXT_COLOR, text="CHAT", font=FONT_BOLD, pady=10, width=20, height=1).pack(padx=200)

    txt = Text(f1, bg=col_1, fg=TEXT_COLOR, font=FONT, width=90,height=20)
    txt.pack()


    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.980)

            

    e1 = Entry(f1, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=80)
    e1.place(x=15,y=560)

    send = Button(f1, text="Send", bg=BG_GRAY,width=10,command=send_1).place(x=915,y=560)



def trainee_chat_login():
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global t1,t2
    tittle=Label(f1,text="TRAINEE_CHAT_BOX",font=("calibri",18),bg=col_1,fg="black")
    tittle.place(x=380,y=150)
    a1=Label(f1,text="ENTER_YOUR_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=230)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=285,width=190,height=30)
    a2=Label(f1,text="ENTER_EMPLOYEE_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=380,y=345)
    t2=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t2.place(x=400,y=400,width=190,height=30)
    b=Button(f1,text="Submit",command=trainee_chat_login_submit).place(x=445,y=450,height=25,width=100)


def trainee_chat_login_submit():
    
    global d
    
    if t1.get()=="" or t2.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid YOUR contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid  YOUR contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid YOUR contact please remove unnecessary letters")


        
    elif not( (t2.get()[0])=="6" or (t2.get()[0])=="7" or (t2.get()[0])=="8" or (t2.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid EMPLOYEE contact please check your contact")
        
    elif not (len(t2.get())==10):
            messagebox.showwarning("Warning","invalid EMPLOYEE contact please check your contact")

    elif re.findall("[a-zA-Z]",(t2.get())):
         messagebox.showwarning("Warning","invalid EMPLOYEE contact please remove unnecessary letters")
         
    else:
        #try:         
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from trainee where contact=%s",t1.get())
            
            hlo=my.fetchone()
            my.execute("select *from employee where contact=%s",t2.get())
            row=my.fetchone()
            print(hlo)
            print(row)
            
            
            
            if hlo == None:
                 messagebox.showwarning("Warning","incorrect trainee contact number")
            elif row == None:
                 messagebox.showwarning("Warning","incorrect employee contact number")
            else:
                
                trainee_Chat()
                global don,con
                txt.delete(1.0, END)
                t_number=t1.get()
                e_number=t2.get()
                db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                my=db.cursor()
         
                c="select * from t_chat where t_contact=%s and e_contact=%s"
                d=t_number,e_number
                my.execute(c,d)
                con=my.fetchall()
                #print(con)
                db.commit()
                db.close()
                send_t()
                e.delete(0, tkinter.END)


            
                



def employee_chat_login():
    for widgets in f1.winfo_children():
      widgets.destroy()
      
      
    global t1,t2
    tittle=Label(f1,text="EMPLOYEE_CHAT_BOX",font=("calibri",18),bg=col_1,fg="black")
    tittle.place(x=370,y=150)
    a1=Label(f1,text="ENTER_YOUR_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=230)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=285,width=190,height=30)
    a2=Label(f1,text="ENTER_TRAINEE_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=380,y=345)
    t2=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t2.place(x=400,y=400,width=190,height=30)
    
    b=Button(f1,text="Submit",command=employee_chat_login_submit).place(x=445,y=450,height=25,width=100)
    
    



def employee_chat_login_submit():
    
    global d
    
    if t1.get()=="" or t2.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    elif not( (t1.get()[0])=="6" or (t1.get()[0])=="7" or (t1.get()[0])=="8" or (t1.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid YOUR contact please check your contact")
        
    elif not (len(t1.get())==10):
            messagebox.showwarning("Warning","invalid  YOUR contact please check your contact")

    elif re.findall("[a-zA-Z]",(t1.get())):
         messagebox.showwarning("Warning","invalid YOUR contact please remove unnecessary letters")


        
    elif not( (t2.get()[0])=="6" or (t2.get()[0])=="7" or (t2.get()[0])=="8" or (t2.get()[0])=="9" ):
        messagebox.showwarning("Warning","invalid EMPLOYEE contact please check your contact")
        
    elif not (len(t2.get())==10):
            messagebox.showwarning("Warning","invalid EMPLOYEE contact please check your contact")

    elif re.findall("[a-zA-Z]",(t2.get())):
         messagebox.showwarning("Warning","invalid EMPLOYEE contact please remove unnecessary letters")
         
    else:
                 
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from employee where contact=%s",t1.get())
            
            hlo=my.fetchone()
            my.execute("select *from  trainee where contact=%s",t2.get())
            row=my.fetchone()
            print(hlo)
            print(row)
            
            
            
            if hlo == None:
                 messagebox.showwarning("Warning","incorrect trainee contact number")
            elif row == None:
                 messagebox.showwarning("Warning","incorrect employee contact number")
            
            else:
                employee_chat()
            
                global don,con
                
                txt.delete(1.0, END) 
                e_number=t1.get()
                print(e_number)
                
                t_number=t2.get()
                
                db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                my=db.cursor()
                c="select * from t_chat where t_contact=%s and e_contact=%s"
                d=t_number,e_number
                my.execute(c,d)
                con=my.fetchall()
                #print(con)
                db.commit()
                db.close()
                send_t()
                e1.delete(0, tkinter.END)








def notice_check():
    global d
    db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
    my=db.cursor()
    my.execute("select * from notice")
    
    row=my.fetchall()
    print(row)
    if row == "":
        pass
    else:
        
        
        d=[]
        for i in range(len(row)):
            e=row[i][1]
            c=row[i][0]
            if e not in d:
                d.append(e)
                d.append(c)
            else:
                d.append(c)
        print(d)               
                
        notice_read(d)

        db.close()

def notice_read(d):
    global send
    
    for j in d:
        t=str(j)
        send =" "+t
        txt.insert(END, "\n\n" + send)       







def notice_feedback():
    global txt
    
    for widget in f1.winfo_children():
        widget.destroy()   

       
   
    lable1 = Label(f1, bg=col_1, fg=TEXT_COLOR, text="FEEDBACK", font=FONT_BOLD, pady=10, width=20, height=1).pack(padx=200)

    txt = Text(f1, bg=col_1, fg=TEXT_COLOR, font=FONT, width=90)
    txt.pack()

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.980)

    send = Button(f1, text="SHOW", bg=BG_GRAY,width=10,command=notice_check).place(x=480,y=580)








def noticeboard():
    # Get today's date
    today = datetime.today()
    # Format the date in day, month, year format
    today_str = today.strftime("%d-%m-%Y")
    print(today_str) # Output: "23-02-2023" (day-month-year)
    day=str(today_str)
    
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    print(entry.get())
    if not ( entry.get()==""):
      
        db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
        my=db.cursor()
        c=("insert into notice(contant,time) values (%s,%s)")
        d=(entry.get(),day)
        my.execute(c,d)
        db.commit()
        db.close()
        entry.delete(0, ctk.END)
    






def NOTICEBOARD():
    global entry,scrollable_frame

    title_label = ctk.CTkLabel(f1, text="NOTICEBOARD", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(padx=10, pady=(40, 20))

    scrollable_frame = ctk.CTkScrollableFrame(f1, width=800, height=400)
    scrollable_frame.pack()
       
    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add_Note")
    entry.pack(fill="x",pady=10)

    add_button = ctk.CTkButton(f1, text="Add", width=500, command=noticeboard)
    add_button.pack(pady=10)










b=Button(f,text="ADMIN",command=hello,bg=col_4)
b.place(x=20,y=30,width=100,height=30)


b1=Button(f,text="TRAINEE",command=trainee_main,bg=col_5)
b1.place(x=220,y=30,width=100,height=30)


b2=Button(f,text="EMPLOYEE",command=employee_main,bg=col_4)
b2.place(x=440,y=30,width=100,height=30)

b5=Button(f,text="CLEAR",command=clear,bg=col_6)
b5.place(x=660,y=30,width=100,height=30)

b6=Button(f,text="EXIT",command=window.destroy,bg=col_7)
b6.place(x=880,y=30,width=100,height=30)


window.mainloop()
