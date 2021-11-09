#!/bin/bash

## User settings in gcp-dev.sh
VM=essentials
ZONE=us-west2-c

gcloud --quiet compute instances delete --zone=$ZONE $VM
