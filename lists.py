#list in Python - list []
# {} - purpose
players=['Cena','Reign','Orton','Styles']
print (players)
print (players[2])
print (players[-2])
players[0]='Brawn'
print (players[0])
print (players[2])
print (players[-1])
print (players[-2])
players.append('Rock') # Append add 1 item at end
print (players[-1])
players.extend(['Stone Cold','Kane']) # extend add multiple items in end
more_players=(['HHH','Shawn'])
players.extend(more_players)
print (players)
# insert methods is used to add the items in index position
players.insert(0,'Lesnar')
players.insert(2,'Goldberg')
print (players)
players.reverse()
print ("the reverse order of players is: {}". format(players))
#Slices
players=['Cena','Reign','Orton','Styles','Rusev','Cena']
raw_players=players[0:1] # returns only 0. the last index not returned
print ('Players in RAW includes : {}'. format(raw_players)) # user {} to retrive list
raw_players=players[0:2]
print ('Players in RAW includes : {}'. format(raw_players))
champ_players=players[:4]
print ('Champion Players includes : {}'. format(champ_players))
smackdown_players=players[2:4]
print ('Players in Smackdown includes : {}'. format(smackdown_players)) 
smackdown_players=players[-3:]
print ('Players in Smackdown includes : {}'. format(smackdown_players)) 

#String slicing
print(players)
alphabets='abcdefghijklmnopqrstuvwxyz'
search_alphabets=alphabets[2:10]
print (alphabets[10])
print (search_alphabets)

#index
players_index=players.index('Cena')
print (players_index)
#players_index=players.index('Kane') # ValueError: 'Kane' is not in list - Error Handling
#print (players_index)

#try and Except
try:
    players_index=players.index('Kane')
except:
    players_index='Kane has resigned from WWE'
print(players_index)   
