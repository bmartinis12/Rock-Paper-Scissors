steps = {}
counter = 0
def player(prev_play, opponent_history=[]):
    global counter
    global steps
    if prev_play != "":
        opponent_history.append(prev_play)

    n = 3

    log = opponent_history

    guess = "S"
    if len(log) > n:
        pattern = join(log[-n:])
        if join(log[-(n + 1):]) in steps.keys():
            steps[join(log[-(n + 1):])] += 1
        else:
            steps[join(log[-(n + 1):])] = 1
        possible = [pattern + "R", pattern + "P", pattern + "S"]
        for i in possible:
            if not i in steps.keys():
                steps[i] = 0

        predict = max(possible, key=lambda key: steps[key])
        if predict[-1] == "P":
            guess = "S"
        if predict[-1] == "R":
            guess = "P"
        if predict[-1] == "S":
            guess = "R"
    counter += 1
    if counter == 1000:
      steps = {}
      counter = 0
    return guess


def join(moves):
    return "".join(moves)
