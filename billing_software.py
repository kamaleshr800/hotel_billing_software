import tkinter as tk
from tkinter import *
import time
import os
import tempfile


class billingsoftware:
    def __init__(self,root):
        self.root=root
        self.root.geometry('900x600+200+60')
        title=Label(self.root,text='Billing Software',font=('times new rommon',30,'bold'
            ),bg='#8A2BE2',fg='white',bd=5,relief=RAISED)
        title.pack(side=TOP,fill=X)

        end=Label(self.root,text='Made by kamalesh',font=('times new rommon',30,'bold'
            ),bg='#8A2BE2',fg='white',bd=5,relief=RAISED)
        end.pack(side=BOTTOM,fill=X)
#=========variable declaration=============
        self.n_idly=IntVar()
        self.n_pongal=IntVar()
        self.n_vadai=IntVar()
        self.n_poori=IntVar()
        self.n_dosa=IntVar()

        self.Total=IntVar()
        self.Quantity=IntVar()
  

        self.c_idly=IntVar()
        self.c_pongal=IntVar()
        self.c_vadai=IntVar()
        self.c_poori=IntVar()
        self.c_dosa=IntVar()

        self.c_idly.set(10)
        self.c_pongal.set(30)
        self.c_vadai.set(10)
        self.c_poori.set(20)
        self.c_dosa.set(40)


