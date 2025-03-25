import taskmanagercli as tm


def main():
    while True:
        print("Options available:")
        print("\nAdd Task : 1")
        print("\nEdit Task Desc : 2")
        print("\nUpdate Status : 3")
        print("\nDelete Task : 4")
        print("\nTask List : 5")
        
        print(f"-" * 30 + "\n")

        option = input("\nEnter wanted option: ")

        if int(option) == 1:
            tm.task_add()
        elif int(option) == 2:
            tm.task_update_desc()
        elif int(option) == 3:
            tm.task_update_status()
        elif int(option) == 4:
            tm.task_delete()
        elif int(option) == 5:
            tm.task_list()
        
        elif int(option) > 5:
            print("Option not available")

if __name__ == "__main__":
    main()