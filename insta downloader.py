from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import instaloader
import threading
import os


root = Tk()
root.title('Download From Instagram')
root.geometry('520x480')
root.resizable(0,0)
root.config(bg='#121212')


def downloadpost():
    link = postlink_Entry.get()

    def download():
        if 'https://www.instagram.com/p/' in link:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                URL = link.replace('https://www.instagram.com/p/', '')
                URL = URL.replace('/','')
                L = instaloader.instaloader()
                post = instaloader.post.from_shortcode(L.context, URL)
                L.download_post(post, target=URL)
                messagebox.showinfo('اطلاع رسانی', '!دانلود موفقیت آمیز بود')
            except:
                messagebox.showerror('خطا', '!لینک شناسایی نشد')
        elif 'https://www.instagram.com/reel/' in link:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                URL = link.replace('https://www.instagram.com/reel/', '')
                URL = URL.replace('/','')
                L = instaloader.instaloader()
                post = instaloader.post.from_shortcode(L.context, URL)
                L.download_post(post, target=URL)
                messagebox.showinfo('اطلاع رسانی', '!دانلود موفقیت آمیز بود')
            except:
                messagebox.showerror('خطا', '!لینک شناسایی نشد')
        else:
            messagebox.showerror('خطا', '!لینک پیدا نشد')

    threading.Thread(target=download).start()



postlink_label = Label(root, text='Post URL', bg='#121212', fg='yellow', font=('arial', 14))
postlink_Entry = Entry(root, width=64)


downloadpost_btn = Button(root, text='Post URL', bg='#121212', fg='yellow', borderwidth=3, font=('arial', 14), width=32, command=downloadpost)
exit_btn = Button(root, text='Exit app', bg='#008000', fg='yellow', borderwidth=3, font=('arial', 14), width=32, command=root.destroy)

# Text_to_link = Button(root, text='send message to creator in telegram', bg='#ff0000',command=messagebox.showinfo('111111'))

postlink_label.grid(row=0, column=0, padx=12, pady=12)
postlink_Entry.grid(row=0, column=1)

downloadpost_btn.place(relx=0.5, rely=0.4, anchor='c')
exit_btn.place(relx=0.5, rely=0.6, anchor='c')

# Text_to_link.place(relx=0.2, rely=0.2, anchor='c')

root.mainloop()
