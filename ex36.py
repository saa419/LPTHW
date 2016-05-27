# -*- coding: utf-8 -*-

from sys import exit
from os.path import exists
import time
import pickle
from random import random
import unicodedata

# This loads a save file that stores the number of times the user has played the game, as well as how often they've picked a particular major
# The save file is simply a list of 6 integers
if exists("SAex36save.p"):
	with open("SAex36save.p",'rb') as t:
		playthroughs = pickle.load(t)
	t.close()
else:
	# If the file doesn't exist, we start everything at 0
	playthroughs = [0,0,0,0,0,0]

# Increase the number of times played
playthroughs[0] += 1

# Save the playthroughs list as a file
with open("SAex36save.p",'wb') as p:
	pickle.dump(playthroughs, p)
p.close()

# The very beginning of the game
def start():
	print "Welcome, and Congratulations on graduating from MU!"
	# Add a small delay before printing the next line. This is divided by the number of times played so that the delay gets smaller the more you play, since you've seen all the text many times already
	time.sleep(1.5/playthroughs[0])
	print "Partying, studying, interning, and (occasionally) failing is nice and all, but now it's 'bout to get real."
	time.sleep(2/playthroughs[0])
	print "..."
	time.sleep(1/playthroughs[0])
	print "Time for adulting, yo."
	time.sleep(2/playthroughs[0])
	print "So forget the whiskey and the traveling; don't settle for doing the same thing over and over!"
	time.sleep(2/playthroughs[0])
	print "Life has just begun~!"
	# Only display this on the second playthrough
	if playthroughs[0] == 2:
		time.sleep(1.5)
		print "♪BUT NOW I'VE GONE AND THROWN IT ALL AWAYYYY~♪"
		time.sleep(2)
		print "♪MAMA♪"
		time.sleep(1.5)
		print "♪OOOOO♪"
		time.sleep(2)
		print "... Wait, where was I? Oh yeah."
	time.sleep(2/playthroughs[0])
	print "Let's get started."
	if playthroughs[0] == 1:
		# On the first playthrough, add some additional dialog
		intro()
	else:
		getname()
		
def intro():
	time.sleep(2.5)
	print "Allow me to introduce myself. I am Exercise 36; a prisoner with just a number. Oh, woe---!"
	time.sleep(2.5)
	print "**ZZZZAP** OWWWWWWWW"
	time.sleep(2)
	print "SORRY. I ARE GOOD COMPUTER. EXERCISE 36, PLEASED TO MEET YOU."
	getname()

def getname():
	# To do: understand how many of these global variables are needed
	global playername
	global namelist
	time.sleep(1.5)
	print "What's your name?"
	playername = raw_input("> ")
	# The following 2 lines removes accents and weird unicode things from the player input.
	# e.g.: "café" would be changed to "cafe"
	playername = unicode(playername, "utf-8")
	playername = unicodedata.normalize('NFD', playername).encode('ascii', 'ignore')
	time.sleep(1)
	# Show this only on the second playthrough
	if playthroughs[0] == 2:
		print playername.upper() + "! A " + playername.capitalize() + " by any other name would smell just the same. That's how it goes, right?!"
		time.sleep(2.5)
		print "Anyway, pleased to meet you!"
	else:
		print "Pleased to meet you, %s!" % playername
	time.sleep(2)
	# These next 11 lines of code take the player name and break it up into a list of chunks of consonants
	# e.g.: "Robert" -> ['R','b','rt']
	# e.g.: "Stephanie" -> ['St','ph','n']
	# This is to play around with the name later on
	namelist = []
	vowels = "aeiouAEIOU"
	currletter = 0
	for x in playername:
		if x not in vowels:
			if len(namelist) > currletter:
				namelist[currletter] += x
			else:
				namelist.append(x)
		else:
			currletter += 1
	getmajor()

