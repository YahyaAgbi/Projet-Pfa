from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox



#fonction Part 
   
def forget_pass():
    def change():
        if chusernameEntry.get()=='' or chpasswordEntry.get()=='' or chconfirmEntry.get()=='':
            messagebox.showerror('Error','Fill the Blanks !',parent=forget)
        elif chpasswordEntry.get()!=chconfirmEntry.get():
            messagebox.showerror('Error','Password unmatch !',parent=forget)
        else:
            conn=pymysql.connect(host='localhost',user='root',passwd='123456',database='userdata')
            mycursor=conn.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(chusernameEntry.get()))
            row=mycursor.fetchone()
            if row==None: 
                messagebox.showerror('Error','Username not found ! ',parent=forget)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(chpasswordEntry.get(),chusernameEntry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Password changed succesfully ! welcome again',parent=forget)
                forget.destroy()
                
                
            
                
            
            
    forget=Toplevel()
    forget.resizable(0,0)
    forget.title('Forget Password')
    forget.geometry('500x500')
   
   
    imagebg=ImageTk.PhotoImage(file='Pic5.jpg')    
    imagebgLabel=Label(forget,image=imagebg)
    imagebgLabel.pack()
    
    
    
    #username entry
    usernameLabel=Label(forget,text='Username',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
    usernameLabel.place(x=150,y=170)
    chusernameEntry=Entry(forget,width=15,font=('Cambria',20,'bold'))
    chusernameEntry.place(x=150,y=190)
    
    #password entry
    passwordLabel=Label(forget,text='password',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
    passwordLabel.place(x=150,y=270)
    chpasswordEntry=Entry(forget,width=15,font=('Cambria',20,'bold'))
    chpasswordEntry.place(x=150,y=290)
    
    #confirm password 
    confirmLabel=Label(forget,text='confirm password',font=('Cambria',10,'bold'),bg='whitesmoke',fg='black') 
    confirmLabel.place(x=150,y=370)
    chconfirmEntry=Entry(forget,width=15,font=('Cambria',20,'bold'))
    chconfirmEntry.place(x=150,y=390)
    
    #button changepass
    buttoncreate=Button(forget,width=20,height=3,text='change password',bg='whitesmoke',cursor='hand2',command=change)
    buttoncreate.place(x=230,y=490)
        
        
    forget.mainloop()
    
    
    
    
    
    
    
def signup():
    login_window.destroy()
    import signup   
def login():
    if usernameEntry=='' or passwordEntry=='':
     messagebox.showerror('Error','Fill the Blanks !') 
    else : 
        try :
            conn=pymysql.connect(host='localhost',user='root',passwd='123456')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error','Database not connected !')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row ==None:
            messagebox.showerror('Error','User not found ')
        else :
            messagebox.showinfo('Sucess','Welcome !')
            login_window.destroy()
            import bakcend
        

  
def user_enter(event): 
    if usernameEntry.get()=='Username':
       usernameEntry.delete(0,END)
    
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    ouveye.config(file='fer.png')
    passwordEntry.config(show='*')
    ouvbutton.config(command=show)

def show():
    ouveye.config(file='ouv.png')
    passwordEntry.config(show='')
    ouvbutton.config(command=hide)

def signup_page():
    login_window.destroy()
    import signup 


login_window=Tk()
login_window.resizable(0,0)
login_window.title('Login Page')

Image=ImageTk.PhotoImage(file="Pic5.jpg")
ImageLabel=Label(login_window,image=Image)
ImageLabel.pack()


heading=Label(login_window,text='LOGIN',font=('Cambria',20,'bold'),fg='Black',bg='Gold')
heading.place(x=200,y=30)

#userEntry

usernameEntry=Entry(login_window,width=15,font=('Cambria',20,'bold'))
usernameEntry.place(x=100,y=110)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

#passwordentry

passwordEntry=Entry(login_window,width=15,font=('Cambria',20,'bold'))
passwordEntry.place(x=100,y=160)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)


#buttonoeil

ouveye=PhotoImage(file='ouv.png')
ouvbutton=Button(login_window,image=ouveye,bd=0,bg='White',activebackground='White',cursor='hand2',command=hide)
ouvbutton.place(x=310,y=165)

#forgetpassword

forgetbutton=Button(login_window,text='did you forget password ?',bd=0,bg='Gold',fg='Black',activebackground='yellow',cursor='hand2',font=('Cambria',8,'bold'),command=forget_pass)
forgetbutton.place(x=120,y=200)

#Login button 

loginButton=Button(login_window,text='Login',bg='Gold', fg='Black',font=('Cambria',15,'bold'),bd=0,cursor='hand2',height=2,width=15,activebackground='Black',command=login)
loginButton.place(x=120,y=250)


#create new account
newLabel=Label(login_window,text='Do you have an account ?',bg='gold',fg='Black',font=('Cambria',8,'bold'))
newLabel.place(x=160,y=400)
newbutton=Button(login_window,text='Create new account',font=('Cambria',15,'bold'),bg='Gold',activebackground='Gold',cursor='hand2',command=signup)
newbutton.place(x=130,y=425)
 


login_window.mainloop()
