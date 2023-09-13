import html
from tkinter import *
from tkinter import StringVar


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.current_option = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def next_options(self):
        self.current_option = self.question_list[self.question_number-1]
        q_option = html.unescape(self.current_option.options)
        return q_option

    def next_answer(self):
        self.current_option = self.question_list[self.question_number-1]
        q_answer = html.unescape(self.current_option.answer)
        return q_answer

    def checkAnswer(self, radio):
        self.current_question = self.question_list[self.question_number-1]
        correct_answer = self.current_question.answer
        if radio.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def ask_play_again(self, play_again):
        if play_again:
            self.question_number = 0
            self.score = 0
            self.current_question = None
            self.current_option = None


