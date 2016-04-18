#i = 0
#numbers = []

def whiloop(endnum, increm):
	i = 0
	numbers = []
	while i < endnum:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + increm
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers

endnum = int(raw_input("What number should we end on? "))
increm = int(raw_input("How much should we increment by? "))

numbers = whiloop(endnum, increm)

print "The numbers: "

for num in numbers:
	print num