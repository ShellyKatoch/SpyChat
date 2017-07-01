# Importing datetime to display the chat time and date
from datetime import datetime

from termcolor import colored


# made a class for spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        # Count the number of words
        self.count = 0

# a class for chat_message
class ChatMessage:

    def __init__(self , message , sent_by_me):
        self.message =colored( message,'green')
        self.time =datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Shelly', 'Ms.', 20, 5)

friend_one = Spy(colored('Rajat Rana', 'Mr', 24,4.5))
friend_two = Spy('Ishita Katoch', 'Ms.', 20, 4.3)
friend_three = Spy('Rounak Banik', 'Mr.', 24, 4.7)


friends = [friend_one, friend_two, friend_three]  # List of friends
