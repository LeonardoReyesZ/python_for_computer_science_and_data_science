8.1 (Check Protection) Although electronic deposit has become extremely popular,
payroll and accounts payable applications often print checks. A serious problem is the intentional alteration of a check amount by someone who plans to cash a check 
raudulently. To prevent a dollar amount from being altered, some computerized check 
writing systems employ a technique called check protection. Checks designed for 
printing by computer typically contain a fixed number of spaces for the printed 
amount. Suppose a paycheck contains eight blank spaces in which the computer is 
supposed to print the amount of a weekly paycheck. If the amount is large, then all 
eight of the spaces will be filled:

1,230.60 (check amount)
--------
01234567 (position numbers)

On the other hand, if the amount is smaller, then several of the spaces would 
ordinarily be left blank. For example,

399.87
--------
01234567

contains two blank spaces. If a check is printed with blank spaces, it’s easier for 
someone to alter the amount. Check-writing systems often insert leading asterisks to 
prevent alteration and protect the amount as follows:

**399.87
--------
01234567

Write a script that inputs a dollar amount, then prints the amount in check-pro-
tected format in a field of 10 characters with leading asterisks if necessary. 
[Hint: In a format string that explicitly specifies alignment with <, ^ or >, you can 
precede the alignment specifier with the fill character of your choice.]


8.2 (Random Sentences) Write a script that uses random-number generation to compose 
sentences. Use four arrays of strings called article, noun, verb and preposition.
Create a sentence by selecting a word at random from each array in the following 
order: article, noun, verb, preposition, article and noun. As each word is picked, 
concatenate it to the previous words in the sentence. Spaces should separate the 
words. When the final sentence is output, it should start with a capital letter and 
end with a period. The script should generate and display 20 sentences.


8.3 (Encrypt a Phrase) In Exercise 5.11, you wrote a function to calculate an encryp-
tion key based on a given sentence. Use this function to generate an encryption key to
help encrypt a phrase. Write a function to encrypt the phrase using the following 
algorithm: To encrypt a phrase, you need to tokenize it using the string method 
split. After this, you can encrypt each word individually. Search for the index of 
each letter of the word in the alphabet. Select the letter in the encryption key with 
the same index. Replace the original letter in the word with the encrypted letter. 
Replace the original word in the tokenized sentence with the encrypted word. If the 
word is only one letter long, it will not be encrypted. When all the individual words 
are encrypted, they are combined into a new sentence making sure that blanks between 
words remain blanks. Enable the user to enter a phrase and subsequently display the 
encrypted phrase.


8.4 (Sorting Words in a Sentence) Write a script that reads a line of text as a 
string,tokenizes the string, and outputs the tokens in alphabetical order. Use space 
characters as delimiters.


8.5 (Tokenizing and Comparing Strings) Write a script that reads a line of text, 
tokenizes the line using space characters as delimiters and outputs only those words 
beginning with the letter 'b'.


8.6 (Tokenizing and Comparing Strings) Write a script that reads a line of text, 
tokenizes it using space characters as delimiters and outputs only those words ending 
with the letters 'ed'.


8.7 (Converting Integers to Characters) Use the c presentation type to display a table
of the character codes in the range 0 to 255 and their corresponding characters.


8.8 (Converting Integers to Emojis) Modify the previous exercise to display 10 emojis
beginning with the smiley face, which has the value 0x1F600: The value 0x1F600 is a 
hexadecimal (base 16) integer. See the online appendix “Number Systems” for 
information on the hexadecimal number system. You can find emoji codes by searching 
online for “Unicode full emoji list.” The Unicode website precedes each character 
code with "U+" (representing Unicode). Replace "U+" with "0x" to properly format
the code as a Python hexadecimal integer.


8.9 (Counting Vowels in a Sentence) Write a script that reads a phrase and calculates
the number of vowels used in it. To assess if a character in the string is a vowel, 
check if it is present in a second string. The second string consists of the vowels 
“aeiou.” For example, the letter “a” is present in the string “aeiou” and is thus 
considered a vowel. Count all the vowels in the given string and output this number 
to the user.


