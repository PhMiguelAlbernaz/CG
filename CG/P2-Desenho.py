#  ==============================================================================
# ---> Base 1: Root                     
import  time as t 
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Editor Gráfico Simples")

#  ==============================================================================
# ---> Etapa 1: Top  - Menue                     
menu = tk.Menu(root)
root.config(menu=menu)

menu_ficheiro = tk.Menu(menu, tearoff=0)                           
menu.add_cascade(label="Ficheiro", menu=menu_ficheiro)

menu_ficheiro.add_command(label="Limpar",                          # O comand "Limpar" limpa o canvas  
                          command=lambda: canvas.delete("all"))
menu_ficheiro.add_command(label="Sair", command=root.destroy)      # O comand "Sair" destruir a janela

#  ==============================================================================
# Direita - Canvas                --->  Etapa 2 
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(side="left", expand=True, fill="both")

# Definição da accao no canvas 
def desenhar():
        i=0
        while i<4:

            barra["value"] +=25            # Status inicial do progress na Progress-Bar é 0 %            
            canvas.delete("all")          # Antes desenhar temos limpar o estado interno do pano
            t.sleep(1)
            root.update()

            cor = combo_cor.get()         # Determine a cor do desenho apartir da Combo-Bar
            tamanho = escala.get()        # Determine o tamanho do desenho apartir da Scale-Bar

            # A Stringvariavel forma ligada ao Radiobutton determinada a forma que seja desejada condicionalmente 
            if forma.get() == "linha":
                canvas.create_line(50, 50, 50 + tamanho, 50,         # Uma linha comeca na posicao (50,50) com o
                                fill=cor, width=3)                # comprimento do tamabho, a expresur 3,
                                                                    # e a cor escolhida

            elif forma.get() == "circulo":                           # Um circulo centrado na posicao (50,50) com 
                canvas.create_oval(50, 50,                           # o raio do tamanho. Preenchido ou não de 
                                50 + tamanho, 50 + tamanho,       # com o valor da Boolvariable preenchido 
                                fill=cor if preenchido.get() else "", # ligado a checkbox
                                outline=cor)                      # A cor é de acordo com a escolha

            elif forma.get() == "retangulo":                          # Um quadrato ente (50,50) e 
                canvas.create_rectangle(50, 50,                       # (50+tamanho,50+tamanho)                             
                                        50 + tamanho, 50 + tamanho,   # o preenchimento e a cor de acordo com 
                                        fill=cor if preenchido.get() else "",  # o circulo
                                        outline=cor)
            
            i+=1
        barra["value"]=0                   # Status final do progress na Progress-Bar é 100 %
    
#  ==============================================================================
#--> Etapa 3: Preencher o Frame do controlo (esquerda)  

# A - Button que ativa a funcao desenhar


frame_controles = tk.Frame(root, padx=10, pady=10)  # Define o Frame a esquerda para colocar os controles
frame_controles.pack(side="left", fill="y")         # Colocar lo na esquerda 
tk.Button(canvas,
          text="Desenhar",
          command=desenhar).pack(pady=5)
            
#  B - Radiobutton: Define a forma para desenhar
forma = tk.StringVar(value="linha")            # Define a Stringvariavel para guardar o resultado do Radiobutton

tk.Label(frame_controles, text="Forma").pack(anchor="w")  # Colocar o Label para asinalar o objectivo do """
# Define as tres opcoes do Radiobutton
tk.Radiobutton(frame_controles, text="Linha",                            # 1. Linha
               variable=forma, value="linha").pack(anchor="w")           
tk.Radiobutton(frame_controles, text="Círculo",                          # 2. Circulo
               variable=forma, value="circulo").pack(anchor="w")
tk.Radiobutton(frame_controles, text="Retângulo",                        # 3. Rectangulo
               variable=forma, value="retangulo").pack(anchor="w")

#  C - Combobox: Define a cor do desenho
tk.Label(frame_controles, text="Cor").pack(anchor="w")       # Colocar o Label para asinalar o objectivo do Combobox
combo_cor = ttk.Combobox(frame_controles,                    # Define as cores opcionais da Combobox 
                         values=["black", "red", "blue", "green"])
combo_cor.current(0)                                         # O valor default é 0 entao preto
combo_cor.pack(fill="x")                                     # Combobox inserido com extensao horizontal

# D - Listbox e Scrollbar: Dar sugestoes para cores suplementar dos basicos no Combobox
lista_cores = tk.Listbox(frame_controles, height=4)
for cor in ["black", "red", "blue", "green", "orange", "purple"]:
    lista_cores.insert(tk.END, cor)
lista_cores.pack()

scroll = tk.Scrollbar(frame_controles)
scroll.pack(side="right", fill="y")

lista_cores.config(yscrollcommand=scroll.set)
scroll.config(command=lista_cores.yview)

# E - Scale: Define o tamanho da figura a desenhar
tk.Label(frame_controles, text="Tamanho").pack(anchor="w")

escala = tk.Scale(frame_controles,
                  from_=20, to=200,
                  orient="horizontal")
escala.pack(fill="x")

# F - Checkbox: Decide se a figura desenhada vai ser preenchido ou desenhada so com os contornos
preenchido = tk.BooleanVar()

tk.Checkbutton(frame_controles,
               text="Preenchido",
               variable=preenchido).pack(anchor="w")

# G - Progressbar: Indica o progresso do sedenho (essencialmente so visivel antes do 1. Desenho)
barra = ttk.Progressbar(frame_controles,
                        length=150,
                        mode="determinate")
barra.pack(pady=10)

#  ==============================================================================
# ---> Base 2: Root EXECUTA O LOOP PRINCIPAL
root.mainloop()