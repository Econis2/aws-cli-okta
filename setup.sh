#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

sudo rm $oktaLocal/bash_functions

$(https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/bash_functions.sh --output $oktaLocal/bash_functions)

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/main.py --output $oktaLocal/main.py)

sudo chmod +x $oktaLocal/main.py

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/newProfile.py --output $oktaLocal/newProfile.py)

sudo chmod +x $oktaLocal/newProfile.py

echo "Creating required Directories"

mkdir awsProfiles

exit 0
