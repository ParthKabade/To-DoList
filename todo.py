def add_task(task_list):
    task_1=input("Enter Task: ").strip()
    task_list.append(task_1)
    print(f"{task_list[-1]} : Task Added Successfully")
    save_tasks(task_list)

def view_task(task_list):
    if len(task_list)>0:
        for index,task in enumerate(task_list,start=1):
            print(f"{index} : {task}")
    else:
        print("No Tasks Availabel")

def remove_tasks(task_list):
    try:
        if len(task_list)>0:
            view_task(task_list)

            print()

            task_number=int(input("enter task (Integer)number whch you want to remove"))
            if task_number>0 and task_number<=len(task_list):
                removed_task=task_list.pop(task_number-1)
                print("Removed task : ",removed_task)
                
                return removed_task
        else:
            print("No Tasks Availabel")

            return None
    except IndexError as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Error: That is not a valid number! Please enter a valid integer")
    


def load_tasks():
    content_list=[]
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:

                # rstrip("\n") removes the trailing newline character from each line
                # while preserving intentional leading spaces/indentation

                cleaned_task=line.strip()

                if cleaned_task:
                    content_list.append(cleaned_task)

    except FileNotFoundError:
        pass
    return content_list

def save_tasks(task_list):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in task_list:
            # Writing each task on a separate line
            file.write(task + "\n")

def main():
    task_list=load_tasks()

    while True:
        print("-------------Menu-------------")
        print()
        print("1:Add_Task")
        print("2:View_Task")
        print("3:Remove_Task")
        print("4:Exit")
    
        choice=str(input("select one of the above"))

        if choice=="1" or choice=="Add_Task":
            add_task(task_list)
        elif choice=="2" or choice=="View_Task":
            view_task(task_list)
        elif choice=="3" or choice=="Remove_Task":
            removed=remove_tasks(task_list)
            if removed!=None:
                save_tasks(task_list)
        elif choice=="4" or choice=="Exit":
            break
        else:
            print("Invalid choice.Plese select between 1 and 4")


if __name__ == "__main__":
    main()

