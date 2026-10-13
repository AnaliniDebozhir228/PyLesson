import tkinter as tk


from view import show_menu

root = tk.Tk()
root.geometry("300x300")
frame_menu = tk.Frame(root, bg="Black", width=300, height=400)

def show_all_tasks():
    show_menu.pack_forget()

def create_menu():
    frame_menu.pack()
    button_show_task = tk.Button(frame_menu, text="Посмотреть задачи", command=show_menu())
    button_show_task.pack()

create_menu()
root.mainloop()