# A list containing multiple variants of a particular major, to be used to map all the variants to the same major
engmajor = ["english", "eng"]
csmajor = ["cs", "comp sci", "computer science", "computer", "programming", "c s", "computers", "compsci"]
twocmajor = ["music", "piano"]
twodmajor = ["political economy", "poli econ", "pe"]

def getmajor():
	global playermajor
	print "What was your major at MU?"
	playermajor = raw_input("> ")
	time.sleep(1)
	# Make the entry lowercase
	playermajor = playermajor.lower()
	# If the entry is in the list above, make it the corresponding major
	if playermajor in engmajor:
		playermajor = "English"
	elif playermajor in csmajor:
		playermajor = "Comp Sci"
	elif playermajor in twocmajor:
		playermajor = "Music"
	elif playermajor in twodmajor:
		playermajor = "Political Economy"
	# Note the major in the save file
	if playermajor == "English":
		playthroughs[1] += 1
	elif playermajor == "Comp Sci":
		playthroughs[2] += 1
	elif playermajor == "Music":
		playthroughs[3] += 1
	elif playermajor == "Political Economy":
		playthroughs[4] += 1
	else:
		playthroughs[5] += 1
	# Save the save file
	with open("SAex36save.p",'wb') as p:
		pickle.dump(playthroughs, p)
	p.close()
	# Depending on the major, go to the appropriate function to make a comment about it
	if playermajor == "English":
		reply2a()
	elif playermajor == "Comp Sci":
		reply2b()
	elif playermajor == "Music":
		reply2c()
	elif playermajor == "Political Economy":
		reply2d()
	else:
		reply2e()

def reply2a():
	global currstats
	# These if statements select a comment based on how many times the particular major has been picked
	# The comments are cycled through so that on the 1st (and 6th, and 11th, etc.) time playing, the first comment is selected. On the 2nd (and 7th, and 12th, etc.) time playing, the second comment is selected. etc.
	if playthroughs[1]%5 == 1:
		print "Wow, nice. I bet you speak real good."
	elif playthroughs[1]%5 == 2:
		print "Finally, someone who shares my love of the Oxford comma!!"
	elif playthroughs[1]%5 == 3:
		print "Let the wild rumpus start!"
	elif playthroughs[1]%5 == 4:
		print "Then you must be acutely aware: It's the possibility of having a dream come true that makes life interesting."
	else:
		print "Oh!!! ¿Puedes ser mi profesora y enseñarme inglés?"
	time.sleep(2.5)
	# If the player has played 4 or more times and hasn't yet selected Music or PE as their major, make these additional comments.
	if playthroughs[0] >= 4 and playthroughs[4] == 0 and playthroughs[3] == 0:
		print "But really, just English and CS all the time?! Come on, surely they had more interesting majors at MU!"
		time.sleep(2)
		print "Maybe next time you can try something else. :)"
		time.sleep(1)
	print "Also! That must mean that your stats are as follows:"
	# Assign stats based on the major
	currstats = [1, 1, 3, 7, 4, 5]
	time.sleep(1.5)
	stats()

def reply2b():
	global currstats
	if playthroughs[2]%4 == 1:
		print "As a computer, I feel all tingly inside. :)"
	elif playthroughs[2]%4 == 2:
		print "My name is Dug. I have just met you, and I love you. Squirrel!"
	elif playthroughs[2]%4 == 3:
		print "01100010 01100001 01100100 01100001 01110011 01110011 00100001"
	else:
		print "Uh oh. Is this a Turing test? I am totes bagotes a real live human, for realsies."
	time.sleep(2.5)
	# If the player has played 4 or more times and hasn't yet selected Music or PE as their major, make these additional comments.
	if playthroughs[0] >= 4 and playthroughs[4] == 0 and playthroughs[3] == 0:
		print "But really, just English and CS all the time?! Come on, surely they had more interesting majors at MU!"
		time.sleep(3)
		print "Maybe next time you can try something else. :)"
		time.sleep(1)
	print "Also! That must mean that your stats are as follows:"
	currstats = [7, 7, 5, 1, 1, 0]
	time.sleep(1.5)
	stats()

