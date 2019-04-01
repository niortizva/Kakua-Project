import string
import random

def getKey():
	lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(30)]
	key = "".join(lst)
	return key
