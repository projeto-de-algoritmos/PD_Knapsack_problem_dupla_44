#from Tkinter import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import tkinter.messagebox

# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP
 
 
# def knapsack(wt, val, W, n):
 
#     # base conditions
#     if n == 0 or W == 0:
#         return 0
#     if t[n][W] != -1:
#         return t[n][W]
 
#     # choice diagram code
#     if wt[n-1] <= W:
#         t[n][W] = max(
#             val[n-1] + knapsack(
#                 wt, val, W-wt[n-1], n-1),
#             knapsack(wt, val, W, n-1))
#         return t[n][W]
#     elif wt[n-1] > W:
#         t[n][W] = knapsack(wt, val, W, n-1)
#         return t[n][W]

def knapsack(capacidade, pesos, valores):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    valor_maximo = dp[n][capacidade]
    itens_selecionados = []
    w = capacidade
    for i in range(n, 0, -1):
        if valor_maximo <= 0:
            break
        if valor_maximo == dp[i - 1][w]:
            continue
        else:
            itens_selecionados.append(i - 1)
            valor_maximo -= valores[i - 1]
            w -= pesos[i - 1]

    return dp[n][capacidade], itens_selecionados[::-1]

# Driver code
#if __name__ == '__main__':
 #   profit = [60, 100, 120]
  #  weight = [10, 20, 30]
   # W = 50
    #n = len(profit)
     
    # We initialize the matrix with -1 at first.
    #t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    # print(knapsack(weight, profit, W, n))
    #print(knapsack(W, weight, profit))

# This code is contributed by Prosun Kumar Sarkar

def Mostra_Mochila(result, packs):
    
    root = tk.Tk()
    root.configure(bg='#5E2C04')
    listbox = tk.Listbox(root, height = 30,
                  width = 50,
                  bg = "#5E2C04",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "#90EE90")
    # Define the size of the window.
    root.geometry("600x600") 

    frame = Frame(root)
    frame.pack(pady=20)

    i = 0
    while True:
        try:
            line = ("Maximo valor:", result, "Peso:", packs[i].weight, "Valor:", packs[i].value)
            listbox.insert(i, line)
            i += 1
        except IndexError:
            break

    # Define a label for the list. 
    label = tk.Label(root, text = "Itens para transporte")
    label.pack()
    listbox.pack()
    listbox.configure(justify='center')

    def voltar():
        print("Ze da manga")

    btn1 = Button(root, text="Voltar", command=voltar)
    btn1.pack()

    root.mainloop()
 
class KnapsackPackage(object):
    """ Knapsack Package Data Class """
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost

class FractionalKnapsack(object):
    def knapsackGreProc(self, W, V, M, n):
        packs = []
        for i in range(n):
            packs.append(KnapsackPackage(int(W[i]), int(V[i])))
        packs.sort(reverse=True)
        remain = M
        result = 0
        i = 0
        stopProc = False

        while not stopProc:
            if packs[i].weight <= remain:
                remain -= packs[i].weight
                result += packs[i].value
                print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)

            if packs[i].weight > remain:
                i += 1

            if i == n:
                stopProc = True

        print("Max Value: ", result)
        Mostra_Mochila(result, packs)



class Passwordchecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

   def initialize_user_interface(self):
       #self.parent.geometry("600x600")
       self.parent.title("Mochila")
       self.label=tk.Label(self.parent,text="Insira a quantidade de itens")
       self.label.configure(bg='#5E2C04', fg='#90EE90')
       self.label.pack()
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.label=tk.Label(self.parent,text="Digite o tamanho total da mochila")
       self.label.configure(bg='#5E2C04', fg='#90EE90')
       self.label.pack()
       self.entry1=tk.Entry(self.parent)
       self.entry1.pack()
       self.label=tk.Label(self.parent,text="Insira os pesos dos itens de acordo com a quantidade")
       self.label.configure(bg='#5E2C04', fg='#90EE90')
       self.label.pack()
       self.entry2=tk.Entry(self.parent)
       self.entry2.pack()
       self.label=tk.Label(self.parent,text="Insira os valores dos itens de acordo com a quantidade")
       self.label.configure(bg='#5E2C04', fg='#90EE90')
       self.label.pack()
       self.entry3=tk.Entry(self.parent)
       self.entry3.pack()
       self.button=tk.Button(self.parent,text="Verificar", command=self.PassCheck, background='Green')
       self.button.pack()
       
   def PassCheck(self):
        size = self.entry.get()
        peso = self.entry1.get()

        if not all([size, peso]):
            tk.messagebox.showwarning("Error", "um ou mais espaços em branco") 
        else:
            IP = list(map(int, self.entry2.get().split()))
            Valor = list(map(int, self.entry3.get().split()))
            
            # W = [30, 10, 2, 4] #-> peso do item
            # V = [50, 25, 2, 6] #-> valor do item
            # M = 37 #-> mochiila
            # n = 4 #-> numero de itens
            N = int(size)
            W = IP #-> IP = Item Peso
            M = int(peso) #-> peso total da mochila
            V = Valor

            print("size", size, "N:" , N , "W:", W , "M:", M , "V", V)        
            proc = FractionalKnapsack()
            proc.knapsackGreProc(W, V, M, N)
            
       

 
 
# function to open a new window
# on a button click
def openNewWindow():
    root = tk.Tk()
    root.geometry("600x600")
    root.configure(bg='#5E2C04')

    run = Passwordchecker(root)
    root.mainloop()


 



# creates a Tk() object
master = tk.Tk()
    
# sets the geometry of main
# root window
master.geometry("600x600")

if __name__ == "__main__":

    label = Label(master, text="Welcome Stranger...")
    label.pack(pady = 10)
    #label.configure(bg='#5E2C04')

    file = "Modded_wagon.png"

    # Obtenha as dimensões do frame
    frame_width = 600
    frame_height = 600

    # Carregue a imagem original
    original_image = Image.open(file)

    # Redimensione a imagem para o tamanho do frame
    resized_image = original_image.resize((frame_width, frame_height), Image.LANCZOS)

    # Crie o objeto ImageTk a partir da imagem redimensionada
    bg = ImageTk.PhotoImage(resized_image)

    # Crie o label com a imagem redimensionada
    label = Label(master, image=bg)
    label.place(x=0, y=0)

    frame = Frame(master)
    frame.pack(pady=20)

    #texto = tk.Label(master, text="Salve esquisito...", bg='#5E2C04', activebackground="#BC03FC")

    master.title('Mercador Medieval')
    # a button widget which will open a
    # new window on button click
    btn = Button(master,
                text ="Iniciar", 
                command = openNewWindow)
    btn.pack(pady = 10)

    btn2 = Button(master, text ="Sair", command = quit)
    btn2.pack(pady = 20) 

    master.configure(bg='#5E2C04')
    # mainloop, runs infinitely
    tk.mainloop()
