# import argv in order to accept arguments from a file
from sys import argv

# Define the arguments: first is the script (default), then the second argument is the input file name
script, input_file = argv

#define the print_all function. This takes an argument "f"
def print_all(f):
	# The print_all function consists of reading the file and printing all the lines
	print f.read()

#define the rewind function. This also takes an argument "f"
def rewind(f):
	# seeks to the specified position. This brings the position back to the beginning of the file (0)
	f.seek(0)

#define the print_a_line function, with 2 arguments: the line to print and the file
def print_a_line(line_count, f):
	# Prints the specified line count and line
	print line_count, f.readline(), # added a comma at end so as to not print the extra line break

# Put the act of opening the input_file into current_file
current_file = open(input_file)

# Prints the intro line
print "First let's print the whole file:\n"

# Passes the input file (via current_file) to the print_all function in order to print the contents of the file
print_all(current_file)

# Prints the next line saying what it's going to do
print "Now let's rewind, kind of like a tape."

# Passes the input file (via current_file) to the rewind function in order to bring the position back to the beginning of the file
rewind(current_file)

# Next instruction
print "Let's print three lines:"

# Just a number showing which line is the current one
current_line = 1
# prints the line count and the line
print_a_line(current_line, current_file)

# Adds 1 to the line count, so makes it 2
# current_line = current_line + 1
current_line += 1
# prints the line count and the next line
print_a_line(current_line, current_file)

# Adds 1 to the line count, so makes it 3
# current_line = current_line + 1
current_line += 1
# prints the line count and the next line
print_a_line(current_line, current_file)