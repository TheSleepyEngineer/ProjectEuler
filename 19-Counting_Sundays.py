month_days={"jan":31, "feb": 28, "mar":31, "apr": 30, "may":31, "june":30, "july":31, "aug":31, "sept":30, "oct":31, "nov":30, "dec":31 }
months=("jan", "feb", "mar", "apr", "may", "june", 'july', "aug", "sept", "oct", "nov", "dec")

sundaysOnTheFirst=0


### Creating circular linked list to contain 7 days of the week:
class Node:
        def __init__(self, dataval=None):
            self.dataval=dataval
            self.nextval=None

        def move(self, steps=1):
            if steps==0:
                return self
            node=self
            for i in range(0,steps):
                node=node.nextval
            return node


### Implementing days of the week linkedlist:

Mon= Node("Mon")
Tues= Node("Tues")
Wed= Node("Wed")
Thurs= Node("Thurs")
Fri= Node("Fri")
Sat= Node("Sat")
Sun = Node("Sun")

Mon.nextval=Tues
Tues.nextval=Wed
Wed.nextval=Thurs
Thurs.nextval=Fri
Fri.nextval=Sat
Sat.nextval=Sun
Sun.nextval=Mon



CurrentDay=Mon



for year in range(1900,2001):
    if year%4==0 and year!=1900:
        month_days["feb"]=29
    else:
        month_days["feb"]=28

    ## get number days left after modulo 7 from the first of the month
    for month in months:
        delta_days=month_days[month]%7
        CurrentDay=CurrentDay.move(delta_days)


         ## add counter of days if meets all conditions:
        if CurrentDay.dataval=="Sun" and year > 1900:
            sundaysOnTheFirst+=1

print(sundaysOnTheFirst)