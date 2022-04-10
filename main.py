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

import errno
import random
import os


# This code was taken from the www. Breaks the rule of simple function but not
# key to program. Just makes things easier to debug
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Define city activities and restaurant lists
def atlanta_activities():
    atlanta_activities_list = ["Falcons' game", 'Marin Luther King Jr. National Historical Park','Georgia Aquarium',\
        'Atlanta Botanical Garden','World of Coca-Cola','High Museum of Art', 'Center for Puppetry Arts',\
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
    boston_restaurant_list = ['Mooncusser','Nighshade Noodle Bar','Sarma','Geppetto','Kava Neo-Taverna',\
        'Urban Health','Barra','Cafe Sushi','Celeste','Bar Volpe']
    return boston_restaurant_list

def chicago_activities():
    chicago_activities_list = ["Cubs' game", "Bears' game",'Willis Tower',\
        'Magnificient Mile','The Bean','Shedd Aquarium','Field Museum',\
            'Adler Planetarium', 'Lincoln Park Zoo','Museum of Science and Industry']
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
        'Erinie Miller Nature Center','Blue Room Jazz Club', 'Worlds of Fun','Kemper Museum of Contemporary Art']
    return  kansas_city_activities_list

def kansas_city_restaurants():
    kansas_city_restaurant_list = ["Joe's Kansas City Barbeque",'Jones BBQ',"Covino Supper Club",'Char Bar','Gram & Dun',\
        "Pirate's Bone Burgers","Lidia's",'Pigwich','The Rieger',"Mickey's Hideaway"]
    return kansas_city_restaurant_list

def seattle_activities():
    seattle_activities_list = ["Seahwaks' game", 'Mt. Rainer Day Trip',\
        'Beneath the streets Underground History Tour','Pike Place Market','Olympic National Park Tour','The Museum of Flight',\
        'Chihuly Garden and Glass','Woodland Park Zoo', 'Space Needle','Museum of Pop Culture']
    return  seattle_activities_list

def seattle_restaurants():
    seattle_restaurant_list = ["Simburna Indian Restaurant","Zylberschtein's","Cafe Juanita",'Cafe Munir','Canlis',\
        "Archipelago","Meesha",'Sushi Kaskiba','Bar del Coro',"Super Six"]
    return seattle_restaurant_list

def city_nickname(city):
    if city == 'Atlanta':
        nickname = "Hot'Lanta"
    elif city == 'Boston':
        nickname = "Beantown"
    elif city == 'Chicago':
        nickname = "The Windy City"
    elif city == 'Houston':
        nickname = 'Space City'
    elif city == 'Kansas City':
        nickname = 'Cowtown'
    elif city == 'Seattle':
        nickname = 'Emerald City'
    else:
        nickame = ''
    return nickname


def cities():
    city_list = ['Atlanta','Boston','Chicago','Houston','Kansas City','Seattle'] 
    return city_list

def transportation_type():
    transportation_list = ['Uber','Rental Car','Train','Skateboard','Bicycle','Segway',\
    'Moped','Electric Scooter','Rickshaw','Rollerblades']
    return transportation_list


def get_y_or_n_from_user(input_message):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        user_input = (input(input_message)).upper()  
        if user_input == 'Y' or user_input == 'N':
            waiting_for_valid_response = False
        elif user_input == 'YES':
            user_input = 'Y'
            waiting_for_valid_response = False
        elif user_input == 'NO':
            user_input = 'N'
            waiting_for_valid_response = False
        else:
            print(f'You entered {user_input}')    
            print('Your response must be either a y (Yes) or n (No)')  
    return user_input



clearConsole()


print("Welcome to Vacation Planner 2022, your automated trip planner")

# Initial settings

user_happy_with_city = False
user_happy_with_activity = False
user_happy_with_restaurant = False
user_happy_with_transportation = False
refresh_city_list = True
refresh_activity_list = True
refresh_restaurant_list = True
refresh_transportation_list = True
user_undecided = True

city_no_count = 0
restaurant_no_count = 0
activity_no_count = 0
transportation_no_count = 0
rejected_city_list = []
rejected_activity_list = []
rejected_restaurant_list = []
rejected_transportation_list = []

# Main Loop

