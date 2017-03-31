import random

language = random.choice('i')

if language == 'i':
	#Italian
	consonants = 'bdzgfgclmnnprstcvsj012345ntttrrrllsscdpm'
	digraphs = ['spl', 'scl', 'scr', 'spr', 'sfr', 'str', 'sbl', 'sm', 'sv', 'sn', 'pl', 'bl', 'fl', 'cl', 'gl', 'pr', 'br', 'fr', 'cr', 'gr', 'tr', 'dr']
	vowels = 'aeioaeiou!@#$%^&'
	doubles = ['tt', 'zz', 'gg', 'cc', 'bb', 'pp']
	
	#other consonants
	c0 = 'gl'
	c1 = 'gn'
	c2 = 'sc'
	c3 = 'sch'
	c4 = 'gh'
	c5 = 'ch'
	c6 = 'qu'
	c7 = ''
	c8 = ''
	c9 = ''
	
	#other vowels
	v0 = 'ua'
	v1 = 'uo'
	v2 = 'ia'
	v3 = 'io'
	v4 = 'ia'
	v5 = 'io'
	v6 = ''
	v7 = ''
	v8 = ''
	
	#replacement vowels
	aReplacements = 'aaaaà'
	eReplacements = 'eeeeè'
	iReplacements = 'iiiiiiiiì'
	oReplacements = 'ooooooooò'
	uReplacements = 'uuuuuuuuù'
	
	#Structure of Words
	wordStructure = ['VC','VCV', 'CV', 'CVCV', 'CVCVCV', 'CVCV', 'VCCV', 'VCV', 'VDV', 'VDV', 'CVDV', 'CVDV', 'DVC', 'DVCV', 'DVDV', 'DVDVCV', 'VC','VCV', 'CV', 'CVCV', 'CVCVCV', 'CVCV', 'VCCV', 'VCV', 'VDV', 'VDV', 'CVDV', 'CVDV', 'DVC', 'DVCV', 'DVDV', 'DVDVCV', 'VC', 'VTV', 'VDV', 'CVTV', 'DVTV', 'DVTV', 'DVTVCV', 'VTV', 'VDV', 'CVTV', 'DVTV', 'DVTV', 'DVTVCV', 'CVCVCVCV', 'DVCVCVCV', 'CVCVDVCV']
elif language == 'e':
	#English - this is going to be tough. holy fuck.
	consonants = 'tttttttttnnnnnnssssssrrrrrrddddllllcccmmwwffggyyppbvkjz'
	digraphs = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']
	vowels = 'eeeeaaaooiiu!@#$%^&*()'
elif language == 'j':
	#Italian
	consonants = 'pbtdkgszrly012345'
	digraphs = ['']
	vowels = 'aiu!'
	doubles = ['']
	
	#other consonants
	c0 = 'sh'
	c1 = 'ch'
	c2 = 'j'
	c3 = 'dg'
	c4 = 'tt'
	c5 = 'dd'
	c6 = ''
	c7 = ''
	c8 = ''
	c9 = ''
	
	#other vowels
	v0 = 'ai'
	v1 = 'au'
	v2 = 'ui'
	v3 = 'ua'
	v4 = ''
	v5 = ''
	v6 = ''
	v7 = ''
	v8 = ''
	
	#replacement vowels
	aReplacements = 'aaaaà'
	eReplacements = 'eeeeè'
	iReplacements = 'iiiiiiiiì'
	oReplacements = 'ooooooooò'
	uReplacements = 'uuuuuuuuù'
	
	#Structure of Words
	wordStructure = ['VC','VCV', 'CV', 'CVCV', 'CVCVCV', 'CVCV', 'VCCV', 'VCV', 'VDV', 'VDV', 'CVDV', 'CVDV', 'DVC', 'DVCV', 'DVDV', 'DVDVCV', 'VC','VCV', 'CV', 'CVCV', 'CVCVCV', 'CVCV', 'VCCV', 'VCV', 'VDV', 'VDV', 'CVDV', 'CVDV', 'DVC', 'DVCV', 'DVDV', 'DVDVCV', 'VC', 'VTV', 'VDV', 'CVTV', 'DVTV', 'DVTV', 'DVTVCV', 'VTV', 'VDV', 'CVTV', 'DVTV', 'DVTV', 'DVTVCV', 'CVCVCVCV', 'DVCVCVCV', 'CVCVDVCV']

nameLength = random.randint(0,6)

def wordmaker(x):
	syllable = random.choice(wordStructure)
	for char in syllable:
		if char == 'C':
			x.append(random.choice(consonants))
		elif char == 'D':
			x.append(random.choice(digraphs))
		elif char == 'T':
			x.append(random.choice(doubles))
		else:
			x.append(random.choice(vowels))

word = []
wordmaker(word)
word = ''.join(word)

word = word.replace('0',c0)
word = word.replace('1',c1)
word = word.replace('2',c2)
word = word.replace('3',c3)
word = word.replace('4',c4)
word = word.replace('5',c5)
word = word.replace('6',c6)
word = word.replace('7',c7)
word = word.replace('8',c8)
word = word.replace('9',c9)

word = word.replace('!',v0)
word = word.replace('@',v1)
word = word.replace('#',v2)
word = word.replace('$',v3)
word = word.replace('%',v4)
word = word.replace('^',v5)
word = word.replace('&',v6)
word = word.replace('(',v7)
word = word.replace(')',v8)


word = word.replace('a',random.choice(aReplacements))
word = word.replace('e',random.choice(eReplacements))
word = word.replace('i',random.choice(iReplacements))
word = word.replace('o',random.choice(oReplacements))
word = word.replace('u',random.choice(uReplacements))

print(word.title())