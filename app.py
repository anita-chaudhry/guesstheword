from flask import Flask, request
from random import randint

app = Flask(__name__)

word_List = ['Abord', 'Drink', 'Floor', 'Reply', 'stone', 'Uncle', 'Plant', 'Apple', 'Crowd', 'Right', 'Dress', 'Video', 'Offer', 'Horn', 'Light', 'Phone', 'Peace', 'Tower']


def get_new_word():
    last_index = len(word_List) - 1
    new_word_index = randint(0, last_index)
    new_word = word_List[new_word_index]
    return new_word.upper()


def box_html(color):
    return '<span style="color:' + color + '; font-size: 3em">&#9632;</span>'


def guess_stats_html(word, guess, guess_num):
    html = ''
    for i, c in enumerate(guess):
        if c == word[i]:
            html += box_html('green')  # correct place
        elif c in word:
            html += box_html('yellow')  # incorrect place
        else:
            html += box_html('red')  # not right letter

    if word == guess:
        html += '<div> Yay! You got it in ' + str(guess_num) + ' guesses! </div>'

    return html


@app.route('/', methods=['GET', 'POST'])
def wordule():
    if request.method == 'GET' or 'guess' not in request.form:
        word = get_new_word()
        guess = ''
        guess_num = 0
        stats_html = ''
    else:
        word = request.form.get('word')
        guess = request.form.get('guess', '').upper()
        guess_num = int(request.form.get('guess_num', 0)) + 1
        stats_html = guess_stats_html(word, guess, guess_num)

    return (
        '<h1>Wordule</h1>'
        '<p>Try to guess the word!</p>'
        + stats_html +
        '<form method="post">'
        '<input type="text" name="guess" maxlength="5" value="' + guess + '">'
        '<input type="hidden" name="word" value="' + word + '" />'
        '<input type="hidden" name="guess_num" value="' + str(guess_num) + '"/>'
        '<input type="submit" value="Guess!" />'
        '</form>'
    )


if __name__ == '__main__':
    app.run(debug=True)
