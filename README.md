# aws-cli-okta
Description:
-
python scripts for adding multi account and auto authentication support for the [okta-aws-cli-assume-role](https://github.com/oktadeveloper/okta-aws-cli-assume-role)

Requirements:
-

 - Install the okta-aws-cli-assume-role tool from: https://github.com/oktadeveloper/okta-aws-cli-assume-role		 
   - __Leave config blank__
 - Install python 2.7

  Installation:
  -
  
1) Open a terminal window 

2) Run this command ```/bin/bash <(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/setup.sh)```

3) OSX / Linux:
    - Run the python script ```/Users/[username]/.okta/newProfile.py```
    
    - This is where you need your configuration information 
    - All questions must have valid configs (no nulls or blanks)
    
Usage:
-
```aws-okta [profileName] [aws command]```
##### Example: 
```aws-okta default sts get-caller-identity```
