import random
import tkinter as tk
import string

def check_strength():
    password= entry.get()
    score=0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        result.set("Password too weak")
    elif score <= 4:
        result.set("Medium")
    else:
        result.set ("Password Strong")
    
def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd= ''.join(random.choice(chars) for _ in range(length))
    entry.delete(0,tk.END)
    entry.insert(0,pwd)
    result.set("Generated Strong Password ")

root = tk.Tk()
root.title("Password Tool")
root.geometry("400x300")
root.config(bg="#f5f5f5")

title = tk.Label(root,text="Password Tool", font=("Arial", 20,"bold"),bg="#f5f5f5")
title.pack(pady=15)

entry = tk.Entry(root,width=30,font=("Arial", 12))
entry.pack(pady=10)

btn_check=tk.Button(root,text="Check Strength",command=check_strength,bg="#4CAF50", fg="white")
btn_check.pack(pady=5)

btn_generate=tk.Button(root, text="Generate Password", command=generate_password, bg="#2196F3", fg="white")
btn_generate.pack(pady=5)

result=tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12), bg="#f5f5f5")
result_label.pack(pady=15)

root.mainloop()


