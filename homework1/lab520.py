service_1total = 0
service_2total = 0

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

service_one = input('Select first service:\n')
service_two = input('Select second service:\n')

if service_one == 'Oil change':
    service_1total = 35
elif service_one == 'Tire rotation':
    service_1total = 19
elif service_one == 'Car wash':
    service_1total = 7
elif service_one == 'Car wax':
    service_1total = 12
elif service_one == '-':
    service_1total = 'No service'

if service_two == 'Oil change':
    service_2total = 35
elif service_two == 'Tire rotation':
    service_2total = 19
elif service_two == 'Car wash':
    service_2total = 7
elif service_two == 'Car wax':
    service_2total = 12
elif service_two == '-':
    service_2total = 'No service'

print('')
print("Davy's auto shop invoice\n")
print('Service 1: ' + service_one + ', $' + str(service_1total))
print('Service 2: ' + service_two + ',' ' $' + str(service_2total))
print('')
print('Total: $' + str(service_1total + service_2total))
