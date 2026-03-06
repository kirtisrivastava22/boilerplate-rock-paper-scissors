# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[], my_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)

    # reset histories if new match
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()

    # default move
    guess = random.choice(["R", "P", "S"])

    if len(opponent_history) > 2:

        # pattern detection (last 2 moves)
        pattern = "".join(opponent_history[-2:])
        counts = {"R":0, "P":0, "S":0}

        for i in range(len(opponent_history)-2):
            if "".join(opponent_history[i:i+2]) == pattern:
                next_move = opponent_history[i+2]
                counts[next_move] += 1

        predicted = max(counts, key=counts.get)

        counter = {"R":"P", "P":"S", "S":"R"}
        guess = counter[predicted]

    my_history.append(guess)

    return guess