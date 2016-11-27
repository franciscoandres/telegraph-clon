import random
import string

def generate_string():
	result = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(24))
	return result
