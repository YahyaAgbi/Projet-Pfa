from tkinter import*
from PIL import ImageTk
import tkinter.ttk as ttk
import tkinter as tk
import pymysql
from tkinter import messagebox

backend=Tk()
# Connect to MySQL database
db = pymysql.connect(host="localhost", user="root", password="123456", database="sneakers")
cursor = db.cursor()

# Define search function
def search():
    search_results=tk.Toplevel(backend)
    search_results.title('results')
    search_results.geometry("500x300")
    
    
    tree1=ttk.Treeview(search_results,columns=('Nom','Image','Description','Prix','Qte','Seuil','dateEntree','dateSortie'))
    tree1.heading("#0",text="Id")
    tree1.heading("Nom",text="Nom")
    tree1.heading("Image",text="Image")
    tree1.heading("Description",text="Description")
    tree1.heading("Prix",text="Prix Unitaire")
    tree1.heading("Qte",text="Qantite")
    tree1.heading("Seuil",text="Sueil")
    tree1.heading("dateEntree",text="Date d'entree")
    tree1.heading("dateSortie",text="Date de Sortie")
    
    xscrollbar = ttk.Scrollbar(search_results, orient="horizontal", command=tree1.xview)
    tree1.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom",fill="x")
    
    tree1.pack()
   
   
   
   
   
    # Get user input
    search_query = searchEntry.get()

    # Execute the first query
    query = f"SELECT * FROM adidas WHERE Nom LIKE '%{search_query}%'"
    cursor.execute(query)
    results1 = cursor.fetchall()
    
    
    # Execute the second query
    query = f"SELECT * FROM northface WHERE Nom LIKE '%{search_query}%'"
    cursor.execute(query)
    results2 = cursor.fetchall()

    query = f"SELECT * FROM Nike WHERE Nom LIKE '%{search_query}%'"
    cursor.execute(query)
    results3 = cursor.fetchall()
    
    query = f"SELECT * FROM Puma WHERE Nom LIKE '%{search_query}%'"
    cursor.execute(query)
    results4= cursor.fetchall()
    
    
    query = f"SELECT * FROM adidas WHERE prix_unitaire = '{search_query}'"
    cursor.execute(query)
    results5 = cursor.fetchall()
    
    query = f"SELECT * FROM northface WHERE prix_unitaire ='{search_query}'"
    cursor.execute(query)
    results6 = cursor.fetchall()

    query = f"SELECT * FROM Nike WHERE prix_unitaire = '{search_query}'"
    cursor.execute(query)
    results7 = cursor.fetchall()
    query = f"SELECT * FROM Puma WHERE prix_unitaire = '{search_query}'"
    cursor.execute(query)
    results8 = cursor.fetchall()
    
    query = f"SELECT * FROM adidas WHERE Qte = '{search_query}'"
    cursor.execute(query)
    results9 = cursor.fetchall()
    
    query = f"SELECT * FROM northface WHERE Qte ='{search_query}'"
    cursor.execute(query)
    results10 = cursor.fetchall()

    query = f"SELECT * FROM Nike WHERE Qte = '{search_query}'"
    cursor.execute(query)
    results11 = cursor.fetchall()
    query = f"SELECT * FROM Puma WHERE Qte = '{search_query}'"
    cursor.execute(query)
    results12 = cursor.fetchall()
    # Clear the existing rows in the table
    for row in tree1.get_children():
        tree1.delete(row)

# Display the results from the first query in the table
    for row in results1:
       tree1.insert("", "end",text=row[0],values=row[1:9])

# Display the results from the second query in the table

    for row in results2:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results3:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results4:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results5:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results6:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results7:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results8:
        tree1.insert("", "end",text=row[0],values=row[1:9])    
    for row in results9:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results10:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results11:
        tree1.insert("", "end",text=row[0],values=row[1:9])
    for row in results12:
        tree1.insert("", "end",text=row[0],values=row[1:9])  
    search_results.mainloop()     







def search_Entry(event):
     if searchEntry.get()=='Search preference : ':
       searchEntry.delete(0,END)
