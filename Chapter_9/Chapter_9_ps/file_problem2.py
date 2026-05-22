
import random

from dev.PYTHON.Chapter_9.progrsm_4 import FILE


def game():

    print("Welcome to the game!")
    score = random.randint(1, 50)

    # fetch the high score
    highscore = FILE.read()
    if (highscore != ""):
        highscore = int(highscore)
    else:
        highscore = 0
    print(f"your score is {highscore}")
    if (score > highscore):
        with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "w") as FILE:
            FILE.write(str(score))
    return score

game()