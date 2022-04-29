# a game of rock, paper, scissors
# the computer will randomly choose rock, paper, or scissors
# the player will then choose rock, paper, or scissors
# the winner is determined by the rules of rock, paper, scissors
# rock beats scissors
# paper beats rock
# scissors beats paper
# if the player and the computer choose the same thing, it's a tie
# if the player beats the computer, they win
# if the computer beats the player, the computer wins
# if someone wins, the game will restart
# the game work in the loop until the player or the computer wins 3 times 
# if the player or the computer wins 3 times, the game will end
# if the player play always the same thing, computer will play to beat the player

import random

player_choice = ""
computer_choice = ""
rock_number = 0
paper_number = 0
scissors_number = 0
player_choices = []
computer_choices = []
computer_random_move = []
win_number = 0
defeat_number = 0

# functions

def get_last_move() -> str:
	global player_choices
	global computer_random_move

	for i in range(len(player_choices) - 1, -1, -1):
		if player_choices[i] != player_choices[len(player_choices) - 1]:
			if player_choices[i] == "r" and player_choices[len(player_choices) - 1] == "p" or player_choices[i] == "p" and player_choices[len(player_choices) - 1] == "r":
				computer_random_move += [False]
				return "s"
			elif player_choices[i] == "r" and player_choices[len(player_choices) - 1] == "s" or player_choices[i] == "s" and player_choices[len(player_choices) - 1] == "r":
				computer_random_move += [False]
				return "p"
			elif player_choices[i] == "p" and player_choices[len(player_choices) - 1] == "s" or player_choices[i] == "s" and player_choices[len(player_choices) - 1] == "p":
				computer_random_move += [False]
				return "r"
	
	computer_random_move += [True]
	return random.choice(["r", "p", "s"])

def get_best_move() -> str:
	global rock_number
	global paper_number
	global scissors_number
	global player_choices
	global computer_random_move

	player_choices_temp = player_choices

	# player_choices is limited to 5

	while len(player_choices_temp) > 5:
		player_choices_temp.pop(0)

	# check 5 least used moves (player_choices)
	# if 3/5 moves are same, computer will beat the player

	if len(player_choices_temp) >= 5:
		if player_choices_temp.count("r") >= 3: # like [r, r, r, p, p] => computer plays p
			computer_random_move += [False]
			return "p"
		elif player_choices_temp.count("p") >= 3: # like [r, p, r, p, p] => computer plays s
			computer_random_move += [False]
			return "s"
		elif player_choices_temp.count("s") >= 3: # like [r, s, s, p, s] => computer plays r
			computer_random_move += [False]
			return "r"
		else:
			computer_random_move += [None]
			lst = ["", ""]
			lstIndex = 0
			if player_choices_temp.count("r") >= 2:
				lst[lstIndex] = "r"
				lstIndex += 1
			if player_choices_temp.count("p") >= 2:
				lst[lstIndex] = "p"
				lstIndex += 1
			if player_choices_temp.count("s") >= 2:
				lst[lstIndex] = "s"
				lstIndex += 1
			if lstIndex > 2:
				print("Error: in get_best_move(), after the while loop, lstIndex is greater than 1.")
				print("Please report this bug to the developer. (https://github.com/LAPCoder/Rock-Paper-Scissors)")
			return random.choice(lst)

	else:

		# check all players choices

		if rock_number > paper_number and rock_number > scissors_number: # r > p > s => player play r => computer play p
			computer_random_move += [False]
			return "p"
		elif paper_number > rock_number and paper_number > scissors_number: # p > r > s => player play p => computer play s
			computer_random_move += [False]
			return "s"
		elif scissors_number > rock_number and scissors_number > paper_number: # s > r > p => player play s => computer play r
			computer_random_move += [False]
			return "r"
		elif rock_number == paper_number and rock_number > scissors_number: # r = p > s => player play r or p => computer play p or s
			computer_random_move += [None]
			return random.choice(["p", "s"])
		elif rock_number == scissors_number and rock_number > paper_number: # r = s > p => player play r or s => computer play p or r
			computer_random_move += [None]
			return random.choice(["p", "r"])
		elif paper_number == scissors_number and paper_number > rock_number: # p = s > r => player play p or s => computer play r or s
			computer_random_move += [None]
			return random.choice(["r", "s"])
		else: # r = p = s => player play r or p or s => computer play r or p or s
			return get_last_move()
	
	print("\nError: BigBug")
	computer_random_move += [True]
	return random.choice(["r", "s", "p"])

