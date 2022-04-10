import hashlib
import re
from tkinter import *
from tkinter import messagebox
from turtle import color
R = Tk()
R.geometry("500x250")
R.configure(bg='#856ff8')
R.title('                                   LOGIN ')

password='SuperHardPassword99'
PASHASH1 = hashlib.md5(password.encode("utf-8")).hexdigest()
def fcomp():
    user=userenter.get()
    pas=passenter.get()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    PASHASH2 = hashlib.md5(pas.encode("utf-8")).hexdigest()
    if user == 'guest' and PASHASH2 == PASHASH1:
       Label(R, text=" Login Successfully ",fg='black',font=('helvetica-bold')).place(x=170,y= 170)
    elif regex.search(pas)!= None or regex.search(user)!= None:
         messagebox.showinfo("Message", " Don't nter special char ")
    elif user=="":
         messagebox.showwarning("Message"," You didn't enter username")
    elif pas=="":
        messagebox.showwarning("Message"," You didn't enter password")
    else : 
        messagebox.showerror("Message", " Wrong password or username ")
Label(R, text='Username',font=("helvetica", 11),bg='#856ff8').grid(row=0)
Label(R, text='Password',font=("helvetica", 11),bg='#856ff8').grid(row=1)
userenter = Entry(R) 
passenter = Entry(R)
userenter.grid(row=0, column=1)
passenter.grid(row=1, column=1)
passenter.config(show = '*')
button = Button(R, text='login',font=("helvetica", 12) ,width=10,command=fcomp).place(x=190,y= 100)
R.mainloop()
