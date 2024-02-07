def all_sequences(matrix, buffer_size):
    def is_valid_move(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in visited

    def explore(row, col, buffer_index, is_vertical):
        visited.add((row, col))
        current_token.append(matrix[row][col])  # append token ke current_token
        if buffer_index == buffer_size - 1:
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

    sequences = []
    current_token = []
    visited = set()
    explore(0, 0, 0, True)  # mulai lagi secara vertikal
    return sequences

def write_sequences_to_file(sequences, filename):
    with open(filename, 'w') as file:
        for seq in sequences:
            for elem in seq:
                file.write(str(elem) + ' ')
            file.write('\n')

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
buffer_size = 4

sequences = all_sequences(matrix, buffer_size)
for seq in sequences:
    print(seq)

write_sequences_to_file(sequences, 'output2.txt')