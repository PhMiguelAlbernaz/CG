import tkinter as tk 
def traducao():
    texto=entry.get()
    label.config(text=f"graus fahrenheit: {float(texto)*9/5 +32}")
janela =tk.Tk()
janela.title("traducao das traducoes da temperatura")

label= tk.Label(janela,text="temperatura")
label.pack()
entry= tk.Entry(janela)
entry.pack()
button= tk.Button(janela,text="enter",command=traducao)
button.pack()
janela.mainloop()
