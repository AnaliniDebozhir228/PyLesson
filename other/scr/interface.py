import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
button = tk.Button()

def start():
    global counter
    counter += 1
    label.config(text=f'{counter}')

counter = 0

label = tk.Label(root, text=f"{counter}")
label.pack(pady=20)

b_s= tk.Button(root, text="<UNK>", command=start)
b_s.pack()
root.mainloop()