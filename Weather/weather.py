try:
    ######## LIBRABIES AND API KEY ################
    import pyfiglet                               #
    import requests                               #
    import sys                                    #
    from datetime import datetime                 #
    api="YOUR_API_KEY"                            #  #Paste your api key inside the "" inverted commas.
    ###############################################
    pf = pyfiglet.figlet_format("MY WEATHER")
    print(pf,"\n version 1.0")
    print()
    print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
    while True:
        location=str(input("[+]Enter Your Location: "))
        print("(*If it shows error or invalid then try with the capital city)")
        print()
        url="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api+"&units=metric"
        try:
            response=requests.get(url)
            if response.status_code==200:
                wdata=response.json()
                current_temp=wdata["main"]["temp"]
                feelslike_temp=wdata["main"]["feels_like"]
                pressure=wdata["main"]["pressure"]
                humidity=wdata["main"]["humidity"]
                weather=wdata["weather"][0]["description"]
                visible=wdata["visibility"]
                visibility=visible/1000
                wind_speed=wdata["wind"]["speed"]
                wind_angle=wdata["wind"]["deg"]
                sea_level=wdata["main"]["sea_level"]
                grnd_lvl=wdata["main"]["grnd_level"]
                country=wdata["sys"]["country"]
                city=wdata["name"]
                    
            ################################## Angle Determination ###########################################
                deg=""
                if wind_angle==0:
                    deg="°N"
                elif wind_angle>0 and wind_angle<90:
                    deg="°NE"
                elif wind_angle==90:
                    deg="°E"    
                elif wind_angle>90 and wind_angle<180:
                    deg="°SE"
                elif wind_angle==180:
                    deg="°S"
                elif wind_angle>180 and wind_angle<270:
                    deg="°SW"
                elif wind_angle==270:
                    deg="°W"
                elif wind_angle>270 and wind_angle<360:
                    deg="°NW"    
                else:
                    deg="°"
            ################################## details #######################################################
                print("----------------------------:Weather Details:---------------------------------------")    
                print("Country: ",country)
                print("City: ",city)
                print("Current Temperature: ",current_temp,"°C")
                print("Feels Like: ",feelslike_temp,"°C")
                print("Pressure: ",pressure,"hPa")
                print("Humidity: ",humidity,"%")
                print("Weather: ",weather)
                print()
                print("--------------:More Details:-----------------")
                print()
                print("Visibility: ",visibility,"km")
                print("Wind Speed: ",wind_speed,"km/h")
                print("Wind Angle: ",wind_angle,deg)
                print("Sea Level: ",sea_level,"km")
                print("Ground Level: ",grnd_lvl,"km")
                print()
                print("------------------------------------------------------------------------------------")
                print()
                while True:
                    n=input("Exit or Continue: ")
                    if n=="Exit" or n=="exit":
                        print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
                        sys.exit()
                    elif n=="Continue" or n=="continue":
                        print()
                        print("-------------------------------------------:New Weather Details:-------------------------------------------------")
                        print()
                        break
                    else:
                        print("Select either Exit or Continue!")
                        print()
                        pass
                    pass
            else:
                print("[-]CITY NOT FOUND!")
                print()
                print("[?]Try With Capital City!")
                print()
                print("--------------------------------------------:New Weather Details:-----------------------------------------")
                print()
                pass
        except Exception:
            print("[-]Something Went Wrong!")
            print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
            sys.exit()
except Exception and KeyboardInterrupt:
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("[-]Something Went Wrong!")
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    sys.exit()
