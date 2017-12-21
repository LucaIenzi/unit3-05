# Created by: luca.ienzi
# Created on: nov 2017
# Created for: ICS3U
#  This program is a facorical program

import ui


def calculate(sender): 
    user_answer = int(view['user_answer'].text)
    if user_answer >= 0:
      factorial = 1
      while (user_answer >= 1):
         factorial = factorial * user_answer
         view['answer_lable'].text = "The answer is" + str (factorial)
         user_answer = user_answer - 1
view = ui.load_view()
view.present('sheet')
import ui


def calculate(sender): 
    user_answer = int(view['user_answer'].text)
    if user_answer >= 0:
      factorial = 1
      while (user_answer >= 1):
         factorial = factorial * user_answer
         view['answer_lable'].text = "The answer is" + str (factorial)
         user_answer = user_answer - 1
view = ui.load_view()
view.present('sheet')
