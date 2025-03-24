import taskmanagercli as tm


def main():
    while True:
        print("Options available:")
        print("\nAdd Task : 1")
        print("\nUpdate Task: 2")
        print("\nDelete Task: 3")
        print("\nTask List: 4")
        print("\nUpdate Task: 5")

        print(f"-" * 30 + "\n")

        option = input("\nEnter wanted option: ")

        if int(option) == 1:
            tm.task_add()
        elif int(option) == 2:
            tm.task_update()
        elif int(option) == 3:
            tm.task_delete()
        elif int(option) == 4:
            tm.task_list()
        elif int(option) == 5:
            tm.task_update()
        elif int(option) > 5:
            print("Option not available")


if __name__ == "__main__":
    main()