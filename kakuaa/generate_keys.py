import numpy as np

char = np.array([
	'0','1','2','3','4','5','6','7','8','9',
	'A','B','C','D','E','F','G','H','I','J',
	'K','L','M','N','O','P','Q','R','S','T',
	'U','V','W','X','Y','Z',
	'a','b','c','d','e','f','g','h','i','j',
	'k','l','m','n','o','p','q','r','s','t',
	'u','v','w','x','y','z'	
])

index = np.random.randint(char.shape[0],size=(30))
string = ''
for s in char[index]:
	string += s
print(string,'\n')
