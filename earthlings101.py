#set 2 difficulty levels: under 10 and over 10. harder difficulity has maybe sides, sharing, 
# shit like that. if you get the hard one wrong, it tells you that you could always go back 
# and lie about your age. get a certain number right to win a prize - if you can also ace
# a quiz about the food!

# -*- coding: utf-8 -*-
import random

# introductions
print("Welcome to Earthlings 101. I will be your teacher, Ms. Hoofaloofa. Oh! Looks like we have a new student!")
playername = raw_input("What's your name? ")
age = int(raw_input("Great to meet you, " + playername + ". How old are you? Use numbers, not letters! "))
print("You're pretty lucky, " + playername + "- " + str(age) + " is the best age! Let's begin. As you all know, millions of light years from our home here on Snoolu, there is an odd, tiny planet called Earth. Earth is filled with, well, Earthlings - camels, roses, mushrooms, dogs, monkeys, and way, way more. But perhaps the oddest of all these Earthlings are the humans. The humans have created skyscrapers and poetry. They have television shows without scripts, and computers that fly! We will learn about all of this. But first we must start small.")

# what to do on a new planet?
touristquestion = raw_input("Quick! " + playername + "! What is the first thing to do when you find yourself on a planet that you've never been to before? Quick! One word! ")
if (touristquestion == "eat" or 
	touristquestion == "Eat" or 
	touristquestion == "dine" or 
	touristquestion == "Dine" or 
	touristquestion == "food" or
	touristquestion == "Food"):
	print("Correct! Look out Snooligans - we got a smart one!")
else: 
	print("Wrong! Snooligans - stop throwing your lafafas at " + playername + ". " + playername + " will get smarter by working hard - that's the whole point!")
print("Anyways, where were we... Aha, yes! When you find yourself on a planet for the first time, you eat! Eating like the locals do is one of the best ways to learn about a new place. Which is a perfect segway to today's lesson. Hope you're hungry!")

# hear about today's lesson?
lessonquestion = raw_input("Okay, " + playername + ". Do you want to hear about today's lesson now? Yes or no. ")
while lessonquestion != "yes" and lessonquestion != "Yes": 
	lessonquestion = raw_input("Okay, " + playername + ". Do you want to hear about today's lesson now? ") 
print("Great! Let's do it! We're going to be using some brand spanking new technology to actually enter the bodies of random humans around Earth. Since eating is such a good way to learn about a new place, We're going to make sure we do it right when they're about to eat a meal. There are only two rules: You have to answer any math-based questions that the humans ask you... and have fun!")

# start game?
enterquestion = raw_input("Alright, " + playername + ". Are you ready to enter a random human's body now? Yes or no. ")
while enterquestion != "yes" and enterquestion != "Yes":
	enterquestion = raw_input("Alright, " + playername + ". Are you ready to enter a random human's body now? ")

# loop game
go = True 
while go is True:

	# randomize food
	print("Ok, " + playername + ". Let's see who you got! You are...")
	food = random.randint(1, 3)
	if food == 1: 
		food = "burrito"
		print("Juana, a 9-year old girl from Mexico who likes burritos! Burritos were created 400 years ago, and feature corn tortillas and local produce. Yum!")
	if food == 2:
		food = "fufu"
		print("Kofi, a 12-year old boy from Ghana who loves fufu! Fufu has the texture of wet pizza dough - you eat it in soup, with your hands, and you don't chew it! Weird? Millions of Ghanaians don't think so!")
	if food == 3:
		food = "falafel"
		print("Abas, a 6-year old boy from the West Bank who loves falafel! Falafel is made of ground chickpeas, and goes delicious in a salad or wrap!")
	
	# randomize guests and portions; increase difficulty with age
	if age <= 10:
		guests = round(random.randint(2, 6), 1)
		portions = round(random.randint(2, 6), 1)
	else:
		guests = round(random.randint(2, 20), 1)
		portions = round(random.randint (2, 20), 1)	

	print(playername + ", there are " + str(guests) + " guests and " + str(portions) + " portions of " + food + ".")

	# answer
	finalanswer = round(float(raw_input("How many portions should each guest get to make it fair? Make sure your answer is to 1 decimal place! ")), 1)
	while finalanswer != round(portions / guests, 1):
		print "Wrong! Try Again..."
		finalanswer = round(float(raw_input("How many portions of " + food + " should each guest get to make it fair? Make sure your answer is to 1 decimal place! ")), 1)

	# play again?	
	againquestion = raw_input("Correct! Would you like to find a new human to eat with? Yes or No. ")
	if againquestion == "yes" or againquestion == "Yes":
		go = True
	else: 
		go = False

# ending
print("Ok. Goodbye!")


