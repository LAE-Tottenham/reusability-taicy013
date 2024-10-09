import requests
from pyfiglet import Figlet
import os, time
import functions2
# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]


f = Figlet(font="slant")
print(f.renderText("HEY!"))

print("Welcome to the weird weather bot :)")
print("-----------------------------------\n")
n = input("May I take your first name please? ")
n = functions2.valid(n)
gender_result = guess_gender(n)
print(f"\nHmmm, I'm {gender_result[1]}% sure you are a {gender_result[0]}.")
print(functions2.correct_gender())

place = functions2.postcode()
# 'altered' print(f"Nice! so you live in {place[0]}.\n")
functions2.creepy(place[0])
functions2.weather_stall()
w = functions2.weather(place)
print(f"\nThe weather in {place[0]}:\n")
print(str(w[0]) + "℃")
print(f"{w[1]} - {w[2]}")

print("\nThank you! Bye.")

###########################################

def weird_weather_bot():
    
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))

    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = input("May I take your first name please? ")
    gender_result = guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    postcode_raw = input("\nSo, what's your postcode? ")
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()

    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")

    print("Let me just check the weather there today...\n")
    
    for i in range(3):
        time.sleep(1)
        print("...")
    
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")

    for i in range(3):
        time.sleep(1)
        print("...")

    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
## the user's inputs do not contain numbers, except from the postcode.
# 2. Validate the user's input based on your preconditions.
## created function called valid
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
## It allows me to organise code so that i know what each function is responsible for. It also allows us to manage the decomposition of a problem as all sub-problems can easily be managed and identified.
# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
## in the file called functions2.py
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.
## new function made 
# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
