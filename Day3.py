# Day 3
# I would like to create one everyday working notification Class, which helps me to store and arrange works everyday.
# list three tasks everyday.
# note how many time I am going to spend.


def printt(func):

    # This python interpreter somehow automatically puts the object (self)
    # as the first argument 'x' of wrap()
    def wrap(x):
        msg = func(x)
        print(msg)

    # To be a decorator, always return the function without execution, i.e. without '()'
    return wrap


class EdCalender:
    import datetime as dt
    now = dt.datetime.now()
    today = now.strftime("%Y-%m-%d")

    def __init__(self, task_1, duration_1, priority_1, task_2, duration_2, priority_2, task_3, duration_3, priority_3):
        self.task_1 = task_1
        self.duration_1 = duration_1
        self.priority_1 = priority_1
        self.task_2 = task_2
        self.duration_2 = duration_2
        self.priority_2 = priority_2
        self.task_3 = task_3
        self.duration_3 = duration_3
        self.priority_3 = priority_3

    def tasksoftoday(self):
        return 'The tasks of today include {}, {}, and {}'.format(self.task_1, self.task_2, self.task_3)

    # trying to figure out the decortor
    # def print_function(func):
    #     def printtt():
    #         func()
    #     return printtt

    @printt
    def message(self):
        msg = 'this is message'
        return msg

    def shout(self):
        msg = 'YES!!!!!!'
        return msg

    def show_priority(self):
        for task, priority in [
            (self.task_1, self.priority_1),
            (self.task_2, self.priority_2),
            (self.task_3, self.priority_3),
        ]:
            print(f'The priority of {task} is Rank {priority}')

    def Plan_Focus_Time(self):
        print("You plan to focus {} min in {}".format(self.duration_1, self.task_1))
        print("You plan to focus {} min in {}".format(self.duration_2, self.task_2))
        print("You plan to focus {} min in {}".format(self.duration_3, self.task_3))

    def total_work_hour(self):
        hours = (self.duration_1 + self.duration_2 + self.duration_3)/60
        print("Today's total working hours is {} hr".format(hours))
        return hours


def main():
    Day_1 = EdCalender('dissertation', 180, 1, 'python lesson-decorator', 180, 2, 'job searching', 60, 3)
    print("Today is {}".format(EdCalender.today))
    print(EdCalender.tasksoftoday(Day_1))
    EdCalender.show_priority(Day_1)
    EdCalender.Plan_Focus_Time(Day_1)
    EdCalender.total_work_hour(Day_1)


def test():
    Day_1 = EdCalender('dissertation', 180, 1, 'python lesson-decorator', 180, 2, 'job searching', 60, 3)
    Day_1.message()


if __name__ == '__main__':
    test()
