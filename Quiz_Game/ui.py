import random
from tkinter import *
from quizworking import QuizBrain

THEME_COLOR = "#375362"
is_right = None


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZBUZZ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Welcome to the Quiz App!"
                 "This quiz consist of 10 questions, select a option corresponding to the question "
                 "here you go!",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.option1 = Button(self.window, text="", width=40, font=('Helvetica', 18), command=lambda: self.option_check(
            self.option1))
        self.option2 = Button(self.window, text="", width=40, font=('Helvetica', 18), command=lambda: self.option_check(
            self.option2))
        self.option3 = Button(self.window, text="", width=40, font=('Helvetica', 18), command=lambda: self.option_check(
            self.option3))
        self.option4 = Button(self.window, text="", width=40, font=('Helvetica', 18), command=lambda: self.option_check(
            self.option4))

        self.button_next = Button(self.window, text='Start', fg='Orange', font=('Verdana', 20),
                                  command=self.get_next_question)
        self.button_restart = Button(self.window, text='ReStart', fg='orange', font=('Verdana', 20),
                                     command=self.get_next_question)
        self.button_next.grid(sticky='W', row=6, column=0, padx=10)
        self.button_restart.grid(sticky='W', row=6, column=1, padx=5)

        self.window.mainloop()

    def display_btn_options(self, options_list, correct_answer):
        self.button_next.config(text="Next")
        index = random.randint(0, 3)
        options_list.insert(index, correct_answer)
        opts = options_list

        self.option1.config(text=opts[0], fg="black")
        self.option2.config(text=opts[1], fg="black")
        self.option3.config(text=opts[2], fg="black")
        self.option4.config(text=opts[3], fg="black")
        options_list.pop(index)

        self.option1.grid(sticky='W', row=2, column=0, columnspan=2, pady=5)
        self.option2.grid(sticky='W', row=3, column=0, columnspan=2, pady=5)
        self.option3.grid(sticky='W', row=4, column=0, columnspan=2, pady=5)
        self.option4.grid(sticky='W', row=5, column=0, columnspan=2, pady=5)

    def disableButtons(self, state):
        self.option1['state'] = state
        self.option2['state'] = state
        self.option3['state'] = state
        self.option4['state'] = state

    def option_check(self, selected_button):
        global is_right

        user_option = selected_button.cget("text")
        is_right = self.quiz.checkAnswer(user_option)
        self.feed_back(is_right)
        selected_button.config(fg="orange")

        # self.disableButtons(state="disabled")

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

        self.button_restart.config(state='disabled')

        self.canvas.config(bg="white")
        self.disableButtons(state="normal")
        self.button_next.config(text="Next")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            q_option = self.quiz.next_options()
            q_answer = self.quiz.next_answer()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.display_btn_options(q_option, q_answer)

        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f" you scored: {self.quiz.score}/10\n Want to Play again?\n  Press RESTART")
            self.disableButtons(state="disabled")
            q_option = self.quiz.next_options()
            q_option.clear()
            self.button_restart.config(state='normal', command=self.restart)

    def restart(self):
        self.canvas.itemconfig(self.question_text,
                               text="Press Start to Start the quiz")
        self.button_next.config(text="Start")
        play_again = True
        self.quiz.ask_play_again(play_again)

    def feed_back(self, is_correct):

        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.disableButtons("disabled")
            q_answer = self.quiz.next_answer()
            self.canvas.config(bg="#8B0000")

            self.canvas.itemconfig(self.question_text, text=f"correct answer:{q_answer}", fill="white")