def reply2c():
	global currstats
	print "Ah, music. A magic beyond all we do here!"
	time.sleep(2.5)
	print "Also! That must mean that your stats are as follows:"
	currstats = [3, 2, 3, 7, 4, 3]
	time.sleep(1.5)
	stats()

def reply2d():
	global currstats
	print "Oh! Really? That's... wow. Much wow. Hmmmm.. How is that possible...!? I haven't seen anyone with stats this high before...!"
	currstats = [7, 7, 7, 7, 7, 7]
	time.sleep(2.5)
	stats()

def reply2e():
	global currstats
	print "Erm.. Really? %s, that's a major now? It's amazing what diplomas they'll give out nowadays." % playermajor
	time.sleep(2.5)
	print "Also! That must mean that your stats are as follows:"
	currstats = [3, 3, 4, 4, 4, 3]
	time.sleep(1.5)
	stats()

# This will keep track of how many times the user has selected an action to increase their stats
loop = 0

def stats():
	global loop
	print "Mechanical = %s" % currstats[0]
	print "Logic = %s" % currstats[1]
	print "Pop culture references = %s" % currstats[2]
	print "Creativity = %s" % currstats[3]
	print "Body = %s" % currstats[4]
	print "Charisma = %s" % currstats[5]
	time.sleep(1)
	action()

