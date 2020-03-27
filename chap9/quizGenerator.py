from pathlib import Path
import os
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany',
'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
   
for quizNum in range(35):

    # Create the quiz and answer key files.
    questionDoc = open(f"quizDoc{quizNum}", 'w')
    answerDoc = open(f"answerDoc{quizNum}", 'w')

    # Write out the header for the quiz.
    questionDoc.write(f"Quiz Number #{quizNum} \n\n")
    answerDoc.write(f"Answer Booklet Number #{quizNum} \n\n")
    
    # Shuffle the order of the states
    questions = list(capitals.keys())
    random.shuffle(questions)
    potentialAnswers = list(capitals.values())
    random.shuffle(potentialAnswers)
    
    # Loop through all 50 states, making a question for each.
    for i in range(50):

        #the real answer to the question
        trueAnswer = capitals[f'{questions[i]}']

        #list of wrong answers to choose three MCQ answers from
        wrongAnswers = [answer for answer in potentialAnswers if answer != trueAnswer]

        questionDoc.write(f"\nQ{i}: What is the capital of {questions[i]}?\n")
        
        questionDoc.write(f"(A) {random.choice(wrongAnswers)}\n(B) {random.choice(wrongAnswers)}\n(C) {random.choice(wrongAnswers)}\n(D) {trueAnswer}")

        answerDoc.write(f'Answer for Q{i}: {trueAnswer}\n')

    questionDoc.close()
    answerDoc.close()
