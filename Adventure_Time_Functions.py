import time
import sys

answer_choices = ['A', 'a', 'B', 'b', 'C', 'c']
A_answers = answer_choices[ : 2]
B_answers = answer_choices[2 : 4]
C_answers = answer_choices[-2 : ]

required = ('>>Use only options given<<')

yes_no = ['yes', 'Yes', 'y', 'no', 'No', 'n']
yes_answers = yes_no[ : 3]
no_answers = yes_no[3 : ]

# Text colors
# from https://www.geeksforgeeks.org/print-colors-python-terminal/

def prRed(skk): # gamekeeper 
    print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): # for you
    print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): # for mechanic
    print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): # extra
    print("\033[95m {}\033[00m" .format(skk)) 
def prBlue(skk): # for nurse
    print("\033[96m {}\033[00m" .format(skk))
    
# Introduction
def intro():
    """Story begins.
    """
    
    print('You wake up in a cold sweat, gasping for air. The room is dark. You realize you are in a bed.')
    time.sleep(3)

    print('You sit up, looking around the unfamiliar room, and try to recall what happened.' 
          '\nYour mind is fuzzy as you try to remember the simplest of things.')
    time.sleep(3)

    name = input('What is your name?\n')
    prGreen('>> "I am ' + name + '."')
    time.sleep(2.5)

    print('There is still some confusion as to why you are here though.')
    time.sleep(1.5)

    print('Your vision starts adjusting to the darkness and you see your coat on the edge of the bed.'
         '\nThere is a letter sticking out of the front pocket.')
    time.sleep(2)
    
intro()
    