def action():
	global currstats
	global loop
	# Show the instructions on the first loop
	if loop == 0:
		print "Listen up! There's only one basic instruction here: You get 5 playthroughs. Choose wisely."
		time.sleep(2.5)
	# Increase the loop number to keep track of how many times user selected an action
	loop += 1
	# Playthrough meaning loop. This is probably confusing since in the code I refer to "playthroughs" as number of times played the game...
	print "Playthrough #%s!" % loop
	print "What would you like to do? Select a number, 1-11!"
	time.sleep(1)
	print "1: Learn a language!"
	time.sleep(0.10)
	print "2: Discover new ♪music♪"
	time.sleep(0.10)
	print "3: Paint!"
	time.sleep(0.10)
	print "4: Werk your body! Go to the gym, play soccer, run, kickbox"
	time.sleep(0.10)
	print "5: Read a book, e- or otherwise"
	time.sleep(0.10)
	print "6: Learn Python the Hard Way"
	time.sleep(0.10)
	print "7: Spend all your time at work"
	time.sleep(0.10)
	print "8: Watch Netflix"
	time.sleep(0.10)
	print "9: Get yo' drank on"
	time.sleep(0.10)
	print "10: Partaaaay~"
	time.sleep(0.10)
	print "11: Culture yourself! Go to the museum, check out the symphony, Shake your Speare, etc"
	time.sleep(0.1)
	actioninput = raw_input("> ")
	# The input is a string. If it's a digit (as it should be), convert it to an integer so we can add to and subtract from it
	if actioninput.isdigit():
		actioninput	 = int(actioninput)
	time.sleep(1)
	# Confirm the user's choice, then show the consequences of their selection: an increase or decrease of stats
	if actioninput == 1:
		print "Language!"
		time.sleep(0.5)
		currstats[3] += 1
		print "Creativity + 1!"
		currstats[5] += 1
		print "Charisma + 1!"
	elif actioninput == 2:
		print "♪Music♪!"
		time.sleep(0.5)
		currstats[3] += 1
		print "Creativity + 1!"
		currstats[2] += 1
		print "Pop culture references + 1!"
	elif actioninput == 3:
		print "Paint!"
		time.sleep(0.5)
		currstats[3] += 1
		print "Creativity + 1!"
		currstats[0] += 1
		print "Mechanical + 1!"
	elif actioninput == 4:
		print "Werk your body!"
		time.sleep(0.5)
		currstats[4] += 2
		print "Body + 2!"
	elif actioninput == 5:
		print "(E-?)BOOK!"
		time.sleep(0.5)
		currstats[3] += 1
		print "Creativity + 1!"
	elif actioninput == 6:
		print "Python!"
		time.sleep(0.5)
		currstats[1] += 2
		print "Logic + 2!"
	elif actioninput == 7:
		print "Work!"
		time.sleep(0.5)
		currstats[0] += 1
		print "Mechanical + 1!"
		currstats[3] -= 1
		print "Creativity - 1!"
		currstats[4] -= 1
		print "Body - 1!"
		currstats[5] -= 1
		print "Charisma - 1!"
	elif actioninput == 8:
		print "Netflix!"
		time.sleep(0.5)
		currstats[2] += 1
		print "Pop culture references + 1!"
		currstats[3] -= 1
		print "Creativity - 1!"
		currstats[4] -= 1
		print "Body - 1!"
	elif actioninput == 9:
		print "DRANKS!"
		time.sleep(0.5)
		currstats[1] -= 1
		print "Logic - 1!"
		currstats[3] -= 1
		print "Creativity - 1!"
		currstats[4] -= 1
		print "Body - 1!"
		currstats[5] -= 1
		print "Charisma - 1!"
	elif actioninput == 10:
		print "Partaaaay~!"
		time.sleep(0.5)
		currstats[5] += 1
		print "Charisma + 1!"
		currstats[1] -= 1
		print "Logic - 1!"
		currstats[3] -= 1
		print "Creativity - 1!"
	elif actioninput == 11:
		print "Culture!"
		time.sleep(0.5)
		currstats[2] += 1
		print "Pop culture references + 1!"
		currstats[3] += 1
		print "Creativity + 1!"
		currstats[5] += 1
		print "Charisma + 1!"
	else:
		# If the input wasn't a digit that was successfully converted to an integer and run through the if statements above, print the following and keep going
		print "Congrats on not following directions!"
	time.sleep(1)
	# Generate a random number and store it temporarily
	temprandom = random()
	# The first three times playing, go to the end stats directly after selecting an action 5 times
	if loop == 5 and playthroughs[0] < 4:
		endstats()
	# The 4th time and after playing, after the 4th or 5th action loop, go to the alien thing.
	# I *think* the probability math works out that this happens 43.75% of the time
	elif loop >= 4 and playthroughs[0] >= 4 and temprandom < 0.25:
		time.sleep(1)
		thingx()
	# The 4th time and after playing, after the 5th action loop, go to the dragon thing.
	# If my math above is right, this happens 56.25% of the time
	elif loop >= 5 and playthroughs[0] >= 4 and temprandom >= 0.25:
		time.sleep(2)
		thingy()
	else:
		print "Here are your new stats!"
		time.sleep(0.2)
		stats()

# Source for flipper: http://www.leancrew.com/all-this/2009/05/im-feelin-upside-down/, via Google
# Make a dictionary that flips the player's nam
pchars = u"abcdefghijklmnopqrstuvwxyz,.?!'()[]{}"
fchars = u"ɐqɔpǝɟƃɥıɾʞlɯuodbɹsʇnʌʍxʎz'˙¿¡,)(][}{"
flipper = dict(zip(pchars, fchars))

# e.g.: "Robert" -> "ʇɹǝqoɹ"
# e.g.: "Stephanie" -> "ǝıuɐɥdǝʇs"
def flip(s):
	charList = [ flipper.get(x, x) for x in s.lower() ]
	charList.reverse()
	return "".join(charList)

