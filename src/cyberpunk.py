import time
from IO import read_file, keyboard_input, write_to_file, write_array, write_ada_solusi, write_no_solusi
from helper import max_array, find_index

#*** mencari semua sequence yang mungkin ***#
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
        explore(0, col_index, 0, True)  # mulai dari kolom index baris pertama
    return sequences, coordinates

#*** mencari bobot hadiah setiap sequences ***#
def hadiah(matrix, sequences, sequence_rewards):
    total_rewards = []

    for array in matrix:
        total_reward = 0
        for i in range(len(sequences)):
            sequence = sequences[i]
            reward = sequence_rewards[i]

            # mengubah array menjadi string
            array_string = ' '.join(array)
            sequence_string = ' '.join(sequence)

            if sequence_string in array_string:
                total_reward += reward

        total_rewards.append(total_reward)

    return total_rewards

#*** MAIN ***#
print("                                             Selamat datang di")
print("")
print("█▀▀ █▄█ █▄▄ █▀▀ █▀█ █▀█ █░█ █▄░█ █▄▀   ▀█ █▀█ ▀▀█ ▀▀█   █▄▄ █▀█ █▀▀ ▄▀█ █▀▀ █░█   █▀█ █▀█ █▀█ ▀█▀ █▀█ █▀▀ █▀█ █░░ █")
print("█▄▄ ░█░ █▄█ ██▄ █▀▄ █▀▀ █▄█ █░▀█ █░█   █▄ █▄█ ░░█ ░░█   █▄█ █▀▄ ██▄ █▀█ █▄▄ █▀█   █▀▀ █▀▄ █▄█ ░█░ █▄█ █▄▄ █▄█ █▄▄ ▄")
print("")
print("oleh Denise Felicia Tiowanni - 13522013")
print("")
print("Jenis masukan: ")
print("1. File (.txt)")
print("2. Keyboard")
input_type = input("Pilih jenis masukan (1/2): ")

if input_type == '1':
    filename = input("Masukkan nama file (.txt): ")
    buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards = read_file(filename)
else:
    jumlah_token_unik, token, buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, ukuran_maksimal_sekuens, sequences, sequence_rewards = keyboard_input()
    # print("Jumlah token unik:", jumlah_token_unik)
    # print("Token:", token)
    # print("Ukuran buffer:", buffer_size)
    # print("Matrix (height):", matrix_height)
    # print("Matrix (width):", matrix_width)
    print("Matrix: ")
    for i in range(matrix_height):
        for j in range(matrix_width):
            print(matrix[i][j], end=' ')
        print()
    print("Jumlah sekuens: ", number_of_sequences)

    for i in range((number_of_sequences)):
        sequence = sequences[i]
        print(sequence)
        print("Hadiah: ", sequence_rewards[i])

start = time.time()

cari_sequences, cari_coordinates = all_sequences(matrix, buffer_size)

total_hadiah = hadiah(cari_sequences, sequences, sequence_rewards)
bobot_hadiah_max = max_array(total_hadiah)
print("Bobot Hadiah:", bobot_hadiah_max)

# mencari indeks dimana bobot hadiah maksimal ditemukan
index = find_index(total_hadiah, bobot_hadiah_max)

end = time.time()

execution_time = round(((end - start)*1000), 2)

# write_to_file(cari_coordinates, 'output_coordinate.txt')
# write_to_file(cari_sequences, 'output.txt')
# write_array(total_hadiah, 'output2.txt')


if bobot_hadiah_max != 0:
    print("Sekuens: ", end='')
    for token in cari_sequences[index-1]:
        print(token, end=' ')

    print()
    print("Koordinat: ")
    for coordinates in cari_coordinates[index-1]:
        print(coordinates, end='\n')
        
    print("Waktu eksekusi:", execution_time, "ms")

    hasil = input("Apakah ingin menyimpan solusi? (y/n) ")
    if hasil == 'y':
        filename = write_ada_solusi(index, cari_sequences, cari_coordinates, bobot_hadiah_max, execution_time)
        print("Solusi telah disimpan dalam file " + filename + ".txt!")
else:
    hasil = input("Apakah ingin menyimpan solusi? (y/n) ")
    if hasil == 'y':
        filename = write_no_solusi(bobot_hadiah_max, execution_time)
        print("Solusi telah disimpan dalam file " + filename + ".txt!")