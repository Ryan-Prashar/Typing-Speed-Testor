from time import time  # importing time function
import random as r     # importing random function

def mistake(paratest, usertest):  #created a mistake function
    incorrect_chars = []
    error_count = 0              #Initializing error
    
    # Determine the length of the shorter string
    min_length = min(len(paratest), len(usertest))

    # Iterate over the length of the shorter string
    for i in range(min_length):
        if paratest[i] != usertest[i]:
            incorrect_chars.append((paratest[i], usertest[i], i))  # store incorrect characters and their positions
            error_count += 1

    # Handle cases where usertest is longer
    if len(paratest) < len(usertest):
        for i in range(min_length, len(usertest)):
            incorrect_chars.append(('*', usertest[i], i))  # indicate extra characters with '*'
            error_count += 1

    return error_count, incorrect_chars

def speed_time(time_s, time_e, userinput):      #created speed function
    time_delay = time_e - time_s                #calculating time taken
    time_R = round(time_delay, 2)               #rounding the time upto 2 digits
    speed = len(userinput) / time_R             #calculating speed
    return round(speed)

#created a test function and inserted 15 different strings in it

test= ["She found an old map hidden in the attic covered in dust and cobwebs  depicting a forgotten land that seemed to promise adventure and mystery", "The scent of fresh bread filled the small bakery mingling with the rich aroma of brewing coffee and the sweet tang of freshly baked pastries", "A sudden gust of wind blew the papers off the desk scattering them across the room like autumn leaves making the office look like a chaotic snowstorm", "The mountains in the distance were shrouded in mist their peaks barely visible through the thick ethereal fog that seemed to hang in the air like a veil","The library was a haven of silence and knowledge its tall shelves lined with books of every size and color promising hours of exploration and discovery", "He played the violin with a passion that captivated the audience his fingers dancing across the strings producing a melody that resonated with their deepest emotions", "The snow began to fall softly covering the ground in a blanket of white, as children eagerly prepared their sleds for a day of fun", "He carefully placed the fragile vase on the shelf admiring its intricate design and the way it caught the light from the window", "The bustling city streets were filled with the sounds of honking cars and busy pedestrians each lost in their own world of thoughts and tasks", "The old library was a treasure trove of knowledge its shelves lined with books that held stories of faraway lands and ancient times", "She stood at the edge of the cliff gazing out at the vast ocean feeling a sense of awe and wonder at the beauty of nature", "The campfire crackled and popped sending sparks into the night sky as the group of friends shared stories and roasted marshmallows", "He typed furiously on his keyboard racing against the clock to meet the deadline his mind focused on the task at hand", "The garden was in full bloom with vibrant flowers and lush greenery creating a colorful tapestry that delighted the senses"]


test1 = r.choice(test)                              #generating random string from the test
print(" **** Typing Speed Test ****")               
print(test1)                                        #printing random test string
print()
time_1 = time()
testinput = input(" Enter : ")                      #taking user input
print()
time_2 = time()

# Generating the results of the test
speed = speed_time(time_1, time_2, testinput)
total_errors, incorrect = mistake(test1, testinput)

#printing the desired results
print('Speed : ', speed, "w/sec")
print("Total Errors : ", total_errors)

#printing the incorrect characters
if incorrect:
    print("Incorrect Characters:")
    for expected, actual, position in incorrect:
        print(f"Position {position}: Expected '{expected}', Got '{actual}'")
else:
    print("No incorrect characters found.")



