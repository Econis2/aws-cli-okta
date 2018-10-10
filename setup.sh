#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/simple/components/bash_functions --output bash_functions)

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/simple/components/main.py --output main.py)

sudo chmod +x main.py

exit 0
