from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re
#fonction part
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    signup_window.destroy()

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Erreur','Erreur de saisie !')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Erreur','Password and confirm are not the same  !')
    else : 
        try:
            connex=pymysql.connect(host='localhost',user='root',password='123456')
            mycursor=connex.cursor()
        except:
            messagebox.showerror('Erreur','Database not connected ')
            return 
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null , email varchar(60), username varchar(20),password varchar(32))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            query='select * from data where username =%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone()
            
            if row != None :
                messagebox.showerror('Erreur','Username already taken')
            else :
                query='insert into data (email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
                connex.commit()
                connex.close()
                messagebox.showinfo('Success','Your account is registred ! Welcome ')
                clear()
                import login

    
    
   
signup_window=Tk()
signup_window.resizable(0,0)
signup_window.title('Signup')

Image=ImageTk.PhotoImage(file='Pic1.jpg')
ImageLabel=Label(signup_window,image=Image)
ImageLabel.pack()

heading=Label(signup_window,text='Sign Up',font=('Cambria',20,'bold'),fg='black',bg='whitesmoke')
heading.place(x=320,y=80)

#Email Entry
emailLabel=Label(signup_window,text='Email',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
emailLabel.place(x=250,y=170)
emailEntry=Entry(signup_window,width=15,font=('Cambria',20,'bold'))
emailEntry.place(x=250,y=190)
#email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#regex = re.compile(email_pattern)
#if regex.match(emailEntry.get()):
#   messagebox.showinfo('Good','Good Email')
#else :
#   messagebox.showerror('Error','Email incorrect')


#username entry
usernameLabel=Label(signup_window,text='Username',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
usernameLabel.place(x=250,y=270)
usernameEntry=Entry(signup_window,width=15,font=('Cambria',20,'bold'))
usernameEntry.place(x=250,y=290)

#password entry
passwordLabel=Label(signup_window,text='password',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
passwordLabel.place(x=250,y=370)
passwordEntry=Entry(signup_window,width=15,font=('Cambria',20,'bold'))
passwordEntry.place(x=250,y=390)

#confirm password 
confirmLabel=Label(signup_window,text='confirm password',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
confirmLabel.place(x=250,y=470)
confirmEntry=Entry(signup_window,width=15,font=('Cambria',20,'bold'))
confirmEntry.place(x=250,y=490)

#button create
buttoncreate=Button(signup_window,width=9,text='Sign up',bg='whitesmoke',cursor='hand2',command=connect_database)
buttoncreate.place(x=320,y=560)

























signup_window.mainloop()


