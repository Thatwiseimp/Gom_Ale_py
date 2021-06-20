


class Mission():
    def __init__(self,name,details):
        self.name=name
        self.details=details

class Avenger():
    def __init__(self,name,true_name,skills,mission_assigned=0,mission_completed=0):
        self.name=name
        self.true_name=true_name
        self.skills=skills
        self.mission_assigned=mission_assigned
        self.mission_completed=mission_completed

    def __str__(self):
        return(f'avenger name:{self.name}\ntrue name:{self.true_name}\nskills:{self.skills}\nmissions asssigned:{self.mission_assigned}\nmissions completed:{self.mission_completed}')


class Captain(Avenger,Mission):
    def __init__(self,name):
        self.name=name
        self.assignment={}
        self.assignment_message='Mission has been assigned. Email notification has been sent or sms notification has been sent'


    def mission_logs(self):
        store=[['Mission name |  status  |  Avengers']]
        for k,v in self.assignment.items():
            store.append([f'{k} |{v}'])
        return store

    def mission_index(self,mission):
        assigned_crew = self.assignment[mission.name]
        return(f'mission details:{mission.details}\nmission status={assigned_crew[0]}\nAvengers:{assigned_crew[1][0]}  and {assigned_crew[1][1]}')

    def avenger_info(self,name):
        return name.__str__()

    def check_availability(self,mission):
        if mission.name not in self.assignment:
            return True
        else:
            store=self.assignment[mission.name]
            return len(store[1])


    def assign_mission(self,mission,A,B):
        if self.check_availability(mission)==True or 1:
            self.assignment[mission.name]='| Assigned',[A.name,B.name]
            return self.assignment_message

    def assign_avenger_to_a_mission(self,mission,avenger):
        if self.check_availability()==1:
            self.assignment[mission.name].append(avenger.name)
        else:
            store=self.assignment[mission.name]
            return (f'{store[0]}and{store[1]} are already on the mission')


    def update_mission(self,mission):
        store=self.assignment[mission.name]
        self.assignment[mission.name]='| Completed'
        return f'Email and sms are sent to {store[0]}and{store[1]}'

    def __str__(self):
        for k,v in self.assignment.items():
            return(f'{k}:{v}')





cf=Captain('Captain Fury')
hk=Avenger('Hawkeye','Clint Barton','Combat & archery')
bw=Avenger('Black Widow','Natasha Romanoff','Combat & martial arts')
hb=Mission('Bring the Hulk Back',"Hulk has gone back to the underground, somebody's gotta bring him back")
cf.assign_mission(hb,hk,bw)


print("Welcome to Captain Fury.\n1. Check the missions\n2. Assign mission to Avengers\n3. Check mission’s details\n4. Check Avenger’s details\n5. Update Mission’s status\n6. List Avengers\n7. Assign avenger to mission.")
