#name: Kathryn McCullough
#e-mail address: kathryn.mccullough1@marist.edu
#description: Make a program where the user can input text and the computer can output stats on the text

def text():
    print("This program accepts a sentence as input and computes")
    print("a variety of statistics about the sentence.\n")
    
    message = input("Please enter the message to be analyzed: ")
    print()
    
    #number of characters
    character=len(message)

    print("The number of characters: ", character)


    #number of words
    word=len(message.split())

    print("The number of words: ", word)


    #average word count
    avg_word= character/word

    print("The average word count: ", avg_word)

    print()
    print("Thanks for playing!")


text()
