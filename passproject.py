from string import printable, whitespace
from random import sample, randint

class Password():

    def __init__(self, length, website):
        self.length = length
        self.website = website

    def generate_password(self):
        printable_chars = printable.strip()
        whitespace_chars = whitespace
        non_whitespace_printable_chars = [c for c in printable_chars if c not in whitespace_chars]
        chosen_chars_list = sample(non_whitespace_printable_chars, self.length)
        generated_password = ''.join(chosen_chars_list)
        return generated_password
        

what_length = int(input("How long your password has to be?  "))
what_website = input('What website do you need password for?  ')   
        
password = Password(what_length, what_website)
print(f'My password for {password.website} is {password.generate_password()} and its length is: {password.length}')
f = open("passlist.text", "a")
f.write(f'My password for {password.website} is {password.generate_password()} and its length is: {password.length}'+'\n')
f.close()




#od 10 włącznie do 15 symboli długość
#mieszanka wszystkich characterów