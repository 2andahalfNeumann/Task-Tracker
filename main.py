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

        option = int(input("\nEnter wanted option: "))


        option_select = {
            1: tm.task_add,
            2: tm.task_update_desc,
            3: tm.task_update_status,
            4: tm.task_delete,
            5: tm.task_list
        }

        action = option_select.get(option)
        if action:
            action()
        else:
            print("Not available")

if __name__ == "__main__":
    main()