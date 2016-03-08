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

pyg = 'ay'

original = input('Enter a word:') # input fxn takes feedback
word = original.lower() # store orginal word is lower case
first = word[0] # takes the first letter of the word
new_word = word[1:len(word)]+first+pyg # get rid of the first letter adds it to the end and applies the suffix

if len(original) > 0 and original.isalpha(): # check for numbers
    print (new_word)
else:
    print ('empty') # empty printed if numbers or empty


