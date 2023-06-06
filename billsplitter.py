import math, random


class BillSplitter:

    def __init__(self):
        self.friends_dict = {}
        self.total_bill = 0.0
        self.friend_num = 0
        self.using_luck = False
        self.lucky = ''

    def open_bill(self):
        # main logic
        self.get_friend_num()
        if self.friend_num > 0:
            self.get_names()
            self.get_bill()
            self.get_lucky()
            self.calculate_and_print_bills()
        else:
            print('No one is sharing the bill')
    def get_friend_num(self):
        try:
            self.friend_num = int(input('Enter the number of friends joining (including you):\n'))
        except ValueError:
            print('Please enter a positive number.')

    def get_names(self):
        print('\nEnter the name of every friend (including you), each on a new line:')
        for i in range(self.friend_num):
            self.friends_dict.update({input(): 0})

    def get_bill(self):
        print('\nEnter the total bill value:')
        try:
            self.total_bill = float(input())
        except ValueError:
            print('Please enter a number.')
            self.get_bill()

    def get_lucky(self):
        print('\nDo you want to use the \"One lucky winner eats free\" feature? Write Yes/No:')
        islucky = input()
        try:
            if islucky == 'Yes':
                self.using_luck = True
                luckyfriends = []
                for friend in self.friends_dict.keys():
                    luckyfriends.append(friend)
                lucky = math.floor(random.randint(0, len(luckyfriends) - 1))
                self.lucky = luckyfriends[lucky]
                print(f'\n{self.lucky} is the lucky one!\n')
            elif islucky == 'No':
                print('\nNo one is going to be lucky')
            else:
                print('Please type Yes or No')
                self.get_lucky()
        except (TypeError, ValueError):
            print('Please type Yes or No')
            self.get_lucky()

    def calculate_and_print_bills(self):
        if self.using_luck:
            for name in self.friends_dict:
                if name != self.lucky:
                    self.friends_dict[name] = round(self.total_bill / (self.friend_num - 1), 2)
            print(self.friends_dict)
        else:
            print(
                {key: round(value + self.total_bill / self.friend_num, 2) for key, value in self.friends_dict.items()})


BillSplitter().open_bill()
