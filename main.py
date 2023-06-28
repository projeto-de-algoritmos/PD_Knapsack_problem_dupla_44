#from Tkinter import *
import tkinter as tk
from tkinter.ttk import *

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
       self.parent.geometry("600x600")
       self.parent.title("Pokeirmanos")
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
       self.button=tk.Button(self.parent,text="Verificar", command=self.PassCheck)
       self.button.pack()
       
   def PassCheck(self):
        size = self.entry.get()
        peso = self.entry1.get()
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
     
    # Toplevel object which will
    # be treated as a new window
    #newWindow = tk.Toplevel(master)
    root = tk.Tk()
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

    #texto = tk.Label(master, text="Salve esquisito...", bg='#5E2C04', activebackground="#BC03FC")

    master.title('Mercador Medieval')
    # a button widget which will open a
    # new window on button click
    btn = Button(master,
                text ="Iniciar",
                command = openNewWindow)
    btn.pack(pady = 10)

    btn2 = Button(master,
                text ="Sair",
                command = quit)
    btn2.pack(pady = 20) 
    master.configure(bg='#5E2C04')
    # mainloop, runs infinitely
    tk.mainloop()