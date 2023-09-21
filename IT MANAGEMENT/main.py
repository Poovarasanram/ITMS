from tkinter import *
from tkinter import messagebox
from functools import partial

import color as cs
import database as db
import pymysql as py

# database conctivity
host_1=db.host
user_1=db.user
password_1=db.password
database_1=db.database


#colors
col_1=cs.color_1
col_2=cs.color_2                            
col_3=cs.color_3
col_4=cs.color_4
col_5=cs.color_5
col_6=cs.color_6
col_7=cs.color_7


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




def intern_id():
    for widgets in f3.winfo_children():
      widgets.destroy()
    for widgets in f1.winfo_children():
      widgets.destroy()
      
      
    
    tittle=Label(f3,text="INTERNSHIP",font=("calibri",14,"bold"),bg=col_3,fg="black")
    tittle.place(x=440,y=5)
    
    
    b=Button(f3,text="SIGN_UP",command=intern)
    b.place(x=20,y=45,width=100)

    b1=Button(f3,text="LOGIN",command=intern_login)
    b1.place(x=220,y=45,width=100)

    b2=Button(f3,text="UPDATE",command=intern_update)
    b2.place(x=430,y=45,width=100)

    b3=Button(f3,text="DELETE",command=intern_del)
    b3.place(x=620,y=45,width=100)

    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)



def trainee_id():
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

    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)


def employee_id():
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

    b4=Button(f3,text="CLEAR",command=employee_clear)
    b4.place(x=820,y=45,width=100)

                          #frame_2 func

                         #login functions

def intern_login():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="INTERN_LOGIN_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=400,y=58)
    
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=intern_login_page).place(x=445,y=350,height=25,width=100)
    


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

#update functions

