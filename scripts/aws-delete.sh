#!/bin/bash

## Settings copied from aws-create.sh
VM=essentials

echo "=== aws-delete.sh $VM"

INSTANCE=$(aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running' 'Name=tag:Name,Values=essentials' --query "Reservations[*].Instances[*].InstanceId" --output text --no-cli-pager)

if [ -n "${INSTANCE}" ] ; then
    echo "+++ terminating $VM $INSTANCE"
    aws ec2 terminate-instances --instance-id $INSTANCE --no-cli-pager
fi
