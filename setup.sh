#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

if [ -f bash_functions ]; then
    sudo rm bash_functions
fi

$(https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/bash_functions.sh --output bash_functions.sh)

mv bash_functions.sh bash_functions

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/main.py --output main.py)

sudo chmod +x main.py

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/newProfile.py --output newProfile.py)

sudo chmod +x newProfile.py

echo "Creating required Directories"

mkdir awsProfiles

exit 0