#   =============product area===========
        F1=Frame(root,bd=5,relief=RIDGE,bg='#8A2BE2')
        F1.place(relx=.02,rely=.11,relwidth=.5,relheight=.68)

        itm=Label(F1, text='Items', font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        itm.grid(row=0,column=0,padx=20,pady=15)

        n=Label(F1, text='Number of\n Items', font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        n.grid(row=0,column=1,padx=30,pady=15)

        cost=Label(F1, text='Cost of\n Items', font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        cost.grid(row=0,column=2,padx=30,pady=15)
#=========items==============
        lbl1=Label(F1,text='Idly',font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        lbl1.grid(row=1,column=0,padx=20,pady=15)
        et1=Entry(F1,font=('Helvetic',10, 'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.n_idly,justify=CENTER)
        et1.grid(row=1,column=1,padx=20,pady=15)
        ct1=Entry(F1,font=('Helvetic', 10,'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.c_idly,justify=CENTER)
        ct1.grid(row=1,column=2,padx=20,pady=15)

        lbl2=Label(F1,text='Pongal',font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        lbl2.grid(row=2,column=0,padx=20,pady=15)
        et2=Entry(F1,font=('Helvetic',10, 'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.n_pongal,justify=CENTER)
        et2.grid(row=2,column=1,padx=20,pady=15)
        ct2=Entry(F1,font=('Helvetic', 10,'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.c_pongal,justify=CENTER)
        ct2.grid(row=2,column=2,padx=20,pady=15)
    
        lbl3=Label(F1,text='Poori',font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        lbl3.grid(row=3,column=0,padx=20,pady=15)
        et3=Entry(F1,font=('Helvetic',10, 'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.n_poori,justify=CENTER)
        et3.grid(row=3,column=1,padx=20,pady=15)
        ct3=Entry(F1,font=('Helvetic', 10,'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.c_poori,justify=CENTER)
        ct3.grid(row=3,column=2,padx=20,pady=15)
  
        lbl4=Label(F1,text='Vadai',font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        lbl4.grid(row=4,column=0,padx=20,pady=15)
        et4=Entry(F1,font=('Helvetic',10, 'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.n_vadai,justify=CENTER)
        et4.grid(row=4,column=1,padx=20,pady=15)
        ct4=Entry(F1,font=('Helvetic', 10,'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.c_vadai,justify=CENTER)
        ct4.grid(row=4,column=2,padx=20,pady=15)
  
        lbl=Label(F1,text='Dosai',font=('Helvetic',15, 'bold'), fg='white',bg='#8A2BE2')
        lbl.grid(row=5,column=0,padx=20,pady=15)
        et5=Entry(F1,font=('Helvetic',10, 'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.n_dosa,justify=CENTER)
        et5.grid(row=5,column=1,padx=20,pady=15)
        ct5=Entry(F1,font=('Helvetic', 10,'bold'), fg='black',bg='white',width=15,bd=3,textvariable=self.c_dosa,justify=CENTER)
        ct5.grid(row=5,column=2,padx=20,pady=15)
  

#   =========textarea==============
        F2=Frame(root,bd=3,relief=RIDGE,bg='#8A2BE2')
        F2.place(relx=.54,rely=.11,relwidth=.44,relheight=.68)


        bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=4,relief=RAISED,fg='white',bg='#8A2BE2')
        bill_title.pack(fill=X)
        scrol_y=Scrollbar(F2,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)
        self.textarea=Text(F2,font='arial 15 bold',yscrollcommand=scrol_y.set)
        self.textarea.pack(fill=BOTH)
        scrol_y.config(command=self.textarea.yview)


 
#===========button frame============

        F3=Frame(root,bd=5,background='white')
        F3.place(relx=.02,rely=.8,relwidth=.96,relheight=.1)


        btn1=Button(F3,text='Generate Bill',font='arial 15',command=self.receipt,fg='white',bg='#FF9912',cursor='hand2')
        btn1.place(relx=0.0,rely=.08,relwidth=.24,relheight=.9)

        btn1=Button(F3,text='Print',font='arial 15',fg='white',command=self.print,bg='#FF9912',cursor='hand2')
        btn1.place(relx=0.25,rely=.08,relwidth=.24,relheight=.9)

        btn1=Button(F3,text='Clear',font='arial 15',fg='white',command=self.reset,bg='#FF9912',cursor='hand2')
        btn1.place(relx=0.5,rely=.08,relwidth=.24,relheight=.9)

        btn1=Button(F3,text='Exit',font='arial 15',fg='white',command=self.exit,bg='#FF9912',cursor='hand2')
        btn1.place(relx=0.75,rely=.08,relwidth=.24,relheight=.9)

        self.text1()

    def receipt(self): 
        self.textarea.delete(1.0,END)   
        self.text1()  
        self.textarea.insert(END,f'\n Items\t   Quantity\t\t  Cost\n')
        if self.n_idly.get()!=0:
            self.textarea.insert(END,f'\nIdly\t\t{self.n_idly.get()}\t  {self.c_idly.get()}$')


        if self.n_dosa.get()!=0:
            self.textarea.insert(END,f'\nDosa\t\t{self.n_dosa.get()}\t  {self.c_dosa.get()}$')


        if self.n_pongal.get()!=0:
            self.textarea.insert(END,f'\nPongal\t\t{self.n_pongal.get()}\t  {self.c_pongal.get()}$')

        if self.n_poori.get()!=0:
            self.textarea.insert(END,f'\nPoori\t\t{self.n_poori.get()}\t  {self.c_poori.get()}$')  

        if self.n_vadai.get()!=0:
            self.textarea.insert(END,f'\nVadai\t\t{self.n_vadai.get()}\t  {self.c_vadai.get()}$') 

        self.total()

        self.textarea.insert(END,'\n=============================\n')
        self.textarea.insert(END,f'\nTotal\t\t{self.Quantity.get()}\t  {self.Total.get()}$')     




    def total(self):
        self.Total.set((self.n_idly.get()*self.c_idly.get()+self.n_dosa.get()*self.c_dosa.get()+self.n_pongal.get()
               *self.c_pongal.get()+self.n_poori.get()*self.c_poori.get()+self.n_vadai.get()*self.c_vadai.get()))
        
        self.Quantity.set(self.n_idly.get()+self.n_dosa.get()+self.n_pongal.get()+self.n_poori.get()+self.n_vadai.get())



    def reset(self):
        self.textarea.delete(1.0,END)
        self.text1()
        
        self.n_idly.set(0)
        self.n_pongal.set(0)
        self.n_vadai.set(0)
        self.n_poori.set(0)
        self.n_dosa.set(0)

        self.c_idly.set(10)
        self.c_pongal.set(30)
        self.c_vadai.set(10)
        self.c_poori.set(20)
        self.c_dosa.set(40)

    def text1(self):
        self.textarea.delete(1.0,END)   
        self.textarea.insert(END,f'=======Morning food stall========\n\nTime : {time.ctime()}\n')
        self.textarea.insert(END,'\n=============================\n')

    def exit(self):
        root.destroy()

    def print(self):
        q=self.textarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'Print')



root=Tk()
ob=billingsoftware(root)
root.mainloop()