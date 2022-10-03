##import numpy

#To do: Add to GitHub, Finish checkBank method

#ok, here is my plan as of 1/31/22: Unless i think of something better then my plan
#is to first check to see if the word guessed is bigger than the previous biggest word
#and if it is then i continue, else it fails, thus efficiency, get an array of names then convert
#that using substrings to an array of letters
#then i use the remove method of lists to remove the first letter from the guessed word
#from the array(letter bank) if it works then i check it against the database of words to see
#if its real and then i make it the new top dog.

def getNames(j):
   ## names = np.array()
    names = []
    for x in range (1,j+1):
        names.append((input("Name of Student " + str(x) + ": ")).lower())
    return(names)

#guess is the word we are checking against db, the array of letters
#https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
def checkList(guess, db):
    Cguess = guess
    database = db
    print("Database is: " + str(database))
    for x in Cguess:
        if(x in database):
            database.remove(x)
            print("Removing: " + x)
        else:
            #print("Final Database is: " + str(database))
            return(False)
    #print("Final Database is: " + str(database))
    return(True)

def createDB(f):
    
    
    ''' 
    with open(f) as file:
        words = [line.split("\n") for line in file.read().splitlines()]
    print(words)
    return words
    '''
    
    '''
    with open(f) as files:
        words = [[e.strip() for e in s.split(',')] for s in files]
    print(words)
    return words
    '''
    '''
    words = []
    info = open(f,'r')
    w = info.readlines()
    for line in info:
        print(line)
        for word in line.split():
            words.append(word)
            #words=words+1
    print(words)
    '''
    with open(f, "r") as file:
        words = []
        for readline in file: 
            line_strip = readline.strip()
           # newline_break += line_strip
            words.append(line_strip)
    print(words)
    return words
    '''
    words = []
    fwords = []
    with open(f) as g:
        words = g.readlines()
    print(words)
    
    for i in range(len(words)):
        fwords.append(words[i].rstrip('\n'))
    #print(fwords)
    return fwords
    '''

#1/31/22 haven't yet if I will check the guess directly against the database or if i will
# make an array of words and check against that

def checkBank(Dguess, bank):
    
   # joe = createDB(bank)
   
   # print('\n \n \n \n')
   # print(joe)
    if (Dguess in bank):
        return True
    else:
        return False
    

def playGame(f):
    print("Let's play a game: \n")
    print("Initializing... \n")

    #its faster and uses less ram if i don't have the methods that do this part
    wordList = createDB(f)
    
    listN = getNames(int(input("How many players are playing? ")))
    bank = ''
    letBank = []
    for x in range (0,len(listN)):
        bank += listN[x]
    for y in bank:
        letBank.append(y)
    print(letBank)
    while True:
        guess = input("Guess: ").lower()
        #print(checkList(guess, letBank))
        if (checkList(guess, letBank) and (checkBank(guess, wordList))):
            print("you win")
            break;
        else:
            print("you lose, try again")
        
    '''
    if (checkBank(guess, bank)):
        print("you win")
    else:
        print("you lose")
        '''
        

