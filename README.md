# Number Guessing Game

Python CLI number guessing game with difficulty levels, hints, and a stats summary at the end.

## Features

- Easy (1-50, 10 attempts) and medium (1-100, 7 attempts) difficulty
- "Too high" / "Too low" feedback, plus a "Very close!" hint within 5 of the number
- Input validation for non-numbers and out-of-range guesses
- Play multiple rounds in one session
- End-of-session stats: rounds played, wins, best round, and average attempts

Hard mode is not implemented yet and falls back to medium.

## Tech Used

- Python 3.x
- Standard library only (`random`)

## How to Run

```bash
git clone https://github.com/harshisonthebook/number-guessing-game.git
cd number-guessing-game
python main.py
```

## Example

```
Choose difficulty (easy/medium/hard): easy
I'm thinking of a number from 1 to 50.
Attempt 1/10. Your guess: 25
Too low.
Attempt 2/10. Your guess: 40
Very close! Too high.
Attempt 3/10. Your guess: 38
Correct! You guessed it.
Play again? (y/n) n
Winning round 1: 3 attempt(s)
Rounds played: 1
Wins: 1
Best round: 3 attempt(s)
Average attempts: 3.00
```

## What I Learned

- Using `while` and `for` loops with `break` and `continue`
- Handling bad input with `try` / `except`
- Tracking stats across rounds with lists

## Author

Harsh
[LinkedIn](https://www.linkedin.com/in/harsh-tiwari7)