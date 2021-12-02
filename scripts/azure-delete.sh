#!/bin/bash

# Provider Config - update *-azure.sh files.

# Static Config - update *.sh files
VM=essentials

echo "=== azure-delete.sh $PROJECT $BRANCH"
SUBSCRIPTION=$(az account show --query id -otsv)
RESOURCE_GROUP="rg-${VM}-dev"

az vm delete --resource-group $RESOURCE_GROUP --name $VM --yes
az group delete --resource-group $RESOURCE_GROUP --yes
