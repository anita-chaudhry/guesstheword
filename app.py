from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

WORD_LIST = ['ABORD', 'DRINK', 'FLOOR', 'REPLY', 'STONE', 'UNCLE', 'PLANT', 'APPLE', 'CROWD', 'RIGHT', 'DRESS', 'VIDEO', 'OFFER', 'HOUSE', 'LIGHT', 'PHONE', 'PEACE', 'TOWER']
MAX_GUESSES = 6
KEYBOARD_ROWS = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
STATUS_PRIORITY = {'absent': 0, 'present': 1, 'correct': 2}


def get_new_word():
    return WORD_LIST[randint(0, len(WORD_LIST) - 1)]


def score_guess(word, guess):
    return [
        'correct' if c == word[i] else 'present' if c in word else 'absent'
        for i, c in enumerate(guess)
    ]


def compute_key_status(rows):
    status = {}
    for guess, scores in rows:
        for letter, score in zip(guess, scores):
            if letter not in status or STATUS_PRIORITY[score] > STATUS_PRIORITY[status[letter]]:
                status[letter] = score
    return status


@app.route('/', methods=['GET', 'POST'])
def wordule():
    error = None

    if request.method == 'POST' and 'history' in request.form:
        word = request.form['word']
        history = request.form['history'].split(',') if request.form['history'] else []
        guess = request.form.get('guess', '').strip().upper()

        if len(guess) != 5 or not guess.isalpha():
            error = 'Enter a 5-letter word.'
        elif len(history) < MAX_GUESSES:
            history.append(guess)
    else:
        word = get_new_word()
        history = []

    won = word in history
    lost = not won and len(history) >= MAX_GUESSES
    rows = [(guess, score_guess(word, guess)) for guess in history]

    return render_template(
        'index.html',
        word=word,
        history=','.join(history),
        rows=rows,
        remaining=range(MAX_GUESSES - len(history)),
        guess_count=len(history),
        won=won,
        lost=lost,
        error=error,
        keyboard_rows=KEYBOARD_ROWS,
        key_status=compute_key_status(rows),
    )


if __name__ == '__main__':
    app.run(debug=True)
