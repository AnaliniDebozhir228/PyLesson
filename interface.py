import tkinter as tk
from view import show_menu


class interface:
    def __init__(self):
        self.root = tk.Tk()  # теперь self.root
        self.root.geometry("300x300")

        self.frame_menu = tk.Frame(self.root, bg="Black", width=300, height=400)

        def show_all_tasks():
            print("Показать задачи")

        def create_menu():
            self.frame_menu.pack()
            button_show_task = tk.Button(
                self.frame_menu,
                text="Посмотреть задачи",
                command=show_all_tasks  # без скобок!
            )
            button_show_task.pack()

        create_menu()  # вызываем меню


if __name__ == "__main__":
    app = interface()
    app.root.mainloop()


    #test