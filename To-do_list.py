def main():
    tasks=[]
    while True:
        print("****** TO-DO LIST ******")
        print(" 1. Add task \n 2. Show task \n 3. mark task as completed \n 4. Exit")
        
        option=input("Enter the option: ")

        if option=='1':
            print()
            no_tasks=int(input("Enter number of tasks you want to add: "))

            for i in range(no_tasks):
                task=input("Enter the task: ")
                tasks.append({"Task":task,"done": False})
                print("Task added!")

        elif option=='2':
            print("\n Tasks:")
            for index,task in enumerate(tasks):
                status="Done" if task["done"] else "Not done"
                print(f"{index+1}.{task['Task']}-{status}")
        
        elif option=='3':
            task_in=int(input("Enter the task number to mark as completed:"))-1
            if 0<= task_in<len(tasks):
                tasks[task_in]["done"]=True
                print("Task marked as completed")
            else:
                print("invalid task number")
        
        elif option=='4':
            print("Exiting out of TO-Do List....")
            break

        else:
            print("Invalid choice. Please select an valid choice.")

if __name__ == "__main__":
    main()