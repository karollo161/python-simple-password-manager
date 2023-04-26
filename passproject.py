from string import printable, whitespace
from random import sample, randint
import csv
import os.path

class MyPassword():

 
    def __init__(self):
        printable_chars = printable.strip()
        whitespace_chars = whitespace
        non_whitespace_printable_chars = [c for c in printable_chars if c not in whitespace_chars]
        chosen_chars_list = sample(non_whitespace_printable_chars, randint(12,16))
        self.password = ''.join(chosen_chars_list)
        self.save_to_csv = self.save_to_csv()
        pass


    def save_to_csv(self):
        print(f'My password is {self.password} and its length is: {len(self.password)}')
        if os.path.isfile('passwords.csv'):
            print('File exists')
            with open('passwords.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.password, len(self.password)])
            file.close()
    
        else:
            print('File does not exist')
            with open('passwords.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.password, len(self.password)])
            file.close()

'''
def generate_password(length):
    printable_chars = printable.strip()
    whitespace_chars = whitespace
    non_whitespace_printable_chars = [c for c in printable_chars if c not in whitespace_chars]
    chosen_chars_list = sample(non_whitespace_printable_chars, length)
    generated_password = ''.join(chosen_chars_list)
    return generated_password
'''    

#choose_length = int(input("How long your password has to be?  "))
#website = input('What website do you need password for?  ')   
        

p1 = MyPassword()
print(p1.password)






