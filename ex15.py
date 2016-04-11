# imports argv feature from sys module
from sys import argv

# Takes the first argument (the script name) and sets it to the script variable;
# takes the second argument (the filename we want to open) and sets it to the filename variable
script, filename = argv

# Sets the opening action to the txt variable
txt = open(filename)

# Prints "Here's your file" plus the name of the file
print "Here's your file %r:" % filename
# Prints the contents of the file by running the open command stored in the txt variable
print txt.read()

# Asks user to type the name of the file again
print "Type the filename again:"
# takes the user's input, writes the new filename into file_again variable
file_again = raw_input("> ")

# Sets the opening action of the new file to the txt_again variable
txt_again = open(file_again)
# Prints the contents of the file by running the open command stored in the txt_again variable
print txt_again.read()
# Close the files
txt.close()
txt_again.close()