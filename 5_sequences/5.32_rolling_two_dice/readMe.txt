5.32

(Intro to Data Science: Rolling Two Dice) Modify the script RollDie.py that we
provided with this chapter’s examples to simulate rolling two dice. Calculate the sum of
the two values. Each die has a value from 1 to 6, so the sum of the values will vary from 2
to 12, with 7 being the most frequent sum, and 2 and 12 the least frequent. The following
diagram shows the 36 equally likely possible combinations of the two dice and their cor-
responding sums:

If you roll the dice 36,000 times:
•The values 2 and 12 each occur 1/36th (2.778%) of the time, so you should
expect about 1000 of each.
•The values 3 and 11 each occur 2/36ths (5.556%) of the time, so you should
expect about 2000 of each, and so on.
Use a command-line argument to obtain the number of rolls. Display a bar plot summa-
rizing the roll frequencies. The following screen captures show the final bar plots for sam-
ple executions of 360, 36,000 and 36,000,000 rolls. Use the Seaborn barplot function’s
optional orient keyword argument to specify a horizontal bar plot.
