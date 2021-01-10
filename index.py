import nltk
from nltk import data
from nltk.tree import Tree
from nltk.draw.tree import draw_trees
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
			return True
	except:
		print("String must be terminals or non-terminals")
		return False
# Load a grammar from to file
grammar = nltk.data.load('file:grammar.cfg')
print(grammar)
inputString = input('Input string: ')
parser = nltk.ChartParser(grammar)
sent = list(map(str, inputString))
if checkString(sent):
	lst = []
	for i in parser.parse(sent):
		lst.append(i)
# output
	if len(lst) > 0:
		print('String ' + inputString + ' was born from grammar')
		if len(lst) > 1: 
			print('The grammar is ambiguity grammar')
			draw_trees(lst[0], lst[1])
		else:
			print('The grammar is not ambiguity grammar')
			draw_trees(lst[0])
	else:
		print('String ' + inputString + ' was\'t born from grammar')