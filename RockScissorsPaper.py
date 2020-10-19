from random import choice

print("Vítej ve hře KÁMEN-NŮŽKY-PAPÍR")
print("Napiš vždy jedno ze tří slov")
print("Hru ukončíš prázdným řádkem - enter")
print()

while True:
	getAlTurn = choice(("kámen","nůžky","papír"))

	while True:
		getUserTurn = input("kámen | nůžky | papír: ")
		if getUserTurn == "kámen" or getUserTurn == "nůžky" or getUserTurn == "papír" or getUserTurn == "":
			break

	if getUserTurn == "":
		print("Program bude ukončen")
		break
	elif getUserTurn == "kámen" and getAlTurn == "nůžky" or getUserTurn == "nůžky" and getAlTurn == "papír" or getUserTurn == "papír" and getAlTurn == "kámen":
		print("Člověk:", getUserTurn, "\nPC:", getAlTurn, "\nVýhra\n")
	elif getAlTurn == "kámen" and getUserTurn == "nůžky" or getAlTurn == "nůžky" and getUserTurn == "papír" or getAlTurn == "papír" and getUserTurn == "kámen":
		print("Člověk:", getUserTurn, "\nPC:", getAlTurn, "\nProhra\n")
	else:
		print("Člověk:", getUserTurn, "\nPC:", getAlTurn, "\nShoda\n")