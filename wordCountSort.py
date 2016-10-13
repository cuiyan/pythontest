import string  

bookName = raw_input('Enter the book name:')
if len(bookName)<1:bookName='thelittleprince.txt'
bookcontent = open(bookName)
wordcount = dict()
# = ['the','little','prince','a','is','are','was','be','were','no','not','did','do','can','could','may','might','to','don\'t','you','has','i','me','my','he','she','it','and','of','that']
for line in bookcontent:
	line = line.strip()
	if len(line)==0:continue
	words = line.split()
	for word in words:
		word = word.lower()
		#if word in exceptword:continue
		dots = string.punctuation
		word = word.translate(None,dots)
		wordcount[word] = wordcount.get(word,0)+1
		
tmp = list()
for k,v in wordcount.items():
	tmp.append((v,k))	
	
tmp.sort(reverse=True)

for val,key in tmp[:10]:
	print key,val