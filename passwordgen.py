import random;

# inp = random.choices("!@#$_*", k=1)

punc1 = random.choices("!@#$_*", k=2)
punc2 = random.choices("!@#$_*", k=2)
num1 = random.choices("1234567890", k=2)
num2 = random.choices("1234567890", k=4)
num3 = random.choices("1234567890", k=1)

password =  "".join(num2) + "".join(punc1) + "".join(num1) + "".join(punc2) + "".join(num3)
print(password)
