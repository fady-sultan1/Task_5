name = input('your name: ')
age =input('Age: ')
age=int(age)-5
street =input('street:')
city =input('city:')
country= input('country:')
print(' "Name: '+ name +'"')
print('"Age: '+ str (age) +'"')
print('"Address: '+street+' '+ city +' '+ country+'"')

msg=f'''Hello  {name}  Your age is   {age} \
     Years Old, Your Address is ' {street +','+ city + ','+country}. '''
print(msg)

print(type(name),type(age),'\n',type(street),type(city),'\n',type(country))

msg_1=f''' "Hello '{name}', How Are You? \ """ Your Age Is "{age}" " + And Your Country Is: {country}'''
print(msg_1)


msg_2=f''' "Hello '{name}', How Are You? \ \n
""" Your Age Is "{age}"" + And \n
 Your City Is: {city} '''
print(msg_2)

name_1='Doaa  Reem'
print('First Letter Is ' +name_1 [0])
print('Third  Letter Is ' +name_1 [2])
print('Last  Letter Is ' +name_1 [-1] )


print(name_1 [7:10])
print(name_1[0:5])
print(name_1[2:8])
print(name_1[:-5:-1])
print(name_1[0:9:2])


name_2="$&$&Mohammed$&$&"
print(name_2.strip('$&'))


msg_3 = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg_3.replace('%7','Love'))
