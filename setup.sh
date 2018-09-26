#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/main.py --output $oktaLocal/main.py

curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/newProfile.py --ouytput $oktaLocal/newProfile.py

echo "Creating required Directories"

mkdir "$oktaLLocal\awsProfiles"

exit 0