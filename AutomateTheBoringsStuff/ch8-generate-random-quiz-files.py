# randomQuizGenerator.py = creates quizzes with questions and answers in
# random order, along with the answer key.


import random


# The quiz data. Keys are states and values are their capitals.
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
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(1, 36):
    # Create the quiz and answer key files.
    quizFile = open('./quizzes/capitalsquiz%s.txt' % (quizNum), 'w')
    answerKeyFile = open('./quizzes/capitalsquiz_answers%s.txt' % (quizNum), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write('State Capitals Quiz (Form%s)' % (quizNum))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    for question in range(50):
        correct_ans = capitals[states[question]]
        wrong_ans = list(capitals.values())
        wrong_ans.pop(wrong_ans.index(correct_ans))
        wrong_ans = random.sample(wrong_ans, 3)
        ans_option = wrong_ans + [correct_ans]
        random.shuffle(ans_option)

        # Write the question and answer option to the quiz file.
        quizFile.write('{}. What is the capital of {}?\n'.format(question + 1, states[question]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], ans_option[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (question + 1, 'ABCD'[ans_option.index(correct_ans)]))

    quizFile.close()
    answerKeyFile.close()
