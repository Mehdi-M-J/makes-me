from tkinter import *

get = Tk()

get.title('تمرین')
get.geometry('400x400+440+145')
get.config(bg='black')

login = Label(get , text='Login' , bg='#fff000').grid(row= 1 , column= 7)

user_name = Label(get , text='User_Name' , bg='#ff0000').grid(row= 3 , column= 6)
password = Label(get , text='Password' , bg='#ff0000').grid(row= 4 , column= 6)

input1 = Entry(get, width=28 , bg='#00ff00').grid(row= 3 , column= 7)
input2 = Entry(get, width=28 , bg='#00ff00').grid(row= 4 , column= 7)

login_btn = Button(get, text='Login' , bg='#fff000' , activebackground='#ff0000').grid(row= 7 , column= 7)

    
get.mainloop()