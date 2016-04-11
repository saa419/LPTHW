print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Testing doing math on input
age = int(age)
agem = age*12
agem2 = agem+12
print "You're also between %r and %r months old! Whoa." % (agem,agem2)