7.1 (Filling arrays) Fill a 2-by-3 array with ones, a 3-by-3 array with zeros and a 
2 by 5 array with 7s.

7.2 (Broadcasting) Use arange to create a 2-by-2 array containing the numbers 0–3.
Use broadcasting to perform each of the following operations on the original array:
a) Cube every element of the array.
b) Add 7 to every element of the array.
c) Multiply every element of the array by 2.

7.3 (Element-Wise array Multiplication) Create a 10-by-10 array containing the
number 4 in each position. Create a second 10-by-10 array containing the numbers 1 to
100 in ascending order. Multiply the first array by the second array.

7.4 (array from List of Lists) Create an array from a list of two lists. The first list consists of the even numbers counting down from 10 to 0 and the second counting up from 0 to 10.

7.5 (Flattening arrays with flatten vs. ravel) Using the array created in
Exercise 7.4, first, flatten the array with the method flatten. Change the second element of the new array to 10. Compare the new and the original array. Second, flatten the array using the method ravel and perform the same comparison.

7.6 (Research: array Method astype) Research in the NumPy documentation the
array method astype, which converts an array’s elements to another type. Use
linspace to create a 1-by-6 array with the values 1.1, 2.2, …, 6.6. Then, use astype to
convert the array to integers, then convert it to an array with floats and finally, convert it to an array of strings.

7.7 (Challenge Project: Reimplement NumPy array Output) You saw that NumPy out-
puts two-dimensional arrays in a nice column-based format that right-aligns every element in a field width. The field width’s size is determined by the array element value that requires the most character positions to display. To understand how powerful it is to have this for matting simply built-in, write a function that reimplements NumPy’s array formatting for two-dimensional arrays using loops. Assume the array contains only positive integer values.

7.8 (Challenge Project: Reimplement DataFrame Output) You saw that pandas displays
DataFrames in an attractive column-based format with row and column labels. The values
within each column are right aligned in the same field width, which is determined by that column’s widest value. To understand how powerful it is to have this formatting built-in,write a function that reimplements DataFrame formatting using loops. Assume the Data-Frame contains only positive integer values and that both the row and column labels are each integer values beginning at 0.

7.9 (Indexing and Slicing arrays) Create an array containing the values 1–15,
reshape it into a 3-by-5 array, then use indexing and slicing techniques to perform each of the following operations: [implement operations (a) to (c) twice, once with positive indexing and once with negative indexing]:
a) Select row 2.
b) Select column 4.
c) Select columns 1–3.
d) Select the element that is in row 1 and column 4.
e) Select all elements from rows 1 and 2 that are in columns 0, 2, and 4.

7.10 (Project: Two-Player, Two-Dimensional Tic-Tac-Toe) Write a script to play two-
dimensional Tic-Tac-Toe between two human players who alternate entering their moves
on the same computer. Use a 3-by-3 two-dimensional array. Each player indicates their
moves by entering a pair of numbers representing the row and column indices of the
square in which they want to place their mark, either an 'X' or an 'O'. When the first player moves, place an 'X' in the specified square. When the second player moves, place an 'O' in the specified square. Each move must be to an empty square. After each move, determine whether the game has been won and whether it’s a draw.

7.11 (Challenge Project: Tic-Tac-Toe with Player Against the Computer) Modify your
script from the previous exercise so that the computer makes the moves for one of the players. Also, allow the player to specify whether he or she wants to go first or second.

7.12 (Super Challenge Project: 3D Tic-Tac-Toe with Player Against the Computer) De-
velop a script that plays three-dimensional Tic-Tac-Toe on a 4-by-4-by-4 board. [Note: This is an extremely challenging project! In the “Deep Learning” chapter, you’ll learn techniques that will help you develop and AI-based approach to solving this problem.]

7.13 (Research and Use Other Broadcasting Capabilities) Research the NumPy broad-
casting rules, then create your own arrays to test the rules.

