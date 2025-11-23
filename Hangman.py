import random
print('''
  _    _          _   _  _____ __  __          _   _    _____          __  __ ______ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |  / ____|   /\   |  \/  |  ____|
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| | | |  __   /  \  | \  / | |__   
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` | | | |_ | / /\ \ | |\/| |  __|  
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  | | |__| |/ ____ \| |  | | |____ 
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|  \_____/_/    \_\_|  |_|______|
                                                                                     
                                                                                     


''')
print("Welcome to hangman game player")
print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= Guess the letters and win your life
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= 
''', '''
  +---+
  |   |
      |
      |
      |
      |
========= 
''']



word_list = ["car", "bike", "laptop", "pc", "keyboard", "house", "sky", "mountain", "ocean", "bluewhale", "tree", "the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "hot", "but", "some", "what", "there", "we", "can", "out", "other", "were", "all", "your", "when", "up", "use", "word", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so", "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "my", "sound", "no", "most", "number", "who", "over", "know", "water", "than", "call", "first", "people", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "sentence", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change", "went", "light", "kind", "off", "need", "picture", "try", "us", "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep", "eye", "never", "last", "let", "thought", "city", "cross", "since", "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late", "run", "don’t", "while", "press", "close", "night", "real", "life", "few", "stop", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "often", "always", "music", "those", "both", "mark", "book", "letter", "until", "mile", "river", "car", "feet", "care", "second", "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "boy", "door", "behind", "became", "top", "ship", "across", "today", "during", "short", "better", "best", "however", "low", "sure", "come", "free", "whole", "check", "game", "order", "rest", "fire", "bad", "cut", "money", "board", "class", "street", "move", "chair", "happy", "size", "dark", "rule", "note", "save", "meet", "unit", "area", "send", "box", "mind", "lose", "cold", "key", "travel", "quick", "voice", "wall", "rich", "simple", "sound", "smile", "true", "wait", "wear", "wind", "write", "yard", "zero"]
chosen_word=random.choice(word_list)
#print(chosen_word)
lives=6

# genrating blank letters
display=[]
space=len(chosen_word)
for sp in range(space):
    display +='_'
print(display)


#asking the user to guess the letter
i=False
while i==False:
    #guessing part
    guess=input("Guess a letter:").lower()
    if guess in display:
        print("You Have already choosen that letter")
        continue
    elif guess not in chosen_word:
        lives -=1
        print(stages[lives])
        if lives==0:
            i=True
            print("The letter is:")
            print(chosen_word)
            print('''
░██     ░██   ░██████   ░██     ░██ ░██ ░█████████        ░███████   ░██████████    ░███    ░███████   
 ░██   ░██   ░██   ░██  ░██     ░██ ░██ ░██     ░██       ░██   ░██  ░██           ░██░██   ░██   ░██  
  ░██ ░██   ░██     ░██ ░██     ░██ ░██ ░██     ░██       ░██    ░██ ░██          ░██  ░██  ░██    ░██ 
   ░████    ░██     ░██ ░██     ░██     ░█████████        ░██    ░██ ░█████████  ░█████████ ░██    ░██ 
    ░██     ░██     ░██ ░██     ░██     ░██   ░██         ░██    ░██ ░██         ░██    ░██ ░██    ░██ 
    ░██      ░██   ░██   ░██   ░██      ░██    ░██        ░██   ░██  ░██         ░██    ░██ ░██   ░██  
    ░██       ░██████     ░██████       ░██     ░██       ░███████   ░██████████ ░██    ░██ ░███████   
                                                                                                       
                                                                                                       
                                                                                                       

''')
    
    else:
        #displaying the chosen words
        for pos in range(space):
            letter=chosen_word[pos]
            if letter==guess:
                display[pos]=guess 
        print(' '.join(display))
        if '_' not in display:
            i=True
            print('''
░██     ░██   ░██████   ░██     ░██    ░██       ░██   ░██████   ░███    ░██ 
 ░██   ░██   ░██   ░██  ░██     ░██    ░██       ░██  ░██   ░██  ░████   ░██ 
  ░██ ░██   ░██     ░██ ░██     ░██    ░██  ░██  ░██ ░██     ░██ ░██░██  ░██ 
   ░████    ░██     ░██ ░██     ░██    ░██ ░████ ░██ ░██     ░██ ░██ ░██ ░██ 
    ░██     ░██     ░██ ░██     ░██    ░██░██ ░██░██ ░██     ░██ ░██  ░██░██ 
    ░██      ░██   ░██   ░██   ░██     ░████   ░████  ░██   ░██  ░██   ░████ 
    ░██       ░██████     ░██████      ░███     ░███   ░██████   ░██    ░███ 
                                                                             
                                                                             
                                                                             


''')