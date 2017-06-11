from datetime import datetime

from termcolor import colored


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = colored(name,'red')
        self.salutation = colored(salutation,'red')
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self , message , sent_by_me):
        self.message =colored( message,'green')
        self.time =datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Katoch', 'Ms.', 20, 4.2)

friend_one = Spy('Rajat Rana', 'Mr', 24,4.5)
friend_two = Spy('Ishita Katoch', 'Ms.', 20, 4.3)
friend_three = Spy('Rounak Banik', 'Mr.', 24, 4.7)


friends = [friend_one, friend_two, friend_three]
