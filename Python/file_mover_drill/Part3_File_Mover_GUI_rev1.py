# Python v3.6.0:41df79263a11, Dec 23 2016
# Student: Freeman Cooley
# Python Course Item 65
# Sources:
#   http://effbot.org/tkinterbook/grid.htm
#   https://www.tutorialspoint.com/python/tk_button.htm
#   https://www.tutorialspoint.com/python/tk_text.htm
#   https://docs.python.org/3/library/os.html
#   https://docs.python.org/3/library/shutil.html
#   https://www.tutorialspoint.com/python/tk_messagebox.htm
#   https://www.tutorialspoint.com/python/tk_place.htm
#   http://tkinter.unpythonic.net/wiki/tkFileDialog
#   https://www.lynda.com/Tkinter-tutorials/Python-GUI-Development-Tkinter/163607-2.html
#       Section 8 GUI training
# Drill: File Mover part 3
#
# This program moves files that have been modified in the last 24 hours with source and destination based on user choice.
# A message box is displayed confirming file moved and destination location

# Importing necessary modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import _tkinter
import os
import time
import shutil


class File_Mover:

    # Definitions
    # Since these definitions are in the same file, they must use "self"
    def choose_Source(self):
        source = filedialog.askdirectory()
        self.source_var.set(source+'/')

    def choose_Dest(self):
        dest = filedialog.askdirectory()
        self.dest_var.set(dest+'/')

    def create_new_window(self):
        window = tk.Toplevel(root)

    # Moving Files. This is from drill part 2
    # Opening a messagebox to show file moved and location
    def moveFiles(self, source, dest):
        folder = os.listdir(source)
        for files in folder:
            old_timey = os.path.getmtime(source+files)
            time_check = time.time() - 86400
            if old_timey >= time_check:
                shutil.move(source+files, dest)
                # Confirmation to user. Using messagebox
                messagebox.showinfo(title = 'File Mover', message = (files + " ...Moved to location: " + os.path.abspath(dest+files)))


    # Building GUI
    def __init__(self, master):

        master.title('File Mover')
        master.resizable(False,False)
        master.configure(background = '#e1d8b9')

        # Setting UI background color & font
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', foreground = '#143849', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack(fill=BOTH)
        ttk.Label(self.frame_header,
                  text = ("Choose Source and Destination Folders. Only files that have been modified in the last 24 hours will be moved.")).pack(padx = 50, pady=50)


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(fill=BOTH)

        # Buttons for choosing folders and moving files
        ttk.Button(self.frame_content, text='Choose Source Folder',
        command= lambda: self.choose_Source()).grid(row=0, column=0, padx=10, pady=10, sticky = W)
        ttk.Button(self.frame_content, text='Choose Destination Folder',
        command= lambda: self.choose_Dest()).grid(row=2, column=0, padx=10, pady=10, sticky = W)
        ttk.Button(self.frame_content, text='Move the Files',
        command= lambda: self.moveFiles(self.source_var.get(),self.dest_var.get())).grid(row=5, column=0, padx=10, pady=20, sticky = W)

        # Entry line for Source Folder
        ttk.Label(self.frame_content, text="Source Folder:").grid(row=1, column=0, padx=10, pady=5, sticky = W)
        self.source_var = StringVar()
        self.start_source = ttk.Entry(self.frame_content, width=80, textvariable=self.source_var)
        self.start_source.grid(row=1, column=2, padx=10, pady=3)

        # Entry line for Destination Folder
        ttk.Label(self.frame_content, text="Destination Folder:").grid(row=3, column=0, padx=10, pady=3, sticky = W)
        self.dest_var = StringVar()
        self.end_dest = ttk.Entry(self.frame_content, width=80, textvariable=self.dest_var)
        self.end_dest.grid(row=3, column=2, padx=10, pady=3)


def main():
    root = Tk()
    filemover = File_Mover(root)
    root.mainloop()

if __name__ == "__main__": main()
