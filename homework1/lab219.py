lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))
water = int(input('Enter amount of water (in cups):\n'))
agave_nectar = (float(input('Enter amount of agave nectar (in cups):\n')))
servings = int(input('How many servings does this make?\n'))
print('')
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')



desired_servings = int(input('How many servings would you like to make?\n'))
print('')

lemon_juice = desired_servings * .3333333
water = desired_servings * 2.66666667
agave_nectar = desired_servings * 0.41666667

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings, 'servings'), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')

converted_lemon = lemon_juice * 0.0625
converted_water = water * 0.0625
converted_agave_nectar = agave_nectar * 0.0625

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings, 'servings'), 'servings')
print('{:.2f}'.format(converted_lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(converted_water), 'gallon(s) water')
print('{:.2f}'.format(converted_agave_nectar), 'gallon(s) agave nectar')

