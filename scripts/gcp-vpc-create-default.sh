#!/bin/bash

## Create a default VPC similar to the GCP default.
echo "===  gcp-vpc-create-default.sh"

echo "+++ creating the default VCP network allowing internal traffic and external ssh and ICMP access"
gcloud compute networks create default
gcloud compute firewall-rules create default-allow-internal --network default --allow all --source-ranges=10.128.0.0/9
gcloud compute firewall-rules create default-allow-external --network default --allow tcp:22,icmp
