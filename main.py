#Jaunel Deans 
#November 3, 2023
#We are creating a login page. We have the correct password. The user is to input their username and password. If the user inputs the correct password, they will be able to login. If the user inputs the wrong password, they will be able to try again. They have 3 tries. If they fail they will have to restart the program.

passWord = "abc123" #create the variable passWord and assign the correct password "abc123" to the varaible. 
userName = input("Welcome to your login page. Enter your username: ")#Create the variable userName and assign the user input of their username to the variable.
userInput = input("Enter your password: ")#Create the variable userInput and assign the user input of their password to the variable.
attempts = 1#Create the variable attempts and assign the value of 1 to the variable to count the number of attempts the user has made.

while userInput != passWord:#start a while loop that checks if the userInput is not equal to the passWord variable. Then the code inside will starts
  print('Error, incorrect password')#print the error message
  userInput = input("Enter your correct password: ")#reassign the userInput variable to the user input of their password.
  attempts = attempts + 1#add 1 to the attempts variable
  
  if attempts == 3 and userInput != passWord:#start an if statement that checks if the attempts variable is equal to 3 and the userInput is not equal to the correct password
    print("You have reached the maximum number of attempts. Goodbye")#print the goodbye message
    raise StopIteration#stop the program so they have to start again

print("Login accepted. " + userName + ", welcome to your account. It took you " + str(attempts) + " to get the correct password.")#print the login accepted message and the username and the number of attempts it took the user to get the correct password. This will only run if the while loop is proven false.