7.14 (Horizontal and Vertical Stacking and Splitting) Create the following arrays:
array1 = np.array([[0, 2], [4, 6]])
array2 = np.array([[1, 3], [5, 7]])
a) Use horizontal stacking to create array3 with array2 to the right of array1.
b) Use vertical splitting to create array4 and array5, with array4 containing the
top row of array3 and array5 containing the bottom row.
c) Sort both array4 and array5 and use horizontal stacking for both sorted
arrays to create array6.
d) Use vertical stacking to create array7 stacking array6 and the product of
array6 with 10.

7.15 (Research and Use NumPy’s concatenate Function) Research NumPy function
concatenate, then use it to reimplement parts (a), (c), and (d) from the previous exercise.

7.16 (Research: NumPy tile Function) Research NumPy's tile function. Use the
tile, vstack, and hstack functions to create a checkerboard pattern. Each “square”
should consist of 4 zeros or 4 ones.

7.17 (Research: NumPy bincount Function) Use the Numpy randint function to cre-
ate an array of 99 0’s and 1’s. A “0” indicates a vote for Candidate 1 and a “1” indicates a vote for Candidate 2. Research and use the NumPy bincount function to count the number of votes per candidate

7.18 (Median and Mode of an array) NumPy arrays offer a mean method, but not
median or mode. Write functions median and mode that use existing NumPy capabilities to
determine the median (middle) and mode (most frequent) of the values in an array. Your
functions should determine the median and mode regardless of the array’s shape. Test your function on three arrays of different shapes.

7.19 (Enhanced Median and Mode of an array) Modify your functions from the pre-
vious exercise to allow the user to provide an axis keyword argument so the calculations can be performed row-by-row or column-by-column on a two-dimensional array.

7.20 (Performance Analysis) In this chapter, we used %timeit to compare the average ex-
ecution times of generating a list of 6,000,000 random die rolls vs. generating an array of 6,000,000 random die rolls. Though we saw approximately two orders of magnitude performance improvement with array, we generated the list and the array using two different random-number generators and different techniques for building each collection. If you use the same techniques we showed to generate a one-element list and a one-element array, creating the list is slightly faster. Repeat the %timeit operations for one-element collections. Then do it again for 10, 100, 1000, 10,000, 100,000, and 1,000,000 elements and compare the results on your system. The table below shows the results on our system, with measurements in nanoseconds (ns), microseconds (μs), milliseconds (ms) and seconds (s).

Number of values List average execution time array average execution time
1                    1.56 μs ± 25.2 ns                  1.89 μs ± 24.4 ns
10                   11.6 μs ± 59.6 ns                  1.96 μs ± 27.6 ns
100                   109 μs ± 1.61 μs                     3 μs ± 147 ns
1000                 1.09 ms ± 8.59 μs                  12.3 μs ± 419 ns
10,000               11.1 ms ± 210 μs                    102 μs ± 669 ns
100,000                111 ms ± 1.77 ms                 1.02 ms ± 32.9 μs
1,000,000               1.1 s ± 8.47 ms                 10.1 ms ± 250 μs

This analysis shows why %timeit is convenient for quick performance studies. How-
ever, you also need to develop performance-analysis wisdom. Many factors can affect performance—the underlying hardware, the operating system, the interpreter or compiler
you’re using, the other applications running on your computer at the same time, and
many more. The way we thought about performance over the years is changing rapidly
now with big data, data analytics and artificial intelligence. As we head into the AI portion of the book, you’ll place enormous performance demands on your system, so it’s
always good to be thinking about performance issues

7.21 (Shallow vs. Deep Copy) In this chapter, we discussed shallow vs. deep copies of
arrays. A shallow copy can be made in several ways. Research the different ways to makea copy of a dictionary. Use the following dictionary
dictionary = {'Sophia': [97, 88]}
implement two different methods to make a shallow copy of this dictionary. Then, modify the list stored in the original dictionary. Display all three dictionaries to see that they have the same contents
Next, use the copy module’s deepcopy function to create a deep copy of the dic-
tionary. Modify the list stored in the original dictionary, then display both dictionaries to prove that each has its own data.

