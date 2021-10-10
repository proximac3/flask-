from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'catastrophizing'

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# import classes from survey.py
from surveys import satisfaction_survey


#  number of current question
question_num = [0]

# check if survey is completed
end = [False]

# Home page route
@app.route('/')
def home():
    # reset current question
    question_num[0] = 0

    survey_item = satisfaction_survey
    return render_template('home.html', surver_items = survey_item)

# thank you page route
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# initialize sessions
@app.route('/session', methods=['POST'])
def session():

    # session['responses'] = ['empty']

    return '<h1> jshdfjbsnfjnduno </h1>'


# Route for questions
@app.route('/questions/<int:id>')
def questions(id):

    # if all questions have been answers and user tries to access further questions
    if id > len(satisfaction_survey.questions) -1  and question_num[0] == len(satisfaction_survey.questions) -1 :
        #route to thnak you page
        flash('Invalid Question')
        return redirect(f"/thank_you")
    elif id > question_num[0]:
        # prevenst user fron skipping questions
        flash('Invalid Question')
        return redirect(f"/questions/{question_num[0]}")
    elif id > len(satisfaction_survey.questions) -1:
        #prevents user from accessing questions that do not exist
        flash('Invalid Question')
        return redirect(f"/questions/{question_num[0]}")
    elif id < question_num[0] and question_num[0] == len(satisfaction_survey.questions) -1:
        # prevents user from accessing questions once they've been answereed.
        return redirect(f"/thank_you")
    elif id < question_num[0]:
        #prevents users from going back to already answered questions
        flash('Invalid Question')
        return redirect(f"/questions/{question_num[0]}")
    elif id == len(satisfaction_survey.questions) -1  :
        #prevents user from accessing question after survey is complete
        if end[0] == True:
            return redirect(f"/thank_you")
        else:
            end[0] = True

    surver_questions = satisfaction_survey.questions[id]
    return render_template('questions.html', survey_q = surver_questions)


# route for answers
@app.route('/answer', methods=['POST'])
def answer():
    submitted_answer = []
    if list(request.form)[0]:
        submitted_answer.append(list(request.form)[0])
    elif list(request.form)[0]:
        submitted_answer.append(list(request.form)[0])

    #adding responses to responses data.
    responses_data.append(submitted_answer[0])

    #keeps track of which questions have been answered
    if question_num[0] < len(satisfaction_survey.questions) -1:
        question_num[0]+=1
    elif question_num[0] == len(satisfaction_survey.questions) -1:
        # once all question gets answered, redirect to thank you page
        return redirect('/thank_you')

    return redirect(f"/questions/{question_num[0]}")





@app.route('/demo')
def demo():

    session['username'] = 'ram'

    return render_template('base.html')


# print responses
@app.route('/print')
def print():

    return render_template('base.html')