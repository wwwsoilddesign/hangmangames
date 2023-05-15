#importing the time module
import time

#welcome the user
string_name = input(" Tell your name...")

print ("Hello," +string_name,"let s plat hangman!")

#wait for 1 second
time.sleep(1)

print("your Hint: the word is 6 characters long. The last character is vowel
 whic does not repate and starting letter occurs thrice.start guessing......")
 time.sleep(0.5)
 there we set the secret word to guess - "giggle"
 
 #here we set the secret
 word_to_guess ="giggle"

#creates an variable with an empty value
guesses = ""

 #determine the number of turns
chances 10

# Create a while loop

#check if the turns are more than zero
while chances > 0:

#make a counter that starts with zero
failed 0

#for every character in secret word for char in word_to_guess:
for char in word_to_guess:

#see if the character in in the players guess if char in guesses:
if char in guesses
# print then out the character
print (char),

else:

# if not found, print a dash print(""),

#and increase the failed counter with one

failed + 1

# if failed is equal to zero

# print You Won

if failed 0:
print ("Congratulations! You've won.")

#exit the script
break
# ask the user go guess a character
         guess input("Guess a character of the word:") set the players guess to guesses guesses + guess

if the guess is not found in the secret word if guess not in word to guess:

#turns counter decreases with 1 (now 9)

chances 1

#print wrong

print ("Wrong guess")

#how many turns are left

print("You have", chances, 'more guesses') if the turns are equal to zero

if chances -- 01

#print "You Loose"

print "Sorry, you've lost.")  
