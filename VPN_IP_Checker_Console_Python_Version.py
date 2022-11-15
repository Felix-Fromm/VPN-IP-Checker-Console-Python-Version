from genericpath import exists
import os
from os import path
import webbrowser
import requests

#--------------------------------------
#----------- Settings Path ------------
#--------------------------------------

# Setting some Strings with the Path and the File name of the Settings file.
sSettingsPath = path.expandvars(r'%LOCALAPPDATA%\IP-VPN-Checker'); #LocalAppData -> /IP-VPN-Checker
sConfigName = "config.ff";

#--------------------------------------
#---------- Function Define -----------
#--------------------------------------

def FirstKeyInput() :
    Output = False;
    print("Insert API-Key:");
    Keyinput = input("");
    if Keyinput.lower() == "visit":
        url = "https:#vpnapi.io/signup"
        webbrowser.open(url, new=0, autoraise=True)

    else :
        try:
            f = open(sSettingsPath + "\\" + sConfigName, "w")
            f.write(Keyinput) # Saves your Key into a File and saves it inside the Settings Folder.
            f.close()
            Output = True;
        except:
            Output = False;
    return Output

def ReCreateKey() :
    Output= False
    print("Type your new key code now:");
    newKey = input() #Reads your userinput and saves it in newKey
    if newKey == None or newKey == "" :
        print("Pls enter a valid Code.");
        Output = False
    else:
        f = open(sSettingsPath + "\\" + sConfigName, "w")
        f.write(newKey) # Saves your Key into a File and saves it inside the Settings Folder.
        f.close()
        Output = True
    return Output

def WrongTextReset() :
    Output = False
    print("Do you want to edit your key? Yes/No (empty = No)")
    userinput = input().lower()
    if userinput == "yes" :
        if ReCreateKey() == False:
            if ReCreateKey() == False:
                if ReCreateKey() == False:
                    if ReCreateKey() == False:
                        if ReCreateKey() == False:
                            print("well i tryed")
        Output = True
    elif userinput == "no" or userinput == "" :
        print("") #End Editmode when no or "" is detected. (Ending with just no code in it)
        Output = True
    else: #When no predefined word matches
        print("Pls enter with one of the answers.");
        Output = False
    return Output

if not os.path.exists(sSettingsPath): #Checks if the Settings Folder exists
    try:
        os.makedirs(sSettingsPath)#Creates it when it doesnt exist.
    except FileExistsError:
        # directory already exists
        pass

if not exists(sSettingsPath + "\\"+sConfigName) : #Asks inverted if the File Exists ( it really asks if it is not exisiting)
    print("You can create a Account and get a API-Key from 'VPNAPI.io' | If you write 'visit' then the site will open for you!")
    if FirstKeyInput() == False:
        if FirstKeyInput() == False:
            if FirstKeyInput() == False:
                if FirstKeyInput() == False:
                    if FirstKeyInput() == False:
                        print("I give up!")

else :
    #This Triggers when it found a Settings file and asks you if you want to rewrite it.
    if WrongTextReset() == False :
        if WrongTextReset() == False :
            if WrongTextReset() == False :
                if WrongTextReset() == False :
                    if WrongTextReset() == False :
                        if WrongTextReset() == False :
                            print("I give up!")

sKey = ""; #Reads the config file and saves the key
with open(sSettingsPath + "\\" + sConfigName, 'r') as file:
    sKey = file.read().rstrip()

#-------------------------------
#--------- Main Code -----------
#-------------------------------
while(True):
    print("Please enter IP. - Example: 8.8.8.8"); 
    sIpToLookUp = input(); #Saves IP as String for URL Build.

    sAPIURL = "https://vpnapi.io/api/"+sIpToLookUp+"?key=" + sKey; #Building the API key with the LookUpIP and your Key.

    sResult = requests.get(sAPIURL);

    print(sResult.text) #Print Output from sResult
