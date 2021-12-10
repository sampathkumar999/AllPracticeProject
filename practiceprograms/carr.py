command=''
started=False
while True:
    command=input('> ').lower()
    if command=='start':
        if started:
            print('car is already started')
        else:
            started=True
            print('car has started')
    elif command=='stop':
        if not started:
            print('car is already stopped')
        else:
            started=False
            print('car has stopped')
    elif command=='help':
        print('''To start the car enter start
To stop the car enter Stop
To quit from game enter quit''')
        
    elif command==('quit'):
        break
else:
    print("i didn't understand")
    
    
