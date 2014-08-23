#Hangman
import pickle
men = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
MAX_LIVES=len(men)
lives=MAX_LIVES
word_file=open("word.dat", "rb")
word=pickle.load(word_file)
word_file.close()
print("Welcome to Hangman!")
print("The word is…\t_", end=" ")
print(" _" * (len(word) - 1))
so_far=""
guess=""
guess=input("What is your guess?")
used=[]
while so_far!=word:
    if guess in word:
        print("Yes!",guess,"is in the word!")
        used.append(guess)
        print("Used Letters:",used)
        so_far.replace(“_”, guess)
    else:
        print("Sorry,",guess,"is not in the word :(.")
        lives-=1    
        print(men[lives])
        used.append(guess)
        print("Used Letters:",used)