def NF():
   NF = tk.Toplevel()
   NF.geometry("700x400")
   NF.title('North Face')
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="green")
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="#8B8B83")
# Set the headings of the columns
   tree=ttk.Treeview(NF,columns=('Nom','Image','Description','Prix','Qte','Seuil','dateEntree','dateSortie'))
   tree.heading("#0",text="ID")
   tree.heading("Nom",text="Nom")
   tree.heading("Image",text="Image")
   tree.heading("Description",text="Description")
   tree.heading("Prix",text="Prix Unitaire")
   tree.heading("Qte",text="Qantite")
   tree.heading("Seuil",text="Sueil")
   tree.heading("dateEntree",text="Date d'entree")
   tree.heading("dateSortie",text="Date de Sortie")
   xscrollbar = ttk.Scrollbar(NF, orient="horizontal", command=tree.xview)
   tree.configure(xscrollcommand=xscrollbar.set)
   xscrollbar.pack(side="bottom",fill="x")
   
   conn = pymysql.connect(host='localhost',user='root',password='123456',database='Sneakers')
   mycursor = conn.cursor()
   query = 'SELECT * FROM northface'
   mycursor.execute(query)
   rows = mycursor.fetchall()
   for row in rows:
    tree.insert("", END, text=row[0], values=row[1:])
    tree.pack()
   NF.mainloop()            

def Puma():
   Puma = tk.Toplevel()
   Puma.geometry("700x400")
   Puma.title('Puma')
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="green")
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="#8B8B83")
# Set the headings of the columns
   tree=ttk.Treeview(Puma,columns=('Nom','Description','Image','Prix','Qte','Seuil','dateEntree','dateSortie'))
   tree.heading("Nom",text="Nom")
   tree.heading("Description",text="Description")
   tree.heading("Image",text="Image")
   tree.heading("Prix",text="Prix Unitaire")
   tree.heading("Qte",text="Qantite")
   tree.heading("Seuil",text="Sueil")
   tree.heading("dateEntree",text="Date d'entree")
   tree.heading("dateSortie",text="Date de Sortie")
   xscrollbar = ttk.Scrollbar(Puma, orient="horizontal", command=tree.xview)
   tree.configure(xscrollcommand=xscrollbar.set)
   xscrollbar.pack(side="bottom",fill="x")

# Add some items to the Treeview
   
   
   
   conn = pymysql.connect(host='localhost',user='root',password='123456',database='Sneakers')
   mycursor = conn.cursor()
   query = 'SELECT * FROM puma'
   mycursor.execute(query)
   rows = mycursor.fetchall()
   for row in rows:
     tree.insert("", END, text=row[0], values=row[1:])

   tree.pack()
  

   Puma.mainloop()     

def Adidas():
   Adidas = tk.Toplevel()
   Adidas.geometry("700x400")
   Adidas.title('ADIDAS')
   style = ttk.Style()
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="#8B8B83")
#Set the headings of the columns
   tree=ttk.Treeview(Adidas,columns=('Nom','Image','Description','Prix_Unitaire','Qte','Seuil','dateEntree','dateSortie'))
   tree.heading("#0",text="ID")
   tree.heading("Nom",text="Nom")
   tree.heading("Image",text="Image") 
   tree.heading("Description",text="Description")
   tree.heading("Prix_Unitaire",text="Prix Unitaire")
   tree.heading("Qte",text="Qantite")
   tree.heading("Seuil",text="Sueil")
   tree.heading("dateEntree",text="Date d'entree")
   tree.heading("dateSortie",text="Date de Sortie")
   xscrollbar = ttk.Scrollbar(Adidas, orient="horizontal", command=tree.xview)
   tree.configure(xscrollcommand=xscrollbar.set)
   xscrollbar.pack(side="bottom",fill="x")
   
   conn = pymysql.connect(host='localhost',user='root',password='123456',database='Sneakers')
   mycursor = conn.cursor()
   query = 'SELECT * FROM adidas'
   mycursor.execute(query)
   rows = mycursor.fetchall()
   for row in rows:
    tree.insert("",'end', text=row[0], values=row[1:])
    tree.pack()
   Adidas.mainloop()     
       
