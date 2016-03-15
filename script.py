"""caesar = "Graham"
praline = "John"
viking = "Teresa"

print (caesar)
print (praline)
print (viking)

print ('this is\'nt flying it\'s falling with style')

second_letter = "Bhaag" [1]
print (second_letter) 

elephant = " Helment Cat"

print (len(elephant))
elephant = "Helment Cat".lower()
print (elephant)
elephant= "Helment Cat".upper()
print (elephant)
elbow= 2.076
print (str(elbow))

the_machine_goes = "Ping"
print (the_machine_goes)

print ("the value of Pi is around "+ str(3+0.14))

# new

string_1 ="Camelot"
string_2 ="place"

print ("Let's not go to %s. 'Tis a sill %s." %(string_1, string_2))

# new

name = input("What is you name?")
quest = input ("What is your quest")
color = input ("What is your favourite color?")

print ("Ah, so your name is %s, your quest is %s,"\
"and your favourite color is %s." % (name, quest, color)) 

from datetime import datetime
now = datetime.now()

print ('%s:%s:%s %s/%s/%s' % (now.hour, now.minute, now.second, now.month, now.day, now.year))"""

"""# Like BEDMAS => Not, And, OR

def using_control_once():
    if True or False:
        return "Success #1"

def using_control_again():
    if 7>6:
        return "Success #2"

print (using_control_once())
print (using_control_again()) 

swer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return  False and False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return  6>7      # Make sure this returns False

# elif statements are only checked if if statements are false!!

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 3>4:    # Start coding here!
        return False# Don't forget to indent
        # the code inside this block!
    elif 4>3:
        return True# Keep going here.
        # You'll want to add the else statement, too!
    else:
        return "all of this is not true"
print (the_flying_circus()) """

#Piglatin traslator

##pyg = 'ay'
##
##original = input('Enter a word:') # input fxn takes feedback
##word = original.lower() # store orginal word is lower case
##first = word[0] # takes the first letter of the word
##new_word = word[1:len(word)]+first+pyg # get rid of the first letter adds it to the end and applies the suffix
##
##if len(original) > 0 and original.isalpha(): # check for numbers
##    print (new_word)
##else:
##    print ('empty') # empty printed if numbers or empty

##word = input ("lets do this?")
##pyg = "ay"
##
##if len(word)>0 and word.isalpha:
##    org=word.lower()
##    first=word[0]
##    new_word= org[1:len(word)]+first+pyg
##    print(new_word)
##else:
##    print ("where")

"""random"""
##print ("Hi I'm the profile generator. Let's make your profile!")
##name = input ("What's your name?")
##if len(name)>0:
##    age = input ("What's your age?")
##    if len(age)>0:
##        like = input("What do you like to do?")
##        if len(like)>0:
##            print ("Hi, my name is %s, I am %s and I like %s." % (name, age, like))
##        else:
##            print("don't you like do stuff?")
##    else:
##        print("No age entered!")
##else:
##    print("No name entered!")

"""definitions"""
##def cube(number):
##    return number**3
##
##def by_three(number):
##   if number%3<1:
##    return cube(number)   
##   else: 
##       return False
##
""" definitions continued"""
##def distance_from_zero(s): # definition to check if input s is a number
##    if type(s) == int or type (s) == float:
##        return abs (s)
##    else:
##        return "Nope"
##    print (s) # print has to be on the same indent as the statements it needs to print
## # to implement type "distance_from_zero(s)" where s is replaced with the input value

""" trip cost calculator"""
##def hotel_cost(nights):
##    return nights*140
##def plane_ride_cost(city):
##    if city=="Charlotte":
##        return 183
##    elif city=="Tampa":
##        return 220
##    elif city == "Pittsburgh":
##        return 222
##    elif city =="Los Angeles":
##        return 475
##def rental_car_cost(days):
##    if days>=7:
##        return (days*40)-50
##    elif days>= 3:
##        return (days*40)-20
##    else:
##        return days*40
##def trip_cost (city, days, spending_money):
##    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
##
##print (trip_cost("Los Angeles",5,600))

""" shut down computer?"""
##d=input("do you want to shut down the computer?")
##def computer(d):
##  if d=="yes":
##      return ("shutting down")
##  elif d=="no":
##      return ("shut down aborted")
##  else:
##      return ("no input")
##
##print (computer(d))

"""list """
##numbers = [5, 6, 7, 8]
##
##print ("Adding the numbers at indices 0 and 2...")
##print( numbers[0] + numbers[2])
##print ("Adding the numbers at indices 1 and 3...")
### Your code here!
##print (numbers[1]+numbers[3])

""" replace a list item"""
##zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
### Last night our zoo's sloth brutally attacked 
###the poor tiger and ate it whole.
##
### The ferocious sloth has been replaced by a friendly hyena.
##zoo_animals[2] = "hyena" # replaces item 3 or index 2
##
### What shall fill the void left by our dear departed tiger?
### Your code here!
##zoo_animals[3] = "elephant" # replaces item 4 or idex 3

""" add to the list"""
##suitcase = [] 
##suitcase.append("sunglasses")
##
### Your code here!
##suitcase.append("shirt")
##suitcase.append("shorts")
##suitcase.append("jacket")
##
##list_length =len(suitcase) # Set this to the length of suitcase
##
##print "There are %d items in the suitcase." % (list_length)
##print suitcase

""" slice an index"""
##animals = "catdogfrog"
##cat  = animals[:3]   # The first three characters of animals
##dog  = animals[3:6]              # The fourth through sixth characters
##frog = animals[6:10]              # From the seventh character to the end
##

"""for loop"""
##start_list = [5, 3, 1, 2, 4]
##square_list = []
##
### Your code here!
##for x in start_list:
##    square_list.append(x**2)
##    
##square_list.sort()
##print (square_list)

""" keys and list """
##menu = {} # Empty dictionary
##menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
##print (menu['Chicken Alfredo'])
##
### Your code here: Add some dish-price pairs to menu!
##menu['Spam']=2.50
##menu['Cabbage']=3.60
##menu['Banana']=1.00
##
##
##
##print ("There are " + str(len(menu)) + " items on the menu.")
##print (menu)

""" add and remove to/from a list"""
### key - animal_name : value - location 
##zoo_animals = { 'Unicorn' : 'Cotton Candy House',
##'Sloth' : 'Rainforest Exhibit',
##'Bengal Tiger' : 'Jungle House',
##'Atlantic Puffin' : 'Arctic Exhibit',
##'Rockhopper Penguin' : 'Arctic Exhibit'}
### A dictionary (or list) declaration may break across multiple lines
##
### Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
##del zoo_animals['Unicorn']
##
### Your code here!
##del zoo_animals['Sloth']
##del zoo_animals['Bengal Tiger']
##
##zoo_animals ['Rockhopper Penguin']='Cotton Candy House'
##
##print (zoo_animals)

"""list and dictionaries"""
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket']=['seashell','strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold']+50

print (inventory)
