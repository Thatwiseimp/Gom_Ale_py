
access={}
avengers_details={}
avengers_directory={}
mission_directory={}
assignment_status={}



class Avenger(object):




    def __init__(self,name):
        self.name=name
        if name=='Captain Fury':
            access[name]=True
            crew=['Captain America','Black Widow','Hawkeye','Thor','Hulk','Iron Man']
            info=[['Steve Rogers','Super Human by strength',0,0],['Natasha Romanoff','Agility & Combat',0,0],['Clint Barton','Combat',0,0],['Bruce Banner','Genetically mutated human',0,0],['Son of Odin','God of thunder',0,0],['Tony Stark','Highly intelligent suit of armour',0,0]]
            for i in range (len(crew)):
                self.set_avenger(f'{crew[i]}')
                avengers_details[(crew[i])]=info[i]
        else: 
            access[name]=False
        
    def set_avenger(self,name):
        Avenger(name)

    def initialize(self):        
            print('------------------------------------\n\n')
            print('Welcome,Captain Fury.. \n 1. Check the missions \n 2. Assign mission to Avengers \n 3. Check mission’s details \n 4. Check Avenger’s details \n 5. Update Mission’s status \n 6. List Avengers \n 7. Assign avenger to mission.')
            response=get_input('Enter an option:' )
            if response==1:
                return self.check_missions()
            elif response==2:
                return self.assign_avengers_to_mission()
            elif response==3:
                return self.check_mission_status()
            elif response==4:
                return self.inspect_avenger()
            elif response==5:
                return self.update_mission_status()
            elif response==6:
                return self.list_avengers()    
            elif response==7:
                return self.assign_mission_to_avenger()
            else: return('Invalid Response')
    
        

        
    def check_missions(self):
        if len(mission_directory.keys())==0:
            return('No mission has been assigned yet.')
        else:
            store=[]
            for k,v in assignment_status.items():
                store.append(k)
                store.append(v[0])
                store.append(v[1])

            print(assignment_status.keys())
            return store


    def inspect_avenger(self):
        name=input('Enter avenger name:').strip()
        store=avengers_details[name]
        return(f'Person Name:{store[0]} \n Abilities:{store[1]} \n Missions Assigned:{store[2]} \n Missions Completed:{store[3]}')
      
        

    def list_avengers(self):
        print('Avenger name\t|Status\t|Assigned mission')
        store=[]
        for k,v in avengers_details.items():
            store.append(k)
            if k in avengers_directory.keys():
                store.append('On Mission')
                store.append(avengers_directory[k])
            else:
                store.append('Available')

        return store



    def check_availability(self,mission_name,avenger):
        
        if mission_name not in mission_directory.keys():
            if avenger not in avengers_directory.keys():
                return True 
            elif len(avengers_directory[avenger])==2:
                print(len(avengers_directory[avenger]))
                return False   
                     
        return(f'{mission_name} is already been allocated')
        


    def serialize(self,mission_name,mission_details,avenger_1,avenger_2): 
        mission_directory[mission_name]=[mission_details],[avenger_1,avenger_2]
        assignment_status[mission_name]='Assigned',[avenger_1,avenger_2]
        self.store(mission_name,avenger_1)
        self.store(mission_name,avenger_2)
        

            
    def store(self,mission_name,avenger):        
        if avenger not in avengers_directory.keys():
            avengers_directory[avenger]=[mission_name]
        else:
            avengers_directory[avenger].append(mission_name)
        info=avengers_details[avenger]
        info[2]+=1
       


    def assign_avengers_to_mission(self):
        print(mission_directory.values())
        avengers=input('Enter Avengers:').split(',')
        mission_name=input('Enter mission name: ').strip()
        mission_details=input('Enter mission details:')
        avenger_1=avengers[0].strip()
        avenger_2=avengers[1].strip()
        if self.check_availability(mission_name,avenger_1):
            if self.check_availability(mission_name,avenger_2):
                self.serialize(mission_name,mission_details,avenger_1,avenger_2) 

                return (f'Mission has been assigned to {avenger_1} and {avenger_2} \n Email or SMS notification has been sent')
            else:
                return(f'Sorry,{avenger_2} has already working on two missions')
        return(f'Sorry,{avenger_1} has already working on two missions')  


    def assign_mission_to_avenger(self):
        avenger=input('Enter avenger name: ')
        mission_name=input('Enter mission name: ')
        info=assignment_status[mission_name]
        if len(info[1])==2:
            return (f'{info[1][0]} and {info[1][1]} are already working on this mission')
        else:
            info[1].append(avenger)
            assignment_status[mission_name]
            return(f'{avenger} is successfully added to the mission')
            


    def check_mission_status(self):
        mission_name=input('Enter Mission Name: ').strip()
        store=mission_directory[mission_name]
        if store[1]!=None:
            return(f'Mission: details:{store[0]}\n Mission status: Assigned\n Avengers:{store[1]}')


        
    
    
    def update_mission_status(self):
        mission_name=input('Enter Mission Name:')
        new_status=input('Enter new status:')
        store=mission_directory[mission_name]
        status=list(assignment_status[mission_name])
        status[0]='Completed'
        assignment_status[mission_name]=status
        return (f'Email and SMS are sent to {store[1][0]} and {store[1][1]}')
            
        
Captain=Avenger('Captain')
def get_input(text):
    return input(text)
