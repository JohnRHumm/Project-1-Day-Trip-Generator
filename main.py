# Project 1: Day Trip Generator

# (5 points):  As a developer, I want to make at least three commits with descriptive messages. 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
# (5 points):  As a user, I want a destination to be randomly selected for my day trip. 
# (5 points):  As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points):  As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points):  As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points):  As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

# Functions for activities and restaurants for individual cities

import random
import os

# This code was taken from the www. Breaks the rule of simple function but not
# key to program. Just makes things easier to debug
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def atlanta_activities():
    atlanta_activities_list = ["Falcons' game", 'Marin Luther King Jr. National Historical Park','Georgia Aquarium',\
        'Atlanta Botanical Garden','World of Coca-Cola','High Museum of Art', 'Center for Puperty Arts',\
            'Oakland Cemetery', 'Zoo Atlanta','Jimmy Carter Presidential Library and Museum']
    return  atlanta_activities_list

def atlanta_restaurants():
    atlanta_restaurant_list = ['The Varisty','Miller Union','Masterpiece','Staplehouse','Spring','Sushi Hayakawa',\
        'Bacchanalia','Boccalupo', "B's Cracklin BBQ"]
    return atlanta_restaurant_list
    
def boston_activities():
    boston_activities_list = ['Red Sox game', "Patriots' game",'Boston Marathon',\
        'Boston Tea Party Ships & Museum','John F. Kennedy Presidential Museum and Library',\
            'Museum of Science', 'Isabela Steward Gardner Museum','Samuel Adams Brewery',\
            'New England Aquarium', 'Castle Island']
    return  boston_activities_list

def boston_restaurants():
    boston_restaurant_list = ['Mooncusser','Nighshade Noodle Bar','Sarma','Geppetto','Kava Neo-Taverna','Urban Health',\
        'Barra','Cafe Sushi','Celeste','Bar Volpe']
    return boston_restaurant_list

def chicago_activities():
    chicago_activities_list = ["Cubs' game", "Bears' game",'Willis Tower',\
        'Magnificient Mile','The Bean','Shedd Aquarium','Field Museum',\
            'Adler Planetarium', 'Lincoln Park Zoo','Museum of Scinece and Industry']
    return  chicago_activities_list

def chicago_restaurants():
    chicago_restaurant_list = ['Superdawg Drive-In','Lost Larson',"Luella's Southern Kitchen",'Smoque BBQ','Lula Cafe',\
        "Johnnie's Beef",'Porto','Lardon','Naudi Signature Pizza','The Walnut Room']
    return chicago_restaurant_list

def houston_activities():
    houston_activities_list = ["Texans' game", 'Space Center Houston','National Museum of Funeral History',\
        'The Museum of Fine Arts, Houston','Houston Museum of Natural Science','The Hobby Center',\
        'San Jacinto Monument and Museum','Gerald D. Hines Waterwall Park', 'Beer Can House','Twilight Epiphany Skyspace']
    return  houston_activities_list

def houston_restaurants():
    houston_restaurant_list = ["Ninfa's Original on Navigation",'La Carafe',"Saigon Hustle",'Underelly Burger','Loro',\
        "Trattoria Sofia",'Chivos','Casa Nomad','Maize','Urbe']
    return houston_restaurant_list

def kansas_city_activities():
    kansas_city_activities_list = ["Chiefs' game", 'National World War I Museum and Memorial',\
        'Boulevard Brewery','Nelson-Atkins Museum of Art','City Market','American Jazz Museum',\
        'Erinie Miller Nature Center','Blue Room Jazz Club', 'Worlds of Fun']
    return  kansas_city_activities_list

def kansas_city_restaurants():
    kansas_city_restaurant_list = ["Joe's Kansas City Barbeque",'Jones BBQ',"Covino Supper Club",'Char Bar','Gram & Dun',\
        "Pirate's Bone Burgers","Lidia's",'Pigwich','The Rieger',"Mickey's Hideaway"]
    return kansas_city_restaurant_list




