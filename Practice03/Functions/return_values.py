#1 It is possible to return and pass any datatype in functions
def team_members(number):
    if number == 1:
        return f'Team {number}: {["Monkey D Luffy", "Roronoa Zoro", "Black leg Sanji"]}'
    
    if number == 2:
        return f'Team {number}: {["Naruto", "Sasuke", "Sakura"]}'
    
    if number == 3:
        return f'Team {number}: {["Iron man", "Thor", "Capitan America"]}'
    
#2 Using returned values
def iron_man_info():
    return {
        "name": "Tony Stark",
        "team": "Avengers",
        "status": "Genius Billionaire"
    }

data = iron_man_info()
name = data["name"]
team = data["team"]


#3 Printinf returned values
def world_war_two_end():
    return 1945

world_war_two_end() # You won't see the result
print(world_war_two_end()) # You will see the result

#4
def captain_america_info():
    return ("Steve Rogers", 1941, "Super Soldier")
