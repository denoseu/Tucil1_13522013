import time
from IO import read_file, write_to_file, write_array, write_ada_solusi, write_no_solusi
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
filename = "input.txt"
buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards = read_file(filename)

start = time.time()

cari_sequences, cari_coordinates = all_sequences(matrix, buffer_size)

total_hadiah = hadiah(cari_sequences, sequences, sequence_rewards)
bobot_hadiah_max = max_array(total_hadiah)
print("Bobot Hadiah:", bobot_hadiah_max)

# mencari indeks dimana bobot hadiah maksimal ditemukan
index = find_index(total_hadiah, bobot_hadiah_max)

end = time.time()

execution_time = ((end - start)*1000)

write_to_file(cari_coordinates, 'output_coordinate.txt')
write_to_file(cari_sequences, 'output.txt')
write_array(total_hadiah, 'output2.txt')


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
        write_no_solusi(bobot_hadiah_max, execution_time)
        print("Solusi telah disimpan dalam file " + filename + ".txt!")