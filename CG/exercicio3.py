import tkinter as tk
#Funcoes
def somar():
    pass
# app
app = tk.Tk()
app.title("")
# frames 
frame = tk.Frame(app)
frame.pack(padx=10,pady=5)
frame2= tk.Frame(app)
frame2.pack(padx=10,pady=5)
#label
label= tk.Label(frame,text="Euro:")
label.pack(side="left")
label= tk.Label(frame2,text="dolar:")
label.pack(side="left")

#entry's
entry= tk.Entry(frame)
entry.pack(side="bottom")
entry3=tk.Entry(frame)
entry3.pack(side="top")
entry2=tk.Entry(frame2)
entry2.pack(side="bottom")
#butoes
button = tk.Button(app,text="mete a dar")
button.pack(padx=5,pady=5)
button2=tk.Button(app,text="troca de moeda")

#fim
app.mainloop()