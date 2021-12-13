#!/bin/bash

gcloud asset search-all-resources --format='value(name)' |grep -vE '/(services|networks|routes|subnetworks|firewalls|serviceAccounts)/' | sort