def nike():
  
  # Create a Tkinter window
  nike = tk.Toplevel()
  nike.geometry("700x400")
  nike.title('NIKE')

# Define the columns of the Treeview
  style = ttk.Style()
  style.configure("Treeview", background="#8B8B83", fieldbackground="#8B8B83")
# Set the headings of the columns
  tree=ttk.Treeview(nike,columns=('Nom','Description','Image','Prix','Qte','Seuil','dateEntree','dateSortie'))
  tree.heading("#0",text="ID")
  tree.heading("Nom",text="Nom")
  tree.heading("Description",text="Description")
  tree.heading("Image",text="Image")
  tree.heading("Prix",text="Prix Unitaire")
  tree.heading("Qte",text="Qantite")
  tree.heading("Seuil",text="Sueil")
  tree.heading("dateEntree",text="Date d'entree")
  tree.heading("dateSortie",text="Date de Sortie")
  xscrollbar = ttk.Scrollbar(nike, orient="horizontal", command=tree.xview)
  tree.configure(xscrollcommand=xscrollbar.set)
  xscrollbar.pack(side="bottom",fill="x")

# Add some items to the Treeview
  conn = pymysql.connect(host='localhost',user='root',password='123456',database='Sneakers')
  mycursor = conn.cursor()
  query = 'SELECT * FROM nike'
  mycursor.execute(query)
  rows = mycursor.fetchall()
  for row in rows:
    tree.insert("", END, text=row[0], values=row[1:])

  tree.pack()
  

  nike.mainloop()



imagebg=ImageTk.PhotoImage(file='Pic3.jpg')    
imagebgLabel=Label(backend,image=imagebg)
imagebgLabel.pack()
backend.resizable(0,0)
backend.title('Store Info')



#search info 
searchEntry=Entry(backend,width='20',font=('Cambria',20,'bold'))
searchEntry.insert(0,'Search preference : ')
searchEntry.place(x=120,y=80)
searchEntry.bind('<FocusIn>',search_Entry)
#search button
searchButton=Button(backend,text='Search',bd=0,bg='#8B8B83',fg='Black',activebackground='yellow',cursor='hand2',font=('Cambria',16,'bold'),command=search)
searchButton.place(x=450,y=80)

#search images 1 = NIKE 
Image1=ImageTk.PhotoImage(file='NikeLogo.png')
NikeButton=Button(backend,image=Image1,bd=0,bg='#988C89',width=300,activebackground='#988C89',command=nike,cursor='hand2')
NikeButton.place(x=40,y=200)
Nikelabel=Label(backend,text='NIKE ORIGINAL',height=4,width=25)
Nikelabel.place(x=355,y=200)

#search images 2 = ADIDAS
Image=ImageTk.PhotoImage(file='AdidasLogo.png')
AdidasButton=Button(backend,image=Image,bd=0,bg='#988C89',width=300,activebackground='#988C89',command=Adidas,cursor='hand2')
AdidasButton.place(x=40,y=320)
Adidaslabel=Label(backend,text='ADIDAS ORIGINAL',height=4,width=25)
Adidaslabel.place(x=355,y=320)

#search images 3 = PUMA
Image2=ImageTk.PhotoImage(file='PumaLogo.png')
PumaButton=Button(backend,image=Image2,bd=0,bg='#988C89',width=300,activebackground='#988C89',command=Puma,cursor='hand2')
PumaButton.place(x=40,y=420)
Pumalabel=Label(backend,text='PUMA ORIGINAL',height=4,width=25)
Pumalabel.place(x=355,y=420)

#search images 2 = NorthFace
Image3=ImageTk.PhotoImage(file='NorthFaceLogo.png')
NFButton=Button(backend,image=Image3,bd=0,bg='#988C89',width=300,activebackground='#988C89',command=NF,cursor='hand2')
NFButton.place(x=40,y=520)
NFlabel=Label(backend,text='THE NORTH FACE',height=4,width=25)
NFlabel.place(x=355,y=520)

















backend.mainloop()