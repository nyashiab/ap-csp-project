# create_a_task_project_2024

#game setup

#questions/answers from the following websites...

# 1. https://www.funtrivia.com/en/Sports/Track-Field-4674.html
# 2. https://www.braingle.com/trivia/18708/track-and-field.html
# 3. https://www.funtrivia.com/trivia-quiz/Sports/Jamaica-at-the-Olympics-335611.html
# 4. https://www.funtrivia.com/trivia-quiz/Sports/Track-and-Field-158304.html



note2 = "Type in (word for word) your answer choice. \n" #a special reminder to the user
score = 0 #starting score
tot_questions = 4 #num of questions in total

correct_ans = ["baton", "200m", "rubber", "kerron stewart"] #a list of the correct answer for each question
keep_going = True #boolean for the game to keep on going

#game procedures
def choices(a,b,c): #function to display choice for each question 
    print ("a:", a)
    print ("b:", b)
    print ("c:", c)

def intro(): #introduces and explains the user to the game
    print()
    print()
    print("Welcome to the Track & Field Quiz Game! In this game, I ask you a series of question on the sport.\n")
    print("If you answer correctly, you get a point and if you don't, you get no points for that question.\n")
    print("At the end your score will be multiplied by 10 to give you a score out of 40.\n")
    print("Let's get started!\n")

def scores (mutlipier): 
    global score 
    if (score * mutlipier < 30): 
        return "Oh no! You received a low score for this game...better luck next time." 
    elif (score * mutlipier == 30 or score * mutlipier < 40): 
        return "Nice job! You received an average score for this game. You're so close!"
    else: 
        return "YAY! You received a high score for this game. You know your track facts!"

def questions ():
    global note2, correct_ans, score #global variables from game setup

    
    print("Question 1: Runners may refer to this as a 'stick'?\n") 
    choices("Javelin", "Baton", "High Jump Bar")
    print(" ")
    ans=input(note2)

    if ans.lower() == correct_ans[0]: 
        score=score+1
        print("Correct\n")
        
    else:
        print("Incorrect the answer was", correct_ans[0], "\n") 

    #QUESTION 2 

    print("Question 2: How long is one lap around an indoor standard track?\n")
    choices("200m", "800m", "600m")
    print(" ")
    ans = input(note2)
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct\n")
    else:
        print("Incorrect the answer was", correct_ans[1], "\n")
    
    #QUESTION 3 

    print("Question 3: What type of track is the fastest?\n")
    choices("Dirt", "Concrete", "Rubber")
    print(" ")
    ans = input(note2)
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct\n")
    else:
        print("Incorrect the answer was", correct_ans[2], "\n")
    
    #QUESTION 4 

    print("Question 4: Four Jamaican athletes won individual gold medals at the 2008 Olympics, held in Beijing. \n")
    print("Usain Bolt was the only male winner, but do you know which of these women was NOT one of the three ladies who took individual gold?\n")

    choices("Shelly-Ann Fraser", "Kerron Stewart", "Melanie Walker")
    print(" ")
    ans = input(note2)
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct\n")
    else:
        print("Incorrect the answer was", correct_ans[3], "\n")


#game loop

while (keep_going == True):
    intro()
    questions()
    print(scores(10))
    play_again = input("Do you want to play again? Answer with a yes or no.")

    if (play_again == "yes"):
        score = 0
    else: 
        keep_going = False


