import random, string

# r = int(input('Enter your range: '))

# pw = string.ascii_letters + string.digits + string.punctuation
# random = ''.join(random.sample(pw, r))
random = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 15))

print("Your generated password is: %s" % random)
