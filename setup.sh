#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/main.py --output $oktaLocal/main.py)

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/newProfile.py --output $oktaLocal/newProfile.py)

echo "Creating required Directories"

mkdir awsProfiles

exit 0