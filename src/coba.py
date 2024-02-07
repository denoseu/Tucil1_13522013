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

sequences = [['BD', 'E9', '1C'], ['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55']]
sequence_rewards = [15, 20, 30]
matrix = [
    ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55'],
    ['BD', '7A', 'BD', 'BD', '1C', 'BD', '55'],
    ['7A', '55', '7A', '1C', 'E9', '55', 'BD'],
    ['7A','BD', '1C', '55', '7A', 'BD', '55']
]

total_rewards = hadiah(matrix, sequences, sequence_rewards)
print("hadiah tiap sequence:", total_rewards)
