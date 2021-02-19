# 2021-02-19

class snow_year_2021:
    import datetime as dt
    snow_date = dt.datetime.now().strftime("%Y-%m-%d")

    def __init__(self, snow_amount, snow_duration, Endless_work):
        self.anxiety = (self.snow_amount * self.snow_duration) ** self.Endless_work
        self.snow_amount = snow_amount
        self.snow_duration = snow_duration
        self.Endless_work = Endless_work

    def snow_anxiety(self, anxiety):
        if self.anxiety > 20:
            return True

        else:
            return 'Go to Hell'
