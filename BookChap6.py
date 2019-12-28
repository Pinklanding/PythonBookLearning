#dictionary

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points=alien_0['points']
print(new_points)

alien_0['position_x']=13
alien_0['position_y']=5
print(alien_0)

alien_1={}
print(alien_1)
alien_1['speed']='fast'
alien_1['position_x']=0
alien_1['position_y']=0

alien_0['color']='yellow'
print(alien_0)

alien_0['speed']='slow'
fast_speed = 3
slow_speed = 1
def move(alien):
    if alien['speed']=='slow':
        alien['position_x'] += slow_speed
    else:
        alien['position_x'] += fast_speed
    print(alien)

move(alien_0)
move(alien_1)

del alien_0['color']
print(alien_0)

fav_lang = {
    'jen':'python',
    'ken':'c',
    'edw':'java',
    'phil':'python'
}

print("Jen's fav lang is " + fav_lang['jen'].title())

for key,value in alien_0.items():
    print(key)
    print(value)

for name,lang in fav_lang.items():
    print(name.title() + "'s fav lang is " + lang.title())

for name in fav_lang.keys():
    print(name)

for lang in fav_lang.values():
    print(lang)

if 'eri' not in fav_lang.keys():
    print("no this person")

print(sorted(fav_lang.keys()))
print(set(fav_lang.values()))

aliens = [alien_0, alien_1]
print(aliens)
for alien in aliens:
    print(alien)

aliens = []
ID=0
for alien_numer in range(30):
    ID += 1
    new_alien = {'ID':ID, 'color':'yellow', 'tools':['knife','hammer']}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)
print(len(aliens))

for alien in aliens[:2]:
    print(alien['ID'])
    for tool in alien['tools']:
        print(tool)

user = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'b':{
        'first':'1',
        'last':'2',
        'location':'a'
    }
}

for name, info in user.items():
    print(name)
    print(info['first'].title() + ' ' + info['last'].title() + ' lives in ' + info['location'].title())