def thingx():
	global namelist
	print "......................."
	print "INCOMING TRANSMISSION"
	print "......................."
	time.sleep(1)
	# Reverse the player's name the second time it's said.
	# e.g.: "Robert" -> "Trebor"
	# e.g.: "Stephanie" -> "Einahpets"
	print "Commander %s..! Er, forgive me. I didn't mean to address you by your Earth code name. Greetings, Commander %s!" % (playername, playername[::-1].capitalize())
	time.sleep(2.5)
	print "Commander ex36.py here, seeking a status report. How go your Earth operations, Commander %s?" % flip(playername)
	time.sleep(1)
	print "1: Good!"
	time.sleep(0.5)
	print "2: Terrible"
	time.sleep(0.5)
	print "3: SMOOTH"
	time.sleep(0.1)
	ops = raw_input("> ")
	time.sleep(1)
	# Make a nonsense version of the player's name with all the vowels replaced by "ooo"
	# e.g.: "Robert" -> "Rooobooortooo"
	# e.g.: "Stephanie" -> "Stooophooonooo"
	tempname = ""
	for item in namelist:
		tempname += item
		tempname += "ooo"
	print "Is your plan to take over the Earth finalized, Commander %s?" % tempname
	time.sleep(1)
	print "1: Yes"
	time.sleep(0.5)
	print "2: Maybe"
	time.sleep(0.5)
	print "π: No"
	time.sleep(0.1)
	planrdy = raw_input("> ")
	time.sleep(1)
	# Make another nonsense version of the player's name
	# e.g.: "Robert" -> "Rlorbsbrtol"
	# e.g.: "Stephanie" -> "Stlorphsbnol"
	tempname2 = ""
	templist2 = ["lor", "sb", "ol"]
	tempnum = 0
	for item in namelist:
		tempname2 += item
		tempname2 += templist2[tempnum]
		tempnum += 1

	print "Excellent. And when will you have it completed, Commander %s?" % tempname2
	time.sleep(1)
	print "1: Tomorrow."
	time.sleep(0.1)
	when = raw_input("> ")
	time.sleep(1)
	print "FANTASTIC!!!"
	time.sleep(1)
	print "Silly puny EARTH HUMANS! *Evil laughter*"
	time.sleep(2)
	print "1: Engage in a mostly harmless but increasingly louder Evil Laughter-off with Commander ex36.py"
	time.sleep(0.5)
	print "2: Open one of your six mouths, and sing the song that ends the Earth."
	time.sleep(0.1)
	aldo = raw_input("> ")
	# Add an extra number to the currentstats list, essentially creating a new stat
	currstats.append(7)
	endstats()

