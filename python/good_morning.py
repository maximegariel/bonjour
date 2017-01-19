from task import Task
from scheduler import Scheduler

# import the library
from appJar import gui

counter = 0


def load_tasks(scheduler):
    task_list = [Task("Breakfast", 8, 55),
                Task("Bathroom", 6, 30)]

class ColorUpdater():
    
    def __init__(self):
        self.counter = 0
        self.task = Task("Breakfast", 8, 55)
        
    def update_color(self):
        if self.counter == 0:
            app.setLabel("title", repr(self.task))
            app.setLabelBg("title", "blue")
            self.counter = 1
        else:
            self.counter =0
            app.setLabelBg("title", "red")


if __name__ == "__main__":
    sched = Scheduler()
    load_tasks(sched)
    from appJar import gui



    app = gui()

    ### fillings go here ###
    app.addLabel("title", "Welcome to appJar")
    # bottom slice - START the GUI
    colo = ColorUpdater()
    # call the getLocation function every second
    app.registerEvent(colo.update_color)

    app.go()

    
