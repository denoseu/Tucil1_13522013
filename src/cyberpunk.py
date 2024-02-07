import time

#*** read file txt ***#
def read_file(filename):
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

#*** cari semua sequences ***#
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

#*** write array of array ke file txt ***#
def write_to_file(sequences, filename):
    with open(filename, 'w') as file:
        for seq in sequences:
            for elem in seq:
                file.write(str(elem) + ' ')
            file.write('\n')

#*** write array ke file txt ***#
def write_array(sequences, filename):
    with open(filename, 'w') as file:
        for seq in sequences:
            file.write(str(seq) + ' ')
            file.write('\n')

#*** hadiah tiap sequences ***#
def hadiah(matrix, sequences, sequence_rewards):
    total_rewards = []

    for array in matrix:
        total_reward = 0
        for i in range(len(sequences)):
            sequence = sequences[i]
            reward = sequence_rewards[i]

            # Mengubah array menjadi string untuk mempermudah pencarian urutan
            array_string = ' '.join(array)
            sequence_string = ' '.join(sequence)

            # Melakukan pencarian urutan dalam string
            if sequence_string in array_string:
                total_reward += reward

        total_rewards.append(total_reward)

    return total_rewards

#*** mencari nilai maksimum dalam suatu array ***#
def max_array(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

#*** find index ***#
def find_index(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i+1
    return -1

#*** MAIN ***#
filename = "input.txt"
buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, sequence_rewards = read_file(filename)

start = time.time()

cari_sequences, cari_coordinates = all_sequences(matrix, buffer_size)
# for seq in cari_sequences:
#     print(seq)

total_hadiah = hadiah(cari_sequences, sequences, sequence_rewards)
# print("hadiah tiap sequence:", total_hadiah)

bobot_hadiah_max = max_array(total_hadiah)
print("Bobot Hadiah:", bobot_hadiah_max)

index = find_index(total_hadiah, bobot_hadiah_max)
# print("index:", index)

end = time.time()
execution_time = ((end - start)*1000)

write_to_file(cari_coordinates, 'output_coordinate.txt')
write_to_file(cari_sequences, 'output.txt')
write_array(total_hadiah, 'output2.txt')


if bobot_hadiah_max != 0:
    print("Sekuens: ", end='')
    for token in cari_sequences[index-1]:
        print(token, end=' ')
    # print(cari_sequences[index-1])

    print()
    print("Koordinat: ")
    for coordinates in cari_coordinates[index-1]:
        print(coordinates, end='\n')
    # print(cari_coordinates[index-1])
        
    print("Waktu eksekusi:", execution_time, "ms")

    hasil = input("Apakah ingin menyimpan solusi? (y/n) ")
    if hasil == 'y':
        with open('solusi.txt', 'w') as file:
            file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
            file.write("Bobot Hadiah: " + str(bobot_hadiah_max) + '\n')
            file.write("Sekuens: ")
            for token in cari_sequences[index-1]:
                file.write(token + ' ')
            file.write('\n')
            file.write("Koordinat: \n")
            for coordinates in cari_coordinates[index-1]:
                file.write(str(coordinates) + '\n')
            file.write("Waktu eksekusi: " + str(execution_time) + " ms")
        print("Solusi telah disimpan dalam file solusi.txt!")
else:
    hasil = input("Apakah ingin menyimpan solusi? (y/n) ")
    if hasil == 'y':
        with open('solusi.txt', 'w') as file:
            file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
            file.write("Bobot Hadiah: " + str(bobot_hadiah_max) + '\n')
            file.write("Tidak ada sekuens yang memenuhi. \n")
            file.write("Waktu eksekusi: " + str(execution_time) + " ms")
        print("Solusi telah disimpan dalam file solusi.txt!")