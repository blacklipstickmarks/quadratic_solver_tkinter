import tkinter as tk
from tkinter import messagebox
import cmath
import numpy as np
import matplotlib.pyplot as plt

def solve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "This is not a quadratic equation (a should not be 0)")
            return

        d = b**2 - 4*a*c
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)

        result = f"x₁ = {round(x1.real, 3)}"
        if x1.imag != 0:
            result += f" + {round(x1.imag, 3)}i"

        result += f"\nx₂ = {round(x2.real, 3)}"
        if x2.imag != 0:
            result += f" + {round(x2.imag, 3)}i"

        label_result.config(text=result)
        plot_graph(a, b, c)

    except ValueError:
        messagebox.showerror("Error", "Enter correct numbers")

def plot_graph(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.figure(figsize=(6,4))
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title("Graph of Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

#interface
window = tk.Tk()
window.title("Quadratic Equation Solver")
window.geometry("300x250")

tk.Label(window, text="Enter coefficients:").pack(pady=5)

tk.Label(window, text="a:").pack()
entry_a = tk.Entry(window)
entry_a.pack()

tk.Label(window, text="b:").pack()
entry_b = tk.Entry(window)
entry_b.pack()

tk.Label(window, text="c:").pack()
entry_c = tk.Entry(window)
entry_c.pack()

tk.Button(window, text="Solve", command=solve).pack(pady=10)
label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=10)

window.mainloop()