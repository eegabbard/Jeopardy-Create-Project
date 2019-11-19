#Emily Gabbard
#Create Project: Trivia
#Section F

#print("In this game of Trivia, your goal is get as many points as you can before getting three wrong! After a game is finished, you'll get an output file", end=" ")
#print("with your score and the questions you got wrong so you can study up! You'll be given a random question, and you get the question right, you get a point.", end=" ")
#print("Once you get three wrong, you get will get a GAME OVER, but you can always replay!")
#print("Good Luck!")

import random
import csv

answers = ["Hydrogen", "Mercury"] 

with open("Trivia.txt", "r") as file:
    contents = file.read()
    questions = contents.split(",")
    
print(questions[1])


#OKKAAYYYYY so what I'm planning on doing is creating an input file with a whole bunch of questions and also create a list of answers where the indexes match
#and then I'm going to pick a random number and assign (this would be a good function) it to a varible and then output that question and see if input equals
#the answer at the same index. I also need to have an incorrect counter and a correct counter and I also dont really want to have an output file since I
#already have an input file. okay youve got this tho :)
