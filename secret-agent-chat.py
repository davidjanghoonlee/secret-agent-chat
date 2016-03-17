from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_opt (sheets, length):
	for sheet in range(sheets):
		with open ("opt" + str(sheet) + ".txt","w") as f:
			for i in range(length):
				f.write(str(randint(0,26)) + "\n")


def load_sheet(filename):
        with open(filename, "r") as f:
                contents = f.read().splitlines()
        return contents

def get_plain_text():
        plain_text = input('Please type your message')
        return plain_text.lower()

def load_file(filename):
        with open(filename, "r") as f:
                contents = f.read()
        return contents

def save_file(filename, data):
        with open(filename, 'we') as f:
                f.write(data)
