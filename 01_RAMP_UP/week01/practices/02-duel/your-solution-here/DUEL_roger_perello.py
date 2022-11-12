gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalf_wins = 0
saruman_wins = 0


for mage_index in range(len(gandalf)):
    if gandalf[mage_index] > saruman[mage_index]:
        gandalf_wins += 1
    else:
        saruman_wins += 1


if gandalf_wins > saruman_wins:
    print(f"Gana Gandalf {gandalf_wins} a {saruman_wins}.")
elif saruman_wins > gandalf_wins:
    print(f"Gana Saruman {saruman_wins} a {gandalf_wins}.") 
else:
    print(f"Hay un empate a {gandalf_wins}.")
