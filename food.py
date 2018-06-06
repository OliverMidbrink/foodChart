import requests
from bs4 import BeautifulSoup


'''
get_food()  <--   if no arguments are passed into the get_food() function, it will automatically return the food for the current week

get_food(24)  <-- if an integer is passed through, the function will return food for the week
                with that number. get_food(24) would return the food for week 24

get_food('next') <-- this will return the food for next week
'''


def get_food(week=-1):
    #These arrays will be returned when calling the function
    standard = []
    vegetarian = []

    week_number = week
    if (week is -1):
        #Get the week number automatically
        r0 = requests.get('https://vecka.nu/')
        s0 = BeautifulSoup(r0.text, 'lxml')
        week_number = int(s0.find('time').text)
    elif(week is 'next'):
        r0 = requests.get('https://vecka.nu/')
        s0 = BeautifulSoup(r0.text, 'lxml')
        week_number = int(s0.find('time').text)+1   # +1 will ensure the function returns the food for next week

    #Get the food info
    r1 = requests.get('https://mpi.mashie.com/public/menu/KK%20Djursholm/17EBA4A7')
    r1.encoding = 'utf-8'

    s1 = BeautifulSoup(r1.text, 'lxml')
    class_input = 'container-fluid main-clear container-week week-{}'.format(week_number)
    r = s1.find('div', {'class':class_input})
    if(r is not None):
        food_info = r.find_all('strong')
        i=0
        for part in food_info:
            food = part.find('span').text
            if(i is 0):
                standard.append(food)
                i=1
            else:
                vegetarian.append(food)
                i=0
    else:
        print('The week you entered does not contain any information')

    return standard, vegetarian





def print_array(input_array): #Just used for printing arrays in a prettier way
    i=0
    for item in input_array:
        i+=1
        print(i,': ',item)








''' Simple Example of Usage '''

'''

s,v = get_food() #Since no arguments are passed, it will get the food for the current week      s recieves the standard food and v recieves the vegetarian food

print('\nStandard\n')
print_array(s)

print(*s)

print('\nVegetarian\n')
print_array(v)

'''
