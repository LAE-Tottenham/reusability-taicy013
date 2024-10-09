# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################
import functions1 as f
user1 = f.user_triangle()
user2 = f.user_triangle()
ans = [f.hyp(user1),f.hyp(user2)]
print(f.hyp(ans))

sohcahtoa = input("Enter 'yes' if you would like to find the value of a missing angle in a right angle triangle: ")
if sohcahtoa.lower() in ['y','yes','']:
    print(f.missing_angle(f.pick_tri(user1,user2)))

pythag = input("Enter 'yes' if you would like to use Pythagoras on triangle to find its hypotenuse: ")
if pythag.lower() in ['y','yes','']:
    print(f.hyp(f.pick_tri(user1,user2)))
sine = input("Enter 'yes' if you would like to use sine rule on triangle to find its hypotenuse: ")
if sine.lower() in ['y','yes','']:
    print(f.sin_rule(f.pick_tri(user1,user2)))
cosine = input("Enter 'yes' if you would like to use cosine rule on triangle to find its hypotenuse: ")
if cosine.lower() in ['y','yes','']:
    print(f.cosine_rule(f.pick_tri(user1,user2)))

def weird_calculation():
    # get the length and width of the first triangle from the user
    opp1 = float(input("Enter your first triangle's opposite side length: "))
    adj1 = float(input("Enter your first triangle's adjacent side length: "))

    # work out the hyp
    import math
    hyp1 = math.sqrt(opp1**2 + adj1**2)

    # get the length and width of the second triangle from the user
    opp2 = float(input("Enter your second triangle's opposite side length: "))
    adj2 = float(input("Enter your second triangle's adjacent side length: "))

    # work out the hyp
    import math
    hyp2 = math.sqrt(opp2**2 + adj2**2)

    # create a third triangle with the hyp1 as the opp and hyp2 as the adj
    opp3 = hyp1
    adj3 = hyp2
    
    import math
    hyp3 = math.sqrt(opp3**2 + adj3**2)
    return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
## user input has to be a number (most of the time)
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
## there were parts of the algorithm htat were frequently repeated; using reusable components makes it easier to organise the code
## error-checking is easier because the code has been condensed: it is easier to locate faulty parts of code
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
## in the file called functions1.py
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
##
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
##
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
