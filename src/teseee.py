def all_sequences(matrix, buffer_size):
    def is_valid_move(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in visited

    def explore(row, col, buffer_index, is_vertical):
        visited.add((row, col))
        current_token.append(matrix[row][col])
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
    for col_index in range(len(matrix[0])):
        explore(0, col_index, 0, True)  # Start from each column index on the first row
    return sequences

matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']   
]
buffer_size = 7
print(all_sequences(matrix, buffer_size))
