import json
from datetime import date, datetime

def load_data():
    try:
     with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"To_Do": [], "Assignments": [], "Routine": []}

def ask_date(question):
    answer = input(question)
    try:
        d = datetime.strptime(answer, "%d-%m-%Y").date()
    except ValueError:
        print("Use DD-MM-YYYY, like 05-12-2026")
        return None
    return str(d)

def ask_time(question):
    answer = input(question)
    try:
        t = datetime.strptime(answer, "%H:%M").time()
    except ValueError:
        print("Use Hour : Minute, like 17:30")
        return None
    return t.strftime("%H:%M")

def save_task(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 4)

def add_task(task, due):
    data = load_data()
    data["Assignments"].append({"task": task, "due": due, "status": False})
    save_task(data)

def add_todo(task, due):
    data = load_data()
    data["To_Do"].append({"task": task, "done by": due, "status": False})
    save_task(data)

def add_routine(task, every):
    data = load_data()
    data["Routine"].append({"routine": task, "every": every, "status": False, "last_done": None})
    save_task(data)
def make():
    print("     ### ADDING TASK ###")
    print("Please pick one (1 or 2 or 3): ")
    print("1) TO DO (For today)")
    print("2) ASSIGNMENT (For the future)")
    print("3) ROUTINE (You do this every x days or weeks)")
    section = input("")

    if section == "1":
        while True:
            print("Type QUIT to leave this section")
            task = input("What do you have today? ")
            if task == "QUIT":
                break
            due = ask_time("When do you want it done? (Hour:Minute | 17:40) ")
            if due is None:
                continue
            add_todo(task, due)
            data = load_data()
            print("Saved! You have saved", len(data["To_Do"]), "task(s)")        

    elif section == "2":
        while True:
            print("Type QUIT to leave this section")
            task = input("What do you need done? ")
            if task == "QUIT":
                break
            due = ask_date("When is it due? (DD-MM-YYYY) ")
            if due is None:
                continue
            add_task(task, due)
            data = load_data()
            print("Saved! You have", len(data["Assignments"]), "task(s)")
    elif section == "3":
        while True:
            print("Type QUIT to leave this section") 
            task = input("What routine do you need? ")
            due = input("Done every how many days? ")
            if task == "QUIT" or due == "QUIT":
                break
            else: 
                days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
                due = due.lower()
                if due in days:
                    every = due
                else: 
                    try:
                        every = int(due)
                    except ValueError:
                        print("Pick a number!")
                        return
                    if not 1 <= int(due) <= 99:
                        print("Pick a number from 1 - 99! ")
                        return
                    
                add_routine(task, every)
                data = load_data()
                print("Saved! You have saved", len(data["Routine"]), "task(s)")

def view(x):
    if x == "x":
        print("     ### VIEWING TASK ###")
        print("Which section you wanna open? (1 or 2 or 3): ")
        print("1) TO DO (For today)")
        print("2) ASSIGNMENT (For the future)")
        print("3) ROUTINE (You do this every x days or weeks)")
        data = load_data()
        e = input("")
        if e == "1": 
            for i,t in enumerate(data["To_Do"]):
             try:
                d = datetime.strptime(t['done by'], "%H:%M")
                d2 = (t.strftime("%I:%M %p").lstrip(0))
                print(f"{i+1}. {t['task']} | Due: {d2}")
             except:
                print(f"{i+1}. {t['task']} | Due: {t['done by']}")
        elif e == "2":
            for i,t in enumerate(data["Assignments"]):
                    d = date.fromisoformat(t["due"])
                    d2 = d.strftime("%d %B %Y")
                    print(f"{i+1}. {t['task']} | Due: {d2}")
        elif e == "3":
            for i,t in enumerate(data["Routine"]):
             try:
                d = date.fromisoformat(t["last_done"])
                d2 = d.strftime("%d %B %Y")
             except: 
                d2 = ("Not yet!")
             if isinstance(t['every'], int):
                print(f"{i+1}. {t['routine']} | Every: {t['every']} day(s) | Last done: {d2}")
             else: 
                print(f"{i+1}. {t['routine']} | Every: {t['every']} | Last done: {d2}")
                         
        else:
                print("That is not an option!")
    elif x != "":
        data = load_data()
        if x == "1": 
         try:
            d = datetime.strptime(t['done by'], "%H:%M")
            d2 = (t.strftime("%I:%M %p").lstrip(0))
            print(f"{i+1}. {t['task']} | Due: {d2}")
         except:
            print(f"{i+1}. {t['task']} | Due: {t['done by']}")
            pass
    elif x == "2":
            for i,t in enumerate(data["Assignments"]):
                    d = date.fromisoformat(t["due"])
                    d2 = d.strftime("%d %B %Y")
                    print(f"{i+1}. {t['task']} | Due: {d2}")
    elif x == "3":
            for i,t in enumerate(data["Routine"]):
                d = date.fromisoformat(t['last_done'])
                d2 = d.strftime("%d %B %Y")
                if isinstance(t['every'], int):
                    print(f"{i+1}. {t['routine']} | Every: {t['every']} day(s) | Last done: {d2}")
                else: 
                    print(f"{i+1}. {t['routine']} | Every: {t['every']} | Last done: {d2}")
            else:
                        print("That is not an option!")
                

