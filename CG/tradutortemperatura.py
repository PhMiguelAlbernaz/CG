import tkinter as tk 
def traducao():
    match entry1.get().lower().strip():
        case "fahrenheit":
            texto=entry2.get()
            label3.config(text=f"graus fahrenheit: {float(texto)*9/5 +32}")
        case "graus":
            texto=entry2.get()
            label3.config(text=f"graus fahrenheit: {1/(float(texto)*9/5 +32)}")

    
janela =tk.Tk()
janela.title("traducao das traducoes da temperatura")
frame=tk.Frame(janela)
frame.pack(padx=10,pady=10)
label= tk.Label(frame,text="medida")
label.pack(side="left")
entry1= tk.Entry(frame)
entry1.pack(side="right")
frame1=tk.Frame(janela)
frame1.pack(padx=20,pady=20)
entry2=tk.Entry(frame1)
entry2.pack(side="right")
label1= tk.Label(frame1,text="temperatura:")
label1.pack(side="left")
frame3=tk.Frame(janela)
frame3.pack(padx=20,pady=20)
label3= tk.Label(frame3,text="")
label3.pack(side="left")


button= tk.Button(janela,text="entry",command=traducao)
button.pack()
janela.mainloop()
