# aws-cli-okta
python scripts for adding multi account and auto authentication support for the okta-aws-cli-assume-role

---

##Instructions:

1) Install all resources from https://github.com/oktadeveloper/okta-aws-cli-assume-role
  ** Do not configure any properties after install **
  
2) Open a terminal window and run this command ```/bin/bash <(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/setup.sh)```
This creates the required directories and downloads the needed python scripts located in the components section of this repo.

3) OSX / Linux:
    Run the python script /Users/[username]/.okta/newProfile.py
    
    This is where you need your configuration information 
    All questions must have valid configs (no nulls or blanks)
 
4) usage: ```aws-okta [profileName] [aws command]```
