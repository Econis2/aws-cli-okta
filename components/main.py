#!/usr/bin/python

import os
import sys
import datetime
import operator

def getActiveProfileInfo(pathActiveProfile):
    # Get the active profiles
    with open(pathActiveProfile,"r") as line:
        listActiveProfiles = [ x.rstrip('\n') for x in line ]
        countActiveProfiles = len(listActiveProfiles) / 5
        #If a previous profile exists
        if countActiveProfiles >= 1:
            dictAccountExpire = {}
            x = 0
            # Add the name of the profile and expire datetime for reference
            while x <= countActiveProfiles - 1:
                n_count = x * 5
                dictAccountExpire[ listActiveProfiles[ n_count ].replace("[",'').replace("]",'') ] = listActiveProfiles[ n_count + 3 ].split(" = ")[1]
                x = x + 1
            return dictAccountExpire
        else:
            return None

def accountExpired(pathActiveProfile, profile):
    if os.path.isfile(pathActiveProfile):
        activeProfile = getActiveProfileInfo(pathActiveProfile)
        try:
            profileIndex = activeProfile.keys().index(profile)
        except:
            profileIndex = -1
        if activeProfile != None and profileIndex != -1:
            datetimeExpire = datetime.datetime.strptime(activeProfile[ profile ].split('.')[0] , '%Y-%m-%dT%H:%M:%S')
            datetimeCurrent = datetime.datetime.now()
            if datetimeCurrent >= datetimeExpire:
                return True
            else:
                return False
        else: return True
    else: return True

def getProfileFromConfig(pathAwsProfiles,nameProfile):
    pathProfileInfo = os.path.join(pathAwsProfiles , nameProfile + ".config")
    with open(pathProfileInfo, "r") as line:
        awsConfigProfiles = [x.rstrip('\n') for x in line]
        profileConfig = [
            '#OktaAWSCLI\n'
            'OKTA_ORG=' + awsConfigProfiles[0] + "\n",
            'OKTA_AWS_APP_URL=' + awsConfigProfiles[1]+ "\n",
            'OKTA_USERNAME=' + awsConfigProfiles[2]+ "\n",
            'OKTA_BROWSER_AUTH=true\n',
            'OKTA_AWS_REGION=' + awsConfigProfiles[3]+ "\n",
        ]
    return profileConfig

def writeCurrentConfigProfile(pathAwsProfile , pathActiveConfig, nameProfile):
    awsConfigProfile = getProfileFromConfig( pathAwsProfile , nameProfile )
    for line in awsConfigProfile:
        try:
            open(pathActiveConfig, "w").writelines(awsConfigProfile)
        except:
            print("Unable to write the Profile")
            exit(5)
        


# Profile Name from bash script execution
nameProfile = sys.argv[1]

# /Users/[username]/.okta/
pathOkta = os.path.join( os.path.expanduser("~"), ".okta")

# List of Files/Directories in .okta/
dirListOkta = os.listdir(pathOkta) 

# /Users/[username]/.okta/awsProfiles/
pathAwsProfiles = os.path.join( pathOkta , "awsProfiles" )

# /Users/[username]/.okta/profiles
pathActiveProfiles = os.path.join( pathOkta , "profiles" )

# /Users/[username]/.okta/config.properties
pathActiveConfig = os.path.join( pathOkta , "config.properties")

# If reqs are not in place prompt for setup
if operator.not_(os.path.isdir(pathAwsProfiles)):
    print ("Run through the configuration python script first")
    exit(3)

account_Status = accountExpired( pathActiveProfiles , nameProfile )

writeCurrentConfigProfile( pathAwsProfiles , pathActiveConfig , nameProfile)

if account_Status == True:
    exit(0)
else:
    exit(1)
