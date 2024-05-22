import string
from random import *

characters = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(characters) for i in range(randint(7, 14)))

print("Oluşturulan parolanız : " + password)
