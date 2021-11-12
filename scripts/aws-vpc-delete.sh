#!/bin/bash

# References:
# * https://docs.aws.amazon.com/vpc/latest/userguide/vpc-subnets-commands-example.html

# Settings in aws-create.sh
VM=essentials

echo "=== aws-vpc-delete.sh $VM"

VPC=$(aws ec2 describe-vpcs --filter "Name=tag:Name,Values=${VM}" --query "Vpcs[].VpcId" --output text)
SUBNET=$(aws ec2 describe-subnets --filter "Name=tag:Name,Values=${VM}" --query "Subnets[].SubnetId" --output text)
SG=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=${VM}" --query "SecurityGroups[].GroupId" --output text)
IG=$(aws ec2 describe-internet-gateways --filters "Name=tag:Name,Values=${VM}" --query "InternetGateways[].InternetGatewayId" --output text)
RT=$(aws ec2 describe-route-tables --filters "Name=tag:Name,Values=${VM}" --query "RouteTables[].RouteTableId" --output text)
echo "+++ networking: $VM,$VPC,$SUBNET,$SG,$IG,$RT."

if [ -n "${SG}" ] ; then
    echo "+++ terminating $VM $SG"
    aws ec2 delete-security-group --group-id $SG --no-cli-pager
fi

if [ -n "${SUBNET}" ] ; then
    echo "+++ terminating $VM $SUBNET"
    aws ec2 delete-subnet --subnet-id $SUBNET --no-cli-pager
fi

if [ -n "${RT}" ] ; then
    echo "+++ terminating $VM $RT"
    aws ec2 delete-route-table --route-table-id $RT --no-cli-pager
fi

if [ -n "${IG}" ] ; then
    echo "+++ terminating $VM $IG"
    aws ec2 detach-internet-gateway --internet-gateway-id $IG --vpc-id $VPC --no-cli-pager
    aws ec2 delete-internet-gateway --internet-gateway-id $IG --no-cli-pager
fi

if [ -n "${VPC}" ] ; then
    echo "+++ terminating $VM $VPC"
    aws ec2 delete-vpc --vpc-id $VPC --no-cli-pager
fi