def intern_update():
    for widgets in f1.winfo_children():
      widgets.destroy()

    global t1
    tittle=Label(f1,text="INTERN_UPDATE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=intern_update_details).place(x=445,y=350,height=25,width=100)
    


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



def intern_del():
    for widgets in f1.winfo_children():
      widgets.destroy()
    global t1
    tittle=Label(f1,text="INTERN_ID_DELETE_PROCESS",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=370,y=58)
    a1=Label(f1,text="ENTER_CONTACT_NUMBER",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=380,y=250)
    t1=Entry(f1,bg="white",fg="black",font=("times new roman",13))
    t1.place(x=400,y=305,width=190,height=30)
    b=Button(f1,text="Submit",command=intern_del_details).place(x=445,y=350,height=25,width=100)
    
#delete functions

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




def employee_clear():
   for widgets in f1.winfo_children():
      widgets.destroy()

def clear():
    
    for widgets in f1.winfo_children():
      widgets.destroy()
    for widgets in f3.winfo_children():
      widgets.destroy()





                              #frame_1 func 
 
def intern():
    for widgets in f1.winfo_children():
      widgets.destroy()

   
    global i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18
    
    tittle=Label(f1,text="INTERNSHIP_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    i1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    i2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    i3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    i4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    i5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    i6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    i7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    i8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="intern_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    i9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    i10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    i11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    i12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    i13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    i14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    i15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    i16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    i17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Stipend",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    i18=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i18.place(x=700,y=535,width=190,height=25)

    a19=Button(f1,text="submit",bg="#8CC0DE",command=intern_submit)
    a19.place(x=440,y=570,width=100)


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
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    t2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    t3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    t4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    t5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    t6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    t7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    t8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="Training_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    t9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    t10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    t11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    t12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    t13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    t14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    t15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    t16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    t17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    t18=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t18.place(x=700,y=535,width=190,height=25)
    
    a19=Button(f1,text="submit",bg="#8CC0DE",command=trainee_submit)
    a19.place(x=440,y=570,width=100)

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
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    e2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    e3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    e4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    e5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    e6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Job_Roll",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    e7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    e8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e8.place(x=200,y=475,width=190,height=25)
    

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    e10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="Gender",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    e11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    e12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="acc_no",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    e13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="Relationship",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    e14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    e15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    e16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    e17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e17.place(x=700,y=475,width=190,height=25)

    a18=Button(f1,bg="#8CC0DE",text="SUBMIT",fg="black",command=employee_submit)
    a18.place(x=450,y=555,width=100,height=25)



def intern_show(i):
    for widgets in f1.winfo_children():
      widgets.destroy()

   
  
    
    tittle=Label(f1,text="INTERNSHIP_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    i1=Label(f1,bg="white",text=i[0],fg="black",font=("calibri",14))
    i1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    i2=Label(f1,bg="white",text=i[1],fg="black",font=("calibri",14))
    i2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    i3=Label(f1,bg="white",text=i[2],fg="black",font=("calibri",14))
    i3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    i4=Label(f1,bg="white",text=i[3],fg="black",font=("calibri",14))
    i4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    i5=Label(f1,bg="white",text=i[4],fg="black",font=("calibri",14))
    i5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    i6=Label(f1,bg="white",text=i[5],fg="black",font=("calibri",14))
    i6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    i7=Label(f1,bg="white",text=i[6],fg="black",font=("calibri",14))
    i7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    i8=Label(f1,bg="white",text=i[7],fg="black",font=("calibri",14))
    i8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="intern_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    i9=Label(f1,bg="white",text=i[8],fg="black",font=("calibri",14))
    i9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    i10=Label(f1,bg="white",text=i[9],fg="black",font=("calibri",14))
    i10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    i11=Label(f1,bg="white",text=i[10],fg="black",font=("calibri",14))
    i11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    i12=Label(f1,bg="white",text=i[11],fg="black",font=("calibri",14))
    i12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    i13=Label(f1,bg="white",text=i[12],fg="black",font=("calibri",14))
    i13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    i14=Label(f1,bg="white",text=i[13],fg="black",font=("calibri",14))
    i14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    i15=Label(f1,bg="white",text=i[14],fg="black",font=("calibri",14))
    i15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    i16=Label(f1,bg="white",text=i[15],fg="black",font=("calibri",14))
    i16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    i17=Label(f1,bg="white",text=i[16],fg="black",font=("calibri",14))
    i17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Stipend",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    i18=Label(f1,bg="white",text=i[17],fg="black",font=("calibri",14))
    i18.place(x=700,y=535,width=190,height=25)




def trainee_show(j):
    for widgets in f1.winfo_children():
      widgets.destroy()
      

    
    tittle=Label(f1,text="TRAINEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    t1=Label(f1,bg="white",text=j[0],fg="black",font=("calibri",14))
    t1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    t2=Label(f1,bg="white",text=j[1],fg="black",font=("calibri",14))
    t2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    t3=Label(f1,bg="white",text=j[2],fg="black",font=("calibri",14))
    t3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    t4=Label(f1,bg="white",text=j[3],fg="black",font=("calibri",14))
    t4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    t5=Label(f1,bg="white",text=j[4],fg="black",font=("calibri",14))
    t5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    t6=Label(f1,bg="white",text=j[5],fg="black",font=("calibri",14))
    t6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    t7=Label(f1,bg="white",text=j[6],fg="black",font=("calibri",14))
    t7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    t8=Label(f1,bg="white",text=j[7],fg="black",font=("calibri",14))
    t8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="Training_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    t9=Label(f1,bg="white",text=j[8],fg="black",font=("calibri",14))
    t9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    t10=Label(f1,bg="white",text=j[9],fg="black",font=("calibri",14))
    t10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    t11=Label(f1,bg="white",text=j[10],fg="black",font=("calibri",14))
    t11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    t12=Label(f1,bg="white",text=j[11],fg="black",font=("calibri",14))
    t12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    t13=Label(f1,bg="white",text=j[12],fg="black",font=("calibri",14))
    t13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    t14=Label(f1,bg="white",text=j[13],fg="black",font=("calibri",14))
    t14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    t15=Label(f1,bg="white",text=j[14],fg="black",font=("calibri",14))
    t15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    t16=Label(f1,bg="white",text=j[15],fg="black",font=("calibri",14))
    t16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    t17=Label(f1,bg="white",text=j[16],fg="black",font=("calibri",14))
    t17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    t18=Label(f1,bg="white",text=j[17],fg="black",font=("calibri",14))
    t18.place(x=700,y=535,width=190,height=25)
    


def employee_show(k):
    for widgets in f1.winfo_children():
      widgets.destroy()
      

    
    tittle=Label(f1,text="EMPLOYEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    e1=Label(f1,bg="white",text=k[0],fg="black",font=("calibri",14))
    e1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    e2=Label(f1,bg="white",text=k[1],fg="black",font=("calibri",14))
    e2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    e3=Label(f1,bg="white",text=k[2],fg="black",font=("calibri",14))
    e3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    e4=Label(f1,bg="white",text=k[3],fg="black",font=("calibri",14))
    e4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    e5=Label(f1,bg="white",text=k[4],fg="black",font=("calibri",14))
    e5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    e6=Label(f1,bg="white",text=k[5],fg="black",font=("calibri",14))
    e6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Job_Roll",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    e7=Label(f1,bg="white",text=k[6],fg="black",font=("calibri",14))
    e7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    e8=Label(f1,bg="white",text=k[7],fg="black",font=("calibri",14))
    e8.place(x=200,y=475,width=190,height=25)
    

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    e10=Label(f1,bg="white",text=k[8],fg="black",font=("calibri",14))
    e10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="Gender",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    e11=Label(f1,bg="white",text=k[9],fg="black",font=("calibri",14))
    e11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    e12=Label(f1,bg="white",text=k[10],fg="black",font=("calibri",14))
    e12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="acc_no",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    e13=Label(f1,bg="white",text=k[11],fg="black",font=("calibri",14))
    e13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="Relationship",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    e14=Label(f1,bg="white",text=k[12],fg="black",font=("calibri",14))
    e14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    e15=Label(f1,bg="white",text=k[13],fg="black",font=("calibri",14))
    e15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    e16=Label(f1,bg="white",text=k[14],fg="black",font=("calibri",14))
    e16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    e17=Label(f1,text=k[15],fg="black",bg="white",font=("calibri",14))
    e17.place(x=700,y=475,width=190,height=25)

#update details
    
 
def intern_user_update(row):
    
    for widgets in f1.winfo_children():
      widgets.destroy()

   
    global i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18
    
    tittle=Label(f1,text="INTERNSHIP_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    i1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i1.insert(0, row[0])
    i1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    i2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i2.insert(0, row[1])
    i2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    i3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i3.insert(0, row[2])
    i3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    i4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i4.insert(0, row[3])
    i4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    i5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i5.insert(0, row[4])
    i5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    i6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i6.insert(0, row[5])
    i6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    i7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i7.insert(0, row[6])
    i7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    i8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i8.insert(0, row[7])
    i8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="intern_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    i9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i9.insert(0, row[8])
    i9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    i10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i10.insert(0, row[9])
    i10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    i11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i11.insert(0, row[10])
    i11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    i12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i12.insert(0, row[11])
    i12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    i13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i13.insert(0, row[12])
    i13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    i14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i14.insert(0, row[13])
    i14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    i15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i15.insert(0, row[14])
    i15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    i16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i16.insert(0, row[15])
    i16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    i17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i17.insert(0, row[16])
    i17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Stipend",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    i18=Entry(f1,bg="white",fg="black",font=("calibri",14))
    i18.insert(0, row[17])
    i18.place(x=700,y=535,width=190,height=25)

    a19=Button(f1,text="submit",bg="#8CC0DE",command=partial(show_intern_update,row))
    a19.place(x=460,y=570,width=100)


def trainee_user_update(row):
    
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18
    
    tittle=Label(f1,text="TRAINEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    t1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t1.insert(0, row[0])
    t1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    t2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t2.insert(0, row[1])
    t2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    t3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t3.insert(0, row[2])
    t3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    t4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t4.insert(0, row[3])
    t4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    t5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t5.insert(0, row[4])
    t5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    t6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t6.insert(0, row[5])
    t6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Full time/part time",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    t7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t7.insert(0, row[6])
    t7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    t8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t8.insert(0, row[7])
    t8.place(x=200,y=475,width=190,height=25)
    
    a9=Label(f1,text="Training_duration",font=("calibri",16),bg=col_1,fg="black")
    a9.place(x=20,y=530)
    t9=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t9.insert(0, row[8])
    t9.place(x=200,y=535,width=190,height=25)

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    t10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t10.insert(0, row[9])
    t10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="College_name",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    t11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t11.insert(0, row[10])
    t11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="10%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    t12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t12.insert(0, row[11])
    t12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="12%(percentage)",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    t13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t13.insert(0, row[12])
    t13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="UG",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    t14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t14.insert(0, row[13])
    t14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    t15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t15.insert(0, row[14])
    t15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="PG",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    t16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t16.insert(0, row[15])
    t16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Percentage",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    t17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t17.insert(0, row[16])
    t17.place(x=700,y=475,width=190,height=25)
    
    a18=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a18.place(x=550,y=530)
    t18=Entry(f1,bg="white",fg="black",font=("calibri",14))
    t18.insert(0, row[17])
    t18.place(x=700,y=535,width=190,height=25)
    
    a19=Button(f1,text="submit",bg="#8CC0DE",command=partial(show_trainee_update,row))
    a19.place(x=460,y=570,width=100)

                 
                
                 
                
      
def employee_user_update(row):
    
    for widgets in f1.winfo_children():
      widgets.destroy()
      
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17
    
    tittle=Label(f1,text="EMPLOYEE_ID",font=("calibri",16,"bold"),bg=col_1,fg="black")
    tittle.place(x=450,y=5)

    a1=Label(f1,text="name",font=("calibri",16),bg=col_1,fg="black")
    a1.place(x=20,y=50)
    e1=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e1.insert(0, row[0])
    e1.place(x=200,y=55,width=190,height=25)
    

    a2=Label(f1,text="age",font=("calibri",16),bg=col_1,fg="black")
    a2.place(x=20,y=110)
    e2=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e2.insert(0, row[1])
    e2.place(x=200,y=115,width=190,height=25)
    
    a3=Label(f1,text="D.O.B",font=("calibri",16),bg=col_1,fg="black")
    a3.place(x=20,y=170)
    e3=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e3.insert(0, row[2])
    e3.place(x=200,y=175,width=190,height=25)

    a4=Label(f1,text="Qualification",font=("calibri",16),bg=col_1,fg="black")
    a4.place(x=20,y=230)
    e4=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e4.insert(0, row[3])
    e4.place(x=200,y=235,width=190,height=25)

    a5=Label(f1,text="Email",font=("calibri",16),bg=col_1,fg="black")
    a5.place(x=20,y=290)
    e5=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e5.insert(0, row[4])
    e5.place(x=200,y=295,width=190,height=25)

    a6=Label(f1,text="contact",font=("calibri",16),bg=col_1,fg="black")
    a6.place(x=20,y=350)
    e6=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e6.insert(0, row[5])
    e6.place(x=200,y=355,width=190,height=25)

    a7=Label(f1,text="Job_Roll",font=("calibri",16),bg=col_1,fg="black")
    a7.place(x=20,y=410)
    e7=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e7.insert(0, row[6])
    e7.place(x=200,y=415,width=190,height=25)

    a8=Label(f1,text="Joining_date",font=("calibri",16),bg=col_1,fg="black")
    a8.place(x=20,y=470)
    e8=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e8.insert(0, row[7])
    e8.place(x=200,y=475,width=190,height=25)
    

    a10=Label(f1,text="Last_name",font=("calibri",16),bg=col_1,fg="black")
    a10.place(x=550,y=50)
    e10=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e10.insert(0, row[8])
    e10.place(x=700,y=55,width=190,height=25)

    a11=Label(f1,text="Gender",font=("calibri",16),bg=col_1,fg="black")
    a11.place(x=550,y=110)
    e11=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e11.insert(0, row[9])
    e11.place(x=700,y=115,width=190,height=25)

    a12=Label(f1,text="City",font=("calibri",16),bg=col_1,fg="black")
    a12.place(x=550,y=170)
    e12=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e12.insert(0, row[10])
    e12.place(x=700,y=175,width=190,height=25)

    a13=Label(f1,text="acc_no",font=("calibri",16),bg=col_1,fg="black")
    a13.place(x=550,y=230)
    e13=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e13.insert(0, row[11])
    e13.place(x=700,y=235,width=190,height=25)

    a14=Label(f1,text="Relationship",font=("calibri",16),bg=col_1,fg="black")
    a14.place(x=550,y=290)
    e14=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e14.insert(0, row[12])
    e14.place(x=700,y=295,width=190,height=25)
    
    a15=Label(f1,text="Pre_company",font=("calibri",16),bg=col_1,fg="black")
    a15.place(x=550,y=350)
    e15=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e15.insert(0, row[13])
    e15.place(x=700,y=355,width=190,height=25)
    
    a16=Label(f1,text="Experience",font=("calibri",16),bg=col_1,fg="black")
    a16.place(x=550,y=410)
    e16=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e16.insert(0, row[14])
    e16.place(x=700,y=415,width=190,height=25)

    a17=Label(f1,text="Salary_package",font=("calibri",16),bg=col_1,fg="black")
    a17.place(x=550,y=470)
    e17=Entry(f1,bg="white",fg="black",font=("calibri",14))
    e17.insert(0, row[15])
    e17.place(x=700,y=475,width=190,height=25)

    a18=Button(f1,bg="#8CC0DE",text="SUBMIT",fg="black",command=partial(employee_update_data, row))
    a18.place(x=460,y=555,width=100,height=25)




    
def intern_submit():
    if i1.get()=="" or i2.get()=="" or i3.get()=="" or i4.get()=="" or i5.get()=="" or i6.get()=="" or i7.get()=="" or i8.get()=="" or i9.get()=="" or i10.get()=="" or i11.get()=="" or i12.get()=="" or i13.get()=="" or i14.get()=="" or i15.get()=="" or i16.get()=="" or i17.get()=="" or i18.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from intern where contact=%s",i6.get())
             i=my.fetchone()

             if i != None:
                 messagebox.showwarning("Warning","contact number already exists")
                
             else:                
                 c="insert into intern(name,age,dob,qualification,email,contact,shift,date,duration,L_name,c_name,ten,tweleth,ug,percentage,pg,pg_percent,stipend) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                 d=(i1.get(),i2.get(),i3.get(),i4.get(),i5.get(),i6.get(),i7.get(),i8.get(),i9.get(),i10.get(),i11.get(),i12.get(),i13.get(),i14.get(),i15.get(),i16.get(),i17.get(),i18.get())            
                 my.execute(c,d)
                 db.commit()    
                 
                 messagebox.showinfo("success","data submitted")                
                 for widgets in f1.winfo_children():
                     widgets.destroy() 
                
                 
                
        except:
            print("hlo")


def trainee_submit():
    if t1.get()=="" or t2.get()=="" or t3.get()=="" or t4.get()=="" or t5.get()=="" or t6.get()=="" or t7.get()=="" or t8.get()=="" or t9.get()=="" or t10.get()=="" or t11.get()=="" or t12.get()=="" or t13.get()=="" or t14.get()=="" or t15.get()=="" or t16.get()=="" or t17.get()=="" or t18.get()=="":
        messagebox.showwarning("Warning","all fields are required")
    
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from trainee where contact=%s",t6.get())
             j=my.fetchone()

             if j!=None:
                 messagebox.showwarning("Warning","contact number already exists")
                
             else:
                 
                 c="insert into trainee(name,age,dob,qualification,email,contact,shift,date,duration,L_name,c_name,ten,tweleth,ug,percentage,pg,pg_percent,salary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                 d=(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t7.get(),t8.get(),t9.get(),t10.get(),t11.get(),t12.get(),t13.get(),t14.get(),t15.get(),t16.get(),t17.get(),t18.get())
                 my.execute(c,d)
                 db.commit()

                 messagebox.showinfo("success","data submitted")
                 for widgets in f1.winfo_children():
                     widgets.destroy()
                 
                
                 
                
        except:
            print("hlo")


def employee_submit():
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()=="" or e8.get()=="" or e17.get()=="" or e10.get()=="" or e11.get()=="" or e12.get()=="" or e13.get()=="" or e14.get()=="" or e15.get()=="" or e16.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from employee where contact=%s",e6.get())
             j=my.fetchone()

             if j!=None:
                 messagebox.showwarning("Warning","contact number already exists")
                
             else:
                 
                 c="insert into employee(name,age,dob,qualification,email,contact,jobroll,joiningdate,L_name,gender,city,accno,relationship,precompany,experience,salary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                 d=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get())
                 my.execute(c,d)
                 db.commit()

                 messagebox.showinfo("success","data submitted")
                 for widgets in f1.winfo_children():
                     widgets.destroy()
                 
                
                 
                
        except:
            print("hlo")



#login page:
        
def intern_login_page():
    
    if t1.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from intern where contact=%s",t1.get())
             i=my.fetchone()

             if i == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
             else:
                 
                 intern_show(i)
                 db.close()
        
        except:
            print(hlo)



def trainee_login_page():

    
    if t1.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from trainee where contact=%s",t1.get())
             j=my.fetchone()

             if j == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
             else:
                 
                 trainee_show(j)
                 db.close()
        
        except:
            print(hlo)



      
def employee_login_page():
    
    if t1.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from employee where contact=%s",t1.get())
             k=my.fetchone()

             if k == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
             else:
                 
                 employee_show(k)
                 db.close()
        
        except:
            print(hlo)

#update page

def intern_update_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")


    else:
        try:         
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from intern where contact=%s",t1.get())
            row=my.fetchone()
            
            if row == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
            else:
                intern_user_update(row)
                db.close()
        
         

      
        except:
            print("hlo")



def trainee_update_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")

    else:
        try:         
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            my.execute("select *from trainee where contact=%s",t1.get())
            row=my.fetchone()
            
            if row == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                 
            else:
                trainee_user_update(row)
                db.close()
        
         

      
        except:
            print("hlo")


def employee_update_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")

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

#update show button


def employee_update_data(row):
    
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="" or e7.get()=="" or e8.get()=="" or e17.get()=="" or e10.get()=="" or e11.get()=="" or e12.get()=="" or e13.get()=="" or e14.get()=="" or e15.get()=="" or e16.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    
    
    else:
        
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from employee where contact=%s",row[5])
             row=my.fetchone()

             if row==None:
                 messagebox.showwarning("Warning","contact number dosn't exists")
                
             else:
                 
                 c="update employee set name=%s,age=%s,dob=%s,qualification=%s,email=%s,jobroll=%s,joiningdate=%s,L_name=%s,gender=%s,city=%s,accno=%s,relationship=%s,precompany=%s,experience=%s,salary=%s where (contact=%s)"
                 d=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e7.get(),e8.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),row[5])
                 my.execute(c,d)
                 db.commit()
                 db.close()
                 messagebox.showinfo("success","Update completed")
                 for widgets in f1.winfo_children():
                     widgets.destroy()


            

def show_intern_update(row):
    if i1.get()=="" or i2.get()=="" or i3.get()=="" or i4.get()=="" or i5.get()=="" or i6.get()=="" or i7.get()=="" or i8.get()=="" or i9.get()=="" or i10.get()=="" or i11.get()=="" or i12.get()=="" or i13.get()=="" or i14.get()=="" or i15.get()=="" or i16.get()=="" or i17.get()=="" or i18.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from intern where contact=%s",row[5])
             row=my.fetchone()

             if row == None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                
             else:                
                 c="update intern set name=%s,age=%s,dob=%s,qualification=%s,email=%s,shift=%s,date=%s,duration=%s,L_name=%s,c_name=%s,ten=%s,tweleth=%s,ug=%s,percentage=%s,pg=%s,pg_percent=%s,stipend=%s where (contact=%s)"
                 d=(i1.get(),i2.get(),i3.get(),i4.get(),i5.get(),i7.get(),i8.get(),i9.get(),i10.get(),i11.get(),i12.get(),i13.get(),i14.get(),i15.get(),i16.get(),i17.get(),i18.get(),row[5])            
                 my.execute(c,d)
                 db.commit()    
                 db.close()
                 messagebox.showinfo("success","Update completed")                
                 for widgets in f1.winfo_children():
                    widgets.destroy()
                
                 
                
        except:
            print("hlo")


def show_trainee_update(row):
    if t1.get()=="" or t2.get()=="" or t3.get()=="" or t4.get()=="" or t5.get()=="" or t6.get()=="" or t7.get()=="" or t8.get()=="" or t9.get()=="" or t10.get()=="" or t11.get()=="" or t12.get()=="" or t13.get()=="" or t14.get()=="" or t15.get()=="" or t16.get()=="" or t17.get()=="" or t18.get()=="":
        messagebox.showwarning("Warning","all field are requried")
    
    
    else:
        try:
             
             db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
             my=db.cursor()
             my.execute("select *from trainee where contact=%s",row[5])
             j=my.fetchone()

             if j==None:
                 messagebox.showwarning("Warning","contact number doesn't exists")
                
             else:
                 
                 c="update trainee set name=%s,age=%s,dob=%s,qualification=%s,email=%s,shift=%s,date=%s,duration=%s,L_name=%s,c_name=%s,ten=%s,tweleth=%s,ug=%s,percentage=%s,pg=%s,pg_percent=%s,salary=%s where (contact=%s)"
                 d=(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t7.get(),t8.get(),t9.get(),t10.get(),t11.get(),t12.get(),t13.get(),t14.get(),t15.get(),t16.get(),t17.get(),t18.get(),row[5])
                 my.execute(c,d)
                 db.commit()
                 db.close()
                 messagebox.showinfo("success","Update completed")
                 for widgets in f1.winfo_children():
                    widgets.destroy()               
                 
                
                 
        except:
                 print("hlo")
 






#del_details

def intern_del_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    
    else:
        try:
            
            db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
            my=db.cursor()
            b="select *from intern where contact=%s"
            d=t1.get()

            my.execute(b,d)
            i=my.fetchone()
            if i==None:
                messagebox.showwarning("Warning","contact number doesn't exists")
        
            else:
                
                db=py.connect(host=host_1,user=user_1,password=password_1,database=database_1)
                my=db.cursor()
                b="delete from intern where contact=%s"
                d=t1.get()

                my.execute(b,d)
                db.commit()
                db.close()
                messagebox.showinfo("success","data deleted")
                for widgets in f1.winfo_children():
                     widgets.destroy()

        except:
              print("hlo")
               
def trainee_del_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    
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
               
        
def employee_del_details():
    if t1.get()=="":
        messagebox.showwarning("Warning","Please Fill all the fields")
        
    
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
                messagebox.showinfo("success","data deleted",)
                for widgets in f1.winfo_children():
                     widgets.destroy()

        except:
              print("hlo")
                


b=Button(f,text="INTERNSHIP",command=intern_id,bg=col_4)
b.place(x=20,y=30,width=100,height=30)

b1=Button(f,text="TRAINEE",command=trainee_id,bg=col_5)
b1.place(x=220,y=30,width=100,height=30)

b2=Button(f,text="EMPLOYEE",command=employee_id,bg=col_4)
b2.place(x=440,y=30,width=100,height=30)


b5=Button(f,text="CLEAR",command=clear,bg=col_6)
b5.place(x=660,y=30,width=100,height=30)

b6=Button(f,text="EXIT",command=window.destroy,bg=col_7)
b6.place(x=880,y=30,width=100,height=30)



window.mainloop()

