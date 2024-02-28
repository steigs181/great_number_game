from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'berries and cream'

@app.route('/')
def index ():
    # conditional creating a variable for number of tries, subtracting based on attempts
    if 'num_of_tries' not in session:
        session['num_of_tries'] = 5
        print(session['num_of_tries'])
    else:
        session['num_of_tries'] = session['num_of_tries'] - 1
        print(session['num_of_tries'])
    return render_template("index.html"), session['num_of_tries']

@app.route('/guess', methods=['POST'])
def guess_the_number():
    # variables
    session['num_guessed'] = int(request.form['num_guessed'])
    answer_int = random.randint(1, 100)
    session['num_of_tries'] = session['num_of_tries']

    # conditionals to check attempts and answer
    if session['num_of_tries'] <= 0:
        if  session['num_guessed'] == answer_int:
            return redirect('/guess_correct')
        else:
            return redirect('/guess_correct')
    else:
        print ('try again')
    return render_template("guess.html")

app.route('/play_again', methods=['POST'])
def Again ():
    session['again'] = request.form['again']
    if 'play_again' in session:
        print('key in session')
    else:
        print('key not in session')
    return redirect ('/')

@app.route('/guess_correct')
def game_end():
    return render_template('guess_correct.html')

if __name__ == "__main__":
    app.run(debug=True)