#This short program will calculate your roadtrip expenses
distance = int(input('How many kilometers will you travel?: '))
lpk = int(input('How many kilos per liter does your vehicle get?: '))
fuel = float(input('What is the current price per liter of fuel?: '))

#Divide the distance of the route by your kilo per liter figure
amount_fuel = distance / lpk

#Multiply the number of liters by the price of fuel
total_cost = amount_fuel * fuel 

print('This trip will require ' + str(amount_fuel) + ' liters of fuel.')
print('At ' + str(fuel) + ' USD per liter.')
print('It will cost ' + str(total_cost) + ' USD in total.')