def get_game_part() -> str:
	# When the game ends and the player win,
	# the game will ask if the player want to get
	# the game part (all choices of the player and the computer)
	# example: [[r, p, false], [p, s, none], [r, s, true]]
	#            *  *  ~~~~~
	#            |  |  |
	#            |  |  computer play a random move? none: beetween two moves
	#            |  computer choice
	#            player choice

	global player_choices
	global computer_choices
	global computer_random_move

	game_part = []

	for i in range(len(player_choices)):
		game_part += [[player_choices[i], computer_choices[i], computer_random_move[i]]]

	return game_part

def loop() -> None:
	global player_choice
	global computer_choice
	global win_number
	global defeat_number
	global rock_number
	global paper_number
	global scissors_number
	global player_choices
	global computer_choices

	# check if player wins
	if win_number >= 3:
		print("You win!")
		if input("\nDo you want to get the game data? (y/n)\n\n\
It's useful to know the history of the game, because you can help me to improve the game.\n\n\
To get the game data and help me to improve the game, you have to type 'y' and press enter.\n\
After that, you will get the game data.\n\
You can go on GitHub (https://github.com/LAPCoder/Rock-Paper-Scissors) and post your game data.\n\n\
If you don't want to get the game data, you have to type 'n' and press enter. => ").lower() == "y":
			print("Game part:")
			print(get_game_part())
			print("Thank you for your help!")
		return
	
	# check if computer wins
	if defeat_number >= 3:
		print("You lose!")
		return

	# computer input
	computer_choice = get_best_move()

	# player input
	player_choice = input("\nRock, paper, or scissors? (r/p/s) ").lower()
	if player_choice == "r":
		rock_number += 1
	elif player_choice == "p":
		paper_number += 1
	elif player_choice == "s":
		scissors_number += 1
	else:
		print("Invalid input!")
		loop()
	
	player_choices += [player_choice]
	computer_choices += [computer_choice]
	
	# print computer choice
	try:
		print("\nComputer chooses " + computer_choice)
	except TypeError:
		print("\nWe found a bug! Please report it on GitHub (https://github.com/LAPCoder/Rock-Paper-Scissors).\nError: TypeError\n")
		print("Game part:", get_game_part())
		return
	except:
		print("\nWe found a bug! Please report it on GitHub (https://github.com/LAPCoder/Rock-Paper-Scissors).\nError: Unknown\n")
		print("Game part:", get_game_part())

	# compare input
	if player_choice == computer_choice:
		print("Tie!")
		loop()
	elif player_choice == "r" and computer_choice == "p":
		print("Computer wins!")
		defeat_number += 1
		loop()
	elif player_choice == "r" and computer_choice == "s":
		print("Player wins!")
		win_number += 1
		loop()
	elif player_choice == "p" and computer_choice == "r":
		print("Player wins!")
		win_number += 1
		loop()
	elif player_choice == "p" and computer_choice == "s":
		print("Computer wins!")
		defeat_number += 1
		loop()
	elif player_choice == "s" and computer_choice == "r":
		print("Computer wins!")
		defeat_number += 1
		loop()
	elif player_choice == "s" and computer_choice == "p":
		print("Player wins!")
		win_number += 1
		loop()
	else:
		print("Invalid input!")
		loop()

if __name__ == "__main__":
	print("\033[3J\033[2J\033[HWelcome to Rock, paper, scissors!")
	loop()
	print("\nThanks for playing!")
