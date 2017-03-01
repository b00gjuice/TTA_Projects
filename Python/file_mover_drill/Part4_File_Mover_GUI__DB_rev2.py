# Python v3.6.0:41df79263a11, Dec 23 2016
# Student: Freeman Cooley
# Python Course Item 66
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
# Drill: File Mover part 4
#
# File Mover Progrom with GUI and database
# A message box is displayed confirming file moved and destination location
# The time of the last file transfer is shown in GUI

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
import datetime
import sqlite3

# Creating a database for file time check
with sqlite3.connect('file_mover.db') as connection:

    c = connection.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Date_Time(check_time DATE)")


class File_Mover:

    # Definitions
    # Since these definitions are in the same file, they must use "self"
    def choose_Source(self):
        source = filedialog.askdirectory()
        self.source_var.set(source+'/')

    def choose_Dest(self):
        dest = filedialog.askdirectory()
        self.dest_var.set(dest+'/')

    # Moving Files. This is modified from drill part 2
    # Opening a messagebox to show file moved and location
    # Recording the time of the last file transfer
    def moveFiles(self, source, dest):
        folder = os.listdir(source)
        for files in folder:
            old_timey = os.path.getmtime(source+files)
            check = time.time() - 86400
            if old_timey >= check:
                shutil.move(source+files, dest)
                # Confirmation to user. Using messagebox
                messagebox.showinfo(title = 'File Mover', message = (files + " ...Moved to location: " + os.path.abspath(dest+files)))
                realTime = datetime.datetime.now()
                c.execute("INSERT INTO Date_Time VALUES(?)",(realTime,))
                connection.commit()

                # Note:
                # This assignment requires I show the time of the last file transfer in the GUI
                # I could have shown the time of the last file transfer very easily with the following line:
                # "self.file_check.set(datetime.datetime.now())" added in place of "set.file.check.set" below
                # However, it would not have met the requirement to retrieve the time from a database
                # Therefore, I had to create a new definition "File_Time" and passed that in as seen below.


                def File_Time():
                    connection = sqlite3.connect('file_mover.db')
                    c = connection.cursor()
                    Time_Check = c.execute("SELECT check_time FROM Date_Time WHERE ROWID = (SELECT MAX(ROWID) FROM Date_Time)")
                    for row in c.fetchone():
                        return (row)
                    connection.close()
                ttk.Label(self.frame_content, text="Last File Check Date/Time:").grid(row=4, column=0, padx=10, pady=40, sticky = W)
                self.file_check = StringVar()
                self.file_check.set(File_Time())
                self.end_dest = ttk.Entry(self.frame_content, width=80, textvariable=self.file_check)
                self.end_dest.grid(row=4, column=2, padx=10, pady=3, sticky = W)


    def DB_Check(self):
        self.moveFiles(self.src_var.get(),self.dst_var.get())
        self.Time_Check.set(self.DB_Return())


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
        command= lambda: self.choose_Source()).grid(row=1, column=0, padx=10, pady=10, sticky = W)
        ttk.Button(self.frame_content, text='Choose Destination Folder',
        command= lambda: self.choose_Dest()).grid(row=3, column=0, padx=10, pady=10, sticky = W)
        ttk.Button(self.frame_content, text='Move the Files',
        command= lambda: self.moveFiles(self.source_var.get(),self.dest_var.get())).grid(row=6, column=0, padx=10, pady=20, sticky = W)

        # Entry line for Source Folder
        ttk.Label(self.frame_content, text="Source Folder:").grid(row=2, column=0, padx=10, pady=5, sticky = W)
        self.source_var = StringVar()
        self.start_source = ttk.Entry(self.frame_content, width=80, textvariable=self.source_var)
        self.start_source.grid(row=2, column=2, padx=10, pady=3)

        # Entry line for Destination Folder
        ttk.Label(self.frame_content, text="Destination Folder:").grid(row=4, column=0, padx=10, pady=3, sticky = W)
        self.dest_var = StringVar()
        self.end_dest = ttk.Entry(self.frame_content, width=80, textvariable=self.dest_var)
        self.end_dest.grid(row=4, column=2, padx=10, pady=3)

        # Showing Startup Time in GUI just for fun
        ttk.Label(self.frame_content, text="Startup Date/Time:").grid(row=0, column=0, padx=10, pady=40, sticky = W)
        self.start_check = StringVar()
        self.start_check.set(datetime.datetime.now())
        self.end_dest = ttk.Entry(self.frame_content, width=80, textvariable=self.start_check)
        self.end_dest.grid(row=0, column=2, padx=10, pady=3, sticky = W)


def main():
    root = Tk()
    filemover = File_Mover(root)
    root.mainloop()

if __name__ == "__main__": main()
