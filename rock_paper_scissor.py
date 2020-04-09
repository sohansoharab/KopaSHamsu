import random

print("\nWelcome to the rock paper scissors game!\n")

condition = True
#declaration
while condition == True:
	print("\nEnter\n'1' for Rock\n'2' for Paper\n'3' for Scissors\n")

	print("How do you want to play?\n1) Play with computer\n2) Play with a friend here beside you\n")
	plyr_choice = int(input("\nInput the option number: "))

	if plyr_choice == 1:
		pc = 0
		human = 0
		amount_game = int(input("\nHow many match do you want to play?\n:"))
		i = 1
		while i <= amount_game:
			print(f"\n####----------Game number #{i}----------####\n")
			i = i+1
			manual_choice = int(input("\nPut your choice\n:"))
			pc_choice = random.randint(1,3)

			if manual_choice == 1:
				print("\nHuman: Rock\n")
			elif manual_choice == 2:
				print("\nHuman: Paper\n")
			elif manual_choice == 3:
				print("\nHuman: Scissors\n")
			else:
				print("\nInvalid input!!!\n")
			
			if pc_choice == 1:
				print("\nPC: Rock\n")
			elif pc_choice == 2:
				print("\nPC: Paper\n")
			elif pc_choice == 3:
				print("\nPC: Scissors\n")

			if manual_choice == pc_choice:
				print("\n**Match tied**\n")
			elif manual_choice == 1 and pc_choice == 2:
				print("\nPC Wins!\n")
				pc = pc+1
			elif manual_choice == 1 and pc_choice == 3:
				print("\nHuman Wins!\n")
				human = human+1
			elif manual_choice == 2 and pc_choice == 3:
				print("\nPC Wins!\n")
				pc = pc+1
			elif manual_choice == 2 and pc_choice == 1:
				print("\nHuman Wins!\n")
				human = human+1
			elif manual_choice == 3 and pc_choice == 1:
				print("\nPC Wins!\n")
				pc = pc+1
			elif manual_choice == 3 and pc_choice == 2:
				print("\nHuman Wins!\n")
				human = human+1
		if pc > human:
			print("\nUltimately PC won!\n")
		elif pc < human:
			print("\nCongratulations! You won!\n")
		else:
			print("\nOh no it is a tie!\n")
	elif plyr_choice == 2:
		frnd_1_name = input("\nPlease Enter Your Name Friend 1:\n")
		frnd_2_name = input("\nPlease Enter Your Name Friend 2:\n")
		frnd_1 = 0
		frnd_2 = 0
		amount_game = int(input("\nHow many match do you want to play?\n:"))
		j = 1
		while j <= amount_game:
			print(f"\n####----------Game number #{j}----------####\n")
			j = j+1
			frnd_1_choice = int(input(f"\nPut your choice {frnd_1_name}\n:"))
			frnd_2_choice = int(input(f"\nPut your choice {frnd_2_name}\n:"))
			if frnd_1_choice == 1:
				print(f"\n{frnd_1_name}: Rock\n")
			elif frnd_1_choice == 2:
				print(f"\n{frnd_1_name}: Paper\n")
			elif frnd_1_choice == 3:
				print(f"\n{frnd_1_name}: Scissors\n")
			else:
				print("Invalid input!!!\n") 
			
			if frnd_2_choice == 1:
				print(f"\n{frnd_2_name}: Rock\n")
			elif frnd_2_choice == 2:
				print(f"\n{frnd_2_name}: Paper\n")
			elif frnd_2_choice == 3:
				print(f"\n{frnd_2_name}: Scissors\n")
			else:
				print("\ninvalid\n")

			if frnd_1_choice == frnd_2_choice:
				print(f"\n**Match tied**\n")
			elif frnd_1_choice == 1 and frnd_2_choice == 2:
				print(f"\n{frnd_2_name} Wins!\n")
				frnd_2 = frnd_2 + 1  
			elif frnd_1_choice == 1 and frnd_2_choice == 3:
				print(f"\n{frnd_1_name} Wins!\n") 
				frnd_1 = frnd_1 + 1
			elif frnd_1_choice == 2 and frnd_2_choice == 3:
				print(f"\n{frnd_2_name} Wins!\n")
				frnd_2 =frnd_2 + 1
			elif frnd_1_choice == 2 and frnd_2_choice == 1:
				print(f"\n{frnd_1_name} Wins!\n")
				frnd_1 = frnd_1 + 1
			elif frnd_1_choice == 3 and frnd_2_choice == 1:
				print(f"\n{frnd_2_name} Wins!\n")
				frnd_2 =frnd_2 + 1
			elif frnd_1_choice == 3 and frnd_2_choice == 2:
				print(f"\n{frnd_1_name} Wins!\n")
				frnd_1 = frnd_1 + 1
		if frnd_2 > frnd_1:
			print(f"\n\nCongratulations! {frnd_2_name} won!\n\n")
		elif frnd_2 < frnd_1:
			print(f"\n\nCongratulations! {frnd_1_name} won!\n\n")
		else:
			print("\n\nOh no it is a tie!\n\n")
	else:
		print("\ninvalid option!\n") 
	do_u_want_more = input("\nIf you want to play more type 'y'\notherwise type 'n'\n")
	if do_u_want_more == 'y':
		print("\nOkay let's play again!")
		condition = True
	elif do_u_want_more == 'n':
		condition = False
		break
	else:
		print("\ninvalid command\n")