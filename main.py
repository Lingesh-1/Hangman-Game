import random as r
#from replit import clear
print("Welcome to Hangman Game!!!")
print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """)
f=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']
ran=r.choice(f).lower()
ans=[]
# print(ran)
anss=""
stages= ['''
     +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
       ===''']
print(stages[0])
live=0

for j in range(len(ran)):
    ans.append('_')
    anss+=ans[j]
print(anss)

enf_of_game=False

while enf_of_game!=True:
    g=input("Guess:").lower()
    #clear()
    if g in ran:
        print(f"You Have Already guessed {g}")
    for i in range(len(ran)):
        if g==ran[i]:
            ans[i]=g

    if g not in ran:
        print(f"{g} is not in the word")
        live+=1
        print(stages[live])
        print(f"\nRemaining Lives:{6-live}\n")
        if live==6:
            enf_of_game=True
            print(f"The Word is {ran.upper()}\n")
            print("You lose!!!")       
    print(ans)

    if '_' not in ans:
        enf_of_game=True
        print("\nYou win!!!")
