import tkinter as tk
from tkinter import filedialog, messagebox
from cyberpunk import all_sequences, hadiah, read_file
from IO import write_ada_solusi, write_no_solusi

class CyberpunkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyberpunk 2077 Breach Protocol")
        
        # Input Frame
        self.input_frame = tk.LabelFrame(self.root, text="Input")
        self.input_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Input Options
        self.input_type = tk.StringVar()
        self.input_type.set("file")

        self.input_type_label = tk.Label(self.input_frame, text="Pilih jenis masukan:")
        self.input_type_label.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(10, 0))

        self.input_type_file = tk.Radiobutton(self.input_frame, text="File (.txt)", variable=self.input_type, value="file")
        self.input_type_file.grid(row=0, column=1, sticky="w", pady=(10, 0))

        self.input_type_keyboard = tk.Radiobutton(self.input_frame, text="Keyboard", variable=self.input_type, value="keyboard")
        self.input_type_keyboard.grid(row=0, column=2, sticky="w", pady=(10, 0))

        # File Input
        self.file_input_label = tk.Label(self.input_frame, text="Nama file:")
        self.file_input_label.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))

        self.file_input_entry = tk.Entry(self.input_frame, width=30)
        self.file_input_entry.grid(row=1, column=1, columnspan=2, sticky="w", pady=(10, 0))

        self.browse_button = tk.Button(self.input_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=3, sticky="w", pady=(10, 0))

        # Action Buttons
        self.execute_button = tk.Button(self.root, text="Execute", command=self.execute_game)
        self.execute_button.pack(pady=(0, 10))

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.file_input_entry.delete(0, tk.END)
            self.file_input_entry.insert(0, filename)

    def execute_game(self):
        input_type = self.input_type.get()
        if input_type == "file":
            filename = self.file_input_entry.get()
            if filename:
                self.execute_from_file(filename)
            else:
                messagebox.showerror("Error", "Nama file tidak valid.")
        elif input_type == "keyboard":
            self.execute_from_keyboard()

    def execute_from_file(self, filename):
        try:
            buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards = read_file(filename)
            cari_sequences, cari_coordinates = all_sequences(matrix, buffer_size)
            total_hadiah = hadiah(matrix, cari_sequences, sequence_rewards)
            bobot_hadiah_max = max(total_hadiah)
            if bobot_hadiah_max != 0:
                index = total_hadiah.index(bobot_hadiah_max)
                write_ada_solusi(index + 1, cari_sequences, cari_coordinates, bobot_hadiah_max, 0)  # Execution time is not available here
            else:
                write_no_solusi(bobot_hadiah_max, 0)  # Execution time is not available here
            messagebox.showinfo("Info", "Eksekusi berhasil!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def execute_from_keyboard(self):
        messagebox.showerror("Error", "Belum diimplementasikan untuk masukan melalui keyboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberpunkApp(root)
    root.mainloop()
