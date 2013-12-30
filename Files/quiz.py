"""
**Quiz Maker** - Make an application which takes various questions form a file, picked randomly, and puts together a quiz for students.
Each quiz can be different and then reads a key to grade the quizzes
"""

import random
import sys

#Open file and get question
def getQuestion(random_question):
	with open('questions.txt') as f:
	    i = 1
	    for line in f:
	        if i == random_question:
	            break
	        i += 1
	print line
#main
def main():
	random_question = random.randint(0,20)
	getQuestion(random_question)
	answer = raw_input()

	answers_key = {
		"1":"The Sun",
		"2":"2007",
		"3":"Central Processing Unit",
		"4":"False",
		"5":"Edwin Hubble",
		"6":"Long",
		"7":"Web Browsers",
		"8":"False",
		"9":"Honda",
		"10":"True",
		"11":"Read Only Memory",
		"12":"CDs",
		"13":"The Sun",
		"14":"International Business Machines",
		"15":"Paul Allen",
		"16":"Isaac Asimov",
		"17":"True",
		"18":"World Wide Web",
		"19":"The Apple iPod",
		"20":"True",
		 }

	correct_answer = answers_key.get(str(random_question))

	if answer == correct_answer:
		print 'Correct! %s' %correct_answer
	else:
		print 'Incorrect! %s' %correct_answer

if __name__ == '__main__':
        status = main()
        sys.exit(status)