import random

def get_statements():
    statements = []
    statements.append(["I have overcome setbacks to conquer an important challenge.", "P"])
    statements.append(["New ideas and projects sometimes distract me from previous ones.", "N"])
    statements.append(["My interests change from year to year.", "N"])
    statements.append(["Setbacks don’t discourage me.", "P"])
    statements.append(["I have been obsessed with a certain idea or project for a short time but later lost interest.", "N"])
    statements.append(["I am a hard worker.", "P"])
    statements.append(["I often set a goal but later choose to pursue a different one.", "N"])
    statements.append(["I have difficulty maintaining my focus on projects that take more than a few months to complete.", "N"])
    statements.append(["I finish whatever I begin.", "P"])
    statements.append(["I have achieved a goal that took years of work.", "P"])
    statements.append(["I become interested in new pursuits every few months.", "N"])
    statements.append(["I am diligent.", "P"])

    return statements

def execute_questionnaire():
    
    #Get statements
    grit_statements = get_statements()

    #Randomize statements
    random.shuffle(grit_statements)

    #Set Score
    score = 0 

    #Display statements using loop

    for s in grit_statements:
        #Present statement
        print(s[0])
        
        #Request user answer
        answer = input("a) Very much like me\nb) Mostly like me\nc) Somewhat like me\nd) Not much like me\ne) Not like me at all\n:")
        
        if s[1] == "P":
        #Calculate scoring for positively framed questions 
            if answer.lower() == "a":
                score = score + 5   
            elif answer.lower() == "b":
                score = score + 4   
            elif answer.lower() == "c":
                score = score + 3 
            elif answer.lower() == "d":
                score = score + 2 
            elif answer.lower() == "e":
                score = score + 1  
            else: 
                print("You must enter a, b, c, d or e.")
        
        if s[1] == "N":
        #Calculate scoring for positively framed questions 
            if answer.lower() == "a":
                score = score + 1   
            elif answer.lower() == "b":
                score = score + 2   
            elif answer.lower() == "c":
                score = score + 3 
            elif answer.lower() == "d":
                score = score + 4 
            elif answer.lower() == "e":
                score = score + 5  
            else: 
                print("You must enter a, b, c, d or e.")

    #Total Score 
    final_score = float(score / 12)
    print("You scored a", final_score)

def instructions():
    print("Please respond to the following 12 statements. Be honest, there are no right or wrong answers!")

instructions()
execute_questionnaire()
