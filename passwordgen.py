import random;
# inp = random.choices("!@#$_*", k=1)
punc1 = random.choices("!@#$_*qwertyuiopasdfghjklzxcvbnm0123456789", k=8)
password =  "".join(punc1) 
print(password)
