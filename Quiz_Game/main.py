import tkinter as tk
from tkinter import messagebox
from quizworking import QuizBrain
from question_model import Question
from data import question_data
from ui import QuizInterface
import random

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_options = question["incorrect_answers"]

    new_question = Question(question_text, question_answer, question_options)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)



