from string import printable, whitespace
from random import sample, randint
import csv
import os.path



def generate_password(length):
    printable_chars = printable.strip()
    whitespace_chars = whitespace
    non_whitespace_printable_chars = [c for c in printable_chars if c not in whitespace_chars]
    chosen_chars_list = sample(non_whitespace_printable_chars, length)
    generated_password = ''.join(chosen_chars_list)
    return generated_password
        

choose_length = int(input("How long your password has to be?  "))
website = input('What website do you need password for?  ')   
        
password = generate_password(choose_length)

print(f'My password for {website} is {password} and its length is: {choose_length}')
if os.path.isfile('passwords.csv'):
    print('File exists')
    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, password, choose_length])
    file.close()
    
else:
    print('File does not exist')
    with open('passwords.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, password, choose_length])
    file.close()





#od 10 włącznie do 15 symboli długość
#mieszanka wszystkich characterów