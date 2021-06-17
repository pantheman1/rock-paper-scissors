print('Rock...r')
print('Paper...p')
print('Scissors...s')

player1 = input("Player 1, make your move:\n").lower()
print("Don't look!!\n" * 20)
player2 = input("Player 2, make your move:\n").lower()

if player1 == player2:
	print(f"Tie! You both chose {player1}.")
	player1 = input("Make another choice--r, p, or s\n")
	print("Don't look!!\n" * 20)
	player2 = input("Make another choice--r, p, or s\n")
elif player1 == 'r' and player2 == 'p' or player1 == 'p' and player2 == 's' or player1 == 's' and player2 == 'r':
	print(f'Player2 wins! {player1} loses to {player2}')
elif player1 == 'r' and player2 == 's' or player1 == 'p' and player2 == 'r' or player1 == 's' and player2 == 'p':
	print(f'Player1 wins! {player1} always beats {player2}')
else:
	print("something went wrong.")