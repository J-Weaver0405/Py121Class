    # ascii calculator
def input_word():

	while True:
		try:
			wd=input('Enter a word:\n').strip()
			break
		except ValueError:
			print("Enter a string!!, wrong value type")
	return wd

def ascii_calculator(n=1):

	all_words=[]
	while n:
		wd=input_word()
		n -= 1
		val=(wd, sum(ord(char) for char in wd))
		print(f"the ascii value of {val[0]} is { val[1]}")
		all_words.append(val)
	return all_words
if __name__ == '__main__':
	ascii_val=ascii_calculator()
	print(ascii_val)

	ascii_val=ascii_calculator(2)
	print(ascii_val)
