# Guess the word

A Wordle clone built with Flask. Guess the hidden 5-letter word in 6 tries.

<a href = "https://guesstheword-cvjb.onrender.com/" target="_blank">Click <b>here</b> </a> to play the live game.

## Here is an example:

![alt text](https://github.com/aatma112/guesstheword/blob/master/game-screenshot.png?raw=false)

## How to play

- Type or click a 5-letter word, then press Guess
- Each letter is colored after a guess:
  - **Green** — correct letter, correct spot
  - **Yellow** — correct letter, wrong spot
  - **Gray** — letter not in the word
- The on-screen keyboard tracks the best-known status of every letter you've used
- You have 6 guesses to find the word.

## Features

- Wordle-style board with full guess history
- Clickable on-screen keyboard with live letter-status colors
- Win/loss detection with a "Play Again" option

## Tech stack

- Python, [Flask](https://flask.palletsprojects.com/)
- Deployed on [Render](https://render.com)

## Run locally

```
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.
