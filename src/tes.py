def check_sequences_in_array(sequences, sequence_rewards, array):
    total_reward = 0

    for i in range(len(sequences)):
        sequence = sequences[i]
        reward = sequence_rewards[i]
        
        if all(item in array for item in sequence):
            total_reward += reward

    return total_reward

sequences = [['BD', 'E9', '1C'], ['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55']]
sequence_rewards = [15, 20, 30]
array = ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55']

total_reward = check_sequences_in_array(sequences, sequence_rewards, array)
print("Total reward:", total_reward)
