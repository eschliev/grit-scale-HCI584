from ctypes import alignment
from tkinter import *
from tkinter import messagebox as mb
import json

# Class for GUI components

class Assessment(object):

    def __init__(self, database_filename, gui):

        # Snag data
        with open(database_filename) as f:
            data = json.load(f)

        self.gui = gui

        # Set statements, framing and responses
        self.statements = data['statements']
        self.framing = data['framing']
        self.responses = data['responses']

        # have a list for the actual responses
        self.response_values = []

        # Set statement number to 0
        self.statement_num = 0

        # Display title and instructions
        self.display_title()

        # Assigns statements to display_statements function to update later
        self.display_statements()

        # Holds an integer value which is used for selected option in a question.
        self.resp_selected = IntVar()

        # Display radio buttons
        self.resps = self.radio_buttons()

        # Display responses
        self.display_responses()

        # Display next button
        self.buttons()

        # Number of statements
        self.data_size = len(self.statements)

        # Counter of score
        self.score = 0

    # generate score for a statement and add to self.score
    def generate_score(self, statement_num):

        # Calculate scoring for positively framed questions
        if self.framing[statement_num] == "P":
            if self.resp_selected.get() == 1:
                self.score += 5
                self.response_values.append(5) # record the value, do this for all other cases
            elif self.resp_selected.get() == 2:
                self.score += 4
                self.response_values.append(4)
            elif self.resp_selected.get() == 3:
                self.score += 3
                self.response_values.append(3)
            elif self.resp_selected.get() == 4:
                self.score += 2
                self.response_values.append(2)
            elif self.resp_selected.get() == 5:
                self.score += 1
                self.response_values.append(1)

        # Calculate scoring for negatively framed questions
        else:
            if self.resp_selected.get() == 1:
                self.score += 1
                self.response_values.append(1)
            elif self.resp_selected.get() == 2:
                self.score += 2
                self.response_values.append(2)
            elif self.resp_selected.get() == 3:
                self.score += 3
                self.response_values.append(3)
            elif self.resp_selected.get() == 4:
                self.score += 4
                self.response_values.append(4)
            elif self.resp_selected.get() == 5:
                self.score += 5
                self.response_values.append(5)

        # print(self.score)

    # Display result in message box

    def display_result(self):

        # Calculate average score
        result = round(float(self.score / self.data_size), 2)

        # Dict that associates the text with a score
        grit_words = {1: "extremely low",
                      2: "low",
                      3: "medium",
                      4: "high",
                      5: "extremely high"}

        # Calculate level (int) from float result
        grit_level = int(result)

        grit_as_word = grit_words[grit_level]

        score_msg = f"You scored a {result} which means you have {grit_as_word} grit."

        mb.showinfo("Result", score_msg)

        print(self.data_size)
        print("value count")

        print(len(self.response_values))

    # length of this values should be same with self.data_size

        # save table of questions and this user's responses
        # use the user's name once you have that added
        with open("results.csv", "w+") as fo:
            for i in range(0, self.data_size): #loop over all statements
                statement = self.statements[i] #gather statement options  
                possible_responses = self.responses[i] #gather responses options
                response_value = self.response_values[i] # this assumes that we have 12 values in that list!
                index = response_value - 1 # convert 1 to 5 into an index (0 to 4)  
                response_text = possible_responses[index] 
                print(f"{i},{statement},{response_text},{response_value}", file=fo) # format with commas and write to file
            print(f"Final Grit Score = {result}, {grit_as_word}", file=fo)

    # Show next statement
    def next_btn(self):

        enter_value = "Please select a value before hitting next."

        # Message box to display error message
        if self.resp_selected.get() == 0:
            mb.showerror("Error", enter_value)
            return

        # score current statement
        self.generate_score(self.statement_num)

        # Move to next Question by incrementing the statement_num counter
        self.statement_num += 1

        # Check if statement_num = data size
        if self.statement_num == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI
            gui.destroy()

        else:
            # Show the next question
            self.display_statements()
            self.display_responses()

    # Display button on the screen

    def buttons(self):

        # Next button
        next_button = Button(self.gui, text="Next", command=self.next_btn, width=10,
                             bg="#288a2e", fg="white", font=("Arial", 16, "bold"))
        next_button.place(x=55, y=470)

        # Quit button
        quit_button = Button(self.gui, text="Quit", command=gui.destroy, width=10,
                             bg="#b0210e", fg="white", font=("Arial", 16, "bold"))
        quit_button.place(x=1050, y=550)

    # Display responses (next to radio buttons including select/deselect behavior)

    def display_responses(self):
        val = 0

        # Deselect radio buttons
        self.resp_selected.set(0)

        # Display responses next to radio buttons
        for response in self.responses[self.statement_num]:
            self.resps[val]['text'] = response
            val += 1

    # Display statements

    def display_statements(self):

        # Statement formatting
        statement_num = Label(self.gui, text=self.statements[self.statement_num],
                              width=100, font=("Arial", 16, "bold"), anchor='w')

        # Statement placement
        statement_num.place(x=50, y=220)

    # Display radio buttons

    def radio_buttons(self):

        # Empty response list
        r_list = []

        # Response placement
        y_pos = 260

        # Add responses to list
        while len(r_list) < 5:

            # Radio button formatting
            radio_btn = Radiobutton(self.gui, text=" ", variable=self.resp_selected, value=len(
                r_list)+1, font=("Arial", 14))

            # Add radio button to list
            r_list.append(radio_btn)

            # Radio button placement
            radio_btn.place(x=50, y=y_pos)

            # Increment the y-axis position by 40
            y_pos += 40

        # Return radio buttons
        return r_list

    # This method is used to Display Title
    def display_title(self):

        # Display/place title
        title = Label(gui, text="Grit Scale Questionnaire", width=71,
                      bg="black", fg="white", font=("Arial", 20, "bold"))
        title.place(x=0, y=2)

        # Display/place name entry
        Label(gui, text="Enter First Name", fg="black",
              font=("Arial", 12,)).place(x=40, y=120)
        name = Entry(gui)
        name.place(x=180, y=120)

        # Display/place instructions
        title = Label(gui,  text="Please respond to the following statement. Be honest - there are no right or wrong answers.",
                      fg="black", font=("Arial", 12,))
        title.place(x=40, y=160)

        # Display/place line break
        title = Label(gui, text="--------------------------------------------------------------------------------------------------------------------------------",
                      fg="black", font=("Arial", 12,))
        title.place(x=40, y=185)


# GUI window
gui = Tk()

# GUI window size
gui.geometry("1200x600")

# GUI window title
gui.title("Grit Scale")

# Object of class
assessment = Assessment("data.json", gui)

# Launch GUI
gui.mainloop()
