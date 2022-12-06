# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) ...
# ...plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

scoreX = 1;
scoreY = 2;
scoreZ = 3;
wins = {"A" : "Y", "B" : "Z", "C" : "X"}
draws = {"A" : "X", "B" : "Y", "C" : "Z"}
losses = {"A": "Z", "B": "X", "C": "Y"}
scores = {"X": 1, "Y": 2, "Z": 3}
score = 0;
f = open("day-2-input", "r");

for l in f:
    if l.strip()[-1] == "Z":
        myPlay = wins.get(l.strip()[-3]);
        score += 6;
        score += scores.get(myPlay);
    elif l.strip()[-1] == "Y":
        myPlay = draws.get(l.strip()[-3]);
        score += 3;
        score += scores.get(myPlay);
    else:
        myPlay = losses.get(l.strip()[-3]);
        score += scores.get(myPlay);
print (score);


