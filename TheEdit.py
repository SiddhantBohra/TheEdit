from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkinter.scrolledtext as tkst
import tkinter


filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
 
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
 
def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oh No!", message="Unable to save file...")
 
root = Tk()
root.option_add("*background", "BLACK")
       
def openFile():
    global filename
    file = askopenfile(parent=root,title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()

def cut():
    root.clipboard_clear()
    text.clipboard_append(string = text.selection_get())
    text.delete(index1 = SEL_FIRST,index2 = SEL_LAST)

def copy():
    root.clipboard_clear()
    text.clipboard_append(string = text.selection_get())

def paste():
    text.insert(INSERT , root.clipboard_get())

def delete():
    text.delete(index1 = SEL_FIRST,index2 = SEL_LAST)
    
def select_all():
    text.tag_add('sel', '1.0', 'end')
        
root.title("TheEdit")
root.resizable(True,True) 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, width=400, height=400, font=("Times New Roman" , 14) , fg = 'yellow',yscrollcommand=scrollbar.set )
text.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=text.yview)

text.config(insertbackground='white')
 
text.pack()

	
 
menubar = Menu(root, background='#374140', foreground='white',
activebackground='#374140', activeforeground='white')
filemenu = Menu(menubar,background='#374140', foreground='white',
activebackground='#374140', activeforeground='white')
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar,background='#374140', foreground='white',
activebackground='#374140', activeforeground='white')
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Delete", command=delete)
editmenu.add_command(label="Select All", command=select_all)


	
root.config(menu=menubar)

root.mainloop()
