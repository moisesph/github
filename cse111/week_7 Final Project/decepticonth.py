"""
Find how many times a word or name is in a list
by: Moises Pleytez
"""

import tkinter as tk
from tkinter import Frame, Label, Button, filedialog as fd, ttk
from tkinter.messagebox import showinfo

import os


def main():
    root = tk.Tk()
    root.resizable(False, False)

    frm_window =tk.Frame(root)
    frm_window.master.title("Decepticonth")
    frm_window.pack(padx=3, pady=3, fill=tk.BOTH, expand=True) 
    set_main(frm_window)
    frm_window.mainloop()

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
    btn_lbl_start = tk.Label(window, text="")
    btn_lbl_start.grid(row=5,column=0)

    word= lbl_name
    doc = button_doc
    compare = comparing(word, doc)


    


def open_file():
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

    showinfo(
        title="Selected File",
        message = f"The file {file_name_only} was selected successfully" #I am trying to show this at the screen
    )

    #Heres a bug where if you don't select anything says it was opened successfully
    


def comparing(name, document):
    compare = ""
    compare = f"The name appears: {compare}"
    print(compare)
    return compare
  #  if name in document:
  #      print("XDDD")
    pass


#Let him know how many times appears




#Ask if he wants to change every word for one

#Replace if yes



if __name__ in "__main__":
    main()