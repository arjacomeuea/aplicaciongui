import tkinter as tk
from tkinter import messagebox, simpledialog


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Crear los widgets principales
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Evento para Enter

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=1, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind("<Double-1>", self.complete_task)  # Evento para doble clic

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            if not task.startswith("[Completada] "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, "[Completada] " + task)
            else:
                messagebox.showinfo("Información", "Esta tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
