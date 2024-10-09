import requests
from pyfiglet import Figlet
import os, time

def valid(entry):
    check = False
    while not check:
        count = 0
        for x in entry:
            if x.isdigit() or x in '}/$!&*()_-+=[]{#~@''""\\|<>,.:;£%? ':
                count = 1
                break
        if count != 1:
            check = True
        else:
            entry = input("Invalid. Enter again: ")
    return entry

def correct_gender():
    ans = input("Am I right? :) (Y/n) ")
    ans = valid(ans)
    return "Wooooooh! Computer 1, Human 0." if ans.lower() in ["","yes","ye","y"] else "Ahhhh, sorry! :("

def postcode():
    p = input("\nSo, what's your postcode? ")
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{p}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    return [area,longitude,latitude]

def chill():
    for i in range(3):
        time.sleep(1)
        print('...')
def weather_stall():
    print("Let me just check the weather there today...\n")
    chill()
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
    chill()

def weather(post):
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={post[2]}&lon={post[1]}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    return [weather_degrees, main_weather_desc, second_weather_desc]

def creepy(p):
    time.sleep(3)
    print(f"--------ERROR--------")
    print("I KNOW WHERE YOU LIVE")
    time.sleep(5)
    for x in range(2):
        print(f"Nice! so you live in {p}.")
        print(" - - - Hello - - - ")
        time.sleep(2)
    chill()