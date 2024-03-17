# Iteration
## Learning Objectives/Goals
- Be able to read, comprehend, trace, adapt and create Python code using selection that:
- Iterates using WHILE loops 
- Sets Boolean conditions to trigger loops
- Uses counters in loop conditions

## Slide deck
[Click here] (https://docs.google.com/presentation/d/1g1X59BvkkuLYxiXMi1xoHShxnK-azGo6vHbul8AAbIA/edit?usp=sharing) for the slide deck.

## TEACHER NOTES - Iteration

This week is focused on **iteration, **the code that makes the computer repeat certain lines of code.  Iteration is often more commonly known as **looping.**

A loop repeats the code inside it.  There are several different types of loop, but in this course we are going to learn about **conditional,** or **while loops.**

A while loop repeats the code inside it **while **the condition is true.  When the computer gets to the start of the loop it checks the condition.  If the condition is **true** the computer enters the loop and runs the code inside it.  If the condition is **false, **the computer skips past the loop and carries on with the rest of the program.

When the computer gets to the end of the loop it goes back and checks the condition again.  If the condition is still true it goes back into the loop and runs the code inside again.  This keeps happening until the condition changes to become false.

To summarise, this code should be written like this:
```
while  condition:

  Code to repeat whilst condition above is true.

Code runs once condition is false and the loop has finished.
```

### Using iteration to validate input - Key points

* The user is asked a question and their response is stored in a variable.
* A loop is started with a condition that can be explained as ‘while the user gets the answer wrong’ - this is a typical use of the not equal to operator.  It often helps to explain to students that, for this sort of problem, the loop should run while the input is NOT what they want/correct.
* Code inside the loop is indented, just like selection.
* Inside the loop, the user is given an error message - not essential but good practice for usability.
* Inside the loop the user is given another chance to input - **this is essential! ** Missing this step means that the user never has a chance to change their answer.  Therefore the loop condition will never change from true to false.  This creates an infinite loop that never ends.  Students often make this error.
* Getting the answer right breaks the loop as the condition is no longer true.  The computer moves on to the code after the loop, in this case a congratulations message.

## CODE EXAMPLES

A loop that runs forever (Python uses the while True structure for this)

```
while True:
  print("Hello world!")
```

Repeat until the user input the correct answer:
```
print("What's the capital of France?")
answer = input()

while answer != "Paris":
  print("Incorrect! Try again")
  print("What's the capital of France?")
  answer = input()

print("Congratulations!")
```
Loop that uses a counter to output numbers from 1 to 10
```
counter = 1

while counter < 11:
  print(counter)
  counter = counter + 1
```

Usr has 3 guesses to get the answer right:
```
guessCount = 1
print("What's the capital of France?")
answer = input()

while answer != "Paris" and guessCount < 4:
  print("Incorrect! Try again")
  print("What's the capital of France?")
  answer = input()
  guessCount = guessCount + 1

if answer == "Paris":
  print("Congratulations!")
else:
  print("You ran out of guesses")
```

### Make

In the **make** tasks, students use the skills learned in the earlier stages of PRIMM to create their own program based on a description of what it should do.

Make sure that the students add comments to explain what the code does.

## Misconceptions & Errors to watch out for.

Make sure that you check for the following things:

- iteration begins with 'while'
- the while line has a condition
- the while line has a colon at the end 
- **all** the code you want to repeat is indented after the while.
- any code that should run once the loop has finished is **not indented**