# Define city list and methods of travel
city_list = ['Atlanta','Boston','Chicago','Houston','Kansas City']

transportation_list = ['Uber','Rental Car','Train','Skateboard','Bicycle','Segway',\
    'Moped','Electric Scooter','Rickshaw','Rollerblades']

clearConsole()

# Determine City
print('Welcome to Vacation Planner 2022. Your automated trip planner')
user_city_list = city_list
user_happy_with_city = False
user_happy_with_activity = False
items_left_in_city_list = len(user_city_list)
city_no_count = 0
refresh_city_list = True
refresh_activity_list = True
refresh_restaurant_list = True
refresh_transportation_list = True
user_undecided = True

while user_undecided:
    # Select City    
    while user_happy_with_city == False and items_left_in_city_list > 0:
        if refresh_city_list:
            user_city_list = city_list
        destination = random.choice(user_city_list)
        if items_left_in_city_list == 1:
            print('You are very particular. Only one city left in the list')
        if city_no_count == 0:
            print(f'Your destination city is: {destination}')
            refresh_city_list = False
        else:
            print(f'Your new destimation city is: {destination}')
        
        user_response = input(f'Do you accept {destination} as your destination city? (y/n): ')   
        if user_response.capitalize() == 'Y':
            user_happy_with_city = True
            print('Destination city accepted!')
            print(f'Welcome to {destination}') # add city slogan if time
        else:
            print('A new destination city will be selected')
            print(f'{destination} has been removed as an option')
            user_city_list.remove(destination)
            items_left_in_city_list = len(user_city_list)
            city_no_count +=1
        if items_left_in_city_list == 0:
            print("No cities left to choose. Looks like you'll be at home.")
            print('Enjoy your Staycation!')
            destination = 'Home'
            user_happy_with_city = True

    # Get custom activity and restaurant list
    if destination == 'Atlanta':
        if refresh_activity_list:
            user_activity_list = atlanta_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = atlanta_restaurants()
            refresh_restaurant_list = False
    elif destination == 'Boston':
        if refresh_activity_list:
            user_activity_list = boston_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = boston_restaurants()
            refresh_restaurant_list = False
    elif destination == 'Chicago':
        if refresh_activity_list:
            user_activity_list = chicago_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = chicago_restaurants()
            refresh_restaurant_list = False
    elif destination == 'Houston':
        if refresh_activity_list:
            user_activity_list = houston_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = houston_restaurants()
            refresh_restaurant_list = False
    elif destination == 'Kansas City':
        if refresh_activity_list:
            user_activity_list = kansas_city_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = kansas_city_restaurants()
            refresh_restaurant_list = False
    else:
        user_activity_list = {'Sitting on couch'}
        user_restaurant_list = {"McDonald's"}
        refresh_activity_list = False
        refresh_restaurant_list = False
    
    # Now Select Activity
    items_left_in_activity_list = len(user_activity_list)
    activity_no_count = 0
    
    while user_happy_with_activity == False and items_left_in_activity_list > 0:
        activity = random.choice(user_activity_list)
        if items_left_in_activity_list == 1:
            print('You are very particular. Only one activity left in the list')
        if activity_no_count == 0:
            print(f'Your activity is : {activity}')
            refresh_activity_list = False
        else:
            print(f'Your new activity is: {activity}')
        
        user_response = input(f'Do you accept {activity} as your activity? (y/n): ')   
        if user_response.capitalize() == 'Y':
            user_happy_with_activity = True
            print('Activity accepted!')
            print(f'Enjoy {activity}') 
        else:
            print('A new activity will be selected')
            print(f'{activity} has been removed as an option')
            user_activity_list.remove(activity)
            items_left_in_activity_list = len(user_activity_list)
            activity_no_count +=1
        if items_left_in_activity_list == 0:
            print("No activities left to choose.")
            print("Enjoy McDonald's")
            destination = "McDonald's"
            user_happy_with_activity = True


    items_left_in_restaurant_list = len(user_restaurant_list)
        
        





