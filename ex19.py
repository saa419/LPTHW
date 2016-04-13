# Defines the cheese_and_crackers function, which takes two arguments: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	# prints the # of cheeses based on cheese_count
	print "You have %d cheeses!" % cheese_count
	# prints the # of boxes of crackers based on boxes_of_crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# prints a few additional lines
	print "Man that's enough for a party!"
	print "Get a blanket!\n"

print "We can just give the function numbers directly:"
# Runs the cheese_and_crackers function with 20 as the # of cheeses and 30 as the # of boxes of crackers
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# sets two variables with the # of cheeses and the # of boxes of crackers
amount_of_cheese = 10
amount_of_crackers = 50

# Runs the cheese_and_crackers function with the two variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# Does math with the function arguments, then runs it
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# Variables and math!
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def randfunction(first,last):
	print "My name is %s %s!" % (first,last)

randfunction("Santiago","Andujar")
randfunction("Batman","man")
randfunction(50,"cent")

def squarefunction(number):
	print "The square of %d is %d!" % (number, number**2)

squarefunction(1)
squarefunction(2)
squarefunction(3)

# Create a while loop to run the squaring function from i to stopnum. In this case, 1-12
stopnum = 12
i=1
while i<=stopnum:
	squarefunction(i)
	i = i + 1

# Create a while loop to run the squaring function from j to stopnumb. Ask for user input for the starting and ending numbers
print "What number should we start with?"
j = int(raw_input("> "))
print "What number should we end with?"
stopnumb = int(raw_input("> "))
while j<=stopnumb:
	squarefunction(j)
	j = j + 1