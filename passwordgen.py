import random;
# inp = random.choices("!@#$_*", k=1)
num = random.choices("!@#$_*qwertyuiopasdfghjklzxcvbnm0123456789", k=8)
password =  "".join(num) 
print(password)
