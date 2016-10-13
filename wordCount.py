import string  

bookName = raw_input('Enter the book name:')
if len(bookName)<1:bookName='thelittleprince.txt'
bookcontent = open(bookName)
wordcount = dict()
exceptword = ['the','little','prince','a','is','are','was','were','no','not','did','do','can','could','may','might','to','don\'t','you','has','i','he','she','it','and','of','that']
dots=[',','.','...','!','--','\'\'']
for line in bookcontent:
	line = line.strip()
	if len(line)==0:continue
	words = line.split()
	for word in words:
		word = word.lower()
		if word in exceptword:continue
		dots = string.punctuation
		word = word.translate(None,dots)
		wordcount[word] = wordcount.get(word,0)+1
		
maxword=None
maxtimes=None
for word,times in wordcount.items():
	if maxtimes is None or maxtimes<times:
		maxtimes = times
		maxword = word

print maxword,maxtimes