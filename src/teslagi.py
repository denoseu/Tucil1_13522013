def hadiah(matrix, sequences, sequence_rewards):
    total_rewards = []

    for array in matrix:
        total_reward = 0
        for i in range(len(sequences)):
            sequence = sequences[i]
            reward = sequence_rewards[i]

            # Penanda indeks untuk array dan sequence
            array_index = 0
            sequence_index = 0

            # Iterasi untuk memastikan setiap elemen dalam sequence berurutan dalam array
            while array_index < len(array) and sequence_index < len(sequence):
                if sequence[sequence_index] == array[array_index]:
                    sequence_index += 1
                array_index += 1

            # Jika semua elemen dalam sequence ditemukan secara berurutan dalam array
            if sequence_index == len(sequence):
                total_reward += reward

        total_rewards.append(total_reward)

    return total_rewards

sequences = [['BD', 'E9', '1C'], ['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55']]
sequence_rewards = [15, 20, 30]
matrix = [
    ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55'],
    ['BD', '7A', 'BD', 'BD', '1C', 'BD', '55'],
    ['7A', '55', '7A', '1C', 'E9', '55', 'BD']
]

total_rewards = hadiah(matrix, sequences, sequence_rewards)
print("hadiah tiap sequence:", total_rewards)
