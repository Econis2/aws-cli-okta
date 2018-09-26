#!/usr/python

import os
import sys

pathOkta = os.path.join( os.path.expanduser("~"), ".okta")
awsConfigFolder = os.path.join( pathOkta, "awsProfiles")

if not os.path.isdir(awsConfigFolder):
    print ("Creating awsProfiles Directory")
    try:
        os.makedirs(awsConfigFolder)
    except:
        print ("Error Creating awsProfiles Directory")
        exit(5)

numOfProfiles = input("How many profiles do you want to create?[Enter a number]: ")

x = 1

while x <= numOfProfiles:
    print("\n")
    profileName = raw_input("Enter the Profile Name: ")
    oktaOrg = raw_input("Enter the URL for the Okta Org: ")
    oktaAppUrl = raw_input("Enter the APP URL for the AWS Okta App: ")
    oktaUsername = raw_input("Enter the Okta username: ")
    awsRegion = raw_input("Enter the AWS region: ")

    profileName = profileName + ".config"
    oktaOrg = oktaOrg + "\n"
    oktaAppUrl = oktaAppUrl + "\n"
    oktaUsername = oktaUsername + "\n"
    awsRegion = awsRegion + "\n"

    attrArray = [oktaOrg,oktaAppUrl,oktaUsername,awsRegion]

    profilePath = os.path.join( awsConfigFolder, profileName)

    try:
        with open(profilePath, "w") as file:
            file.writelines(attrArray)
    except:
        print("Something went wrong")

    x = x + 1