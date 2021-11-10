#!/bin/bash

# Options
BRANCH="${1:-gcp-dev}" # checkout branch $1

# Static Config - update gcp-*.sh files
NAME=learner
VM=essentials
ZONE=us-west2-c
PROJECT=CLASS-Essentials
GITHUB=github.internet2.edu
REPO="git@${GITHUB}:CLASS/${PROJECT}.git"

echo "=== gcp-dev.sh $PROJECT $BRANCH"

echo "+++ creating VM"
gcloud compute instances create --zone=$ZONE $VM --machine-type=e2-highcpu-4 --preemptible


echo "+++ wait for boot"
while ! gcloud compute ssh --zone=$ZONE $NAME@$VM --command='hostname' ; do
    sleep 1
done

echo "+++ configuring VM"

gcloud compute ssh --zone=$ZONE $NAME@$VM --ssh-flag='-A' <<EOF
sudo apt install --yes git python3-pip python3-venv bash-completion
ssh-keyscan ${GITHUB} > .ssh/known_hosts
git config --global color.ui auto
git config --global push.default simple
git config --global pull.ff only
git config --global user.name "$(git config user.name)"
git config --global user.email "$(git config user.name)"
git clone --branch $BRANCH $REPO
EOF

echo "+++ configure local ssh"
gcloud compute config-ssh

echo "+++ starting Jypter"
gcloud compute ssh --zone=$ZONE $NAME@$VM --ssh-flag='-t -L 8080:localhost:8080 -L 8081:localhost:8081' --command="cd $PROJECT ; ./scripts/jupyter-lab.sh"
