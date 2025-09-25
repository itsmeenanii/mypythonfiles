#guessing game
i=1
while i<=3 :
    guess=int(input('Guess: '))
    if guess==3 :
        print('You won !!!')
        break
    i=i+1
else :
    print('Sorry You failed !!!')         