# For future references
def main_menu():
    """Main menu for future references.
    """
    
    prPurple('Welcome.')
    time.sleep(1)
    prPurple('Come along for a thrilling adventure.')
    time.sleep(1.5)
    print ("""  A. Okay.
  B. Leave.""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers:
            time.sleep(2)
            print('')
            intro()
            break
            
        elif response in B_answers:
            print('What a shame.')
            break
            
    while response not in answer_choices:
        print(required)
        time.sleep(1.5)
        
        main_menu()
        break

def restart():
    """Restart option for future references.
    """
    
    selection = ''
    
    while selection not in yes_no:
        selection = input('>> Decide again? \n yes/no \n')
    
        if selection in yes_answers:
            time.sleep(1.5)
            main_menu()
            break

        elif selection in no_answers:
            print('Good-bye.')
            sys.exit()
            break

        else:
            print(">>I didn't understand that.<<")
            time.sleep(1.5)
            restart()
            break
            
 # First decision
def choice_1():
    """ Decision for reading a letter for details.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    response = ' '

    while response not in yes_no:
        response = input('>> Do you go and reach for it?\n yes/no \n')
        if response in yes_answers:
            print('You grab the letter and open it up to read.\n')
        elif response in no_answers:
            print('Your head begins to hurt, as if it is telling you the answer is in the letter.')
            
            while response in no_answers:
                response = input('>> Do you go and reach for it?\n yes/no \n')
                if response in yes_answers:
                    print('You grab the letter and the pain diminishes. You open it up to read.\n')
                    break
                    
                elif response in no_answers:
                    print('The pain increases and your vision gets blurry until you cannot open your eyes.')
                    time.sleep(2)
                    
                    print('The pain is unbearable and knocks you out.')
                    time.sleep(2.5)
                    
                    restart()
                    break

                else:
                    print("I didn't understand that.\n")
        else: 
            print("I didn't understand that.\n")

choice_1()

def story_1():
    """ Story details begin.
    """
    print('"Dear Sibyl,"')
    time.sleep(1.5)

    print('At that moment, you get flashbacks.')
    time.sleep(1.5)

    print("You realize you are a small clairvoyant detective called 'Sibyl' who received a cryptic message about a cold case.")
    time.sleep(1.5)

    print('Shaking your head, you continue on reading the letter.')
    time.sleep(1.5)

    print('"Dear Sibyl,"'
         '\n"I know it has been 15 years, but..."')
    time.sleep(1)

    print('"I know my brother is out there. I can just feel it. Nobody would believe me, but I know you feel it too."')
    time.sleep(2)

    print('"I got a letter to this house party on the other side of the hill, towards the fields."'
         '\n"The letter was signed by my brother. I recognize his signature anywhere."')
    time.sleep(3)

    print('"But... the wording is nothing like him."')
    time.sleep(1.5)

    print('"I have attached his letter to this. Please. I can only entrust this to you."')
    time.sleep(2)

    print('You now understand the piercing headaches. It is because of the contract with the client.')
    time.sleep(1)

    print('Since your headaches will come back if you do not help, you decide to look around for a light.')
    time.sleep(2)
    
story_1()

# Second decision
def choice_2():
    """ Decision for lighting.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print('You see an oil lamp next to the bedside table. You decide to:')
    time.sleep(1.5)
    print ("""  A. Scoff at and ignore it.
  B. Pick it up and turn it on.
  C. Look for other light options.""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in B_answers:
            print('The room brightens up and you see that there is no other furniture and window. Just a door out.')
            break

        elif response in A_answers or C_answers:
            print('The splitting headache comes back.')
            time.sleep(1.5)

            print('You decide to: ')
            print ("""  A. Scoff at and ignore it.
  B. Pick it up and turn it on.
  C. Look for other light options.""")

            response = input('>>> ')

            while response in answer_choices:
                if response in B_answers:
                    print('You grab the light and the pain diminishes.'
                          '\nYou turn it on to see there is no other furniture.'
                          '\nThere is no window. Just a door out.')
                    break

                elif response in A_answers or C_answers:
                    print('The pain increases and your vision gets blurry until you cannot open your eyes.')
                    time.sleep(2)

                    print('The pain is unbearable and knocks you out.')
                    time.sleep(1.5)

                    restart()
                    break

            while response not in answer_choices:
                print(required)
                time.sleep(1)
                
                choice_2()
                break
                    
        while response not in answer_choices:
            print(required)
            time.sleep(1)

            choice_2()
            break
                    
    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_2()
        break

choice_2()

# Out the room we go
print('The door creaks as you open it. You find yourself in a hallway with two doors to your left.'
      '\nTo your right is a double door towards the end of the hall.')
time.sleep(2)

# Third decision
def choice_3():
    """ Decision for a entering a door.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print('After looking around, you decide to go check out the:')
    print("""  A. Door furthest to your left.
  B. Door closest to your left.
  C. Double door down the far right.""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers:  # furthest to left: room without doorknob
            print('You walk up and realize there is no knob.')
            print('It is locked, so you decide to:')
            print("""  A. Go to the double door furthest down the hall.
  B. Go to the next closest door.
  C. Break down the door.""")

            response = input('>>> ')
            
            while response in answer_choices:
                if response in A_answers:  # double door
                    print('You walk towards the grandiose double door and open it.')
                    break

                elif response in B_answers:  # room locked
                    print('You twist the knob and find that it is locked.')
                    print('You have no key, so you decide to:')
                    print("""  A. Go to the double door furthest down the hall.
  B. Break down the door.""")
                    
                    while response in answer_choices:
                        if response in A_answers:  # double door
                            print('You walk towards the grandiose double door and open it.')
                            break
                            
                        elif response in B_answers: # break down door
                            print('You attempt to break the door down and end up injuring your limbs.')                
                            print('The door is still locked, so you go down the hallway to the final door')
                            break
                            
                    while response not in answer_choices:
                        print(required)
                        time.sleep(1)
                        
                        choice_3()
                        break

                elif response in C_answers:  # break down the door w/o knob
                    print('You attempt to break the door down and end up injuring your limbs.')
                    print('The door is still locked.')
                    print('You decide to walk towards the grandiose double door and open it.')
                    break
                    
            while response not in answer_choices:
                print(required)
                time.sleep(1)
                
                choice_3()
                break

        elif response in B_answers: # door closest to left: locked door
            print('You twist the knob but it would not budge.')
            print("You don't have a key, so you:")
            print("""  A. Go to the double door furthest down the hall.
  B. Go to the next closest door.
  C. Break down the door.""")

            response = input('>>> ')

            while response in answer_choices:
                if response in A_answers:  # double door
                    print('You walk towards the grandiose double door and open it.')
                    break

                elif response in B_answers:  # door w/o knob
                    print('You walk up and realize there is no knob.')
                    print('It is locked, so you decide to:')
                    print("""  A. Go to the double door furthest down the hall.
  B. Break down the door.""")
                    
                    while response in answer_choices:
                        if response in A_answers:  # double door
                            print('You walk towards the grandiose double door and open it.')
                            break
                            
                        elif response in B_answers:  # break down door w/o knob
                            print('You attempt to break the door down and end up injuring your limbs.')               
                            print('The door is still locked. You go down the hallway to the final door')
                            break
                    while response not in answer_choices:
                        print(required)
                        time.sleep(1)
                
                        choice_3()
                        break

                elif response in C_answers:  # break down locked door
                    print('You attempt to break the door down and end up injuring your limbs.')             
                    print('The door is still locked. You go down the hallway to the final door') 
                    break

            while response not in answer_choices:
                print(required)
                time.sleep(1)
                
                choice_3()
                break           

        elif response in C_answers: # door down the hallway
            print('You walk towards the grandiose double door and open it.')
            break
        
    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_3()
        break
        
choice_3()

# Into the dining room
print('You see that it is a dining room and walk in.')
time.sleep(1)

print("The tables are set up and you spot a nametag with your client's name on it.")
time.sleep(1.5)

print('You try to get a closer look at the set-up, but then hear whispering.')
time.sleep(1.5)

print('You look up and see a nurse and mechanic talking to each other.')
print('Everyone notices each other, so you decide to walk over to them.')
time.sleep(3)

print("Since you don't know anything about them, you keep up the persona that you are your client.")
print('The nurse introduces herself first. Then the mechanic.')
time.sleep(3.5)

prGreen('"How do you know my brother?" you ask casually.')
time.sleep(2)

print('The two ladies look at each other with confusion in their eyes.')
time.sleep(1)

prBlue('"Your brother? What do you mean?" asked the nurse.')
time.sleep(1.3)

print('Now it was your turn to be confused.')
time.sleep(1)

prGreen('"This dinner party is for a house warming, is it not?"')
time.sleep(1.5)

prYellow('The mechanic scratches her head. "I was invited here for government funding. Same with her."')
time.sleep(2)

print('As you try to connect the dots together, the chandelier lights flicker and go out.')
time.sleep(2)

print('Panic starts to set in. There is shrill screaming. Then, the lights come back on.')
time.sleep(2.5)

print('You look around and see that the nurse and mechanic are tied down to their seats.')
print('You quickly look around again but see nobody else in the room.')
time.sleep(5)

# Hunter appears
prRed('"Hello all. I am so glad you were able to join me for this marvelous feast," a creepily enthusiastic voice said.')
time.sleep(3)

print('You continue whipping your head around but find no new figures.')
time.sleep(1.5)

print('You can see the nurse and mechanic struggling with deep panic in their eyes.')
time.sleep(1.5)

prRed('The voice continued, "Oh, do not squirm so much little ones. You will need your energy."')
time.sleep(2)
print('You were about to ask what was this about when the voice cut you off.')
time.sleep(1.5)

prRed('"Hello, there Sybil," the voice turned serious.')
time.sleep(1.5)

prRed('"I am so disheartened by the thought of my brother not trusting me. He had to call you to come here."')
time.sleep(2)

print('You think over the situation, wondering how this person knew your identity. "My brother", he said?'
     '\nSo many questions were going through your mind.')
time.sleep(3)

prYellow('"What is all this?!?!" the mechanic shrieked. "Sibyl? Who are you? Are you in on this?"')
print('On top of having your own questions, you are bombarded with her questions, causing anxiety to set in.')
time.sleep(3)

prRed('The voice chuckles. "All right, let us cut to the chase before more energy is wasted."')
time.sleep(2)

prRed('"Welcome to my beautiful manor. We are going to have a lovely feast tonight."')
prRed('"You can call me "Gamekeeper". As the name implies, I hunt. And I love it."')
time.sleep(4)

# Fourth decision: fight or flight

def choice_4():
    print('As you listen on, you start connecting the dots.'
          '\nYou are the prey.')
    print('Understanding the situation, you:')
    print("""  A. Ask questions.
  B. Stand still, frozen with fear.
  C. Make a run for it.""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers:
            print('Your flight response is not kicking in, but you have some fight in you.')
            print('You demand answers.')
            time.sleep(2)

            prGreen('You shout toward the ceiling, "How do you know my client and his brother!?!?"')
            time.sleep(3)

            prRed("""Oh, Sybil has some fight! That's a good quality in a detective!""")
            time.sleep(2)

            prRed('It continues with, "How about for each task you complete, I give you details?"')
            time.sleep(3)

            print('Tasks? What tasks?')
            time.sleep(2)

            prRed('"Oh, I never got to explain what we are going to do! Pardon my rudeness."')
            time.sleep(2)

            print('Upon hearing that statement, you:')
            print("""  A. Continue listening.
                    B. Ask more questions.""")

            response = input('>>> ')
            
            while response in answer_choices:
                if response in A_answers:
                    break
                elif response in B_answers:
                    print("You're so angry you cannot stand to hear what he has to say.")
                    time.sleep(1.5)

                    prGreen('"Enough fooling around!" you shout so loud that it echoes throughout the room.')
                    time.sleep(1.5)

                    print('It is silent for a few seconds.')
                    time.sleep(2)

                    prRed('"Oh, more of that fighting spirit! This is going to be fun."')
                    time.sleep(1.5)

                    prRed('"However, I cannot have you constantly interrupting me. We will all starve!"')
                    time.sleep(3)

                    print('As you are about to interject again, the lights go out.')
                    print('You feel yourself jerk and get dragged backwards.')
                    print('You start protesting but your mouth gets covered by a handkerchief.')
                    time.sleep(5)

                    print('The lights go back on.')
                    time.sleep(2)

                    prRed('"I am terribly sorry Sybil, but we must continue!"')
                    time.sleep(2)
                    break
                    
            while response not in answer_choices:
                print(required)
                time.sleep(1)
                
                choice_4()
                break

        elif response in B_answers:
            print('Your flight response is not kicking in.')
            time.sleep(1.5)

            print("So many questions run through your mind that you don't know what to ask.")
            print('The nurse and mechanic seem to be frozen in fear as well.')
            time.sleep(3.5)

            print('"Well, since there seems to be no objections, let us continue with the rules!"')
            time.sleep(2)
            
            break

        elif response in C_answers:
            print('Your flight response kicks in.'
                  '\nYou bolt toward the door you came from, ignoring everyone and everything else')
            time.sleep(4)

            prRed('"Where are you going?" the Gamekeeper shouts.')
            time.sleep(2)

            print('You head pass the double doors, down the hall.'
                  '\nYou realize the only door available is the room you awoke in.')
            time.sleep(3)

            print('You try to think of something to do, but the manical laughter is disrupting your thoughts.')
            print('The piercing headaches come back.')
            time.sleep(2)

            print('As an idea comes to mind, you hear a thud behind you.')
            time.sleep(1.5)

            print('You hear a scream as you begin turning your head.')
            time.sleep(2)

            print('Then, you black out for eternity.')
            time.sleep(1.5)

            restart()
            
            break
        
    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_4()
        break

choice_4()

# Story continues: Game details
prRed('"The rules are simple. Decode 5 of the 7 ciphers placed throughout the field!"'
      '"This will get you the password needed to unlock 2 of 3 doors in order to escape!"')
time.sleep(5)

print('Gamekeeper chuckles before continuing.')
time.sleep(1.5)

prRed('"Obviously, if that happens, you win."'
      '"\nHowever, I win if I catch you and tie you to marked trees."'
      '"\nYour teammates can attempt to rescue you!"')
time.sleep(4)

prGreen('You begin to panic again. You think,"Ciphers? Does this guy really expect all of us to know how to decode?"')
time.sleep(3)

prGreen('"Well I do know a bit, but does everyone else?!? Will I be carrying the team?"')
time.sleep(1.5)

print('As you think about the disadvantages, Gamekeeper cuts off your thoughts.')
time.sleep(3)

prRed('"Do not fret! The way to decode is simply to answer the given question correctly!"')
time.sleep(2)

prGreen('"Is this Jeopardy??" you think to yourself.')
time.sleep(1.5)

prRed('"I specifically chose you three because I know you are all very knowledgeable."'
      '"\nIt would be sooo boring if I chose clueless prey. The catch would be too easy."')
time.sleep(4)

print('There is silence.')
time.sleep(2)

print('"Since there are no objections, let us begin in an hour!"')
time.sleep(3)

# Let the games begin
print('>>Timeskip<<')
time.sleep(1.5)

print("You're led to the field via light indicators. Alone.")
time.sleep(2)

print('"I guess we are starting off at different locations," you nervously think.')
time.sleep(2)

print('You look around. There really is no other way to escape.')
time.sleep(1.5)

print('You pull out the device you were given.'
      '"Okay, so this thing will give us the pieces of the password that got decoded,"'
      '"\nthe stats of each person,"'
      '"\nand the location of each person if they get injured by the hunter or if they are decoding."')
time.sleep(5)

print('You enter the vast field, unsure of how you will even be able to find ciphers, let alone each other.')
print('You get a few deep breaths in before the counter starts.')
time.sleep(3)

prPurple('-Beep-')
time.sleep(1)
prPurple('-Beep-')
time.sleep(1)
prPurple('-Beeeeep-')
time.sleep(1.5)

print('You bolt toward the abandoned building you see, hoping to see a cipher or teammate.')
time.sleep(2)

print("You're in luck! You see a cipher inside right away."
      "\nThere is a long glowing antenna atop of it.")
time.sleep(3)

print('"I guess that is how we will identify ciphers," you think.')
time.sleep(1)

print('You get to it and take a look at the screen:')
time.sleep(1)

print()
print('Encoded Message: \t', 'İĭĴĴķ')
print()
time.sleep(2)

print('There are three red buttons with nothing else on them.')
time.sleep(2)

print('You tap a random one and a question appears:')
time.sleep(2)

# Cipher 1
def question_1():
    """ 1st cipher quiz question and answer.
    
    Returns:
    Scenario based on correctness of answer.
    """
    
    print('"Question: This author is most famously known for his novel "No Longer Human"."')
    time.sleep(2)
    print("""  A. Shuuji Tsushima
  B. Ryuunosuke Akutagawa
  C. Fyodor Dostoevsky""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers:
            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('CORRECT')
            time.sleep(1)

            print()
            print('Decoded Message: \t', 'hello')
            print()

            print('"Nice!" you whisper to yourself.')
            time.sleep(1.5)
            break

        elif response in B_answers or C_answers:

            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('WRONG')
            time.sleep(1)

            print('At the same time, an sudden electric current runs through you!')
            time.sleep(1.5)

            time.sleep(2)

            print('Ouch! What the?!')
            print('"Seriously?! Am I really supposed to know this?!"')
            time.sleep(2)
            break

    while response not in answer_choices:
        print("Huh? How did you choose a different answer if there's only 3 buttons?")
        time.sleep(2)
        
        question_1()
        break

question_1()

# Fifth decision
print('You start to hear a thumping sound coming from another room.')
time.sleep(1.5)

def choice_5():
    """ Decision for an escape route.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print("You're not willing to risk it, so you run in the other direction.")
    time.sleep(1)
    
    print('You head towards the:')
    print("""  A. Staircase
  B. Kitchen
  C. Outside""")

    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers:
            print('You head upstairs. There is no cipher.')
            time.sleep(1.5)

            print('There is nothing helpful.')
            time.sleep(1)

            print('You begin walking towards the staircase when you hear footsteps coming up.')
            time.sleep(1)

            print('You look at your tracker device real quick and see that others are deciphering.')
            print('The only other individual on this playing field is Gamekeeper.')
            time.sleep(4)

            prGreen('There is no other place to go. "What now???", you think.')
            time.sleep(1.5)

            print('You frantically glance around...')
            time.sleep(1)

            print('The window!')
            time.sleep(1)

            prGreen('"I have to."')
            time.sleep(1.5)

            print("You don't have time to think anymore.")
            print('You take a deep breath and hop off the ledge.')
            time.sleep(2)

            print('You miraculously land uninjured.')
            time.sleep(1)
            
            break

        elif response in B_answers or C_answers:
            print('As you run towards the entranceway, a figure pops out.')
            time.sleep(1)

            print('You stop dead in your tracks.')
            time.sleep(1.5)

            print('The figure comes into view and is revealed to be...')
            time.sleep(2)

            print('Gamekeeper!')
            time.sleep(1.5)

            print('Or, at least who you assume to be is the Gamekeeper.'
                 "\nGranted you've never seen him.")
            time.sleep(2.5)

            print('His build is huge. He looks like he is AT LEAST 7 feet tall.')
            print('The other thing about him is that he shields his face by wearing a deer head.')
            time.sleep(3)

            print('What is that in his hands??? A CHAIN WITH A SPIKED HOOK AT THE END OF IT?!?!')
            time.sleep(2)

            print('You try and hightail the way you came from.')
            time.sleep(1.5)

            prGreen('"My sprinting is like his speed-walking???", you think.')
            time.sleep(1.5)

            print('You are bolting towards the entrance you came from.')
            print('You are outside now, running aimlessly in hopes of shaking him off.')
            time.sleep(2.5)

            print('As you continue, you suddenly feel a sharp slap behind your back.')
            time.sleep(1.5)

            print('You take the risk of looking back and see the Gamekeeper swinging the chain.')
            time.sleep(1.5)

            print('It dawns upon you that this is indeed VERY REAL.')
            time.sleep(2)

            print('You continue sprinting with all you have.')
            time.sleep(1.5)

            print('You feel yourself get hooked, dragged backwards, and lifted into the air.')
            time.sleep(2)

            print('You flail around to try and escape.')
            time.sleep(1.5)

            prRed('"Sorry Sybil."')
            time.sleep(1)

            print('You knock out.')
            time.sleep(2)

            restart()
            break
            
    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_5()
        break

choice_5()

prPurple('>>Timeskip<<')
time.sleep(1)

# Cipher 2
print('You walk up to the second cipher.')
time.sleep(1)

print()
print('Encoded Message: \t', 'ǨøļåïÆqų')
print()

time.sleep(1)

def question_2():
    """2nd cipher quiz question and answer.
    
    Returns:
    Scenario based on correctness of answer.
    """
    
    print('"Question: This leg nerve is the longest in the body:"')
    time.sleep(2)
    print("""  A. Saphenous
  B. Deep peroneal
  C. Sciatic""")
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers or B_answers:

            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('WRONG')
            time.sleep(1)

            print('At the same time, an sharp electric current runs through you!')
            time.sleep(1.5)

            print('Another question comes up.'
                 "\nIt's a physics question...")
            time.sleep(1.5)

            print('You decide it is too risky, since the zap is loud and can draw attention.')
            break

        elif response in C_answers:
            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('CORRECT')
            time.sleep(1)

            print()
            print('Decoded Message: \t', 'already')
            print()

            print('With that puzzle piece, you look to your device.')
            time.sleep(1.5)

            print('It seems that the nurse was successful as well.')
            time.sleep(1.5)

            print("So far, the password reads 'hello', 'already','are'.")
            break
        
    while response not in answer_choices:
        print("Huh? How did you choose a different answer if there's only 3 buttons?")
        time.sleep(1)
        
        question_2()
        break
        
question_2()

# The plot thickens
print("The adrenaline is starting to die down.")
time.sleep(1)

print("You don't think you have enough energy to continue.")
time.sleep(1)

print("All is quiet, so you decide to sit, even if it's just for a few minutes.")
time.sleep(2)

print('The device shows that the nurse is attempting to decode a cipher somewhere to the far east.')
time.sleep(1.5)

print('You feel the pain starting to come...')
time.sleep(1)
            
prPurple('-Beep-')
time.sleep(1)

print('You glance at the source of the sound: your device.')
time.sleep(1)

print('On the screen is a picture of a deer head.')
time.sleep(1.5)

print('You jump a little, becoming more alert now.'
     '\nYou look around but nobody is there.')
time.sleep(3)

print('You look again and see that the screen is telling you something.')
time.sleep(1.5)

prRed('Hello Sybil. If you are getting these messages, that means you are doing well!')
time.sleep(2)

prRed('As promised, I will give you information.')
time.sleep(1.5)

print('You look around again to make sure nobody is around.')
time.sleep(1.5)

prRed('Do not worry about me knowing your whereabouts.'
     '\nThese messages are automated for when the group deciphers correctly.')
time.sleep(4)

print('You look up one last time.')
time.sleep(1)

prGreen('"How does this guy know what I think all the time???"')
time.sleep(1.5)

print('The device beeps another time.')
time.sleep(1)

prRed('"I am not the brother of your client."'
     '\n"I am a hunter who simply loves hunting.')
time.sleep(2.5)

prRed('"Why and how did I decide to hunt humans?"'
     '\n"Quite simple really."')
time.sleep(2.5)

prRed('"Humans are intelligent."')
time.sleep(1.5)

prRed('"Humans are entertaining."')
time.sleep(1.5)

prRed('"Yet, humans are wretched."')
time.sleep(2)

print('The screen goes black and all you see is your reflection.')
time.sleep(2)

print('It takes you a moment to process the words, but when you do, you tap the screen for answers.')
time.sleep(2)

print('Nothing. Just the usual stats and password.')
time.sleep(1)

prGreen('"Wretched? Well, yes some are but does this guy plan to eradicate all humans??? Is HE human???"')
time.sleep(3)

print('You ruffle your hair in frustration and decide now is not the time to think about it.')
time.sleep(2.5)

prGreen('"If I want answers, I am going to have to decipher."')
time.sleep(1.5)

prGreen('"If I want to SURVIVE, I am going to have to decipher."')
time.sleep(1.5)

print('You get up and start wandering again.')
time.sleep(1)

prPurple('>>Timeskip<<')
time.sleep(1)

# Cipher 3
print('You see a glowing tower in the distance.')
time.sleep(1.3)

print('Another cipher!')
time.sleep(1)

print('You jog towards the area, a corn field, and hear the hum of the machine.')
time.sleep(2)

prGreen('"A cipher in a corn maze huh? Could be a good or bad thing..."')
time.sleep(2)

print('Encoded Message: \t', 'žŧǮǡ')

def question_3():
    """ 3rd cipher quiz question and answer.
    
    Returns:
    Scenario based on correctness of answer.
    """
    
    print('"Question: Name the author: "I wanted the ideal animal to hunt... So I said,'
          '\n"It must have courage, cunning, and, above all, it must be able to reason."')
    time.sleep(5)
    print("""  A. Ernest B. Schoedsack
  B. Zaroff Rainsford
  C. Richard Connell""")
    time.sleep(5)
    
    prGreen('"Sounds oddly familar..."')
    time.sleep(1.5)
    
    response = input('>>> ')
    
    while response in answer_choices:
        if response in A_answers or B_answers:

            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('WRONG')
            time.sleep(1)

            print('At the same time, an sharp electric current runs through you!')
            time.sleep(1.5)

            print('You prepare yourself as a new question comes up.')
            time.sleep(1.5)

            prPurple('-rustle-  -rustle-')
            time.sleep(1.5)

            print('You whip your head toward the noise.')
            time.sleep(1.5)
            
            break

        elif response in C_answers:
            print('You tap and button and immediately afterwards, the screen changes:')
            time.sleep(2)

            print('CORRECT')
            time.sleep(1)

            print('"Good thing I read a lot."')
            time.sleep(1.5)

            prPurple('-rustle-  -rustle-')
            time.sleep(1.5)

            print('Instead of checking the password, you whip your head toward the noise.')
            time.sleep(1.5)
            
            break
        
    while response not in answer_choices:
        print("Huh? How did you choose a different answer if there's only 3 buttons?")
        time.sleep(2)
        
        question_3()
        break
        
question_3()

# Reunion
print('You see the nurse jogging toward you.')
time.sleep(1.5)

prGreen('"OMG, a teammate," you say as you sigh in relief.')

print('Upon closer inspection, you see she has several rips in her clothes and a splint on her arm.')
time.sleep(1.5)

print('Her hair is frazzled and she looks pale.')
time.sleep(1.5)

prBlue("""After panting for air, she says, "You're alive!""")
time.sleep(1.5)

prGreen('"Are you okay?" you ask.')
time.sleep(1.5)

print('The nurse was about to answer when you both hear a bloodcurdling scream closeby.')
time.sleep(2)

prBlue('"AAAAHH... that must be the mechanic!"')
time.sleep(1.5)

print('You look at your device and see that the mechanic is frozen on the map.'
     '\nThis must mean she is tied to a tree...')
time.sleep(4)

prGreen('"Do we try and save her?" you think to yourself.')
time.sleep(2)

print('You look at the nurse and she is shaking.')
time.sleep(1.5)

print('You check the device again. It looks like you only need 1 more cipher!')
time.sleep(2)

prGreen('"Do we leave her and focus on decoding?"'
     '"Or do we risk it so all 3 of us can survive?"')
time.sleep(3.5)

prPurple('...')
time.sleep(1.5)

# Flashback scenario - for future reference
def flashback():
    """ Flashback of interaction between you and the nurse.
    
    Returns:
    Scenario with nurse giving you a syringe.
    """
    
    prPurple('>>Flashback<<')
    time.sleep(1.5)

    prBlue('"Here. This is a poison I created from berries I found around."')

    print('In her hand is a syringe with some purple liquid.')
    print('You blink at the nurse.')
    time.sleep(3)

    prGreen("""I won't ask.""")
    time.sleep(2)

    prBlue('"Good."')
    time.sleep(2)

    print('>>Flashback end<<')
    time.sleep(1)
    
# Rescue mechanic scenario - for future reference
def rescue_mechanic():
    """ Decision to rescue the mechanic.
    
    Returns:
    Situation where you and the nurse try to rescue the mechanic together.
    """
    
    prGreen('"..."')
    time.sleep(1)
                
    prGreen('"Yeah... we should save her."')
    time.sleep(1.5)
                
    prGreen('"It should be fine with both of us there... right?" you say to yourself.')
    time.sleep(2)
                
    print('You both quickly but quietly jog toward the source of the scream.')
    time.sleep(1.5)

    print('Some trees are in sight. The two of you get close and hide behind a wall.')
    time.sleep(2)

    print("The nurse takes a peek to see the mechanic and Gamekeeper's back.")
    time.sleep(2)

    print('The nurse covers her mouth and whips her head towards you.')
    time.sleep(2)

    prPurple('>>Timeskip<<')
    time.sleep(1)

    print('You decide to distract the Gamekeeper while the nurse rescues the mechanic.')
    time.sleep(1.5)

    prGreen('"This works in the movies, so it could work here, right?" you ask yourself.')
    time.sleep(2)

    print('You hope for the best and make a run towards the nearby bushes.')
    time.sleep(2)

    prRed('"!"')
    time.sleep(1.5)

    print("You've caught Gamekeeper's attention!")
    time.sleep(1.5)

    print('You hear the chains and stomps coming toward you.')
    time.sleep(2)

    flashback()

    print('A sharp hit lands on your back.')
    time.sleep(1.5)

    print('You speed up to escape another hit.')
    time.sleep(1.5)

    prRed("""Sybil! You're making things difficult for me.""")
    time.sleep(2)

    print('You run further and further from the mechanic and nurse.')
    time.sleep(2)
    
    prPurple('-BEEEEEEEEEEEEP-')
    time.sleep(1)
    
    prGreen('"The alarm for password completion! I have to get to a gate!"')

    print('Suddenly, you feel yourself being pulled backwards.')
    time.sleep(2)

    print("It's like you're going backwards on a roller coaster.")
    time.sleep(1.5)

    prRed('"Hi Sybil."')
    print('The voice is right by your ear.'
         "\nYou're floating in the air.")
    time.sleep(4)
    
# Seventh decision - for future reference
def choice_7():
    """ Decision for using poison.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print('In this seemingly helpless state, you choose to:')
    print("""  A. Use the poison.
  B. Save the poison.""")

    response = input(">>> ")

    while response in answer_choices:
        if response in A_answers:
            prGreen("""I'm not here to die!""")
            time.sleep(1.5)

            print("You take out the syringe and stab it into Gamekeeper's arm.")
            time.sleep(2)

            print('...')
            time.sleep(1.5)

            prRed("AAAAAAAAAAAHHHHH!!!")
            time.sleep(1.5)

            print('You fall to the ground with a thud.')
            time.sleep(1.5)

            print('You scramble up quickly and try to run away.')
            print('You create some distance between but suddenly get tugged back.')
            time.sleep(3)

            print('You take the chance to look back and see Gamekeeper crouched over.')
            time.sleep(2)

            print('You look closely and see him hugging at the chain.')
            time.sleep(1.5)

            prGreen("""I'm like a dog on a leash!" you think.""")
            time.sleep(1.5)

            print('Your heart starts pumping from anxiety.')
            
            break

        elif response in B_answers:
            prGreen('"Only for absolute emergencies," you tell yourself.')
            break

    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_7()
        break
        
# Story continues - Sixth decision
def choice_6():
    """ Decision to rescue the mechanic or not.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print('The two of you decide to:')
    print("""  A. Leave the mechanic.
  B. Rescue the mechanic.""")
    
    response = input('>>> ')

    while response in answer_choices:
        if response in A_answers:
            prGreen('"We cannot risk it," you say.')
            time.sleep(2)

            prBlue('"Wait!"')
            time.sleep(2)

            prBlue('"What if she can help us with the cipher?"')
            time.sleep(2)

            def choice_6_i():
                """ Decision embedded if certain decision is made.
                
                Returns:
                Scenario depending on answer choice selected.
                """
                
                print('You think about it and decide:')
                print("""  A. Leave the mechanic.
    B. Rescue the mechanic.
    C. Compromise.""")

                response = input('>>> ')
                
                if response in A_answers:
                    print('You slap her face to knock some sense into her.')
                    time.sleep(2)

                    prGreen('"Now is NOT the time for kindess!!!"')
                    time.sleep(1.5)

                    prGreen('"We are trying to SURVIVE."')
                    time.sleep(1.5)

                    print('The nurse looks at you with wide eyes but then slowly nods.')
                    time.sleep(2)

                    prPurple('-rustle-  -rustle-')
                    time.sleep(2)

                    print('You both look up from each other.')
                    time.sleep(1)

                    print('You hear the sound of chains moving.')
                    time.sleep(1.5)

                    prGreen('"Oh no..." you think to yourself.')
                    time.sleep(1.5)

                    print('It is too late.')
                    time.sleep(1.5)

                    print('The Gamekeeper is here.')
                    time.sleep(1)

                    print('The both of you come face to face with Gamekeeper.')
                    time.sleep(1.5)

                    print('Then, you black out for eternity.')
                    time.sleep(1.5)

                    restart()

                elif response in B_answers:
                    rescue_mechanic()
                    choice_7()

                elif response in C_answers:
                    prGreen('"That is pretty risky, but, yeah, we should save her."')
                    time.sleep(2)

                    prGreen('"I think you should try to decode the last cipher."'
                           '\n"I will go get the mechanic."')
                    time.sleep(3)

                    print('The nurse looks at you hesitantly but then slowly nods.')
                    time.sleep(2.5)

                    prPurple('>>Timeskip<<')
                    time.sleep(1.5)

                    print("You're hiding behind a wall."
                          "\nYou peek over to see the mechanic and the Gamekeeper's back.")
                    time.sleep(5)

                    print('You decide to throw a rock towards the nearby bushes.')
                    time.sleep(2)

                    print('You see Gamekeeper turn his head that way then go back to the mechanic.')
                    time.sleep(2)

                    print('You do it one more time.')
                    time.sleep(2)

                    print('This time, you see Gamekeeper smirk and walk toward the bushes.')
                    time.sleep(2)

                    print('Once you see he is far enough, you rush over to the mechanic.')
                    time.sleep(2)

                    print('As the knots loosen and the mechanic hits the ground...')
                    time.sleep(2.5)

                    prPurple('-BEEEEEEEEEEEEP-')
                    time.sleep(1.5)

                    print('A loud alarm rings through the field.')
                    time.sleep(2)

                    prYellow('"The gates! We have to go and punch in the completed password!"')
                    time.sleep(3)

                    prGreen('"It seems the nurse was able to decode the final cipher."')
                    time.sleep(2)

                    print('You both start running in the other direction when you feel yourself get grabbed.')
                    time.sleep(2.5)

                    print("It's as if you're going backwards on a roller coaster.")
                    time.sleep(1.5)

                    prRed('"Hi Sybil."')
                    print('The voice is right by your ear.'
                         "\nYou're floating in the air.")
                    time.sleep(4)

                    print('You look forward and see the mechanic frantically getting farther away.')
                    time.sleep(2)

                    flashback()
                    choice_7()

                else:
                    print(required)

            choice_6_i()
            break

        elif response in B_answers:
            rescue_mechanic()
            choice_7()
            break

    while response not in answer_choices:
        print(required)
        time.sleep(1)
        
        choice_6()
        break

choice_6()

# The truth? comes out

PrRed('"Oh dear, Sybil. Happy reunion, is it not?"')

prGreen('"..."')

prRed('"I am quite amazed you are sacrificing yourself to save her."')
time.sleep(1.5)

prRed('"Though you have not decoded a cipher, I will let you in on some more secrets."')
time.sleep(2)

prGreen('"..."')

prRed('"Remember when I told you humans are wretched?"')
time.sleep(2)

prRed('"Well, your teammates are quite the examples of just that."')
time.sleep(2)

prGreen('"Huh? What does he mean?"')
time.sleep(1)

prRed('"What I mean is the nurse and mechanic are criminals."')
time.sleep(1.5)

prRed("""Have you heard of the nurse called 'The Angel of Death'?""")
prRed('"The one who went around killing her patients?"')
time.sleep(4)

prRed('"Well this nurse is basically a copycat of hers."')
time.sleep(2)

prRed("""She manipulates her poor severely patients' families."""
    '\n"Telling them she has an under-the-table-type medicine guaranteed to cure."')
time.sleep(5)

prRed('"Obviously, they are desperate and will believe a medical professional."')
time.sleep(2.5)

prRed('"In the end, she takes their money, kills the patients herself, and flees."')
time.sleep(3)

print('You stare at Gamekeeper, silent due to shock.')
time.sleep(2)

prGreen('"Am I supposed to believe this guy?"')
time.sleep(2)

prRed("""It's your decision to believe me."""
      "\n""However, I'm feeling generous so I'll tell you about the others too.""")
time.sleep(5)

prRed('"The mechanic plans to manipulate the planes at the airport."')
time.sleep(3)

prRed('"This will kill thousands upon thousands of people."')
time.sleep(3)

prRed('"And for what reason? To fulfill her own selfish needs."')
prRed("""She is going to pitch ideas she STOLE that aims to 'save' them all.""")
time.sleep(6)

print('Again, you stare at Gamekeeper.')
time.sleep(1.5)

prRed('"As for your client and his brother..."')
time.sleep(1.5)

prRed('"They are a team robber-murderers."')
time.sleep(2)

prRed('"There was a massive quarrel 16 years ago, resulting in the split."')
time.sleep(2)

prRed('"The brother snuck away with most of the money in the night."')
prRed('"He happened to stumble here and well... the rest is history (laughs)."')
time.sleep(4)

prRed('"So, your client really just wants the money."')
time.sleep(2)

prRed('"Well, now that those criminals are going to escape, I have to catch them."')
print('The Gamekeeper drops you to the ground and starts stomping away.')
time.sleep(3.5)

# Thinking it over
print('You stand there all alone, frozen.')
time.sleep(1.5)

prGreen('"Am I to believe him...?"')
time.sleep(1.5)

print('His claims run through your mind...')
time.sleep(2)

prGreen('"If the nurse is such an expert, the poison would have worked, right?"')
time.sleep(2)

prGreen('"Unless she did that on purpose...?"')
time.sleep(1.5)

print('You shake your head.')
time.sleep(1.5)

prGreen("""No! The Gamekeeper is huge. Of course a tiny thing wouldn't work on him!""")
time.sleep(2)

prGreen('"What about the mechanic?"')
time.sleep(1.5)

prGreen('"I can see her lazing around... She barely even successfully decoded..."')
time.sleep(2)

prGreen('"My client?"'
       '\n"He did offer me an extremely large sum of money..."'
       '\n"And with a simple salesperson job and no family, where would he be getting that?"')
time.sleep(5)

print('You start connecting puzzle pieces in attempt to fully grasp everything.')
time.sleep(2)

prGreen("""Why should I trust Gamekeeper? He's HUNTING HUMANS.""")
time.sleep(1.5)

prGreen('"Why did he even let me go?"')
time.sleep(2)

# Final decision
def choice8():
    """ Final decision: To believe or not to believe.
    
    Returns:
    Scenario depending on answer choice selected.
    """
    
    print('You wrack your brain over everything, eventually deciding to:')
    print("""  A. Believe him.
    B. Ignore all claims.""")
                    
    response = input(">>> ")
                    
    while response in answer_choices:
        if response in A_answers: # the good ending
            print('You start running in the direction where you recall seeing a locked gate.')
            time.sleep(2)

            prGreen("""I'll just have to escape on my own.""")
            time.sleep(1)

            prPurple('>>Timeskip<<')
            time.sleep(1.5)

            print('You approach the gate and see the mechanic trying to get out.')
            time.sleep(1)

            print("After hearing Gamekeeper's stories, you're hesitant to approach her."
                 '\nBut the exit is right there.')
            time.sleep(2)

            prGreen('"Hey!"')
            time.sleep(0.5)

            print('The mechanic jumps.')
            prYellow("""OMG it's you! I need some help here!""")
            time.sleep(2)

            prGreen("""Where's the nurse?""")
            time.sleep(1)

            prYellow("""It's over for her,""")
            print('She says it ominously, but you decide not to press for it.')
            time.sleep(3)

            print('You see her fumbling with the device.')
            prGreen('"Does she even know how to use it? Some mechanic she is..."')
            time.sleep(2)

            print('You push her to the side and do it yourself.')
            prGreen("""I'm not sure how I feel about helping out a potential murderer..."""
                    '\n"But I need to survive too."')
            time.sleep(3)

            print('You take out the device with your shaky hands, and connect it to the screen.')
            time.sleep(1)

            print('The mechanic has her hands on your left shoulder.')
            time.sleep(1)

            print('The screen says to hold down the button for it to work, so you do so.')
            time.sleep(1.5)

            prPurple('"hello"')
            time.sleep(2.5)

            print('You hear footsteps and the sound of chains.')
            time.sleep(1)

            print("You don't look back but you can tell he's getting closer.")

            prPurple('"you"')
            time.sleep(1)

            prPurple('"are"')
            time.sleep(1)

            print('You feel a jolt and fall backwards.')
            time.sleep(1.5)

            prYellow("""Thanks for your help! I'll remember you when I get out of here!""")
            time.sleep(1.5)

            print('The mechanic has pushed you out of the way!')
            time.sleep(1)

            print('You tremble on the ground, in shock.')

            prPurple('"already"')
            time.sleep(1.5)

            prPurple('"dead"')
            time.sleep(1.5)

            print('There is silence.')
            time.sleep(1.5)

            print("The doors aren't opening.")
            time.sleep(1)

            prYellow('"WHAT? WHAT IS THIS?" the mechanic yells.')
            time.sleep(1)

            prYellow('"YOU DID THIS, HUH?" she points a finger at you.')
            time.sleep(1.5)

            print("Before you can say anything, Gamekeeper's hook passes you and grabs at the mechanic.")
            time.sleep(1.5)

            print("She yelps and in the blink of an eye, she is in Gamekeeper's grasp.")
            time.sleep(2)

            prRed('"What a nice little reunion."')
            time.sleep(1)

            print('You hear the mechanic begging Gamekeeper to have mercy.')
            print('He shakes her to shut her up.')
            time.sleep(2)

            prRed('"Hello again Sybil. I see she has backstabbed you as well."')
            time.sleep(1)

            print('You stare with wide eyes.')
            time.sleep(1)

            prRed("""Oh don't stare at me like a deer in headlights! That should be me! (laughs)""")
            time.sleep(1)

            prRed('"Anyway, the mechanic here also betrayed the nurse."')
            PrRed('"She did the same thing! Practically pushing the nurse to me so she could escape."')
            time.sleep(4)

            prRed('"Disappointed but not surprised. She made the catch so easy for me."')
            time.sleep(1.5)

            prGreen('"I need to get out of here NOW," you think.')
            time.sleep(1)

            print('Your flight response kicks in and you flee away from the gate.')
            time.sleep(1.5)

            prYellow('"NOOOOOOOO"')
            time.sleep(1)

            print('You run farther and farther, trying to get away from everything.')
            time.sleep(1.5)

            print('You hear Gamekeeper cackle in the distance.')
            time.sleep(1)

            print('Suddenly, a stampede of buck and deer come and block your way.')
            time.sleep(1)

            print('You stumble and stare face to face with a deer head.')
            time.sleep(1)

            print('But not just any deer head.')
            time.sleep(1)

            print("Gamekeeper's deer head.")
            time.sleep(1)

            prRed('"Hello Sybil," he says in a serious tone.')
            print('He then begins to laugh manically.')
            time.sleep(3)

            print('The pattering of the stampede.')
            time.sleep(0.5)

            print("Gamekeeper's laugh.")
            time.sleep(0.5)

            print('The overwhelming fear.')
            time.sleep(0.5)

            print('Everything causes your head to want to split in half.')
            print('The world begins spinning out of control.')
            time.sleep(1)

            prGreen('"AAAAAAAAAAAAAAAAHHHHH"')
            time.sleep(1.5)

            prPurple('...')
            time.sleep(1)

            print("You open your eyes. You are in your office. It's raining outside.")
            time.sleep(1.5)

            print('In front of you is the client.')
            time.sleep(1)

            print('"So, what did you see, Sybil?"')
            time.sleep(1)

            print('You blink at the client. Unable to say anything.')
            time.sleep(1.5)

            print('"Sybil?"')
            time.sleep(1)

            print('"What did you see?! Will you take up the offer to find my brother?!",'
                  '\nthe client asks, impatiently.')
            time.sleep(2)

            print('You finally muster up the ability to speak.')
            prGreen('"Your brother is gone."')
            time.sleep(2)

            print('"What do you mean? What was that feeling the other day?!"')
            time.sleep(1)

            prGreen("""I'm terribly sorry, it must have been a mistake.""")
            time.sleep(1.5)

            print('"You wasted all my time for a mistake?!" Some clairvoyant you are!'
                 '\nI even offered you so much money!')
            time.sleep(2.5)

            print("The client's fist hits the desk.")
            time.sleep(1)

            print('The door slams shut.')
            time.sleep(1)

            print('You rub your hand down your face.')
            time.sleep(1)

            print('You look out your third-story window and onto the street below.')
            time.sleep(1)

            print('You see your client push someone.')
            time.sleep(1)

            print('Suddenly, he gets headbutted by a deer.')
            time.sleep(1.5)

            prGreen('"Wait... a deer??? In the city???"')

            prPurple('>>END<<')
            break

        elif response in B_answers: # the bad ending
            prGreen('"This is utter nonsense! I have to find the others!"')
            time.sleep(1.5)

            print("It doesn't take you long as you hear screaming.")
            time.sleep(1)

            print('You look at your device and run in that direction.')
            time.sleep(1)

            prPurple('>>Timeskip<<')

            print('Right before you is the nurse in the tree and the mechanic is booking it.')
            time.sleep(1.5)

            prYellow("""It's over for the nurse! I'm out of here!!!""")
            time.sleep(1.5)

            print('You glance over at the nurse and see she is not resisting the ties.'
                 "\nShe's not even moving.")
            time.sleep(2)

            print("It's hard to simply ignore, but you need to escape.")
            time.sleep(1.5)

            prGreen('"Come on, this way!" you tell the mechanic.')
            time.sleep(1)

            print('Just then, the Gamekeeper comes out from the shadows.')
            time.sleep(1)

            prRed('"Oh Sybil, you have decided to ignore me?"'
                 '"\nI am so disheartened. You leave me no choice."')
            time.sleep(3)

            prPurple('>>Timeskip<<')
            time.sleep(1)

            print('You and the mechanic run towards the gate you recall seeing before.')
            time.sleep(2)

            prYellow('THERE IT IS!')
            time.sleep(1)

            print('You look behind and see no Gamekeeper in sight.')
            prGreen('"When did we lose him?" you think inside.')
            time.sleep(2)

            prGreen('"Whatever! We have to punch in the code."')
            time.sleep(1.5)

            print('Both of you approach the small screen.')
            prGreen("""We're SO CLOSE.""")
            time.sleep(2)

            print('You take out the device with your shaky hands, and connect it to the screen.')
            time.sleep(1)

            print('The mechanic has her hands on your left shoulder.')
            time.sleep(1)

            print('The screen says to hold down the button for it to work, so you do so.')
            time.sleep(1.5)

            prPurple('"hello"')
            time.sleep(2.5)

            prPurple('"you"')
            time.sleep(1)

            prPurple('"are"')
            time.sleep(1)

            print('Before you can continue, you feel a shake and hear a gasp behind you.')
            time.sleep(1)

            print('You drop the device, look back, and see that Gamekeeper has her in his grasp.')
            print('You hear her begging him to let her live.')
            time.sleep(2)

            print('Gamekeeper raises his weapon and slams it down on the mechanic.')
            time.sleep(1)

            print('You look away in time to avoid seeing the gruesome act.')
            time.sleep(1)

            prGreen("""It's just me. I can do this.""")
            time.sleep(1)

            print('You slam your finger on the button for the last few words:')
            time.sleep(0.5)

            prPurple('"already"')
            time.sleep(1)

            prPurple('"dead"')
            time.sleep(1.5)

            print('The screen turns red with a deer head on it.')
            time.sleep(1)

            print("The doors aren't opening.")
            time.sleep(1)

            prGreen('"NO!"')
            time.sleep(1.5)

            prRed('"Hello, Sybil.You are already dead."')
            time.sleep(1.5)

            print('Then, you black out for eternity.')
            time.sleep(2)

            prPurple('>>END<<')
            break
            
    while response not in answer_choices:
        print(required)
        time.sleep(1)

        choice_8()
        break