8.10 (Project: Simple Sentiment Analysis) Search online for lists of positive 
sentiment words and negative sentiment words. Create a script that inputs text, then 
determines whether that text is positive or negative, based on the total number of 
positive words and the total number of negative words. Test your script by searching 
for Twitter tweets on a topic of your choosing, then entering the text for several 
tweets. In the data science case study chapters, we’ll take a deeper look at 
sentiment analysis.


8.11 (Project: Evaluate Word Problems) Write a script that enables the user to enter
mathematical word problems like “two times three” and “seven minus five”, then use
string processing to break apart the string into the numbers and the operation and 
return the result. So “two times three” would return 6 and “seven minus five” would 
return 2. To keep things simple, assume the user enters only the words for the 
numbers 0 through 9 and only the operations 'plus', 'minus', 'times' and 'divided by'


8.12 (Project: Scrambled Text) Use string-processing capabilities to keep the first 
and last letter of a word and scramble the remaining letters in between the first and 
last. Search online for “University of Cambridge scrambled text” for an intriguing 
paper on the readability of texts consisting of such scrambled words. Investigate the 
random module’s shuffle function to help you implement this exercise’s solution.


8.13 (Regular Expressions: Replacing Substrings) Use regular expressions to change the
name in a line from a poem. Jennifer, you are more beautiful than the most beautiful 
rose


8.14 (Regular Expressions: Capturing Substrings) Reimplement Exercises 8.5 and 8.6
using regular expressions that capture the matching substrings, then display them.


8.15 (Regular Expressions: Count Number of Occurrences of a Letter) Use the findall
function to check the number of occurrences of the letter “a” in the sentence.
The mouse that the cat that the dog that the man frightened and chased ran away


8.16 (Regular Expressions: Locating URLs) Use a regular expression to search through a
string and to locate all valid URLs. For this exercise, assume that a valid URL has 
the form http://www.domain_name.extension, where extension must be two or more 
characters.


8.17 (Using Regular Expressions for Autocorrection) When we type a message on a
smartphone, autocorrect changes the text we enter to remove errors. One common error
is using two capital letters to start a capitalized word instead of one. Write a 
script that uses regular expressions to correct this error using the following 
algorithm:

  a) Search for all capitalized letters in the sample text.
  b) Check for each capitalized letter if the next letter is also capitalized.
  c) If this is the case, change the second letter to lower case.
  d) Repeat this process until you reach the end of the phrase.

Test your script with different phrases with different errors.


8.18 (Using Regular Expressions for Password Validation) When choosing a password,
a user is often confronted with a set of rules they have to comply with in order to 
set a valid password. Write a script using the necessary regular expressions to check 
if a password is valid. For a chosen password to be valid, it should contain at least 
one lowercase and one uppercase letter and at least one number. The use of whites 
paces in a password is not allowed. Provide the necessary feedback to the user for 
their chosen password.


8.19 (Regular Expressions: Testing Regular Expressions Online) Before using any 
regular expression in your code, you should thoroughly test it to ensure that it 
meets your needs. Use a regular expression website like regex101.com to explore and 
test existing regular expressions, then write your own regular expression tester.


8.20 (Regular Expressions: Munging Dates) Dates are stored and displayed in several
common formats. Three common formats are

042555
04/25/1955
April 25, 1955

Use regular expressions to search a string containing dates, find substrings that 
match these formats and munge them into the other formats. The original string should 
have one date in each format, so there will be a total of six transformations.


