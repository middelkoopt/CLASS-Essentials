#!/bin/bash

# Provider Config - update *-azure.sh files.

# Static Config - update *.sh files
VM=essentials

RESOURCE_GROUP=$VM
az vm delete --resource-group $RESOURCE_GROUP --name $VM --yes
#az group delete --resource-group $RESOURCE_GROUP --yes
