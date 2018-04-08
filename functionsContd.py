# function contd
def player_name():
    name=input("Enter the name of player : ")
    return name

def player_sport():
    sport=input("Enter the name of the Sport : ")
    return sport

def getname_sport(name,sport):
    print ( 'Legendary player {} gets hall of fame award for {} this year'. format(name,sport))

def name_sport():
      name=player_name()
      sport=player_sport()
      getname_sport(name,sport)
          
name_sport()
