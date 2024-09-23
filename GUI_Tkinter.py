mport tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para mostrar eventos
        self.frame_eventos = ttk.Frame(root)
        self.frame_eventos.pack(padx=10, pady=10)

        # TreeView para listar eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("fecha", "hora", "descripcion"), show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10)

        # Campos de entrada
        self.label_fecha = ttk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        self.label_hora = ttk.Label(self.frame_entrada, text="Hora:")
        self.label_hora.grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        self.label_descripcion = ttk.Label(self.frame_entrada, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones
        self.boton_agregar = ttk.Button(root, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(padx=10, pady=5)

        self.boton_eliminar = ttk.Button(root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(padx=10, pady=5)

        self.boton_salir = ttk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack(padx=10, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()
        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(selected_item)

    def limpiar_campos(self):
        self.fecha_entry.delete(0, 'end')
        self.hora_entry.delete(0, 'end')
        self.descripcion_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
