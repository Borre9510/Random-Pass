import secrets

chars = "abcdefghijklmnñopqrstuvwxyz1234567890"
password= ""

for i in range(16):
    password+= secrets  .choice(chars)

print(f"Your password is:{password}")
