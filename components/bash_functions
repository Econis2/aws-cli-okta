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