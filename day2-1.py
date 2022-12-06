# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
import time;

scoreX = 1;
scoreY = 2;
scoreZ = 3;
wins = ["A Y", "B Z", "C X"];
draws = ["A X", "B Y", "C Z"];
score = 0;
x = "A Y";
f = open("day-2-input", "r");
for l in f:
    if l.strip() in wins:
        score += 6;
        if l.strip()[-1] == "X":
            score += 1;
        if l.strip()[-1] == "Y":
            score += 2;
        if l.strip()[-1] == "Z":
            score += 3;
    elif l.strip() in draws:
        score += 3;
        if l.strip()[-1] == "X":
            score += 1;
        if l.strip()[-1] == "Y":
            score += 2;
        if l.strip()[-1] == "Z":
            score += 3;
    else:
        if l.strip()[-1] == "X":
            score += 1;
        if l.strip()[-1] == "Y":
            score += 2;
        if l.strip()[-1] == "Z":
            score += 3;

print(score);
