'''
Heroes beta 1.1
hy
2018-8-21
'''
import random
welcome = 'Welcome to heros world!'
map = ['#'] * 9
mapins = "\n-*- The world is like this! -*-\n %s \n '*'is your location " % (map,)
mak='-'
instruction = '''
control your hero:
| A for 'left' | D for 'right' |
'''

print (mak*60)
print('|                ',welcome,'                 |')
print("| The world is like this #####,'A'for left,'D'for right ",'  |')
print (mak*60)
name = input('Input your name:')
hp = 100
if not name:
    name = 'player 01'
usermsg = {'name': name, 'hp': hp}
print("Your hero's name is:", usermsg['name'], 'and HP is:', usermsg['hp'])
print(mapins, instruction)
def apple(hp):
    hp+=10
    return hp
def bomb(hp):
    hp-=10
    return hp
eventlist=[apple,bomb]
point = 0
while True:
    map[point] = '*'
    print('You are here :%s' % ''.join(map))
    userinput = input('go or quit:')
    if userinput == 'Q':
        print('You quit the game!')
        break
    elif userinput == 'A' and point > 1:
        map[point] = '#'
        point -= 1
        usermsg['hp'] = random.choice(eventlist)(usermsg['hp'])
        print('blood is %s' % usermsg['hp'])

    elif userinput == 'D' and point < 8:
        map[point] = '#'
        point += 1
        usermsg['hp'] = random.choice(eventlist)(usermsg['hp'])
        print('blood is %s' % usermsg['hp'])

    else:
        print('Please input the correct order!')
        print(instruction)


