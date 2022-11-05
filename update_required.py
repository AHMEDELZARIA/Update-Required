#Function determines whether device needs update or not
def update_required(device_info):
    OSVersion = float(device_info[2])
    
    #Device doesn't need update if OSversion is less than 8.0
    if OSVersion >= 8.0:
        return True
    else:
        return False
      
#Determine Version update of device
def determine_update(device_info):
    update_req = update_required(device_info) # a boolean representing if an update is required
    OSType = device_info[1]
    OSVersion = float(device_info[2])
    month = int((device_info[3]).split('-')[1]) # Split the date by -, take the middle element, convert to int
 
    if update_req == True:
        if OSType == "iOS": #if update is required, then immediately version 1
            return "Version 1"
        elif OSType == "Android" and OSVersion >= 10.0:
            return "Version 2"
        elif OSType == "Android" and OSVersion >= 8.0 and OSVersion < 10.0: 
            if month >= 1 and month <=6: #If last update between January and June, if not, execute else
                return "Version 3"
            else:
                return "Version 4"
    #If no update required
    else:
        return "No Update"
      
#Returns list of devices needed to update
def determine_device_update(devices):
    #Initialize empty list
    system_update = []
    
    #Loops through devices and appends to list sublists of update required devices
    for i in range(len(devices)): 
        if update_required(devices[i]) == True:
            #Initialize a sub list
            new_info = []
            
            #Fill list with serial number and version number
            new_info.append(devices[i][0])
            new_info.append(determine_update(devices[i]))
            
            #Append sublist to main list
            system_update.append(new_info)
        #If no update required just skip
        else: 
            continue
    
    return system_update
  
# TESTING
def main():
    devices = [['GX010365', 'iOS', '8.1', '2019-04-10'], #Version 1
              ['BX041085', 'Android', '12.0', '2019-09-13'], #Version 2
              ['BX031112', 'Android', '5.0', '2019-02-13'], #No Update
              ['BX210529', 'iOS', '7.0', '2019-11-15'], #No Update
              ['GX031153', 'Android', '9.0', '2019-04-11'], #Version 3
              ['BX601829', 'iOS', '9.0', '2019-04-28'], #Version 1
              ['BX481436', 'iOS', '10.1', '2019-01-10'], #Version 1
              ['GX301320', 'Android', '9.0', '2019-07-13']] #Version 4
    device_updates = determine_device_update(devices)
    print(device_updates)
    
main()
