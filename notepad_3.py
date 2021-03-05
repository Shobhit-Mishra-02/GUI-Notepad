from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class Notepad():
    def __init__(self, width, height):#creating the window
        self.win=Tk()
        self.win.geometry(f"{width}x{height}")
        self.file=None
        self.textarea=Text(self.win, wrap="none", undo=True)
        self.win.title("Untitled-Notepad")
        self.win.wm_iconbitmap("3.ico")
    
    def menu_creator(self):#creating the menubar
        menubar=Menu(self.win)
        self.win.config(menu=menubar)

        def newfile():
            self.win.title("Untitled Text-Notepad")
            self.file=None
            self.textarea.delete(1.0, END)

        def openfile():
            try:
                
                self.file=askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text document", "*.txt")])
                self.textarea.delete(1.0, END)
                self.win.title(f"{os.path.basename(self.file)}-Notepad")
                f=open(self.file, "r")
                self.textarea.insert("end-1c", f.read())
            except:
                pass

        def saveasfile():
            if self.file!=None:
                msg.showerror("Error", "The file has been saved.")
            elif self.file==None:
                try:
                    self.file=asksaveasfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text document", "*.txt")])
                    f=open(self.file, "w")
                    f.write(self.textarea.get(1.0, END))
                    self.win.title(f"{os.path.basename(self.file)}-Notepad")
                except:
                    pass

        def savefile():
            if self.file==None:
                msg.showerror("Error", "The file has not been saved yet, first save as the file.")
            else:
                f=open(self.file, "w")
                f.write(self.textarea.get(1.0, END))

        def exit():
            self.win.destroy()

        def cut():
            self.textarea.event_generate(("<<Cut>>"))
        def copy():
            self.textarea.event_generate(("<<Copy>>"))
        def paste():
            self.textarea.event_generate(("<<Paste>>"))
        def undo():
            self.textarea.edit_undo()
        
        def font_changed(font):
            self.textarea.config(font=f"{font}")
            
        def fontselector():
            self.win.tk.call('tk', 'fontchooser', 'configure', '-font','helvertica 10', '-command', self.win.register(font_changed))
            self.win.tk.call('tk', 'fontchooser', 'show')

        def aboutapp():
            msg.showinfo("About the application","This is a simple notepad.")

        def func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu):
            m=Menu(menubar, tearoff=0)
            for i in range(len(menu_lb)):
                m.add_command(label=menu_lb[i], command=menu_command[i])
            menubar.add_cascade(label=nameofsubmenu, menu=m)

        menu_lb=["New", "Open", "Save as.. ", "Save", "Exit"]
        menu_command=[newfile, openfile, saveasfile, savefile, exit]
        nameofsubmenu="File"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        menu_lb=["Cut", "Copy", "Paste", "Undo", "Font"]
        menu_command=[cut, copy, paste, undo, fontselector]
        nameofsubmenu="Edit"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        menu_lb=["About application.."]
        menu_command=[aboutapp]
        nameofsubmenu="Help"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

    def text(self):#creating the text widget
        scroll_V=Scrollbar(self.win)
        scroll_V.grid(row=0, column=1, sticky="ns")
        scroll_V.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=scroll_V.set)

        scroll_H=Scrollbar(self.win, orient=HORIZONTAL)
        scroll_H.grid(row=1, column=0, sticky="we")
        scroll_H.config(command=self.textarea.xview)
        self.textarea.config(xscrollcommand=scroll_H.set)

        self.textarea.grid(row=0, column=0, sticky="news")

        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(0, weight=1)
        
        self.textarea.columnconfigure(0, weight=1)
        self.textarea.columnconfigure(0, weight=1)
 
    def end(self):#ending of the loop
        self.win.mainloop()



if __name__=="__main__":
    a=Notepad(400,400)
    a.menu_creator()
    a.text()
    a.end()
