import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random, time, os

class GUI(tk.Tk):
    def max_array(array):
        max = array[0]
        for i in range(len(array)):
            if array[i] > max:
                max = array[i]
        return max

    def find_index(array, value):
        for i in range(len(array)):
            if array[i] == value:
                return i+1
        return -1

    def all_sequences(matrix, buffer_size):
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

    def hadiah(matrix, sequences, sequence_rewards):
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

    def calculate(self, buffer_value, matrix_width, matrix_height, matrix, no_of_sequences, sequences, sequence_rewards):
        start = time.time()
        cari_sequences, cari_coordinates = GUI.all_sequences(matrix, buffer_value)
        rewards = GUI.hadiah(cari_sequences, sequences, sequence_rewards)
        max_reward = GUI.max_array(rewards)
        index = GUI.find_index(rewards, max_reward)
        end = time.time()
        execution_time = end - start

        
        print("Matrix: ")
        for i in range(matrix_height):
            for j in range(matrix_width):
                print(matrix[i][j], end=' ')
            print()
        print("Jumlah sekuens: ", no_of_sequences)

        for i in range((no_of_sequences)):
            sequence = sequences[i]
            print(sequence)
            print("Hadiah: ", sequence_rewards[i])
            
        print("Bobot Hadiah:", max_reward)
        print("Sekuens: ", cari_sequences[index-1])
        print("Koordinat: ", cari_coordinates[index-1])
        print("Execution Time: ", execution_time*1000, "ms")
        
        self.result(matrix, cari_sequences, cari_coordinates, max_reward, index, execution_time)
        
        return matrix, cari_sequences, cari_coordinates, max_reward, index, execution_time

    def result(self, matrix, cari_sequences, cari_coordinates, max_reward, index, execution_time, event=None):
        self.canvas.delete("all")

        background_img = Image.open("src/assets/resultbg.png")
        background_img = background_img.resize((1500, 810))
        self.background_photo = ImageTk.PhotoImage(background_img)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        header_img = Image.open("src/assets/result_header.png")
        header_img = header_img.resize((1435, 260))
        self.header_photo = ImageTk.PhotoImage(header_img)
        self.canvas.create_image(0, 10, image=self.header_photo, anchor="nw")

        matrix_img = Image.open("src/assets/matrix.png")
        matrix_img = matrix_img.resize((600, 530))
        self.matrix_photo = ImageTk.PhotoImage(matrix_img)
        self.canvas.create_image(40, 210, image=self.matrix_photo, anchor="nw")

        cell_width = 230 / len(matrix[0])
        cell_height = 230 / len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x0 = 150 + j * cell_width
                y0 = 350 + i * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(matrix[i][j]))

        seq_result_img = Image.open("src/assets/seq_result.png")
        seq_result_img = seq_result_img.resize((600, 280))
        self.seq_result_photo = ImageTk.PhotoImage(seq_result_img)
        self.canvas.create_image(750, 180, image=self.seq_result_photo, anchor="nw")

        reward_result_img = Image.open("src/assets/reward_result.png")
        reward_result_img = reward_result_img.resize((250, 180))
        self.reward_result_photo = ImageTk.PhotoImage(reward_result_img)
        self.canvas.create_image(750, 470, image=self.reward_result_photo, anchor="nw")

        time_result_img = Image.open("src/assets/time_result.png")
        time_result_img = time_result_img.resize((250, 180))
        self.time_result_photo = ImageTk.PhotoImage(time_result_img)
        self.canvas.create_image(1080, 470, image=self.time_result_photo, anchor="nw")

        x_offset, y_offset = 1, 1 
        self.canvas.create_text(920 + x_offset, 380 + y_offset, text=cari_sequences[index-1], font=("Arial", 22), fill="#FFD11A")
        self.canvas.create_text(920, 380, text=cari_sequences[index-1], font=("Arial", 22), fill="#2C75D4")

        self.canvas.create_text(870 + x_offset, 590 + y_offset, text=max_reward, font=("Arial", 22), fill="#FFD11A")
        self.canvas.create_text(870, 590, text=max_reward, font=("Arial", 22), fill="#2C75D4")

        self.canvas.create_text(1200 + x_offset, 580 + y_offset, text=(round(execution_time*1000)), font=("Arial", 22), fill="#FFD11A")
        self.canvas.create_text(1200, 580, text=(round(execution_time*1000)), font=("Arial", 22), fill="#2C75D4")

        self.canvas.create_text(1200 + x_offset, 600 + y_offset, text="ms", font=("Arial", 22), fill="#FFD11A")
        self.canvas.create_text(1200, 600, text="ms", font=("Arial", 22), fill="#2C75D4")

        save_img = Image.open("src/assets/save.png")
        save_img = save_img.resize((300, 50))
        self.save_photo = ImageTk.PhotoImage(save_img)
        self.save_image = self.canvas.create_image(890, 680, image=self.save_photo, anchor="nw")
        self.canvas.tag_bind(self.save_image, "<Button-3>", self.save_input_clicked(matrix, cari_sequences, cari_coordinates, max_reward, index, execution_time))
    
    
    def save_input_clicked(self, matrix, cari_sequences, cari_coordinates, max_reward, index, execution_time, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        print(file_path)
        if file_path:
            if max_reward != 0:
                with open(file_path, 'w') as file:
                    file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
                    file.write("Bobot Hadiah: " + str(max_reward) + '\n')
                    file.write("Sekuens: ")
                    for token in cari_sequences[index-1]:
                        file.write(token + ' ')
                    file.write('\n')
                    file.write("Koordinat: \n")
                    for coordinates in cari_coordinates[index-1]:
                        file.write(str(coordinates) + '\n')
                    file.write("Waktu eksekusi: " + str(execution_time*1000) + " ms\n")
                    file.write("#*************************************************# \n")
            else:
                with open(file_path, 'w') as file:
                    file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
                    file.write("Bobot Hadiah: " + str(max_reward) + '\n')
                    file.write("Tidak ada sekuens yang memenuhi. \n")
                    file.write("Waktu eksekusi: " + str(execution_time*1000) + " ms\n")
                    file.write("#*************************************************# \n")
            print("File saved successfully:", file_path)
        else:
            print("Save operation cancelled.")
    
            
    def file_input_clicked(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            print("File selected:", file_name)
            with open(file_name, 'r') as file:
                buffer_size = int(file.readline().strip())
                matrix_width, matrix_height = map(int, file.readline().split())
                matrix = [list(file.readline().split()) for _ in range(matrix_height)]
                number_of_sequences = int(file.readline().strip())
                sequences = []
                sequence_rewards = []

                for _ in range(number_of_sequences):
                    sequences.append(file.readline().split())
                    sequence_rewards.append(int(file.readline().strip()))
                
                GUI.calculate(self, buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards)
       
        else:
            print("No file selected.")

    def keyboard_input_clicked(self, event=None):
        no_of_tokens = simpledialog.askstring("Input", "Jumlah token unik:")
        
        tokens = simpledialog.askstring("Input", "Token (ex: AA BB CC):")
        tokens = tokens.split()

        buffer_value = simpledialog.askstring("Input", "Ukuran buffer:")
        buffer_value = int(buffer_value)

        matrix_size = simpledialog.askstring("Input", "Ukuran matriks:")
        col_mtx, row_mtx = matrix_size.split()
        matrix_width = int(row_mtx)
        matrix_height = int(col_mtx)

        matrix = [['' for i in range(matrix_width)] for j in range(matrix_height)]
        for j in range (matrix_height):
            for k in range (matrix_width):
                matrix[j][k] = random.choice(tokens)
        
        no_of_sequences = simpledialog.askstring("Input", "Jumlah sekuens:")
        no_of_sequences = int(no_of_sequences)

        max_tokens_per_sequences = simpledialog.askstring("Input", "Ukuran maksimal sekuens:")
        max_tokens_per_sequences = int(max_tokens_per_sequences)

        sequences = []
        for a in range(int(no_of_sequences)):
            ukuran = random.randint(2, int(max_tokens_per_sequences))
            sequence = []
            for b in range(ukuran):
                sequence.append(random.choice(tokens))
            sequences.append(sequence)
        
        sequence_rewards = []
        for c in range(int(no_of_sequences)):
            sequence_rewards.append(random.randint(8, 80))
        
        GUI.calculate(self, buffer_value, matrix_width, matrix_height, matrix, no_of_sequences, sequences, sequence_rewards)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Cyberpunk 2077 Breach Protocol Solver")
        
        self.geometry("2560x1600")
        
        self.canvas = tk.Canvas(self, width=2560, height=1600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        background_img = Image.open("src/assets/homebg.png")
        background_img = background_img.resize((1500, 810))
        self.background_photo = ImageTk.PhotoImage(background_img)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        
        header_img = Image.open("src/assets/header.png")
        header_img = header_img.resize((1435, 325))
        self.header_photo = ImageTk.PhotoImage(header_img)
        self.canvas.create_image(0, 100, image=self.header_photo, anchor="nw")
        
        file_img = Image.open("src/assets/fileinput.png")
        file_img = file_img.resize((280, 130))
        self.file_photo = ImageTk.PhotoImage(file_img)
        self.file_image = self.canvas.create_image(350, 500, image=self.file_photo, anchor="nw")
        self.canvas.tag_bind(self.file_image, "<Button-1>", self.file_input_clicked)

        keyboard_img = Image.open("src/assets/keyboardinput.png")
        keyboard_img = keyboard_img.resize((280, 130))
        self.keyboard_photo = ImageTk.PhotoImage(keyboard_img)
        self.keyboard_image = self.canvas.create_image(800, 500, image=self.keyboard_photo, anchor="nw")
        self.canvas.tag_bind(self.keyboard_image, "<Button-1>", self.keyboard_input_clicked)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
