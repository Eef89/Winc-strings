# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#1
player_1 = 'Marco van Basten'
player_2 = 'Ruud Gullit'
#2
goal_0 = 32
goal_1 = 54
#3
scorers = f'{player_2} {str(goal_0)}, {player_1} {str(goal_1)}'
print(scorers) 
#4
report = f'{player_2} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)
#part 2
#1
player = 'Marco van Basten'
#2
first_name_find = player.find(' ')
first_name = player[:first_name_find]
print(first_name)
#3
last_name_len = len(player) - player.find(' ') - 1
print(last_name_len)
#3 methode 2
last_name_len2 = len(player[first_name_find+1:])
print(last_name_len2)
#4
name_short = f'{player[:1]}. {player[first_name_find+1:]}'
print(name_short)
#5
chant = f'{first_name}! ' * (first_name_find - 1) + f'{first_name}!' 
print(chant)
#6
good_chant = (chant[:-1] != ' ')
print(good_chant)

# print(good_chant)