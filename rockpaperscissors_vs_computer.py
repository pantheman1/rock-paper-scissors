from random import randint

play_again = "y"

while play_again == "y":
	times = int(input("How many games do you want to play out of?\n"))
	player_wins = 0
	comp_wins = 0
	while player_wins <= times / 2 and comp_wins <= times / 2 and player_wins + comp_wins < times:
		print(f"Player score: {player_wins}")
		print(f"Computer score: {comp_wins}")
		user_choice = input("(Enter your choice): r, p, or s\n").lower()

		def random_choice():
			choices = ['r', 'p', 's']
			rand = randint(0,2)
			return choices[rand]

		rand_choice = random_choice()

		if user_choice == rand_choice:
			print("It's a tie!")
		elif user_choice == 'r' and rand_choice == 'p' or user_choice == 'p' and rand_choice == 's' or user_choice == 's' and rand_choice == 'r':
			print(f"Computer plays: {rand_choice}")
			print(f'You lost! {user_choice} loses to {rand_choice}')
			comp_wins += 1
		elif user_choice == 'r' and rand_choice == 's' or user_choice == 'p' and rand_choice == 'r' or user_choice == 's' and rand_choice == 'p':
			print(f"Computer plays: {rand_choice}")
			print(f'You win! {user_choice} always beats {rand_choice}')
			player_wins += 1
	if player_wins > times / 2:
		print(f"You won the tournament with {player_wins} wins!")
	elif comp_wins > times / 2:
		print(f"Computer wins the tournament with {comp_wins} wins.")
	else:
		print(f"It's a tie...Player score: {player_wins}, Computer score: {comp_wins}")
	play_again = input("Play again? y/n\n")