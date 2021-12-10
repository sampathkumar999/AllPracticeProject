
key=9
count=0
limit=3
while count<limit:
    guess=int(input('enter guess:'))
    count=count+1
    if guess==key:
        print('you win!')
        break
else:
     print('you lost')
       
        

    
