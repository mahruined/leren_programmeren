import random
participants = []

loop = True
while loop:
    name = input('enter a name from one of the participants ')
    if name in participants:
        print('name already entered')
    else:
        participants.append(name)
        if len(participants) >2:
            another_name = input('do you want to enter another participant? ').lower()
            if another_name in ('nee','n','no'):
                loop = False
pairedparticipants = list(zip(participants[::2],participants[1::2]))
print (pairedparticipants)