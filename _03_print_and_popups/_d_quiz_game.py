from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    Score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    math = simpledialog.askinteger(title= 'Hmmm1', prompt= "whats 48.355x36?   (round)")
    #      // 2.  Ask the user a question 

    #      // 3.  Use an if statement to check if their answer is correct
    if math==1741:
    #      // 4.  if the user's answer was correct, add one to their score 
        Score = Score+1


    build = simpledialog.askstring(title= 'Hmmmm2', prompt= "Whats the tallest building?")
    if build=="burj khalifa":
        Score = Score+2


    history = simpledialog.askstring(title= 'Hmmmmm3', prompt= "When did christopher Columbus come to the Americas ")
    if history==1492:
        Score = Score+3


    print(Score)
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
