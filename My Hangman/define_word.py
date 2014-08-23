import pickle
word=input(“What should the word for your hangman game be?”)
file=open(“word.dat”)
pickle.dump(word, file)
file.close()