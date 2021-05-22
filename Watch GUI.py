from tkinter import*
from tkinter.ttk import*
 
 #import strftime functo to retrive system time
from time import strftime

#creating tikinter windoes
root=Tk()

# this function is ued to display time to the label
def time():
    string=strftime('%H:%M:%S %p!')
    lbl=config(text=string)
    lbl.after(1000, time)

    #lbl stlying
    lbl=label(root, font=("calibri 40 bold"),bg='purple', foreground='white')

    #placing
    lbl.pack(anchor='center')
    time()







root.title('Prince Kumar')
root.mainloop()