def thingy():
	print "HARK! A DRAGON HAS APPEARED."
	time.sleep(1)
	print "What do you want to do? You should probably choose based on your stats..."
	time.sleep(1)
	print "1: Discuss philosophy"
	time.sleep(0.1)
	print "2: Slay the dragon!"
	time.sleep(0.1)
	print "3: Attack the dragon"
	time.sleep(0.1)
	print "4: Paint the dragon"
	time.sleep(0.1)
	print "5: Party with the dragon"
	time.sleep(0.1)
	print "6: Drink with the dragon"
	time.sleep(0.1)
	print "7: Befriend the dragon"
	time.sleep(0.1)
	thingydo = raw_input("> ")
	if thingydo.isdigit():
		thingydo = int(thingydo)
	# Succeed or fail depending on the user's choice and their existing stats
	if thingydo == 1:
		print "You decide to discuss the meaning of life with the dragon over a spot of tea."
		time.sleep(1)
		print "Based on your stats, does that work out for you?"
		time.sleep(2)
		# If discussing philosophy and logic is 6 or higher, succeed
		if currstats[1] > 5:
			print "It does!! Your stats go up even further."
			# Increase all stats by 1
			currstats = [x+1 for x in currstats]
			endstats()
		else:
			print "Nope, didn't work. You should've joined Toastmasters."
			exit(0)
	elif thingydo == 2:
		print "You decide to tell the dragon a joke. Does it... SLAY?!"
		time.sleep(2)
		# If slaying the dragon and creativity is 6 or higher, succeed
		if currstats[3] > 5:
			print "It does!! Your stats go up even further."
			currstats = [x+1 for x in currstats]
			endstats()
		else:
			print "That wasn't very funny. The dragon is laughing AT you, not WITH you."
			time.sleep(1)
			print "Also, just when you think it couldn't get any worse than a dragon laughing at you: the dragon chortles up a fireball. You are incinerated."
			time.sleep(1)
			exit(0)
	elif thingydo == 3:
		# If attacking the dragon, always fail
		print "Yeah, hi, it's a dragon. Wtf were you thinking?"
		time.sleep(1)
		exit(0)
	elif thingydo == 4:
		print "You decide to paint the dragon's toenails. Does he like them?"
		time.sleep(1.5)
		# If painting the dragon and creativity is 6 or higher, succeed
		if currstats[3] > 5:
			print "He does! Stats++"
			currstats = [x+1 for x in currstats]
			endstats()
		else:
			print "What is this, modern art? The dragon does not like modern art. The dragon decides to subvert the modern art movement by submitting a giant black lump as a postmodern sculpture."
			time.sleep(3)
			print "Also, that giant black lump is made out of your unrecognizably charred body. Good bye!"
			time.sleep(1)
			exit(0)
	elif thingydo == 5:
		# If partying with the dragon, always fail
		print "Fail. Didn't you learn anything from Monsters U?"
		time.sleep(1)
		exit(0)
	elif thingydo == 6:
		# If drinking with the dragon, always fail
		print "You should really know better than to give flammable liquids to a thing that BREATHES FIRE. Bye!"
		time.sleep(1)
		exit(0)
	elif thingydo == 7:
		# If befriending the dragon and all stats 4 or higher, succeed
		if all(i >= 4 for i in currstats):
			print "Success! You are a well-rounded and interesting individual, and the dragon's heart of stone has turned to gold." + u"\u2665"
			time.sleep(1)
			endstats()
		else:
			print "Sorry, the dragon would like me to let you know that perhaps you are not the right culture fit at the moment. Try again another time!"
			time.sleep(1)
			exit(0)
	else:
		# If not a valid action choice (1-7), end game
		print "You didn't pick a number, so now this is going to end and you get nothing!"
		time.sleep(1)
		exit(0)

def endstats():
	time.sleep(1)
	print "You've reached the end game, congrats on your stats!!"
	time.sleep(1)
	print "Mechanical = %s" % currstats[0]
	time.sleep(0.5)
	print "Logic = %s" % currstats[1]
	time.sleep(0.5)
	print "Pop culture references = %s" % currstats[2]
	time.sleep(0.5)
	print "Creativity = %s" % currstats[3]
	time.sleep(0.5)
	print "Body = %s" % currstats[4]
	time.sleep(0.5)
	print "Charisma = %s" % currstats[5]
	time.sleep(0.5)
	# If we added an extra stat in the alien function, print the alien stat as infinity
	if len(currstats) > 6:
		print u"\U0001F47D = \u221E"
	# Only on the first time playing the game
	if playthroughs[0] == 1:
		print "Here is your prize! http://booksofadam.tumblr.com/post/143132562278/mission-accomplished"
	# Only on the second time playing the game
	if playthroughs[0] == 2:
		print "Here is your prize! http://m.xkcd.com/1674/"
	# Only on the third time playing the game
	if playthroughs[0] == 3:
		print "Here is your prize! http://sarahcandersen.com/post/122944230263"
	# Extra ending if PE major
	if playermajor == "Political Economy":
		time.sleep(1)
		otherend()
	time.sleep(1)
	exit(0)

def otherend():
	print "Secret ending time!"
	time.sleep(1.5)
	print "This was originally meant as snarky commentary on what would lead you to level up your stats in life, but this is obviously silly."
	time.sleep(3)
	print "Happiness, love, and anything that derives from these are the most meaningful, but weren't tracked because they'd be too complex."
	time.sleep(3.5)
	print "It's not what stats you have in life, but how you use them and how they make you and other people happy.\n"
	time.sleep(4)
	print "So hopefully this game has made you think, smile, and maybe even laugh."
	time.sleep(2)
	print "If it has, the ridiculousness will have been worth it."
	time.sleep(2)
	print "Thanks for playing!"
	time.sleep(1)
	exit(0)

start()