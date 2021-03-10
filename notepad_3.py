# Author : Shobhit Mishra
# Here I have created a notepad with help of tkinter toolkit 

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

        # This function will add a new file in the notepad
        def newfile():
            self.win.title("Untitled Text-Notepad")
            self.file=None
            self.textarea.delete(1.0, END)

        # This function will allow as to a saved file from our system
        def openfile():
            try:
                self.file=askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text document", "*.txt")])
                self.textarea.delete(1.0, END)
                self.win.title(f"{os.path.basename(self.file)}-Notepad")
                f=open(self.file, "r")
                self.textarea.insert("end-1c", f.read())
            except:
                pass
        
        # This function will save the file and gives a name to the file
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
        # This function will add the changes in the notepad
        def savefile():
            if self.file==None:
                msg.showerror("Error", "The file has not been saved yet, first save as the file.")
            else:
                f=open(self.file, "w")
                f.write(self.textarea.get(1.0, END))
        
        # This function will teminate the GUI window
        def exit():
            self.win.destroy()

        # This function will perform the cut operation
        def cut():
            self.textarea.event_generate(("<<Cut>>"))
        
        # This function will perform the copy operation
        def copy():
            self.textarea.event_generate(("<<Copy>>"))
        
        # This function will perform the paste operation
        def paste():
            self.textarea.event_generate(("<<Paste>>"))
        
        # This function will perform the undo operation
        def undo():
            self.textarea.edit_undo()
        
        # This function will impliment the change in  the font which we have selected 
        def font_changed(font):
            self.textarea.config(font=f"{font}")
        
        # This will allow us to select a new font  
        def fontselector():
            self.win.tk.call('tk', 'fontchooser', 'configure', '-font','helvertica 10', '-command', self.win.register(font_changed))
            self.win.tk.call('tk', 'fontchooser', 'show')

        # This will give a message about the GUI
        def aboutapp():
            msg.showinfo("About the application","This is a simple notepad.")

        def func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu):# This function will create the title menu and the title of each sub_menu
            m=Menu(menubar, tearoff=0)
            for i in range(len(menu_lb)):
                m.add_command(label=menu_lb[i], command=menu_command[i])
            menubar.add_cascade(label=nameofsubmenu, menu=m)

        # Here we are using func_for_submenu to create the menues
        
        # File menu
        menu_lb=["New", "Open", "Save as.. ", "Save", "Exit"]
        menu_command=[newfile, openfile, saveasfile, savefile, exit]
        nameofsubmenu="File"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)
        # Edit menu
        menu_lb=["Cut", "Copy", "Paste", "Undo", "Font"]
        menu_command=[cut, copy, paste, undo, fontselector]
        nameofsubmenu="Edit"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)
        # About menu (which will give the intro to the notepad)
        menu_lb=["About application.."]
        menu_command=[aboutapp]
        nameofsubmenu="Help"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

    # Here I have created a text widget, where we will write the text. 
    def text(self):
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


# Here the notepad starts
if __name__=="__main__":
    a=Notepad(400,400)
    a.menu_creator()
    a.text()
    a.end()