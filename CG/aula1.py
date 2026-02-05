import tkinter as tk
root=tk.Tk()
root.title("windows")
root.geometry("400x400")
label = tk.Label(root,text="ola amigo")
label.pack()
entry = tk.Entry(root)
entry.pack()
frame= tk.Frame(root)
frame.pack()
def ring():
    texto= entry.get()
    label.config(text=f"ola {texto}")
entry =tk.Entry(frame)
entry.pack()   

button= tk.Button(frame, text="clique",command=ring,font=("Helvetica",24),fg="#4d4d4d")
button.pack(padx=20,pady=20)
root.mainloop()