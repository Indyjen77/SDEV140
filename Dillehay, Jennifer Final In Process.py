from tkinter import *
from tkinter import filedialog

#from PIL import ImageTk, Image

root = Tk()
root.title("Jennifer Dillehay")
root.iconbitmap(r"C:\Users\jp462\OneDrive\Desktop\IVYTECH\PYTHON\M06\sticky_notes_icon_259264.ico")



def open():
    top = Toplevel()
    top.title("Open DHR")
    root.iconbitmap(r"C:\Users\jp462\OneDrive\Desktop\IVYTECH\PYTHON\M06\sticky_notes_icon_259264.ico")
    root.filename = filedialog.askopenfilename(initialdir="enter link here", title="Select A File", filetypes=(("png files","*.png"),("all files","*.*")))
    btn2 = Button(top, text="close window", command=top.destroy).pack()
    

btn = Button(root, text="Open new DHR" , command=open).pack()





mainloop()
