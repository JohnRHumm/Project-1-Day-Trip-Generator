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
        "Johnnie's Beef",'Porto','Lardon','Naudi Signature Pizza']
    return chicago_restaurant_list

# Define city list and methods of travel
city_list = {'Atlanta','Boston','Chicago'}

type_of_travel_list = {'Uber','Rental Car','Train','Skateboard','Bicycle','Segway',\
    'Foot','Electric Scooter','Rickshaw','Rollerblades'}




activities_list = atlanta_activities()
print(activities_list)

restaurant_list = atlanta_restaurants()
print(restaurant_list)