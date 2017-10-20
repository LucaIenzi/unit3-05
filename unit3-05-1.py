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
