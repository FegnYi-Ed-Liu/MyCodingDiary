# 02/20/2021

# two friends and their daughter visited my house today, which is a wonderful afternoon.
# We had many helpful advises and suggestions. Just think to write one class to record friends' visit, and the topic we
# discussed.
from datetime import datetime


class Friendship:
    import datetime as dt
    now = dt.datetime.now()
    today = now.strftime("%Y-%m-%d")

    def __init__(self, name, visittimes, topic, visittype, COVIDConcern, date=now):
        self.name = name
        self.visit = visittimes
        self.topic = topic
        self.visittype = visittype
        self.COVIDConcern = COVIDConcern
        self.date = date

    def visitdate(self):
        return self.date.strftime("%Y-%m-%d")

    def check_if_weekend(self):
        day = self.date
        weekday = datetime.isoweekday(day)
        if weekday == 6 | weekday == 7:
            print('it is weekend')
        else:
            print('it is weekday')


def main():
    today_1 = Friendship('Elu', 1, 'life and work', 'in person', True)
    today_2 = Friendship('ChaoChun', 1, 'work and family', 'inperson', False)


def test():
    today_1 = Friendship('Elu', 1, 'life and work', 'in person', True)
    today_2 = Friendship('ChaoChun', 1, 'work and family', 'in person', False)
    print(Friendship.visitdate(today_1))
    print(Friendship.check_if_weekend(today_1))
