#!/bin/bash

## Settings copied from aws-create.sh
VM=essentials

## Create a simple VPC.
echo "===  aws-vpc-create.sh"

echo "+++ creating '$VM' networking allowing internal traffic and external ssh and ICMP access"
aws ec2 create-vpc \
    --tag-specifications "ResourceType=vpc,Tags=[{Key=Name,Value=$VM}]" \
    --cidr-block 10.0.0.0/16 \
    --no-cli-pager
VPC=$(aws ec2 describe-vpcs --filter "Name=tag:Name,Values=${VM}" --query "Vpcs[].VpcId" --output text)
echo "+++ created VPC $VPC"

aws ec2 create-subnet \
    --tag-specifications "ResourceType=subnet,Tags=[{Key=Name,Value=$VM}]" \
    --vpc-id $VPC \
    --cidr-block 10.0.0.0/16 \
    --no-cli-pager
SUBNET=$(aws ec2 describe-subnets --filter "Name=tag:Name,Values=${VM}" --query "Subnets[].SubnetId" --output text)
echo "+++ created subnet $SUBNET"

aws ec2 create-security-group \
    --group-name $VM \
    --description $VM \
    --vpc-id $VPC \
    --no-cli-pager
SG=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=${VM}" --query "SecurityGroups[].GroupId" --output text)
echo "+++ created security group $SG"

# SSH, ICMP
aws ec2 authorize-security-group-ingress \
    --group-id $SG \
    --protocol=tcp --port=22 --cidr 0.0.0.0/0 \
    --no-cli-pager
aws ec2 authorize-security-group-ingress \
    --group-id $SG \
    --protocol=icmp --port=-1 --cidr 0.0.0.0/0 \
    --no-cli-pager

aws ec2 create-internet-gateway \
    --tag-specifications "ResourceType=internet-gateway,Tags=[{Key=Name,Value=$VM}]" \
    --no-cli-pager
IG=$(aws ec2 describe-internet-gateways --filters "Name=tag:Name,Values=${VM}" --query "InternetGateways[].InternetGatewayId" --output text)
echo "+++ created internet gateway $IG"

aws ec2 attach-internet-gateway \
    --internet-gateway-id $IG \
    --vpc-id $VPC \
    --no-cli-pager

aws ec2 create-route-table \
    --tag-specifications "ResourceType=route-table,Tags=[{Key=Name,Value=$VM}]" \
    --vpc-id $VPC \
    --no-cli-pager
RT=$(aws ec2 describe-route-tables --filters "Name=tag:Name,Values=${VM}" --query "RouteTables[].RouteTableId" --output text)
echo "+++ created route table $RT"

aws ec2 create-route \
    --route-table-id $RT \
    --gateway-id $IG \
    --destination-cidr-block 0.0.0.0/0 \
    --no-cli-pager

aws ec2 associate-route-table \
    --route-table-id $RT \
    --subnet-id $SUBNET \
    --no-cli-pager

aws ec2 modify-subnet-attribute \
    --subnet-id $SUBNET \
    --map-public-ip-on-launch \
    --no-cli-pager

echo "+++ networking: $VM,$VPC,$SUBNET,$SG,$IG,$RT."
