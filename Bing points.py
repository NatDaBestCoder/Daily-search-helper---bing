import keyboard
import time
import random
#50 searches is usually enough to keep this 
times = 50
delay = 5
# reads the words.txt file and saves all the words in the varible "words"
words = ()
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]    
# picks a random word in words.txt file
def word():
    wordthing = random.choice(words)
    
    
    print(wordthing)
    return str(wordthing)

keyboard.send('windows+1')
time.sleep(2)

keyboard.send('ctrl+t')
time.sleep(0.5)

for i in range(times):
    keyboard.write(word())
    time.sleep(0.5)
    keyboard.send('enter')
    time.sleep(delay)
    keyboard.send('ctrl+e')
    time.sleep(0.5)

keyboard.send('d+o+n+e')



exit()