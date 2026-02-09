import tkinter  as tk
def somar():
    numero2=Entrada1.get()
    numero1=Entrada.get()
    label.config(text=f"{float(numero1)+float(numero2)}")

def subtrair():
    numero1=Entrada.get()
    numero2=Entrada1.get()
    label.config(text=f"{float(numero1)-float(numero2)}")

janela  = tk.Tk()
janela.title("calculadora")


Entrada= tk.Entry(janela)
Entrada.pack(padx=10,pady=5)
Entrada1= tk.Entry(janela)
Entrada1.pack(padx=10,pady=5)

label= tk.Label(janela,text="nada")
label.pack(padx=10,pady=5)

butao= tk.Button(janela,text="somar",command=somar)
butao.pack(padx=10,pady=5)
butao1= tk.Button(janela,text="subtrair",command=subtrair)
butao1.pack(padx=10,pady=5)

janela.mainloop()