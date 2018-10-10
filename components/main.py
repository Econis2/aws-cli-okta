#!/usr/bin/python

import os
import sys
import datetime
import operator

def checkExpired():

    tryStatus = {
        "code": '',
        "message": ''
    }

    oktaBase = os.path.join( os.path.expanduser("~"), ".okta")
    oktaProfile = os.path.join( oktaBase, "profiles")

    # Get the active profiles
    if os.path.exists(oktaProfile):

        with open(oktaProfile,"r") as line:

            try:
                #active profile Expiration Line
                expireLine = [ x.rstrip('\n') for x in line ][3]

            # File is blank - New Account Required
            except IndexError:
                tryStatus['code'] = 205
                tryStatus['message'] = "Account Expired"
                
                return tryStatus
            # Random Exception
            except:
                tryStatus['code'] = 500
                tryStatus['message'] = "Unable to extract Expiry info"

                return tryStatus

            # Commpare Today with Expire Time
            try:
                dateTimeExpire = datetime.datetime.strptime(expireLine.split('.')[0] , '%Y-%m-%dT%H:%M:%S')
                dateTimeCurrent = datetime.datetime.now()
            except:
                tryStatus['code'] = 500
                tryStatus['message'] = "Unable to extract Expiry info"

                return tryStatus
        
            if dateTimeCurrent >= dateTimeExpire:
                tryStatus['code'] = 200
                tryStatus['message'] = "empty"
                
                return tryStatus
            else:
                tryStatus['code'] = 205
                tryStatus['message'] = "Account Expired"
                
                return tryStatus

    else:
        tryStatus.code = 500
        tryStatus.message = "File not found: " + oktaProfile

        return tryStatus

# Depricated - Functionality moved to bash_functions
#def createProfile():
#
#   # create Status codes for function completion
#    tryStatus = {
#        "code": '',
#        "message": ''
#    }
#
#    #Base path of the ~/.okta directory
#    oktaProfilePath = os.path.join( os.path.expanduser("~"), "./okta/config.properties" )
#
#    try:
#        os.remove(oktaProfilePath)
#    except:
#        print("Unable to remove the exisitng configuration")
#
#       tryStatus['code'] = 500
#        tryStatus['message'] = "Unable to remove the exisitng configuration"
#
#        return tryStatus
#
#    print("/n")
#    #Get a list of required props
#    test = raw_input("Enter for testing")
#    propList = [
#        ("OKTA_ORG=" + sys.argv[2] + "\n"),
#        ('OKTA_AWS_APP_URL=' + sys.argv[3] + "\n"),
#        ('OKTA_USERNAME=' + sys.argv[4] + "\n"),
#        ('OKTA_BROWSER_AUTH=true\n'),
#        ('OKTA_AWS_REGION=' + sys.argv[5] + "\n")
#    ]
#    try:
#        open(oktaProfilePath, "w").writelines(propList)
#    except:
#        print("Unable to write/replace ~/.okta/config.properties")
#        
#        tryStatus['code'] = 500
#        tryStatus['message'] = "Unable to write/replace ~/.okta/config.properties"
#        
#        return tryStatus
#    
#    tryStatus['code'] = 200
#    tryStatus['message'] = "empty"
#    
#    return tryStatus
    
def clearConfig():

    def clearFile(inPath):

        tryStatus = {
            "code": '',
            "message": ''
        }

        if os.path.exists(inPath):
            try:
                os.remove(inPath)
            except:
                print("Unable to remove " + inPath)

                tryStatus['code'] = 500
                tryStatus['message'] = "Unable to remove " + inPath

                return tryStatus
        
            try:
                open(inPath , "w")
            except:
                print("Unable to create blank file " + inPath)

                tryStatus['code'] = 500
                tryStatus['message'] = "Unable to create blank file " + inPath

                return tryStatus
        else:
            try:
                open(inPath , "w")
            except:
                print('Unable to create blank ' + inPath)

                tryStatus['code'] = 500
                tryStatus['message'] = "Unable to create blank " + inPath
                
                return tryStatus
        
        tryStatus['code'] = 200
        tryStatus['message'] = "empty"

        return tryStatus

    tryStatus = {
        "code": "",
        "message": ""
    }

    awsBase = os.path.join( os.path.expanduser("~"), ".aws" )
    oktaBase = os.path.join( os.path.expanduser("~"), ".okta" )

    awsConfig = os.path.join( awsBase, "config" )
    awsCreds = os.path.join( awsBase, "credentials" )
    oktaProfiles = os.path.join( oktaBase, "profiles")
    oktaCurrentSession = os.path.join( oktaBase, ".current-session")

    aws_creds = clearFile(awsCreds)
    os.chmod(awsConfig, 0600)
    okta_profiles = clearFile(oktaProfiles)
    
    okta_session = {
        "code": "",
        "message": ""
    }

    try:
        os.remove(oktaCurrentSession)

    except:
        okta_session['code'] = 500
        okta_session['message'] = "Unable to remove " + oktaCurrentSession

    if aws_config['code'] == 200 and aws_creds['code'] == 200 and okta_profiles['code'] == 200 and okta_session['code'] == 200:
        tryStatus['code'] = 200
        tryStatus['message'] = "Empty"

        return tryStatus
    else:
        tryStatus['code'] = 500
        tryStatus['message'] = "Unable to reset session files"

        return tryStatus
        

#Depricated - functionality moved to bash_functions
#def configure():
#    
#    stats = clearConfig()
#
#    if stats['code'] == 200:
#        stats = createNewProfile()
#
#        if stats['code'] == 200:
#            exit(0)
#    
#    else:
#        print( str(stats['code']) + ": [" + stats['message'] + "]")
#        exit(5)

def logout():

    stats = clearConfig()

    if stats['code'] == 200:
        exit(3)

    else:
        print( str(stats['code']) + ": [" + stats['message'] + "]")
        exit(5)

def status():

    stats = checkExpired()

    if stats['code'] == 200:
        #exit not-expired
        exit(1)
    
    elif stats['code'] == 205:
        #exit expired
        exit(0)
    
    else:
        exit(5)

#Depricated
# Made if/else statements
#def paramSwitch(param):
#    switch = {
#        1: configure,
#        2: logout,
#        3: status
#    }
#    
#    func = switch.get(param, lambda: "No Value Provided")
#    print func()

# Command Param
param = sys.argv[1]

#functionality moved to bash_functions
#if param == "configure":
#    configure()

if param == "logout":
    logout()

elif param == "status":
    status()

else:
    print("No option found")