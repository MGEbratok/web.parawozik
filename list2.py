import customtkinter as ctk
from tkinter import messagebox

class ShoppingListApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x600")
        self.title("Список покупок")

        self.items = [] 


        self.entry = ctk.CTkEntry(self, placeholder_text="Введіть назву товару")
        self.entry.pack(pady=5, padx=10, fill='x')

        self.category_var = ctk.StringVar(value="Загальне")
        self.category_menu = ctk.CTkOptionMenu(self, variable=self.category_var,
                                               values=["Загальне", "Овочі", "М’ясо", "Молочне", "Напої", "Інше"])
        self.category_menu.pack(pady=5, padx=10)


        self.add_button = ctk.CTkButton(self, text="Додати", command=self.add_item)
        self.add_button.pack(pady=5)

        self.listbox = ctk.CTkTextbox(self, height=300)
        self.listbox.pack(pady=10, padx=10, fill='both', expand=True)

        self.sort_alpha_button = ctk.CTkButton(self, text="Сортувати (А-Я)", command=self.sort_alphabetically)
        self.sort_alpha_button.pack(pady=5)

        self.sort_cat_button = ctk.CTkButton(self, text="Сортувати за категоріями", command=self.sort_by_category)
        self.sort_cat_button.pack(pady=5)

        self.done_button = ctk.CTkButton(self, text="Позначити куплене", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self, text="Видалити вибране", command=self.delete_item)
        self.delete_button.pack(pady=5)

    def add_item(self):
        name = self.entry.get().strip()
        category = self.category_var.get()
        if name:
            self.items.append({"name": name, "category": category, "done": False})
            self.entry.delete(0, 'end')
            self.update_listbox()
        else:
            messagebox.showwarning("Помилка", "Назва товару не може бути порожньою!")

    def update_listbox(self):
        self.listbox.delete("1.0", "end")
        for idx, item in enumerate(self.items, start=1):
            status = "✔ " if item["done"] else ""
            line = f"{idx}. {status}{item['name']} [{item['category']}]\n"
            self.listbox.insert("end", line)

    def sort_alphabetically(self):
        self.items.sort(key=lambda x: x["name"].lower())
        self.update_listbox()

    def sort_by_category(self):
        self.items.sort(key=lambda x: x["category"])
        self.update_listbox()

    def get_selected_index(self):
        index = self.listbox.index("insert").split(".")[0]
        if index.isdigit():
            index = int(index) - 1
            if 0 <= index < len(self.items):
                return index
        return None

    def mark_done(self):
        idx = self.get_selected_index()
        if idx is not None:
            self.items[idx]["done"] = True
            self.update_listbox()

    def delete_item(self):
        idx = self.get_selected_index()
        if idx is not None:
            del self.items[idx]
            self.update_listbox()


if __name__ == "__main__":
    ctk.set_default_color_theme("theme.json")
    app = ShoppingListApp()
    app.mainloop()
ctk.set_default_color_theme("theme.json")