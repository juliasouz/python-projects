import tkinter as tk
from tkinter import ttk, messagebox

def calcular_salario():
    try:
        horas = float(entrada_horas.get())
        valor_hora = float(entrada_valor_hora.get())
        horas_extras = float(entrada_horas_extras.get()) if entrada_horas_extras.get() else 0
        valor_hora_extra = float(entrada_valor_hora_extra.get()) if entrada_valor_hora_extra.get() else 0
        descontos = float(entrada_descontos.get()) if entrada_descontos.get() else 0

        salario_base = horas * valor_hora
        salario_extra = horas_extras * valor_hora_extra
        salario_bruto = salario_base + salario_extra
        salario_liquido = salario_bruto - descontos

        resultado.set(f"O salário líquido é: R${salario_liquido:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Salário")

# Variável para exibir o resultado
resultado = tk.StringVar()

#Estilo
estilo = ttk.Style()
estilo.theme_use('xpnative')

# Layout da interface
ttk.Label(root, text="Horas Trabalhadas:").grid(row=0, column=0, padx=10, pady=5)
entrada_horas = ttk.Entry(root)
entrada_horas.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Valor por Hora:").grid(row=1, column=0, padx=10, pady=5)
entrada_valor_hora = ttk.Entry(root)
entrada_valor_hora.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Horas Extras:").grid(row=2, column=0, padx=10, pady=5)
entrada_horas_extras = ttk.Entry(root)
entrada_horas_extras.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Valor por Hora Extra:").grid(row=3, column=0, padx=10, pady=5)
entrada_valor_hora_extra = ttk.Entry(root)
entrada_valor_hora_extra.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Descontos:").grid(row=4, column=0, padx=10, pady=5)
entrada_descontos = ttk.Entry(root)
entrada_descontos.grid(row=4, column=1, padx=10, pady=5)

ttk.Button(root, text="Calcular", command=calcular_salario).grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(root, textvariable=resultado).grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
root.mainloop()