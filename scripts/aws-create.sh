#!/bin/bash

# Options
BRANCH="${1:-aws-dev}" # checkout branch $1

# Provider Config - update aws-*.sh files.

# Static Config - update *.sh files
NAME=learner
VM=essentials
PROJECT=CLASS-Essentials
GITHUB=github.internet2.edu
REPO="git@${GITHUB}:CLASS/${PROJECT}.git"

echo "=== aws-create.sh $PROJECT $BRANCH"

VPC=$(aws ec2 describe-vpcs --filter "Name=tag:Name,Values=${VM}" --query "Vpcs[].VpcId" --output text)
SUBNET=$(aws ec2 describe-subnets --filter "Name=tag:Name,Values=${VM}" --query "Subnets[].SubnetId" --output text)
SG=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=${VM}" --query "SecurityGroups[].GroupId" --output text)

echo "+++ networking: $VM $VPC $SUBNET $SG"
if [ -z "${VPC}" -o -z "${SUBNET}" -o -z "${SG}" ] ; then
    echo "--- '${VM}' networking does not exist.  Use 'aws-vpc-create.sh' to create"
    exit 1
fi

IP=$(aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running' 'Name=tag:Name,Values=essentials' --query "Reservations[*].Instances[*].PublicIpAddress" --output text --no-cli-pager)
if [ -z "${IP}" ] ; then
    echo "+++ creating VM"
    aws ec2 run-instances \
        --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$VM}]" \
        --image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
        --instance-type m6i.large \
        --subnet-id $SUBNET \
        --security-group-ids $SG \
        --key-name $NAME \
        --no-cli-pager
fi

while [ -z ${IP:=$(aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running' "Name=tag:Name,Values=${VM}" --query 'Reservations[*].Instances[*].PublicIpAddress' --output text --no-cli-pager)} ] ; do
    echo "+++ waiting for IP"
    sleep 1
done

echo "+++ wait for boot and cloud-init ${VM} ${IP}"
ssh-keygen -R $IP
while ! ssh ec2-user@$IP sudo cloud-init status --wait ; do
    sleep 1
done

echo "+++ configuring VM"

ssh ec2-user@$IP -A <<EOF
sudo ln -s /home/ec2-user /home/$NAME
sudo yum install -y git python3-pip python3-venv bash-completion
ssh-keyscan ${GITHUB} > .ssh/known_hosts
git config --global color.ui auto
git config --global push.default simple
git config --global pull.ff only
git config --global user.name "$(git config user.name)"
git config --global user.email "$(git config user.email)"
git clone --branch $BRANCH $REPO
EOF

echo "+++ configure ~/.ssh/$VM.config"
cat > ~/.ssh/$VM.config <<EOF
Host essentials
    HostName $IP
    CheckHostIP=no
    ForwardAgent=yes
    User=ec2-user
EOF

echo "+++ starting Jypter"
ssh ec2-user@$IP -t -L 8080:localhost:8080 -L 8081:localhost:8081 "cd $PROJECT ; ./scripts/jupyter-lab.sh"

echo "+++ ssh command"
echo "ssh ec2-user@$IP"
