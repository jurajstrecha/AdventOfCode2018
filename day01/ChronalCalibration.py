import sys

def compute(initial_frequency, changes_file):
	frequency = initial_frequency

	for line in changes_file:
		if line[0] == '+':
			frequency = frequency + int(line[1:])
		elif line[0] == '-':
			frequency = frequency - int(line[1:])
		else:
			print('Input value error: numbers should be preceeded by a \'+\' or \'-\' signs.')
	
	return frequency

def main():
	if len(sys.argv) == 3:
		initial_frequency = int(sys.argv[1])
		changes_file = open(sys.argv[2])
	else:
		initial_frequency = 0
		changes_file = open('input.csv')
	
	result = compute(initial_frequency, changes_file)
	print(result)

if __name__ == "__main__":
	main()
