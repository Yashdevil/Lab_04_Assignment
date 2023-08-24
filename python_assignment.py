# Yash Dev Ladha E22CSEU0068 
class table:
    d={1:["Mumbai","India","Sri Lanka","DAY"],
    2:["Delhi","England","Australia","DAY-NIGHT"],
    3:["Chennai","India","South Africa","DAY"],
    4:["Indore","England","Sri Lanka","DAY-NIGHT"],
    5:["Mohali","Australia","South Africa","DAY-NIGHT"],
    6:["Delhi","India","Australia","DAY"]
    }
    

    def match(self,name):
        for i in table.d:
            if(table.d[i][1]==name or table.d[i][2]==name):
                print(table.d[i][1],"vs ",table.d[i][2])
                
    def location(self, loc):
        for i in table.d:
            if(table.d[i][0]==loc):
                print(table.d[i][1],"vs ",table.d[i][2])

    def Timing(self, day):
        for i in table.d:
            if(table.d[i][3]==day):
                print(table.d[i][1],"vs ",table.d[i][2])
    
            
obj = table()
while(True):
    print("1. List of all the matches of a Team ")
    print("2. List of Matches on a Location") 
    print("3. List of Matches based on timing.")
    print("4.exit")
    print()
    a = int(input("enter choice  : " ))
    if(a==1):
        b = input("Enter team ")
        obj.match(b)
    elif(a==2):
        c = input("Enter location ")
        obj.location(c)
    elif(a==3):
        d = input("Enter timing ")
        obj.Timing(d)
    elif(a==4):
        break