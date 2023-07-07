import tkinter as tk
from tkinter.ttk import *

def knapsack(wt, val, W, n, t):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1, t), knapsack(wt, val, W, n-1, t))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1, t)
        return t[n][W]

def Mostra_Mochila(result, packs):
    root = tk.Tk()
    root.configure(bg='#5E2C04')
    listbox = tk.Listbox(root, height=30, width=50, bg="#5E2C04", activestyle='dotbox', font="Helvetica", fg="#90EE90")
    root.geometry("600x600")
    i = 0
    while True:
        try:
            line = ("Maximo valor:", result, "Peso:", packs[i].weight, "Valor:", packs[i].value)
            listbox.insert(i, line)
            i += 1
        except IndexError:
            break

    label = tk.Label(root, text="Itens para transporte")
    label.pack()
    listbox.pack()
    listbox.configure(justify='center')
    root.mainloop()

class KnapsackPackage(object):
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
        N = int(size)
        W = IP
        M = int(peso)
        V = Valor

        t = [[-1 for i in range(M + 1)] for j in range(N + 1)]
        print("size", size, "N:", N , "W:", W , "M:", M , "V:", V)
        proc = FractionalKnapsack()
        proc.knapsackGreProc(W, V, M, N)

def openNewWindow():
    root = tk.Tk()
    root.configure(bg='#5E2C04')
    run = Passwordchecker(root)
    root.mainloop()

master = tk.Tk()
master.geometry("600x600")

if __name__ == "__main__":
    label = Label(master, text="Welcome Stranger...")
    label.pack(pady=10)
    btn = Button(master, text="Iniciar", command=openNewWindow)
    btn.pack(pady=10)
    btn2 = Button(master, text="Sair", command=quit)
    btn2.pack(pady=20)
    master.configure(bg='#5E2C04')
    tk.mainloop()
