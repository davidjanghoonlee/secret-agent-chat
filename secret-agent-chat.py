from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_opt (sheets, length):
	for sheet in range(sheets):
		with open ("opt" + str(sheet) + ".txt","w") as f: