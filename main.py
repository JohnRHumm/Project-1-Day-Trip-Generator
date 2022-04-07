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


def atlanta_activities():
    atlanta_activities_list = ["Falcons' game", 'Marin Luther King Jr. National Historical Park','Georgia Aquarium',\
        'Atlanta Botanical Garden','World of Coca-Cola','High Museum of Art', 'Center for Puperty Arts',\
            'Oakland Cemetery', 'Zoo Atlanta','Jimmy Carter Presidential Library and Museum']
    return  atlanta_activities_list

def atlanta_restaurants():
    atlanta_restaurant_list = ['The Varisty','Miller Union','Masterpiece','Staplehouse','Spring','Sushi Hayakawa',\
        'Bacchanalia','Boccalupo', "B's Cracklin BBQ"]
    return atlanta_restaurant_list
    


activities_list = atlanta_activities
print(activities_list)

restaurant_list = atlanta_restaurants
print(restaurant_list)