from ctypes import alignment
from tkinter import *
from tkinter import messagebox as mb
import json


#Class for GUI components
class Assessment(object):

    def __init__(self, database_filename, gui):
         
        #Snag data 
        with open(database_filename) as f:
            data = json.load(f)
 
        self.gui = gui

        #Set statements, framing and responses 
        self.statements = (data['statements'])
        self.framing = (data['framing'])
        self.responses = (data['responses'])


        #Set statement number to 0
        self.statement_num=0
        
        #Display title and instructions 
        self.display_title()

        #Assigns statements to display_statements function to update later
        self.display_statements()
         
        #Holds an integer value which is used for selected option in a question.
        self.resp_selected=IntVar()
        
        #Display radio buttons
        self.resps = self.radio_buttons()
         
        #Display responses
        self.display_responses()
         
        #Display next button
        self.buttons()
         
        #Number of statements
        self.data_size = len(self.statements)
         
        #Counter of score
        self.score=0
        

    # generate score for a statement and add to self.score
    def generate_score(self, statement_num):

        #self.resp_selected.get() is an int not a string!
        # Please check if my associations for P and N
        # are correct.

        #Calculate scoring for positively framed questions 
        if self.framing[statement_num] == "P":
            if self.resp_selected.get() == 1:
                self.score += 5
            elif self.resp_selected.get() == 2:
                self.score += 4   
            elif self.resp_selected.get() == 3:
                self.score += 3 
            elif self.resp_selected.get() == 4:
                self.score += 2 
            elif self.resp_selected.get() == 5:
                self.score += 1 

        #Calculate scoring for negatively framed questions 
        else:
            if self.resp_selected.get() == 1:
                self.score += 1   
            elif self.resp_selected.get() == 2:
                self.score += 2   
            elif self.resp_selected.get() == 3:
                self.score += 3 
            elif self.resp_selected.get() == 4:
                self.score += 4 
            elif self.resp_selected.get() == 5:
                self.score += 5 
        
        #print(self.score)


    #Display result in message box 
    def display_result(self):

        #Calculate average score 
        result = round(float(self.score / self.data_size), 2)
        
        score_1 = "You scored a", result, "which means you have extremely low grit."
        score_2 = "You scored a", result, "which means you have low grit."
        score_3 = "You scored a", result, "which means you have medium grit."
        score_4 = "You scored a", result, "which means you have high grit."
        score_5 = "You scored a", result, "which means you have extremely high grit."

        #Message box to display results
        if result <= 1: 
            mb.showinfo("Result", score_1)
        elif result <= 2:
            mb.showinfo("Result", score_2)
        elif result <= 3:
            mb.showinfo("Result", score_3)
        elif result <= 4:
            mb.showinfo("Result", score_4)
        elif result <= 5:
            mb.showinfo("Result", score_5)
    
    
    #Show next statement
    def next_btn(self):
        
        enter_value = "Please select a value before hitting next."

        #Message box to display error message 
        if self.resp_selected.get() == 0:
            mb.showerror("Error", enter_value)
            return

        # score current statement
        self.generate_score(self.statement_num)

        #Move to next Question by incrementing the statement_num counter
        self.statement_num += 1
         
        #Check if statement_num = data size
        if self.statement_num == self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            gui.destroy()

        else:
            #Show the next question
            self.display_statements()
            self.display_responses()
 
 
    #Display button on the screen
    def buttons(self):
         
        #Next button 
        next_button = Button(self.gui, text="Next", command=self.next_btn, width=10, 
                             bg="green", fg="white", font=("Arial", 16, "bold"))
        next_button.place(x=350, y=380)
 
        #Quit button 
        quit_button = Button(self.gui, text="Quit", command=gui.destroy, width=10, 
                             bg="red", fg="white", font=("Arial", 16, "bold"))
        quit_button.place(x=40, y=380)


    #Display responses (next to radio buttons including select/deselect behavior)
    def display_responses(self):
        val=0
         
        #Deselect radio buttons 
        self.resp_selected.set(0)
         
        #Display responses next to radio buttons 
        for response in self.responses[self.statement_num]:
            self.resps[val]['text']=response
            val+=1

 
    #Display statements 
    def display_statements(self):
         
        #Statement formatting 
        statement_num = Label(self.gui, text=self.statements[self.statement_num], 
                              width=100, font=("Arial", 16, "bold"), anchor='w')
         
        #Statement placement
        statement_num.place(x=70, y=100)
 
    
    #Display radio buttons 
    def radio_buttons(self):
         
        #Empty response list 
        r_list = []
         
        #Response placement 
        y_pos = 150
         
        #Add responses to list 
        while len(r_list) < 5:
             
            #Radio button formatting 
            radio_btn = Radiobutton(self.gui, text=" ", variable=self.resp_selected, value=len(r_list)+1, font=("Arial", 14))
            

            #Add radio button to list 
            r_list.append(radio_btn)
             
            #Radio button placement 
            radio_btn.place(x=100, y=y_pos)

             
            #Increment the y-axis position by 40
            y_pos += 40
         
        #Return radio buttons
        return r_list
    
    #This method is used to Display Title
    def display_title(self):
         
        #Display title 
        title = Label(gui, text="Grit Scale Questionnaire", fg="black", font=("Arial", 20, "bold"))
         
        #Place title 
        title.place(x=0, y=2)
 
        #Display instructions
        title = Label(gui, text="Please respond to the following statement. Be honest - there are no right or wrong answers.", fg="black", font=("Arial", 12,))
         
        #Place instructions
        title.place(x=0, y=40)


#GUI window
gui = Tk()
 
#GUI window size 
gui.geometry("1200x600")
 
#GUI window title 
gui.title("Grit Scale")
 
#Object of class
assessment = Assessment("data.json", gui)
 
#Launch GUI
gui.mainloop()


#Intro landing page 
#WHAT IS GRIT?
#• Grit is defined as perseverance and passion for long-term goals
#• It entails working strenuously toward challenges, maintaining effort and interest over years despite failure, adversity, and plateaus in progress
#• Grit is unrelated to talent and can be built through a growth mindset
