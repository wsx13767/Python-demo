rooms = {
        'Hall' : {
                'south': 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },
        'Kitchen' : {
                'north' : 'Hall',
                'east'  : 'BathRoom',
                'item'  : 'food'
            },
        'Dining Room' : {
                'west' : 'Hall',
                'south': 'BathRoom',
                'item' : 'water'
            },
        'BathRoom' : {
                'north' : 'Dining Room',
                'west' : 'Kitchen',
                'item' : 'Boss'
            }
    }
#door = ['Hall','Kitchen','Dining Room','BathRoom']
bag = []
room = 'Hall'

def getMap():
    print('------------------------------')
    print('|    Hall      | Dining Room |')
    print('|              |             |')
    if room == 'Hall' :
        print('|      *                     |')
    elif room == 'Dining Room' :
        print('|                     *      |')
    else :
        print('|                            |')
    print('|              |             |')
    print('|              |             |')
    print('------   ------------   ------')
    print('|              |             |')
    print('|              |             |')
    if room == 'Kitchen' :
        print('|      *                     |')
    elif room == 'BathRoom' :
        print('|                     *      |')
    else :
        print('|                            |')
    print('|              |             |')
    print('|              |             |')
    print('------------------------------')

def isWin() :
    if len(bag) == 3 :
        return True
    else :
        return False
count = 1
while True :
    if count == 1 :
        print('Do you want watch map. You have only one chance!')
        chance = input()
        if chance == 'yes' :
            count = count -1
            getMap()
   # print(rooms[room]['item'] == 'OO' )
    if isWin() :
        break
    try :
        if rooms[room]['item'] == 'Boss' :
            break
    except :
        print('')
    
    print('You are in the ' + room)
    print('Inventory : ' + str(bag))
    try :
        print('You see a ' + rooms[room]['item'])
    except :
        print('')
    method = input()
    if method.startswith('go') :
        place = method.split(' ')[1]
        try :
            room = rooms[room][place]
        except :
            print('!!!!!!!!!You can\'t ' + method + '!!!!!!!!!!')
    elif method.startswith('get') :
        try :
            if rooms[room]['item'] == method.split(' ')[1] :
                bag.append(rooms[room]['item'])
                del rooms[room]['item']
        except :
            print('No items in the room!!!!!!')
    else :
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
if isWin() :
    print('You are Win!!!!!')
else :
    print('You are GAME OVER!!!')