7.22 (Pandas: Series) Perform the following tasks with pandas Series:
a) Create a Series from the list [7, 11, 13, 17].
b) Create a Series with five elements that are all 100.0.
c) Create a Series with 20 elements that are all random numbers in the range 0 to
   100. Use method describe to produce the Series’ basic descriptive statistics.
d) Create a Series called temperatures of the floating-point values 98.6, 98.9,
   100.2 and 97.9. Using the index keyword argument, specify the custom indi-
   ces 'Julie', 'Charlie', 'Sam' and 'Andrea'.
e) Form a dictionary from the names and values in Part (d), then use it to initialize
   a Series.

7.23 (Pandas: DataFrames) Perform the following tasks with pandas DataFrames:
a) Create a DataFrame named temperatures from a dictionary of three tempera-
   ture readings each for 'Maxine', 'James' and 'Amanda'.
b) Recreate the DataFrame temperatures in Part (a) with custom indices using
   the index keyword argument and a list containing 'Morning', 'Afternoon'
   and 'Evening'.
c) Select from temperatures the column of temperature readings for 'Maxine'.
d) Select from temperatures the row of 'Morning' temperature readings.
e) Select from temperatures the rows for 'Morning' and 'Evening' temperature
   readings.
f) Select from temperatures the columns of temperature readings for 'Amanda'
   and 'Maxine'.
g) Select from temperatures the elements for 'Amanda' and 'Maxine' in the
   'Morning' and 'Afternoon'.
h) Use the describe method to produce temperatures’ descriptive statistics.
i) Transpose temperatures.
j) Sort temperatures so that its column names are in alphabetical order.

7.24 (AI Project: Introducing Heuristic Programming with the Knight’s Tour) An in-
teresting puzzler for chess buffs is the Knight’s Tour problem, originally proposed by the mathematician Euler. Can the knight piece move around an empty chessboard and touch each of the 64 squares once and only once? We study this intriguing problem in depth here.
The knight makes only L-shaped moves (two spaces in one direction and one space
in a perpendicular direction). Thus, as shown in the figure below, from a square near the middle of an empty chessboard, the knight (labeled K) can make eight different moves (numbered 0 through 7).

a) Draw an eight-by-eight chessboard on a sheet of paper, and attempt a Knight’s
Tour by hand. Put a 1 in the starting square, a 2 in the second square, a 3 in the
third, and so on. Before starting the tour, estimate how far you think you’ll get,
remembering that a full tour consists of 64 moves. How far did you get? Was
this close to your estimate?

b) Now let’s develop a script that will move the knight around a chessboard rep-
resented by an eight-by-eight two-dimensional array named board. Initialize
each square to zero. We describe each of the eight possible moves in terms of
its horizontal and vertical components. For example, a move of type 0, as
shown in the preceding figure, consists of moving two squares horizontally to
the right and one square vertically upward. A move of type 2 consists of moving
one square horizontally to the left and two squares vertically upward. Horizon-
tal moves to the left and vertical moves upward are indicated with negative
numbers. The eight moves may be described by two one-dimensional arrays,
horizontal and vertical, as follows:

horizontal[0] = 2 vertical[0] = -1
horizontal[1] = 1 vertical[1] = -2
horizontal[2] = -1 vertical[2] = -2
horizontal[3] = -2 vertical[3] = -1
horizontal[4] = -2 vertical[4] = 1
horizontal[5] = -1 vertical[5] = 2
horizontal[6] = 1 vertical[6] = 2
horizontal[7] = 2 vertical[7] = 1

Let the variables current_row and current_column indicate the row and
column, respectively, of the knight’s current position. To make a move of type
move_number (a value 0–7), your script should use the statements
current_row += vertical[move_number]
current_column += horizontal[move_number]
Write a script to move the knight around the chessboard. Keep a counter
that varies from 1 to 64. Record the latest count in each square the knight
moves to. Test each potential move to see if the knight has already visited that
square. Test every potential move to ensure that the knight does not land off
the chessboard. Run the application. How many moves did the knight make?

