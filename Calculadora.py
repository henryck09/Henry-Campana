import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")
        
        self.entrada = tk.Entry(root, width=16, font=('Arial', 18), borderwidth=2, relief="solid")
        self.entrada.grid(row=0, column=0, columnspan=4)
        
        self.crear_botones()
        
    def crear_botones(self):
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for boton in botones:
            action = lambda x=boton: self.click_boton(x)
            tk.Button(self.root, text=boton, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def click_boton(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except Exception as e:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            self.entrada.insert(tk.END, valor)

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()