def view_all():
     data = load_data()
     for i,t in enumerate(data["To_Do"]):
        try:
            d = datetime.strptime(t['done by'], "%H:%M")
            d2 = (t.strftime("%I:%M %p").lstrip(0))
            print(f"{i+1}. {t['task']} | Due: {d2}")
        except:
            print(f"{i+1}. {t['task']} | Due: {t['done by']}")
     for i,t in enumerate(data["Assignments"]):
        d = date.fromisoformat(t['due'])
        d2 = d.strftime("%d %B %Y")
        print(f"{i+1}. {t['task']} | Due: {d2}")
     for i,t in enumerate(data["Routine"]):
        d = date.fromisoformat(t['last_done'])
        d2 = d.strftime("%d %B %Y")
        if isinstance(t['every'], int):
            print(f"{i+1}. {t['routine']} | Every: {t['every']} day(s) | Last done: {d2}")
        else: 
            print(f"{i+1}. {t['routine']} | Every: {t['every']} | Last done: {d2}")

def routine_systems():
    d = date.today()
    data = load_data()
    for t in range(len(data['Assignments']) - 1, -1, -1):
        d2 = data['Assignments'][t]['due']
        if d2 == str(d):
            task = data['Assignments'][t]['task']
            due = "Today! (Assignment)"
            data = load_data()
            data['To_Do'].append({"task": task, "done by": due, "status": False})
            del(data['Assignments'][t])
            save_task(data)
        else:
            pass
            


def complete(section):
    names = {"1": "To_Do", "2": "Assignments", "3": "Routine"}
    if section == "QUIT" or section == "0":
        return
    
    if section not in names:              # bad section: stop here
        print("That ain't an option!")
        return    

    x = names[section]                    # "1" becomes "To_Do", and so on
    data = load_data()

    if len(data[x]) == 0:                 # empty list: nothing to complete
        print("Nothing in this section yet!")
        return
    print("     ### COMPLETING TASK ###")

    for i, t in enumerate(data[x]):
        name = t.get("task", t.get("routine"))    # see note below
        print(f"{i+1}. {name} | Done: {t['status']}")
    print("Type QUIT to return to main section")
    answer = input("Pick one to complete: ")      # outside the loop, plain string

    if answer == "QUIT":
        return

    try:
        n = int(answer)                   # the conversion happens inside the try
    except ValueError:
        print("Type a number!")
        return

    if 1 <= n <= len(data[x]):
        data[x][n - 1]["status"] = True
        if x == "Routine":
            data[x][n - 1]["last_done"] = str(date.today())
        save_task(data)                   # save the same data you changed
        print("You have completed 1 Task!")   # only prints on success
    else:
        print("Please pick a valid number!")


def delete(sec, number):
        data = load_data()
        if sec == "1":
            z = "To_Do"
        elif sec == "2":
            z = "Assignments"
        elif sec == "3":
            z = "Routine"
        else:
         print("That ain't an option!")
         return 

        try:
            number = int(number)
        except: 
            print("Type a number!")
            return

        if not 1 <= number <= len(data[z]):       
            print("Please pick a valid number!")
            return
        
        print("Confirm? Y/N ")
        pick = input("")
        if pick == "Y" or pick == "y": 
         del data[z][number - 1]
         save_task(data)
         print(f"Succesfully deleted 1 task!")
        else:
         print("Delete is cancelled ")

while True:
     routine_systems()
     data = load_data()
     for i in range(len(data['To_Do']) - 1, -1, -1):
         if data['To_Do'][i]['status'] == True:
             del(data["To_Do"][i])
             save_task(data)
         else:
             pass
     for i in range(len(data['Assignments']) - 1, -1, -1):
         if data['Assignments'][i]['status'] == True:
             del(data["Assignments"][i])
             save_task(data)
         else:
             pass
     print("### N.O.R.M.A.N ### ")
     print("0. Quit")
     print("1. Add Task ")
     print("2. View Task ")
     print("3. Complete Task ")
     print("4. Delete Task ")
     print("Please pick one! ")
     p = input("> ")
     if p == "1":
          make()
     elif p == "2":
          view("x")
     elif p == "3":
          pick = input("Pick one:\n"
                        "0.) QUIT\n"
                        "1.) To do\n"
                        "2.) Assignments\n"
                        "3.) Routine\n"
                        "> ")
          complete(pick)
     elif p == "4":
        while True:
          section = input("Pick one:\n"
                        "0.) QUIT\n"
                        "1.) To do\n"
                        "2.) Assignments\n"
                        "3.) Routine\n"
                        "> ")          
          if section == "0" or section == "QUIT":
              break
          else:
              view(section)
              print("Type QUIT to go back")
              task = input("Pick a task: 1, 2, 3, Etc \n"
                           "> ")
          if task == "QUIT" :
            pass
          else:
            delete(section, task)

     elif p == "0":
         break

     else:
          print("Invalid choice! ")

