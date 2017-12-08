if __name__ == '__main__':

	output = 'machine_language.txt'
	filename = 'googlebooks-eng-all-2gram-20120701-ma'

	write_file = open(output, 'w')

	with open(filename, 'r') as file:
		for idx, line in enumerate(file):
			line = line.lower()

			if 'machine' in line and 'language' in line:
				write_file.write(line)

	write_file.close()
