import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
import random

class BreachProtocolSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyberpunk 2077 Breach Protocol Solver")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_intro = tk.Label(self.root, text="Welcome to Cyberpunk 2077 Breach Protocol Solver", font=("Helvetica", 16))
        self.label_intro.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.label_input_type = tk.Label(self.root, text="Jenis masukan:")
        self.label_input_type.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.input_type = tk.StringVar()
        self.input_type.set("file")
        self.radio_file = tk.Radiobutton(self.root, text="File (.txt)", variable=self.input_type, value="file")
        self.radio_file.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.radio_keyboard = tk.Radiobutton(self.root, text="Keyboard", variable=self.input_type, value="keyboard")
        self.radio_keyboard.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        self.button_solve = tk.Button(self.root, text="Solve", command=self.solve)
        self.button_solve.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.label_output = tk.Label(self.root, text="")
        self.label_output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def solve(self):
        input_type = self.input_type.get()
        if input_type == "file":
            filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if filename:
                self.solve_from_file(filename)
        elif input_type == "keyboard":
            self.solve_from_keyboard()

    def solve_from_file(self, filename):
        try:
            start_time = time.time()
            buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards = self.read_file(filename)
            cari_sequences, cari_coordinates = self.all_sequences(matrix, buffer_size)
            total_hadiah = self.hadiah(cari_sequences, sequences, sequence_rewards)
            bobot_hadiah_max = self.max_array(total_hadiah)
            index = self.find_index(total_hadiah, bobot_hadiah_max)
            execution_time = time.time() - start_time

            self.display_result(bobot_hadiah_max, cari_sequences[index-1], cari_coordinates[index-1], execution_time)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def read_file(self, filename):
        with open(filename, 'r') as file:
            buffer_size = int(file.readline().strip())
            matrix_width, matrix_height = map(int, file.readline().split())
            matrix = [list(file.readline().split()) for _ in range(matrix_height)]
            number_of_sequences = int(file.readline().strip())
            sequences = []
            sequence_rewards = []

            for _ in range(number_of_sequences):
                sequences.append(file.readline().split())
                sequence_rewards.append(int(file.readline().strip()))

        return buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards

    def all_sequences(self, matrix, buffer_size):
        def is_valid_move(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in visited

        def explore(row, col, buffer_index, is_vertical):
            visited.add((row, col))
            current_token.append(matrix[row][col]) 
            current_coordinate.append((col+1, row+1))
            if buffer_index == buffer_size - 1:
                coordinates.append(current_coordinate[:])
                sequences.append(current_token[:])
            else:
                directions = [(1, 0), (-1, 0)] if is_vertical else [(0, 1), (0, -1)]
                for dr, dc in directions:
                    new_row, new_col = row, col
                    for _ in range(buffer_size - buffer_index):
                        new_row, new_col = new_row + dr, new_col + dc
                        if is_valid_move(new_row, new_col):
                            explore(new_row, new_col, buffer_index + 1, not is_vertical)

            visited.remove((row, col))
            current_token.pop()
            current_coordinate.pop()

        sequences = []
        coordinates = []
        current_coordinate = []
        current_token = []
        visited = set()
        for col_index in range(len(matrix[0])):
            explore(0, col_index, 0, True)
        return sequences, coordinates

    def hadiah(self, matrix, sequences, sequence_rewards):
        total_rewards = []

        for array in matrix:
            total_reward = 0
            for i in range(len(sequences)):
                sequence = sequences[i]
                reward = sequence_rewards[i]

                array_string = ' '.join(array)
                sequence_string = ' '.join(sequence)

                if sequence_string in array_string:
                    total_reward += reward

            total_rewards.append(total_reward)

        return total_rewards

    def max_array(self, array):
        max_val = array[0]
        for val in array:
            if val > max_val:
                max_val = val
        return max_val

    def find_index(self, array, value):
        for i, val in enumerate(array):
            if val == value:
                return i + 1
        return -1

    def display_result(self, bobot_hadiah_max, cari_sequences, cari_coordinates, execution_time):
        result_text = f"Bobot Hadiah: {bobot_hadiah_max}\n"
        result_text += "Sekuens: " + ' '.join(cari_sequences) + "\n"
        result_text += "Koordinat:\n" + '\n'.join(map(str, cari_coordinates)) + "\n"
        result_text += f"Waktu eksekusi: {execution_time*1000} ms"
        self.label_output.config(text=result_text)

    def create_widgets(self):
        self.label_intro = tk.Label(self.root, text="Welcome to Cyberpunk 2077 Breach Protocol Solver", font=("Helvetica", 16))
        self.label_intro.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.label_input_type = tk.Label(self.root, text="Input Type:")
        self.label_input_type.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.input_type = tk.StringVar()
        self.input_type.set("file")
        self.radio_file = tk.Radiobutton(self.root, text="File (.txt)", variable=self.input_type, value="file", command=self.toggle_widgets)
        self.radio_file.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.radio_keyboard = tk.Radiobutton(self.root, text="Keyboard", variable=self.input_type, value="keyboard", command=self.toggle_widgets)
        self.radio_keyboard.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        # Input Section
        self.input_frame = tk.LabelFrame(self.root, text="Input Data")
        self.input_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.widgets_for_keyboard_input = []
        self.labels = ["Unique Tokens:", "Tokens (Separated by space):", "Buffer Size:", "Matrix Size (Width x Height):", "Number of Sequences:", "Max Tokens per Sequence:"]
        for i, label_text in enumerate(self.labels):
            label = tk.Label(self.input_frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self.input_frame)
            entry.grid(row=i, column=1, columnspan=2, padx=10, pady=5, sticky="we")
            self.widgets_for_keyboard_input.append(entry)

        # Solve Button
        self.button_solve = tk.Button(self.root, text="Solve", command=self.solve)
        self.button_solve.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        # Output Section
        self.output_frame = tk.LabelFrame(self.root, text="Output")
        self.output_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.label_output = tk.Label(self.output_frame, text="")
        self.label_output.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Toggle Widgets
        self.toggle_widgets()

    def toggle_widgets(self):
        # Hide input data widgets by default
        self.input_frame.grid_remove()

        # Show input data widgets if "Keyboard" radio button is selected
        if self.input_type.get() == "keyboard":
            self.input_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="we")


    def solve_from_keyboard(self):
        try:
            # Gather inputs
            jumlah_token_unik = int(self.widgets_for_keyboard_input[0].get())
            tokens = self.widgets_for_keyboard_input[1].get().split()
            buffer_size = int(self.widgets_for_keyboard_input[2].get())
            matrix_size_str = self.widgets_for_keyboard_input[3].get().split("x")
            matrix_width = int(matrix_size_str[0].strip())
            matrix_height = int(matrix_size_str[1].strip())
            number_of_sequences = int(self.widgets_for_keyboard_input[4].get())
            sequence_max = int(self.widgets_for_keyboard_input[5].get())

            # Randomize matrix elements
            matrix = [['' for _ in range(matrix_width)] for _ in range(matrix_height)]
            for j in range(matrix_height):
                for k in range(matrix_width):
                    matrix[j][k] = random.choice(tokens)

            sequences = []
            sequence_rewards = []
            for _ in range(number_of_sequences):
                # Randomize sequence elements
                sequence = random.sample(tokens, min(sequence_max, len(tokens)))
                sequences.append(sequence)
                sequence_rewards.append(random.randint(8, 80))

            # Find all sequences in the matrix
            start_time = time.time()
            all_sequences, all_coordinates = self.all_sequences(matrix, buffer_size)

            # Calculate rewards for each sequence
            total_rewards = self.hadiah(all_sequences, sequences, sequence_rewards)

            # Find the sequence with the maximum total reward
            max_reward_index = total_rewards.index(max(total_rewards))
            execution_time = time.time() - start_time

            # Display the optimal sequence along with its coordinates and total reward
            result_text = f"Bobot Hadiah: {total_rewards[max_reward_index]}\n"
            result_text += f"Sekuens: {' '.join(all_sequences[max_reward_index])}\n"
            result_text += "Koordinat:\n"
            coordinates = all_coordinates[max_reward_index]
            for coord in coordinates:
                result_text += f"{coord}\n"
            result_text += f"Waktu eksekusi: {execution_time*1000} ms"

            self.label_output.config(text=result_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = BreachProtocolSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
