#Dumkele Osegi PSID 1894081
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

gallon_of_paint = float(wall_area) / 350
paint_needed = gallon_of_paint

cans_needed = round(gallon_of_paint)

print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')


print('Cans needed:', cans_needed, 'can(s)\n')

can_color = {
    'Red': 35,
    'Blue': 25,
    'Green': 23,
}
can_color = int(input('Choose a color to paint the wall:'))
print('Cost of purchasing', can_color, 'paint:\n')
