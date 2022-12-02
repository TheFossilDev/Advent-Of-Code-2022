# Challenge 2: Run a simulated set of rock-paper-scissors game and get the score

# The potentially complicated part of this one is managing the possibilities for outcomes
# I'm going to make a dictionary of the throws I make vs the scores I get for each, and then make a list of scenarios that I win
# If the throw isn't in any of those, then it's either a draw or loss
# A draw is if the two throws are equal so that's easy to check with another list

pointsPerThrow = {
  "X": 1, # Rock
  "Y": 2, # Paper
  "Z": 3  # Scissors
}

drawCombos = ["A X", "B Y", "C Z"]

# I win if R + P, P + S, S + R
winningCombos = ["A Y", "B Z", "C X"]

FILENAME = "input.txt"
inputFile = open(FILENAME, "r")

totalScore = 0
for line in inputFile:
  # print(line[0], "vs", line[2])
  totalScore += pointsPerThrow[line[2]]
  if line.strip() in winningCombos:
    totalScore += 6
  elif line.strip() in drawCombos:
    totalScore += 3

print("You would win",totalScore,"points!")

# ======== Part 2 =========

# Now I need to try to intentially win or lose or draw each round.
# I'll use another dictionary to figure out what I need to throw to do what

throwToWin = {
  "A": 2, # They throw rock, I throw paper
  "B": 3, # They throw paper, I throw scissors
  "C": 1  # They throw scissors, I throw rock
}

throwToDraw = {  # I just match them
  "A": 1,
  "B": 2,
  "C": 3
}

throwToLose = {
  "A": 3, # They throw rock, I throw scissors
  "B": 1, # They throw paper, I throw rock
  "C": 2, # They throw scissors, I throw paper
}

totalScore = 0
# Need to close and reopen the file to walk through it again
inputFile.close()
inputFile = open(FILENAME, "r")

for line in inputFile:
  # Using a "switch statement" here instead of if/else
  match line[2]:
    case "X": # Lose
      totalScore += 0 + throwToLose[line[0]]
    case "Y": # Draw
      totalScore += 3 + throwToDraw[line[0]]
    case "Z": # Win
      totalScore += 6 + throwToWin[line[0]]

print("You would get", totalScore, "points!")