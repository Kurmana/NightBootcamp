import random
start = 1

# choice = input('please pick one: kamen, nojnicy, bumaga: ')
game = ['kamen', 'nojnicy', 'bumaga']
while True:
    try:
        for i in game:
            gemo = random.choice(game)
            choice = input('please pick one: kamen, nojnicy, bumaga: ')
            if gemo == 'kamen' and choice == 'bumaga':
                print('vy vyigrali')
            if gemo == 'bumaga' and choice == 'kamen':
                print('you lost')
            if gemo == 'nojnicy' and choice == 'bumaga':
                print('you lost')
            if gemo == 'bumaga' and choice == 'nojnicy':
                print('vy vyigrali')
            if gemo == 'nojnicy' and choice == 'kamen':
                print('vy vyigrali')
            if gemo == 'kamen' and choice == 'nojnicy':
                print('you lost')
            if gemo == choice:
                print('nichiya')
            start = int(input('if you want to try again press 1 '))
            if start != 1:
                print('bye')
                break

    except:
        print('please only enter kamen or nojnicy or bumaga')

