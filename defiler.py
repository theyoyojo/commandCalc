#module to save and load structured file data to and from a usable structure, a dictionary being the first planned implementation
import sys

#figure out the type of a given line
def getLineType(line):
	first = line[0]
	if first == '#':
		return 'comment'
	elif first == '{':
		return 'open'
	elif first == '}':
		return 'close'
	else:
		return 'definition'

#turn an attribute into a value
def extractFromAttribute(attribute):
	True #TODO

#turn raw header item into dict of allowed attributes and types
def parseHeader (newItem):
	print(newItem)
	newDict = {}
	for line in newItem:
		isKey = True #are we before the = sign? if so, we are parsing the key, if not, we are parsing the value
		key = ''
		value = ''
		for char in line:
			if char == '\t' or char == '\n':
				continue
			if char == '=':
				isKey = False
			elif isKey == True:
				key += char
			else:
				value += char
		newDict[key] = value
	return newDict


def loadFileToDict(name):
	location = 0 #this is the current number of the instance being parsed, 0 is the header, >0 is the body
	newDict = {} #this is the final dictionary to be outputed for use
	allowed = {} #this is a dictioary of allowed attributes and their data types
	newItem = [] #this is the current item being proccessed before being appended to the dictionary
	isIn = False #are we within an instance? not initially

	raw = open(name,'r')
	for line in raw:
		typ = getLineType(line) #the type of the current line
		#sys.stdout.write(typ + str(location)+line)
		#sys.stdout.write(line[0])
		if not typ == 'comment':
			if typ == 'open':
				if isIn == False:
					isIn = True
			elif typ == 'close':
				isIn = False	
				if location == 0:
					allowed = parseHeader(newItem)
					print(allowed)
				else:
					True#parseInstance(newItem, allowed)
				location += 1
				newItem = []			
			elif typ == 'definition':
				newItem.append(line)
		#print(newItem)
			

loadFileToDict("defaultCommands.txt")
	
