import Planner

class planner_controller:
    planner_light = Planner.planner_main()

    def print_menu(self):
        print("\nMenu:\n")
        print("1. Add event\n")
        print("2. Show all events \n")
        print("3. Find event by the date \n")
        print("4. Delete event by date \n")


    def menu_choose(self):
        while True:
            self.print_menu()
            check = input()
            if check == '1':
                self.planner_light.new_task_inp()
            elif check == '2':
                self.planner_light.print_shed()
            elif check == '3':
                print('Enter date to find planned event')
                self.planner_light.find_event_by_date()
            elif check == '4':
                print('Enter date of evenet you want to delete')
                self.planner_light.delete_event()



