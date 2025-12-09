"""
Find how many times a word or name is in a list
by: Moises Pleytez
"""

import tkinter as tk
from tkinter import Frame, Label, Button, filedialog as fd, ttk
from tkinter.messagebox import showinfo

import os
import string
import webbrowser

# I need to put everything in lower case 
 
def main():
    """Creates the root window for the program"""
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
    """It has the content of the program"""

    lbl_name = tk.Label(window, text="What is the word or number to search?")
    lbl_name.grid(row=0, column=0)

    entry_name = tk.Entry(window, background="sky blue")
    entry_name.grid(row=1, column=0)


    lbl_doc = tk.Label(window, text="And the document? (Remember)")
    lbl_doc.grid(row=2, column=0)
    button_doc = ttk.Button(window, text="Open a File", command=open_file)
    button_doc.grid(row=3, column=0)

    btn_start = tk.Button(window, text="Find!")
    btn_start.grid(row=4, column=0)


    output_message = tk.StringVar()

    btn_lbl_start = tk.Label(window, textvariable=output_message)
    btn_lbl_start.grid(row=5,column=0)

    btn_spam_website = tk.Button(window, text="Here's about me!")
    btn_spam_website.grid(row=6, column=0)



    def comparing(name, document):
        """Counts the times that the word is in the document"""
        total = 0

        

        for word in document:
            if name in word:
                total+= 1
        text_comparison = f"Times that the word are repeated are {total}"
        return text_comparison



    def message_btn():
        """Shows different messages at the end of the button"""
        global word
        word = entry_name.get()
        word = word.lower()

        if " " in word:
            output_message.set("Do not enter spaces") 
            return
        
        if word.strip() == "":
            output_message.set("Please Enter a word") 
            return

        try:
            doc = body_document
        except NameError:
            output_message.set("Please Enter a word")    
        try:
            make_lower_case(doc)
            lbl_comparison_final = comparing(word, doc)
            output_message.set(lbl_comparison_final)
        except UnboundLocalError:
            output_message.set("Please Enter a file")    
        

   
    btn_start.config(command=message_btn)

    btn_spam_website.config(command=open_url)

def open_url():
    """Open my biography making Spam"""
    url = "https://moisesph.github.io/wdd130"
    webbrowser.open_new_tab(url)


def open_file():
    """Open the file cleaning it with any unwanted sign"""
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


def make_lower_case(document):
    """Makes the List lower"""

    for i, words in enumerate(document):
        document[i] = words.lower()


    return words


#Requirements
#1. The report be nice                          Yes
#2. Report with total of 12 hours               NO
#3. Runs ok and with no incorrect results       NO
#4. 4 functions (I have 3)                      YES
#5. Program use 1 module                       YES
#6. Two Test Functions                          NO
#7. All test function pass                      NO
#8. Two asserts and 2 call in each test function NO



#Look how to attach the key enter to the button action

if __name__ in "__main__":
    main()