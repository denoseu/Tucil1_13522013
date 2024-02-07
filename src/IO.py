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

#*** write file solusi ketika bobot hadiah != 0 ***#
def write_ada_solusi(index, cari_sequences, cari_coordinates, bobot_hadiah_max, execution_time):
    filename = input("Masukkan nama file solusi: ")
    with open('test/' + filename + '.txt', 'w') as file:
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
    return filename

#*** write file solusi ketika bobot hadiah = 0 ***#
def write_no_solusi(bobot_hadiah_max, execution_time):
    filename = input("Masukkan nama file solusi: ")
    with open('test/' + filename + '.txt', 'w') as file:
        file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
        file.write("Bobot Hadiah: " + str(bobot_hadiah_max) + '\n')
        file.write("Tidak ada sekuens yang memenuhi. \n")
        file.write("Waktu eksekusi: " + str(execution_time) + " ms")
    return filename