#!/bin/bash

echo "Getting Required Files"

username=$(whoami)
oktaLocal="/Users/$username/.okta"

cd $oktaLocal

cat > $oktaLocal/bash_functions <<-EOM
#!bin/bash

function aws-okta {

    paramFirst=$0

    user=$(whoami)
    #Sets the account profile determines Account Status
    result=$(python /Users/$user/.okta/main.py $@)

    #Renew Token
    if (( $? == 0 )); then
        withokta aws $@
    
    #Use Existing
    elif (( $? == 1 )); then
        aws --profile $@
    fi

}
EOM

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/main.py --output main.py)

sudo chmod +x main.py

$(curl https://raw.githubusercontent.com/Econis2/aws-cli-okta/master/components/newProfile.py --output newProfile.py)

sudo chmod +x newProfile.py

echo "Creating required Directories"

mkdir awsProfiles

exit 0
