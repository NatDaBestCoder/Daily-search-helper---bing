import keyboard
import time
import random
import settings



# reads the words.txt file and saves all the words in the varible "words"
words = ()
with open('UpdatedVersion\words.txt', 'r') as file:
    words = [line.strip() for line in file]   
 
# picks a random word in words.txt file
def word():
    wordthing = random.choice(words)
    ##Debug command below
    ##print(wordthing)
    return str(wordthing)

keyboard.send(settings.command)
time.sleep(2)

keyboard.send('ctrl+t')
time.sleep(0.5)

for i in range(settings.times):
    keyboard.write(word())
    time.sleep(0.5)
    keyboard.send('enter')
    time.sleep(settings.delay)
    keyboard.send('ctrl+e')
    time.sleep(0.5)

keyboard.send('d+o+n+e')

exit()