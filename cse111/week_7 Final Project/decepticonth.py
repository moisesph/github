"""
Find how many times a word or name is in a list
by: Moises Pleytez
"""

import tkinter as tk
from tkinter import Frame, Label, Button, filedialog as fd, ttk
from tkinter.messagebox import showinfo

import os
import string

# I need to put everything in lower case 
 
def main():
    root = tk.Tk()
    root.resizable(False, False)

    frm_window =tk.Frame(root)
    frm_window.master.title("Decepticonth")
    frm_window.pack(padx=3, pady=3, fill=tk.BOTH, expand=True) 
    set_main(frm_window)
    frm_window.mainloop()
    body_document = ""
#Sencitive to case letters


def set_main(window):


    
    lbl_name = tk.Label(window, text="What is the word which are you looking for?")
    
        
   
    lbl_name.grid(row=0, column=0)
    entry_name = tk.Entry(window, background="sky blue")
    entry_name.grid(row=1, column=0)


    lbl_doc = tk.Label(window, text="And the document?")
    lbl_doc.grid(row=2, column=0)
    button_doc = ttk.Button(window, text="Open a File", command=open_file)
    button_doc.grid(row=3, column=0)

    btn_start = tk.Button(window, text="Find!")
    btn_start.grid(row=4, column=0)


    output_message = tk.StringVar()

    btn_lbl_start = tk.Label(window, textvariable=output_message)
    btn_lbl_start.grid(row=5,column=0)

    

    def comparing(name, document):
        total = 0
        for word in document:
            if name in word:
                total+= 1
        text_comparison = f"Times that the word are repeated are {total}"
        return text_comparison



    def message_btn():
        
        word = entry_name.get()
        
        try:
            doc = body_document
        except NameError:
            output_message.set("Please Enter a word")    
        try:
            lbl_comparison_final = comparing(word, doc)#
            output_message.set(lbl_comparison_final)
        except UnboundLocalError:
            output_message.set("Please Enter a file")    
        
        if word == "" or word == " ":
            output_message.set("Please Enter a word")  
        

   
    btn_start.config(command=message_btn)


def open_file():
    global body_document
    filetypes = (
        ("text files", "*.txt"),
        ("word Files", ("*.doc", "*.docx")), #It is not recognicing this kind of documents
        ("All files", "*.*")
        )

    filename = fd.askopenfilename(
        title="open a file",
        initialdir = "/",
        filetypes=filetypes)

    file_name_only = os.path.basename(filename)


    #Heres a bug where if you don't select anything says it was opened successfully

    try:
        with open(filename, "r", encoding="utf-8") as f:

            old_body_document = [line.strip().split() for line in f] #This to open the file properly

            all_old_body_document = [word for sublist in old_body_document for word in sublist] #This to put it in a string to make it easy to process

            string_body_document = " ".join(all_old_body_document) # This to put it in one list

            body_document = string_body_document.split()

            showinfo(
            title="Selected File",
            message = f"The file {file_name_only} was selected successfully" 
            )
    except FileNotFoundError:
            showinfo(
            title="Error",
            message = "Please select a File!" 
            )



#Requirements
#1. The report be nice
#2. Report with total of 12 hours
#3. Runs ok and with no incorrect results
#4. 4 functions (I have 3)
#5. Program use 1 module                       YES
#6. Two Test Functions
#7. All test function pass
#8. Two asserts and 2 call in each test function



#Look how to attach the key enter to the button action

if __name__ in "__main__":
    main()