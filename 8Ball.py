# Python Project recreating the 8-Ball toy in Python code. 
# Magic 8 Ball Simulation

import random
import time

answers = ['It is certain.',
'It is decidedly so.',
'Without a doubt.',
'Yes – definitely.',
'You may rely on it.',
'As I see it, yes.',
'Most likely.',
'Outlook good.',
'Yes.',
'Signs point to yes.',
'Reply hazy, try again.',
'Ask again later.',
'Better not tell you now.',
'Cannot predict now.',
'Concentrate and ask again.',
'Don\'t count on it.',
'My reply is no.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful.']

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the 8 ball...")
    time.sleep(0.5)
    print("The value is....")
    time.sleep(0.5)
    print(random.choice(answers))

    roll_again = input("Roll the ball again?")
