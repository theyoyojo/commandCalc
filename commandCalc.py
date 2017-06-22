#A calculator that is very strange to use, will be programmable
#By Joel O Savitz, (c) 2017
import os

#get the value of a variable TODO
def unVar(var):
	if True:
		return float(var)


#starting with the first value, add all values
def add(words):
	result = 0
	for i in range(1, len(words)):
		result += unVar(words[i])
	return result

#starting with the first value, subtract subsequent values
def subtract(words):
	result = unVar(words[1])
	for i in range(2, len(words)):
		result -= unVar(words[i])
	return result

def multiply(words):
	results = 1
	for i in range(1, len(words)):
		results *= unVar(words[i])
	return results

def divide(words):
	results = unVar(words[1])
	for i in range(2, len(words)):
		results /= unVar(words[i])
	return results

#make sure the command exists and has a correct number of arguments TODO
def validateCommand(words, commandFile):
	valid = commandFile.readlines()
	print(valid)
	return True

#make sure command exists and is allowed, then check if arguments are valid
def validateCommandFile(valid):
	try:
		commandFile = open("commands.txt","r+")
	except FileNotFoundError:
		commandFile = open("commands.txt","w")	
		for item in valid:
			commandFile.write(item)
	else:
		True
		#validate user command file TODO
	return commandFile #remove this when done, function should do all of the work

def output(output):
	print(output)

#get and process input
def inputLoop(prompt,commandFile):
	exit = 0
	while(exit == 0):
		raw = input(prompt)
		words = raw.split()
		if words and validateCommand(words, commands):
			output(eval(words[0] + "(" + str(words) + ")"))
		if words:
			if words[0] == "exit":
				exit = 1
			
#setup anything, display information, start things up
def main():
	print("Command Calculator v0.1 alpha")
	inputLoop("(+-*/)>>",getCommandFile())
	
coms = validateCommandFile()

for i in coms:
	print(i)
