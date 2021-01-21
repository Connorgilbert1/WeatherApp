#WEATHER CATCHER SCRIPT
import time

#This whole script is just one massive function lol


def Start():

    #Creates UserSelection variable and sets it to blank
    UserSelection=" "

    #Welcome sequence
    print("WELCOME TO WEATHER CATCHER 2021 BY CG AND RC\n")
    time.sleep(.8)
    
    #Presents the request for information
    print("WHAT WEATHER INFORMATION WOULD YOU LIKE?\n")
    time.sleep(.8)
    #Making a cool little border that splits that request and options up
    print(("-")*58)
    
    #UserSelection data is gathered. \n is to make it easier to read. 
    UserSelection=input("\nOPTION 1 : ALL CURRENT WEATHER DATA AVAILABLE\nOPTION 2: CURRENT TEMPERATURE & HUMIDITY\nOPTION 3: EXPECTED RAINFALL & BAROMETIC PRESSURE\n\nPLEASE INPUT YOUR CHOICE AS 1,2 OR 3\n")
            

   #Sorts through the choices...
    if UserSelection == "1":
        while True:
            #Demo to prove it works(can delete this soon after completion)
            print("\nREACHED OPTION ONE")
            #Here you should change the name of the text file in the open() function to be the name of the notepad '.txt' file that holds the Weather Data.
            #To show that it works I've made a text file that says "connection complete" when this section is executed.
            AllWeatherData = open("AllWeatherData.txt", "r")
            print(AllWeatherData.read())

            #Making a ContinueFunction so the user can loop back into the selection menu for another selection process. Start() is helpful as a def here.
            ContFunc=" "
            ContFunc = input("\nINPUT ANY KEY TO RETURN TO MENU\n")
            time.sleep(0.8)

            if ContFunc!=" ":
                Start()
                
    #Sort...
    elif UserSelection == "2":
        while True:
            #Demo...
            print("\nREACHED OPTION TWO")
            #Here you should change the name of the text file in the open() function to be the name of the notepad '.txt' file that holds the Weather Data(Temperature+Humidity).
            #To show that it works I've made a text file that says "connection complete" when this section is executed.
            TemperatureWeatherData = open("TemperatureWeatherData.txt", "r")
            print(TemperatureWeatherData.read())

            #ContinueFunction...
            ContFunc=" "
            ContFunc = input("\nINPUT ANY KEY TO RETURN TO MENU\n")
            time.sleep(0.8)
            
            if ContFunc!=" ":
                Start()
                
    #Sort...            
    elif UserSelection == "3":
        while True:
            #Demo...
            print("\nREACHED OPTION THREE")
            #Here you should change the name of the text file in the open() function to be the name of the notepad '.txt' file that holds the Weather Data(Pressure+Rainfall)
            #To show that it works I've made a text file that says "connection complete" when this section is executed.
            RainfallWeatherData = open("RainfallWeatherData.txt", "r")
            print(RainfallWeatherData.read())
            
            #ContinueFunction...
            ContFunc=" "
            ContFunc = input("\nINPUT ANY KEY TO RETURN TO MENU\n")
            time.sleep(0.8)

            if ContFunc!=" ":
                Start()
                
    #Catchment for the silly buggers who can't input 1,2 or 3 correctly.
    else:
        print("\nPLEASE ENTER YOUR CHOICE AS 1,2 OR 3\n")
        print("restarting...\n")
        time.sleep(0.8)
        Start()
        

            

            
#Iniation
Start()

            
        
    
        
        








    
    
