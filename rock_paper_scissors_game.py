# Created by: Jenny Trac
# Created on: Oct 10 2017
# Let's the user play rock, paper, scissors against the computer

import ui
from numpy import random

computer_choice = random.randint(1, 4)

print(computer_choice)

def rock_touch_up_inside(sender):
    if computer_choice == 1:
        view['result_label'].text = "The computer chose rock. You tied."
    if computer_choice == 2:
        view['result_label'].text = "The computer chose paper. You lose."
    if computer_choice == 3:
        view['result_label'].text = "The computer chose scissors. You win."

def paper_touch_up_inside(sender):
    if computer_choice == 1:
        view['result_label'].text = "The computer chose rock. You win."
    if computer_choice == 2:
        view['result_label'].text = "The computer chose paper. You tied."
    if computer_choice == 3:
        view['result_label'].text = "The computer chose scissors. You loser."
        
def scissors_touch_up_inside(sender):
    if computer_choice == 1:
        view['result_label'].text = "The computer chose rock. You lose."
    if computer_choice == 2:
        view['result_label'].text = "The computer chose paper. You win."
    if computer_choice == 3:
        view['result_label'].text = "The computer chose scissors. You tied."

view = ui.load_view()
view.present('sheet')
