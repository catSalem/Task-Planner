
class planner_main:
    def __init__(self):
        self.shedule = {}

    def new_task_append(self, task_date_check, task_value):
        if task_date_check in self.shedule:
            print('This date is alredy sheduled')
        else:
            self.shedule[task_date_check] = task_value

    def new_task_inp(self):
        print('First input event date')
        event_key = input()
        print('Now input event you need to remind')
        event_value = input()
        self.new_task_append(event_key, event_value)

    def find_event_by_date(self):
        pri = input()
        if pri in self.shedule:
            print('"' + self.shedule.get(pri) + '"')
        else:
            print('There is no such event')

    def delete_event(self):
        del self.shedule[input()]



    def print_shed(self):
        for x in self.shedule:
            print(x + ' : ' + '"' + self.shedule.get(x) + '"')



