# Create a dictionary and
# take input from the user
# and return the meaning of
# the word from the dictionary

moreWordsForDictionary = True

# A class named "dictionary" having two fundamental data types: string, string
class dictionary:
    def __init__(self, _word, _meaning):
        self.word = _word
        self.meaning = _meaning

# This is function 1
def dic1():
    d1 = {} #Creating an object "d1" of the class "dictionary"

    # loop will run until the user wants no more words to insert in the dictionary
    while(moreWordsForDictionary):
        d1[input("Tell the word for that meaning : ")] = input("\nExplain the meaning : ")

        # this "more" vaiable gets the string input
        more = input("Want to enter more data to the dictionary ? (y/n) : ")
        if (more.lower() == 'n' or 
            more.lower() == 'no' or
            more.lower() == 'no more' or
            more.lower() == 'stop' or
            more.lower() == 'quit'):
            break

    print("\n\nPrinting the dictionary : ") 
    print(d1, end="\n\n")

# This is the required code defined as a function
def dic2():
    d2 = {
        "lol" : "Laugh Out Loud",
        "np" : "No Problem",
        "gn" : "Good Night",
        "afk" : "Away From Keyboard"
    }
    userInput = input("Enter the word to know it's meaning : ")
    print(d2.get(userInput))

# the program starts from here
if __name__=="__main__":
    # dic1()
    dic2()

    