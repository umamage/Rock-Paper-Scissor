# This approach uses pattern recognition to anticipate the opponent's moves based on their history 
# and adjusts its strategy accordingly to maximize the win rate.
# Initialize freqPatterns Dictionary: This dictionary will be used to store the frequency of patterns of moves.
freqPatterns={}
# Define the player Function: This function takes prev_play (the opponent's last move) and opponent_history (a list of all previous opponent moves).

def player(prev_play, opponent_history=[]):
    # If prev_play is not empty, it appends it to opponent_history
    if prev_play != "":
        opponent_history.append(prev_play) 
        
    # The variable patternlen is set to 6, which means the AI will look at the last 6 moves to find patterns
    patternlen = 6

    # history is set to opponent_history
    history = opponent_history

    # initialize guess to rock
    guess = "R"

    # If the length of history is greater than patternlen, the code will look for patterns.
    if len(history) > patternlen:
        pattern = convertToStr(history[-patternlen:])
        #print("Pattern: ",pattern)
        
        # The code checks if the current pattern plus the last move exists in the steps dictionary. 
        # If it does, it increments the count; otherwise, it initializes it to 1.
        if convertToStr(history[-(patternlen + 1):]) in freqPatterns.keys():
            freqPatterns[convertToStr(history[-(patternlen + 1):])] += 1
        else:
            freqPatterns[convertToStr(history[-(patternlen + 1):])] = 1
        
        # print(steps)

        # The code generates possible patterns that include the current pattern followed by each possible move (Rock, Paper, Scissors).
        # It ensures that each possible pattern is in the steps dictionary, initializing any missing patterns to 0.

        possiblities = [pattern + "R", pattern + "P", pattern + "S"]

        for i in possiblities:
            if not i in freqPatterns.keys():
                freqPatterns[i] = 0

        # The code predicts the opponent's next move by finding the pattern with the highest count in the steps dictionary.
        oppMove = max(possiblities, key=lambda key: freqPatterns[key])

        # Based on the predicted move, it sets guess to the move that would beat the predicted move:
        # if the last entry in predict equals paper, then guess equals scissor
        # else if the last entry in predict equals rock, then guess equals paper
        # else if the last entry in predict equals scissor, then guess equals rock
        if oppMove[-1] == "P":
            guess = "S"
        elif oppMove[-1] == "R":
            guess = "P"
        elif oppMove[-1] == "S":
            guess = "R"
    # return the guess
    return guess

# convertToStr is a helper function that concatenates a list of moves into a single string.
def convertToStr(moves):
    return "".join(moves)