c) After attempting to write and run a Knight’s Tour script, you’ve probably
developed some valuable insights. We’ll use these insights to develop a heuristic
(i.e., a common-sense rule) for moving the knight. Heuristics do not guarantee
success, but a carefully developed heuristic greatly improves the chance of suc-
cess. You may have observed that the outer squares are more troublesome than
the squares nearer the center of the board. In fact, the most troublesome or in-
accessible squares are the four corners.
Intuition may suggest that you should attempt to move the knight to the
most troublesome squares first and leave open those that are easiest to get to so
that when the board gets congested near the end of the tour, there will be a
greater chance of success.
We could develop an “accessibility heuristic” by classifying each of the
squares according to how accessible it is and always moving the knight (using
the knight’s L-shaped moves) to the most inaccessible square. We fill two-
dimensional array accessibility with numbers indicating from how many
squares each particular square is accessible. On a blank chessboard, each of the
16 squares nearest the center is rated as 8, each corner square is rated as 2, and
the other squares have accessibility numbers of 3, 4 or 6 as follows:

2 3 4 4 4 4 3 2
3 4 6 6 6 6 4 3
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
4 6 8 8 8 8 6 4
3 4 6 6 6 6 4 3
2 3 4 4 4 4 3 2

Write a new version of the Knight’s Tour, using the accessibility heuristic.
The knight should always move to the square with the lowest accessibility
number. In case of a tie, the knight may move to any of the tied squares.
Therefore, the tour may begin in any of the four corners. [Note: As the knight
moves around the chessboard, your application should reduce the accessibility
numbers as more squares become occupied. In this way, at any given time
during the tour, each available square’s accessibility number will remain equal
to precisely the number of squares from which that square may be reached.]
Run this version of your script. Did you get a full tour? Modify the script to
run 64 tours, one starting from each square of the chessboard. How many full
tours did you get?

7.25 (Knight’s Tour Project: Brute-Force Approaches) In Part (c) of the previous exer-
cise, we developed a solution to the Knight’s Tour problem. The approach used, called the “accessibility heuristic,” generates many solutions and executes efficiently.
As computers continue to increase in power, we’ll be able to solve more problems
with sheer computer power and relatively unsophisticated algorithms. Let’s call this
approach “brute-force” problem solving.
a) Use random-number generation to enable the knight to walk around the chess-
board (in its legitimate L-shaped moves) at random. Your script should run one
tour and display the final chessboard. How far did the knight get?

b) Most likely, the script in Part (a) produced a relatively short tour. Now modify
your script to attempt 1,000,000 tours. Use a one-dimensional array to keep
track of the number of tours of each length. When your script finishes attempt-
ing the 1,000,000 tours, it should display this information in a neat tabular for-
mat. What was the best result?

c) Most likely, the script in Part (b) gave you some “respectable” tours, but no full
tours. Now let your script run until it produces a full tour. [Caution: This ver-
sion of the script could run for hours on a powerful computer.] Once again,
keep a table of the number of tours of each length, and display this table when
the first full tour is found. How many tours did your script attempt before pro-
ducing a full tour? How much time did it take?

d) Compare the brute-force version of the Knight’s Tour with the accessibility-
heuristic version. Which required a more careful study of the problem? Which
algorithm was more challenging to develop? Which required more computer
power? Could we be certain (in advance) of obtaining a full tour with the ac-
cessibility-heuristic approach? Could we be certain (in advance) of obtaining a
full tour with the brute-force approach? Argue the pros and cons of brute-force
problem-solving in general.

7.26 (Knight’s Tour Project: Closed-Tour Test) In the Knight’s Tour, a full tour occurs when the knight makes 64 moves, touching each square of the chessboard once and only once. A closed tour occurs when the 64th move is one move away from the square in which the knight started the tour. Modify the script you wrote in Exercise 7.24 to test for a closed tour if a full tour has occurred
