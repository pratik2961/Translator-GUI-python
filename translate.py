from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES



def converstion(text="type",src="English",dest="Hindi"):
    text1 = text[0:-2]
    src1 = src 
    dest1 = dest
    trans  = Translator()
    # trans._translate(text, dest, src, override)
    translated  = trans.translate(text,dest=dest1,src=src1)
    return translated

def data():
    s = comb_source.get()
    d = comb_target.get()
    
    i = source_txt.get(1.0,END)
    
    text_get = converstion(text = i ,src=s,dest=d)
    
    output_txt.delete(1.0,END)
    output_txt.insert(END, text_get)
    

root = Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg='black')

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="black",fg="white")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

source_label = Label(frame,text="Input Text :",font=("Time New Roman",15,"bold"),fg="white",bg="black")
source_label.place(x=30,y=140,height=20,width=110)

source_txt = Text(frame,font=("Time New Roman",12),bg="black",fg="white",wrap=WORD)
source_txt.place(x=30,y=170,height=100,width=440)

source_label = Label(frame,text="Input Text :",font=("Time New Roman",15,"bold"),fg="white",bg="black")
source_label.place(x=30,y=140,height=20,width=110)

source_txt = Text(frame,font=("Time New Roman",12),bg="black",fg="white",wrap=WORD)
source_txt.place(x=30,y=170,height=100,width=440)

output_label = Label(frame,text="Output Text :",font=("Time New Roman",15,"bold"),fg="white",bg="black")
output_label.place(x=30,y=290,height=20,width=125)

output_txt = Text(frame,font=("Time New Roman",12),bg="black",fg="white",wrap=WORD)
output_txt.place(x=30,y=320,height=100,width=440)

list_text = list(LANGUAGES.values())

comb_source = ttk.Combobox(frame,values=list_text)
comb_source.place(x=390,y=140,height=20,width=80) 
comb_source.set("english")

change_btn = Button(frame,text="Translate",bg="black",fg="white",relief=RAISED,font=("Time New Roman",12,"bold"),command=data)
change_btn.place(x=190,y=440,height=40,width=100)

comb_target = ttk.Combobox(frame,values=list_text)
comb_target.place(x=390,y=290,height=20,width=80) 
comb_target.set("english")


root.mainloop()