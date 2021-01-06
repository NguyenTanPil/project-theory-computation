import nltk, re, pprint
from nltk import CFG, data
# Load a grammar from to file
grammar = nltk.data.load('file:grammar.cfg')
# grammar = nltk.CFG.fromstring(grammarInput)
# print grammar
print(grammar)
# Check valid of input string
def checkString(sent):
	try:
		# check string non-terminal
		for item in sent:
			if item.isupper():
				print('String must be terminals')
				return False
		# check string in set terminal
		for i in parser.parse(sent):
			pass
		return True
	except:
		print("String must be terminals or non-terminals")
		return False

# main
inputString = input('Input string: ')
parser = nltk.ChartParser(grammar)
sent = list(map(str, inputString))
print(sent)
if checkString(sent):
	status = False
	tree = nltk.Tree.fromstring('()')
	for i in parser.parse(sent):
 	 # print(i.productions())
		tree = str(i)
		status = True
		if status:
			break

# main	
	if(status):
		print('String ' + inputString + ' was born from grammar')
		drawTree = nltk.Tree.fromstring(tree)
		drawTree.draw()
	else:
		print('String ' + inputString + ' was\'t born from grammar')
