import datetime


class GameTime:

    def __init__(self):
        # Game time starts at 21:00:00 On the 20th October 2016
        self.time = datetime.datetime(hour=21, minute=00, second=00, year=2016, month=10, day=22)

    def add_minutes(self, amount=1):
        self.time = self.time + datetime.timedelta(minutes=int(amount))
