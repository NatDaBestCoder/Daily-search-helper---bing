import keyboard
import time
import random

times = 50

alphabet = [chr(i) for i in range(ord('a'), ord('z') +1)]

def randomchar():
    char = random.choice(alphabet)
    return str(char)

keyboard.send('windows+1')
time.sleep(2)

keyboard.send('ctrl+t')
time.sleep(0.5)

for i in range(times):
    keyboard.send(randomchar()+'+'+randomchar()+'+'+randomchar())
    time.sleep(0.5)
    keyboard.send('enter')
    time.sleep(4)
    keyboard.send('ctrl+e')
    time.sleep(0.5)

keyboard.send('d+o+n+e')


exit()

