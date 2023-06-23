import tkinter as tk
import os.path
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from criar_link_simbolico import criar_link_simbolico

entry_origem = None
entry_destino = None


def selecionar_pasta_origem():
    global entry_origem
    pasta_origem = filedialog.askdirectory()
    entry_origem.delete(0, tk.END)
    entry_origem.insert(0, pasta_origem)

def selecionar_pasta_destino():
    global entry_destino
    nome_pasta = entry_destino.get()
    pasta_destino = os.path.join(os.path.expanduser("~"), "OneDrive", nome_pasta)
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, pasta_destino)
    

def mostrar_mensagem(titulo, mensagem):
    root = tk.Tk()
    root.title(titulo)
    root.geometry("300x120")
    
    label = tk.Label(root, text=mensagem)
    label.pack(pady=20)
    
    button_frame = ttk.Frame(root)
    button_frame.pack()
    
    ok_button = ttk.Button(button_frame, text="OK", command=root.destroy)
    ok_button.pack(side=tk.LEFT, padx=10)
    
    fechar_button = ttk.Button(button_frame, text="Fechar o Programa", command=root.quit)
    fechar_button.pack(side=tk.LEFT)
    
    root.mainloop()
    

def criar_interface_grafica():
    global entry_origem
    global entry_destino
    
    root = tk.Tk()
    root.title("Sincronizar pastas com o OneDrive")
    root.geometry("700x300")
    
    fonte_arial = tkFont.Font(family="Arial", size=9)
    
    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat")
    
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(expand=True)
    
    label_origem = ttk.Label(main_frame, text="Pasta de Origem:")
    label_origem.grid(row=0, column=0, sticky=tk.W)
    
    entry_origem = ttk.Entry(main_frame, width=50)
    entry_origem.grid(row=0, column=1, sticky=tk.W+tk.E)
    
    button_origem = ttk.Button(main_frame, text="Selecionar Pasta", command=selecionar_pasta_origem)
    button_origem.grid(row=0, column=2, padx=10)
    
    label_destino = ttk.Label(main_frame, text="Pasta no OneDrive:")
    label_destino.grid(row=1, column=0, sticky=tk.W)

    entry_destino = ttk.Entry(main_frame, width=50)
    entry_destino.grid(row=1, column=1, sticky=tk.W+tk.E)

    text_box = tk.Text(main_frame, width=50, height=5, wrap='word', state='disabled', font=fonte_arial)
    text_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    
    def adicionar_avisos(texto):
        text_box.configure(state='normal')
        text_box.insert(tk.END, texto + "\n")
        text_box.configure(state='disable')
        text_box.see(tk.END) 
        
    adicionar_avisos("Por favor, evite utilizar nomes de pastas já existentes no OneDrive e certifique-se de executar o programa com privilégios de administrador.")
    
    def criar_link():
        nome_pasta = entry_destino.get()
        pasta_destino = os.path.join(os.path.expanduser("~"), "OneDrive", nome_pasta)
        destino = pasta_destino
        origem = entry_origem.get()
        sucesso, mensagem = criar_link_simbolico(destino, origem)
        if sucesso:
            mostrar_mensagem("Sucesso", mensagem)
        else:
            mostrar_mensagem("Erro", mensagem)
    
    button_criar_link = ttk.Button(main_frame, text="Criar Link", command=criar_link)
    button_criar_link.grid(row=3, column=1, pady=20)
    
    root.mainloop()