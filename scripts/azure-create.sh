#!/bin/bash

# Options
BRANCH="${1:-azure-dev}" # checkout branch $1

# Provider Config - update *-azure.sh files.
LOCATION=centralus

# Static Config - update *.sh files
NAME=learner
VM=essentials
PROJECT=CLASS-Essentials
GITHUB=github.internet2.edu
REPO="git@${GITHUB}:CLASS/${PROJECT}.git"

echo "=== azure-create.sh $PROJECT $BRANCH"
SUBSCRIPTION=$(az account show --query id -otsv)
RESOURCE_GROUP="rg-${VM}-dev"

echo "+++ creating resource group $RESOURCE_GROUP $SUBSCRIPTION"
az group create --resource-group $RESOURCE_GROUP --location $LOCATION

echo "+++ creating VM $VM"
# Ubuntu is "Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest"
# Debian is "Debian:debian-10:10:latest"
# Resource Group scope "subscriptions/$SUBSCRIPTION/resourceGroups/$RESOURCE_GROUP"
az vm create --resource-group $RESOURCE_GROUP --name $VM \
    --image Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest \
    --size Standard_D2_v4 \
    --storage-sku StandardSSD_LRS \
    --public-ip-sku Standard \
    --assign-identity \
    --scope "subscriptions/$SUBSCRIPTION/resourceGroups/$RESOURCE_GROUP" \
    --role Contributor \
    --admin-username $NAME

echo "+++ get IP for $VM"
IP=$(az vm show --name $VM --resource-group $RESOURCE_GROUP -d --query publicIps -otsv)

echo "+++ configure ~/.ssh/$VM.config"
cat > ~/.ssh/$VM.config <<EOF
Host essentials
    HostName $IP
    CheckHostIP=no
    ForwardAgent=yes
    User=$NAME
EOF

echo "+++ wait for boot and cloud-init ${VM} ${IP}"
ssh-keygen -R "$IP"
while ! ssh $NAME@$IP sudo cloud-init status --wait ; do
    sleep 1
done

echo "+++ configuring VM"
ssh -A $NAME@$IP <<EOF
echo '--- connected to $NAME@$IP'
sudo apt-get update
sudo apt-get install --yes azure-cli
az login --identity
sudo apt-get install --yes git python3-pip python3-venv bash-completion jq
ssh-keyscan ${GITHUB} > .ssh/known_hosts
git config --global color.ui auto
git config --global push.default simple
git config --global pull.ff only
git config --global user.name "$(git config user.name)"
git config --global user.email "$(git config user.email)"
git clone --branch $BRANCH $REPO
EOF

echo "+++ starting Jypter"
ssh $NAME@$IP -t -L 8080:localhost:8080 -L 8081:localhost:8081 "cd $PROJECT ; ./scripts/jupyter-lab.sh"

echo "+++ ssh command"
echo "ssh $NAME@$IP"
