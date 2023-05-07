from tkinter import *
from PIL import ImageTk
import tkinter.ttk as ttk
import tkinter as tk
import pymysql
import io 


# Define search function
def search():
    search_results = tk.Toplevel(backend)
    search_results.geometry("500x300")
    search_results.title('results')

    tree1 = ttk.Treeview(search_results, columns=('Nom', 'Image', 'Description', 'Prix', 'Qte', 'Seuil', 'dateEntree', 'dateSortie'))
    tree1.heading("#0", text="Id")
    tree1.heading("Nom", text="Nom")
    tree1.heading("Image", text="Image")
    tree1.heading("Description", text="Description")
    tree1.heading("Prix", text="Prix Unitaire")
    tree1.heading("Qte", text="Qantite")
    tree1.heading("Seuil", text="Seuil")
    tree1.heading("dateEntree", text="Date d'entree")
    tree1.heading("dateSortie", text="Date de Sortie")

    xscrollbar = ttk.Scrollbar(search_results, orient="horizontal", command=tree1.xview)
    tree1.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")

    db = pymysql.connect(host="localhost", user="root", password="123456", database="sneakers")
    mycursor = db.cursor()

    search_query = searchEntry.get()

    # Name:
    tree1.delete(*tree1.get_children())
    query = f"SELECT * FROM product WHERE Nom LIKE '%{search_query}%'"
    mycursor.execute(query)
    result1 = mycursor.fetchall()

    for row in result1:
        tree1.insert("", "end", text=row[0], values=row[1:])

    # Prix:
    if search_query.isdigit():
        query = f"SELECT * FROM product WHERE Prix={search_query}"
    else:
        query = f"SELECT * FROM product WHERE Prix='{search_query}'"
    mycursor.execute(query)
    result2 = mycursor.fetchall()

    for row in result2:
        tree1.insert("", "end", text=row[0], values=row[1:])

    # Qte:
    if search_query.isdigit():
        query = f"SELECT * FROM product WHERE Qte={search_query}"
    else:
        query = f"SELECT * FROM product WHERE Qte='{search_query}'"
    mycursor.execute(query)
    result3 = mycursor.fetchall()

    for row in result3:
        tree1.insert("", "end", text=row[0], values=row[1:])

    tree1.pack()
    tree1.configure(height=20)
    

    search_results.mainloop()
    

def search_Entry(event):
    if searchEntry.get()=="Search preference":
         searchEntry.delete(0,END)


def NF():
    
   NF = tk.Toplevel()
   NF.geometry("700x400")
   NF.title('North Face')
   
   style = ttk.Style()
   style.configure("Treeview", background="#8B8B83", fieldbackground="green")

   
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
   
   
   query ="SELECT * FROM product where Nom ='North Face'"
   mycursor.execute(query)
   rows = mycursor.fetchall()
   
   for row in rows:
      tree.insert("",END, text=row[0], values=row[1:])
      
   tree.pack()
   tree.config(height=20)
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
   query = "SELECT * FROM product where Nom ='puma'"
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
   tree1=ttk.Treeview(Adidas,columns=('Nom','Image','Description','Prix_Unitaire','Qte','Seuil','dateEntree','dateSortie'))
   tree1.heading("#0",text="ID")
   tree1.heading("Nom",text="Nom")
   tree1.heading("Image",text="Image") 
   tree1.heading("Description",text="Description")
   tree1.heading("Prix_Unitaire",text="Prix Unitaire")
   tree1.heading("Qte",text="Qantite")
   tree1.heading("Seuil",text="Sueil")
   tree1.heading("dateEntree",text="Date d'entree")
   tree1.heading("dateSortie",text="Date de Sortie")
   xscrollbar = ttk.Scrollbar(Adidas, orient="horizontal", command=tree1.xview)
   tree1.configure(xscrollcommand=xscrollbar.set)
   xscrollbar.pack(side="bottom",fill="x")
   
   conn = pymysql.connect(host='localhost',user='root',password='123456',database='Sneakers')
   mycursor = conn.cursor()
   query = "SELECT * from product where Nom='adidas'"
   mycursor.execute(query)
   rows = mycursor.fetchall()
   for row in rows:
    tree1.insert("",'end', text=row[0], values=row[1:])
    tree1.pack()
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
  query = "SELECT * FROM product where Nom='Nike'"
  mycursor.execute(query)
  rows = mycursor.fetchall()
  for row in rows:
    tree.insert("", END, text=row[0], values=row[1:])

  tree.pack()
  tree.configure(height=20)
  

  nike.mainloop()

backend=Tk()
backend.resizable(0,0)
backend.title('Store Info')

imagebg=ImageTk.PhotoImage(file='Pic3.jpg')    
imagebgLabel=Label(backend,image=imagebg)
imagebgLabel.pack()





#search info 
searchEntry=tk.Entry(backend,font=('Cambria',26,'bold'))
searchEntry.place(x=105,y=80)
searchEntry.insert(0,'Search preference')
searchEntry.bind('<FocusIn>',search_Entry)
#search button
searchButton=tk.Button(backend,text='Search',bd=0,bg='#8B8B83',fg='Black',activebackground='yellow',cursor='hand2',font=('Cambria',18,'bold'),command=search)
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
