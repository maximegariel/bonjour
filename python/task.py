import datetime
import time

class Task():
    def __init__(self, description, hours, minutes):
        self._end_time = datetime.time(hours, minutes)
        self._description = description

    def remaining_time(self, time):
        year = datetime.datetime.today().year
        mon = datetime.datetime.today().month
        day = datetime.datetime.today().day
        time_end = datetime.datetime(year, mon, day,
                                 self._end_time.hour,
                                 self._end_time.minute,
                                 self._end_time.second)
        
        return time_end -  time

    def __repr__(self):
        return "{} - {} remaining".format(self._description, self.remaining_time(datetime.datetime.now())) 



if __name__ == "__main__":
    import time
    my_task = Task("Breakfast", 8, 55)
    my_task_2 = Task("Bathroom", 6, 30)
    for i in range(10):
        print(my_task)
        print(my_task_2)
        
        time.sleep(1)