while user_undecided:
    # Select City 
    
    if refresh_city_list:
         user_city_list = cities()
         refresh_city_list = False
    items_left_in_city_list = len(user_city_list)
    if user_happy_with_city == False:
        print('Selecting Destination City')
    while user_happy_with_city == False and items_left_in_city_list >= 0:
        if items_left_in_city_list > 0:
            destination = random.choice(user_city_list)
            if items_left_in_city_list == 1:
                print('You are very particular. Only one city left in the list')
            if city_no_count == 0:
                print(f'Your destination city is: {destination.upper()}')
            else:
                print(f'Your new destimation city is: {destination.upper()}')
           
            message_to_user = (f'Do you accept {destination} as your destination city? (y/n): ')
            user_response = (get_y_or_n_from_user(message_to_user)).upper()
            if user_response == 'Y':
                user_happy_with_city = True
                print('Destination city accepted!')
                print(f'Welcome to {city_nickname(destination)}') # add city slogan if time
                print('----------')
                print('')
            else:
                print(" ")
                print('A new destination city will be selected')
                print(f'{destination} has been removed as an option')
                user_city_list.remove(destination)
                items_left_in_city_list = len(user_city_list)
                city_no_count +=1
                rejected_city_list.append(destination) 
        else:
            print("No cities left to choose. Looks like you'll be at home.")
            print('Enjoy your Staycation!')
            destination = 'Home'
            activity = 'Sitting on Couch'
            restaurant = "McDonald's"
            transportation = 'Walking'
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
    elif destination == 'Seattle':
        if refresh_activity_list:
            user_activity_list = seattle_activities()
            refresh_activity_list = False
        if refresh_restaurant_list:
            user_restaurant_list = seattle_restaurants()
            refresh_restaurant_list = False
    else:
        activity = 'Sitting on Couch'
        restaurant = "Mc'Donalds"
        transportation = 'Walking'
        user_happy_with_activity = True  
        user_happy_with_restaurant = True  
        user_happy_with_transportation = True 
        user_activity_list = []
        user_restaurant_list = []
        user_transportation_list = []
        refresh_transportation_list = False
        rejected_transportation_list = transportation_type()
    
    # Now Select Activity
    items_left_in_activity_list = len(user_activity_list)
    if user_happy_with_activity == False:
        print(f'Selecting Activity in {destination}')
    while user_happy_with_activity == False and items_left_in_activity_list >= 0:
         if items_left_in_activity_list > 0:
            activity = random.choice(user_activity_list)
            if items_left_in_activity_list == 1:
                print('You are very particular. Only one activity left in the list')
            if activity_no_count == 0:
                print(f'Your activity is : {activity.upper()}')
            else:
                print(f'Your new activity is: {activity.upper()}')
            message_to_user = (f'Do you accept {activity} as your activity? (y/n): ')
            user_response = (get_y_or_n_from_user(message_to_user)).upper()
            if user_response == 'Y':
                user_happy_with_activity = True
                print('Activity accepted!')
                print(f'Enjoy {activity}') 
                print('----------')
                print('')
            else:
                print(" ")
                print('A new activity will be selected')
                print(f'{activity} has been removed as an option')
                user_activity_list.remove(activity)
                items_left_in_activity_list = len(user_activity_list)
                activity_no_count +=1
                rejected_activity_list.append(activity) 
         else:
            print("No activities left to choose.")
            print("Enjoy sitting your behind on your couch!")
            activity = "Sitting on Couch"
            user_happy_with_activity = True

    # Now Select Restaurant
    items_left_in_restaurant_list = len(user_restaurant_list)
    if user_happy_with_restaurant == False:
        print(f'Selecting Restaurant in {destination}')
    while user_happy_with_restaurant == False and items_left_in_restaurant_list >= 0:
        if items_left_in_restaurant_list > 0:
            restaurant = random.choice(user_restaurant_list)
            if items_left_in_restaurant_list == 1:
                print('You are very particular. Only one restaurant left in the list')
            if restaurant_no_count == 0:
                print(f'Your restaurant is : {restaurant.upper()}')
                refresh_restaurant_list = False
            else:
                print(f'Your new restaurant is: {restaurant.upper()}')
            message_to_user = (f'Do you accept {restaurant} as your restaurant? (y/n): ')
            user_response = get_y_or_n_from_user(message_to_user)
            if user_response.upper() == 'Y':
                user_happy_with_restaurant = True
                print('Restaurant accepted!')
                print(f'Enjoy {restaurant}') 
                print('----------')
                print('')
            else:
                print(" ")
                print('A new restaurant will be selected')
                print(f'{restaurant} has been removed as an option')
                user_restaurant_list.remove(restaurant)
                items_left_in_restaurant_list = len(user_restaurant_list)
                restaurant_no_count +=1
                rejected_restaurant_list.append(restaurant) 
        else:
            print("No restaurants left to choose.")
            print("Enjoy your Big Macs at McDonald's!")
            restaurant = "McDonald's"
            user_happy_with_restaurant = True

    # Now Select Transportation
    if refresh_transportation_list:
        user_transportation_list = transportation_type()
        refresh_transportation_list = False
    items_left_in_transportation_list = len(user_transportation_list)
    if user_happy_with_transportation == False:
        print(f'Selecting Method of Transportation around {destination}')
    while user_happy_with_transportation == False and items_left_in_transportation_list >= 0:
        if items_left_in_transportation_list > 0:
            transportation = random.choice(user_transportation_list)
            if items_left_in_transportation_list == 1:
                print('You are very particular. Only one method of transportation left in the list')
            if transportation_no_count == 0:
                print(f'Your method of transportation is : {transportation.upper()}')
                refresh_transportation_list = False
            else:
                print(f'Your new method of transportation is: {transportation.upper()}')
            message_to_user = (f'Do you accept {transportation} as your method of transportation? (y/n): ')
            user_response = get_y_or_n_from_user(message_to_user)
            if user_response.upper() == 'Y':
                user_happy_with_transportation = True
                print('Method of transportation accepted!')
                print(f'You will be getting around by {transportation}') 
                print('----------')
                print('')
            else:
                print(" ")
                print('A new method of transportation will be selected')
                print(f'{transportation} has been removed as an option')
                user_transportation_list.remove(transportation)
                items_left_in_transportation_list = len(user_transportation_list)
                transportation_no_count +=1
                rejected_transportation_list.append(transportation) 
        else:
            print("No method of transportation left to choose.")
            print("Enjoy your walking around on foot!")
            transportation = "Walking"
            user_happy_with_transportation = True
    
    print('You have made all of your selections') 
    user_pressed_c = False 
    while user_pressed_c == False:
        user_input = (input('Please press C to continue and summarize your selections: ')).upper()
        if user_input == 'C':
            user_pressed_c = True

    # Summarize selections
    clearConsole()
    print('**** Summary of Selections ****')
    print(f'Destination:  {destination}')
    print(f'Activity: {activity}')
    print(f'Restaurant: {restaurant}')
    print(f'Method of Transportation: {transportation}')

    # Final chance for user to make changes
    message_to_user = (f'Do you accept everything listed above for your trip? (y/n): ')
    user_response = (get_y_or_n_from_user(message_to_user)).upper()
    if user_response == 'Y':
        print('Fantastic! Your trip details have been finalized!')
        user_undecided = False
    else:
        print('What do you wnat to change?')
        valid_response = False
        while valid_response == False:
            if destination == 'Home':
                message_to_user = ("You currently haven't selected a city and are staying home. " 
                    "If you wnat to change your trip you need to select a valid destination first.") 
                print(message_to_user)
                user_input = input('Please type (D) to change your destination: ').upper()
                if user_input == 'D':
                    valid_response = True
            else:
                message_to_user = ("Please type (D) to change destination (A) to change activity (R) to change resturant " 
                    "or (T) to change Trasnportation: ")
                user_input =  input(message_to_user).upper()
                if user_input == 'D' or user_input == 'A' or user_input == 'R' or user_input == 'T':
                    valid_response = True
        if user_input == 'D':
            message_to_user = ("Keep in mind if you change your destination, your activity and "
                "restaurant will change too. Do you still want to change? (y/n): ")
            user_response = (get_y_or_n_from_user(message_to_user)).upper()
            if user_response == 'Y':
                 if not destination == 'Home':
                    user_city_list.remove(destination) 
                    rejected_city_list.append(destination)
                 user_happy_with_city = False
                 user_happy_with_activity = False
                 user_happy_with_restaurant = False
                 refresh_activity_list = True
                 refresh_restaurant_list = True
                 restaurant_no_count = 0
                 activity_no_count = 0
                 rejected_activity_list = []
                 rejected_restaurant_list = []
                 print(f'Your list of rejected cities are {rejected_city_list}')
                 message_to_user = ('Do you want keep these cities on your rejected list (y/n): ')
                 user_response_2nd = (get_y_or_n_from_user(message_to_user)).upper()
                 if user_response_2nd == 'Y':
                     refresh_city_list = False
                 else:
                     refresh_city_list = True
                     rejected_city_list = []
                     city_no_count = 0
                 print(" ")
            else:
                continue
        elif user_input == 'A':
             message_to_user = ('Do you want to change your activity? (y/n): ')    
             user_response = (get_y_or_n_from_user(message_to_user)).upper()
             if user_response == 'Y':
                 if not activity == 'Sitting on Couch':
                    user_activity_list.remove(activity) 
                    rejected_activity_list.append(activity)
                 user_happy_with_activity = False
                 print(f'Your list of rejected activities are {rejected_activity_list}')
                 message_to_user = ('Do you want keep these activities on your rejected list (y/n): ')
                 user_response_2nd = (get_y_or_n_from_user(message_to_user)).upper()
                 if user_response_2nd == 'Y':
                     refresh_activity_list = False
                 else:
                     refresh_activity_list = True
                     rejected_activity_list = []
                     activity_no_count = 0
                 print(" ")
             else:
                 continue
        elif user_input == 'R':
             message_to_user = ('Do you want to change your restaurant? (y/n): ')    
             user_response = (get_y_or_n_from_user(message_to_user)).upper()
             if user_response == 'Y':
                 if not restaurant == "McDonald's":
                    user_restaurant_list.remove(restaurant) 
                    rejected_restaurant_list.append(restaurant)
                 user_happy_with_restaurant = False
                 print(f'Your list of rejected restaurants are {rejected_restaurant_list}')
                 message_to_user = ('Do you want keep these restaurants on your rejected list (y/n): ')
                 user_response_2nd = (get_y_or_n_from_user(message_to_user)).upper()
                 if user_response_2nd == 'Y':
                     refresh_restaurant_list = False
                 else:
                     refresh_restaurant_list = True
                     rejected_restaurant_list = []
                     restaurant_no_count = 0
                 print(" ")
             else:
                 continue
        elif user_input == 'T':
             message_to_user = ('Do you want to change your method of trasnportation? (y/n): ')    
             user_response = (get_y_or_n_from_user(message_to_user)).upper()
             if user_response == 'Y':
                 if not transportation == "Walking":
                    user_transportation_list.remove(transportation) 
                    rejected_transportation_list.append(transportation)
                 user_happy_with_transportation = False
                 print(f'Your list of rejected methos of transportation are {rejected_transportation_list}')
                 message_to_user = (f'Do you want keep these methods of transportation on your rejected list (y/n): ')
                 user_response_2nd = (get_y_or_n_from_user(message_to_user)).upper()
                 if user_response_2nd == 'Y':
                     refresh_trasnportation_list = False
                 else:
                     refresh_transportation_list = True
                     rejected_transportation_list = []
                     transportation_no_count = 0
                 print(" ")
             else:
                 continue
        else:
            message_to_user('Internal Error')
            err = -1
            break

# Now Print final message to user

if not destination == 'Home':
     print(" ")
     print(" ")
     message_to_user = (f"Enjoy your trip to {destination}, {city_nickname(destination)}, where you will get around the city by "
        f"{transportation}.")
     print(message_to_user)
     message_to_user =(f"During the day you will go to the/a {activity}. You will finsh your day "
        f"by dining at {restaurant}.")
     print(message_to_user)
     print("Please enjoy your trip and thank you for using the 2022 Trip Planner")
     print(" ")
     print(" ")
     
else:
     print(" ")
     print(" ")
     message_to_user = ("Looks like you will be staying at home on your couch eating McDonald's and "
        "walking around on foot. Enjoy!")
     print(message_to_user)
     print(" ")
     print(" ")





        





