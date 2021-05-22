# problem statement:: https://mail.google.com/mail/u/0/#search/bhavya/FMfcgxwLtQMgHRXXhXsGHBcXldBnKZdG?projector=1&messagePartId=0.1

empSlot={}
empCab={}
empCancel={}
time=0
bookedSlots=[]

   
    

def sameSlot(func):
    def wrapper(*args,**kwargs):
        if bookedSlots.count(slot)<(cabCount/2):
            result=func(*args,**kwargs)
            return result
        else:
            print(f'Sorry.. Cannot allocate for slot-{slot} at the moment..Please check different slot or try later')

    return wrapper

def serialize(emp,slot,booking,cabs):
    
    if booking=='1':
        cab_allocation(emp,slot,cabs)
    elif booking=='-1':
        cab_cancellation(emp,slot,cabs)
    else:
        print('Invalid input')

def checkForCabs(cabs):
    if len(cabs)!=0:
        return True
    elif len(cabs)==0:
        tripDone(cabs)

def coolDown(emp):
    for i in range(60):
        continue
    empCancel[emp]-=1
    return 

def tripDone(cabs):
    for i in range(60):
        continue
    values=list(empCab.values())
    print(f'** Cab-{values[0]} added back to the pool **')
    return 

def subsequentCancel(emp):
    if emp in empCancel.keys():
        if empCancel[emp]<2:
            return True
    else:
        return True

def alreadyBooked(emp):
    if emp not in empSlot.keys():
        return True



@sameSlot
def cab_allocation(emp,slot,cabs):
    if checkForCabs(cabs) and subsequentCancel(emp):
        if alreadyBooked(emp):
            empSlot[emp]=slot
            empCab[emp]=cabs[0]
            cabs.pop(0)
            bookedSlots.append(slot)
            
            print(f'Cab-{empCab[emp]} allocated for emp {emp} for slot-{slot} (remaining cabs={len(cabs)} ) ')
        else:
            print(f'Employee {emp} is already allocated cab-{empCab[emp]} for slot-{empSlot[emp]} ')
        
    else:
        if not subsequentCancel(emp):
            print('*** Sorry request denied. Please wait for 80 seconds to try again.. ***')
            coolDown(emp)
            cab_allocation(emp,slot,cabs)
        else:
            print('** No cabs in the pool...Please wait!! **')
            tripDone(cabs)
            values=list(empCab.values())
            cabs.append(values[0])
@sameSlot
def cab_cancellation(emp,slot,cabs):
    
    empSlot.pop(emp)
    cabs.insert(0,empCab[emp])
    if emp in empCancel.keys():
        empCancel[emp]+=1
    else:
        empCancel[emp]=1
    
    print(f'Booking for slot-{slot} is cancelled by Employee-{emp} (remaining cabs={len(cabs)}) ')
    print(f'Cab {empCab[emp]} has returned back to the pool ')
    empCab.pop(emp)
    
    






empCount=int(input())
cabCount=int(input())
cabs=[i+1 for i in range(cabCount)]
while True:
    emp,slot,booking=list(input().split())
    serialize(emp,slot,booking,cabs)