8.21 (Project: Metric Conversions) Write a script that assists the user with some 
common metric-to-English conversions. Your script should allow the user to specify 
the names of the units as strings (i.e., centimeters, liters, grams, and so on for 
the metric system and inches, quarts, pounds, and so on for the English system) and 
should respond to simple questions, such as 'How many inches are in 2 meters?'
'How many liters are in 10 quarts?' Your script should recognize invalid conversions. 
For example, the following question is not meaningful, because 'feet' is a unit of 
length and 'kilograms' is a unit of mass: 'How many feet are in 5 kilograms?'
Assume that all questions are in the form shown above. Use regular expressions to 
capture the important substrings, such as 'inches', '2' and 'meters' in the first 
sample question above. Recall that functions int and float can convert strings to 
numbers.


8.22 (Project: Cooking with Healthier Ingredients) In the “Dictionaries and Sets” 
chapter’s exercises, you created a dictionary that mapped ingredients to lists of 
their possible substitutions. Use that dictionary in a script that helps users choose 
healthier ingredients when cooking. The script should read a recipe from the user and 
suggest healthier replacements for some of the ingredients. For simplicity, your 
script should assume the recipe has no abbreviations for measures such as teaspoons, 
cups, and tablespoons, and uses numerical digits for quantities (e.g., 1 egg, 2 cups) 
rather than spelling them out (one egg, two cups). Your program should display a 
warning such as, “Always consult your healthcare professional before making 
significant changes to your diet.” Your program should take into consideration that 
replacements are not always one-for-one. For example, each whole egg in a recipe can 
be replaced with two egg whites.


8.23 (Project: Guess the Correct Synonym) In this project, you will write a guessing
game where the user is given a hint, and they need to find its synonym. To start your
script, you will need to create a dictionary to store both the hint (key) and the 
synonym (value). Add a minimum of 5 key-value pairs to the dictionary. Write a first 
function to select a random key-value pair from this dictionary. Do not use the 
popitem() method to write this function as this is absent in later python versions. 
Write a second function that displays the hint and allows the user to guess the 
different letters of the word. Each time, the user guesses a letter, the number of 
correctly guessed letters is displayed. If all the letters of the word are found, the 
user will have the possibility to guess the synonym. The appropriate output is shown 
on the screen depending on whether the guess was correct or not.


8.24 (Research: Inter-Language Translation) This exercise will help you explore one of
the most challenging problems in natural language processing and artificial 
intelligence. The Internet brings us all together in ways that make inter-language 
translation particularly important. As authors, we frequently receive messages from 
non-English speaking readers worldwide. Not long ago, we’d write back asking them to 
write to us in English so we could understand. With advances in machine learning, 
artificial intelligence and natural language processing, services like Google 
Translate (100+ languages) and Bing Microsoft Translator (60+ languages) can 
translate between languages instantly. In fact, the translations are so good that 
when non-English speakers write to us in English, we often ask them to write back in 
their native language, then we translate their message online. There are many 
challenges in natural language translation. To get a sense of this, use online 
translation services to perform the following tasks:

  a) Start with a sentence in English. A popular sentence in machine translation lore
    is from the Bible’s Matthew 26:41, “The spirit is willing, but the flesh is weak.”
  b) Translate that sentence to another language, like Japanese.
  c) Translate the Japanese text back to English.

Do you get the original sentence? Often, translating from one language to another and
back gives the original sentence or something close. Try chaining multiple language 
translations together. For instance, we took the phrase in Part (a) above and 
translated it from English to Chinese Traditional to Japanese to Arabic and back to 
English. The result was, “The soul is very happy, but the flesh is very crisp.” Send 
us your favorite translations!


8.25 (Project: State of the Union Speeches) All U.S. Presidents’ State of the Union
speeches are available online. Copy and paste one into a large multiline string, then 
display statistics, including the total word count, the total character count, the 
average word length, the average sentence length, a word distribution of all words, a 
word distribution of words ending in 'ly' and the top 10 longest words. In the 
“Natural Language Processing (NLP)” chapter, you’ll find lots of more sophisticated 
techniques for analyzing and comparing such texts.


8.26 (Research: Grammarly) Copy and paste State of the Union speeches into the free
version of Grammarly or similar software. Compare the reading grade levels for 
speeches from several presidents.
