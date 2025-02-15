import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = weight_entry.get().strip()
        height = height_entry.get().strip()
        
        if not weight or not height:
            messagebox.showerror("Missing Info", "Please enter both weight and height.")
            return
        
        weight = float(weight)
        height = float(height)
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return
        
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight "
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight "
        elif 25 <= bmi < 29.9:
            category = "Overweight "
        else:
            category = "Obese "
        
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}", fg="blue")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("320x250")
root.resizable(False, False)

tk.Label(root, text="Enter your weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Enter your height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

calc_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
