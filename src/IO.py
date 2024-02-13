import random, os

#*** read file txt ***#
def read_file(filename):
    relative_path = ""
    
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(os.path.dirname(current_directory))

    full_path = os.path.join(parent_directory, relative_path, filename)
    
    print(full_path)

    with open(full_path, 'r') as file:
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

#*** read from keyboard ***#
def keyboard_input():
    jumlah_token_unik = input("Jumlah token unik: ")
    token_input = input("Masukkan token: ")
    token = token_input.split()

    buffer_size = int(input("Ukuran buffer: "))

    ukuran_matriks = input("Ukuran matriks: ")
    col_mtx, row_mtx = ukuran_matriks.split()
    matrix_width = int(col_mtx)
    matrix_height = int(row_mtx)

    matrix = [['' for i in range(matrix_width)] for j in range(matrix_height)]
    for j in range (matrix_height):
        for k in range (matrix_width):
            matrix[j][k] = random.choice(token)

    number_of_sequences = int(input("Jumlah sekuens: "))
    ukuran_maksimal_sekuens = int(input("Ukuran maksimal sekuens: "))

    sequences = []
    for a in range(int(number_of_sequences)):
        ukuran = random.randint(2, int(ukuran_maksimal_sekuens))
        sequence = []
        for b in range(ukuran):
            sequence.append(random.choice(token))
        sequences.append(sequence)

    sequence_rewards = []
    for c in range(int(number_of_sequences)):
        sequence_rewards.append(random.randint(8, 80))

    return jumlah_token_unik, token, buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, ukuran_maksimal_sekuens, sequences, sequence_rewards

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
        file.write("Waktu eksekusi: " + str(execution_time) + " ms\n")
        file.write("#*************************************************# \n")
    return filename

#*** write file solusi ketika bobot hadiah = 0 ***#
def write_no_solusi(bobot_hadiah_max, execution_time):
    filename = input("Masukkan nama file solusi: ")
    with open('test/' + filename + '.txt', 'w') as file:
        file.write("#**** Cyberpunk 2077 Breach Protocol Solution ****# \n")
        file.write("Bobot Hadiah: " + str(bobot_hadiah_max) + '\n')
        file.write("Tidak ada sekuens yang memenuhi. \n")
        file.write("Waktu eksekusi: " + str(execution_time) + " ms\n")
        file.write("#*************************************************# \n")
    return filename