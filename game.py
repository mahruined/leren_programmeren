import sys
import time
import random
def print_delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
print ('''welcome to 
 _   _                                                     _     _ 
| | | |                                                   | |   | |
| |_| |__   ___   _ __   _____      __ __      _____  _ __| | __| |
| __| '_ \ / _ \ | '_ \ / _ \ \ /\ / / \ \ /\ / / _ \| '__| |/ _` |
| |_| | | |  __/ | | | |  __/\ V  V /   \ V  V / (_) | |  | | (_| |
 \__|_| |_|\___| |_| |_|\___| \_/\_/     \_/\_/ \___/|_|  |_|\__,_|
''')
print_delay ('''this is the new world a place where monsters roam the lands freely, from small insectoids to giant dragons,primates,dinosaurs and reptiles,''')
start = input (' its a dangerous world out there are you sure you can do this (y/n) ')
if start == ('y'):
    print_delay ('''thats the spirit!! now first things first let me give you a debrief of the situation real quick the monster we are hunting today is called a Rathalos.
Rathalos are large, bipedal wyverns with a spiny, armored hide covering their body. 
Rathalos also possess a flame sac which is used to produce deadly flaming projectiles from the mouth. The talons upon their feet are highly poisonous and are known to inflict toxic mortal wounds on larger prey.
so you better be carefull not to get hit by any of those. it lives in the very depths of the acient forest fiercely protecting its territory, 
''')
elif start == ('n'):
    print ('''they should have never given you your hunter license this is pathetic
 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
''')
name = input ('how rude of me ive never aske you for your name, mind if you tell me hunter')
print (f'ah {name}!! that name sounds like the name of a true warrior. now off you go hunter')

