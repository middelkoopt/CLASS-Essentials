#!/bin/bash

## Clean VM in prep for (re)running VM work

echo "=== gcp-clean-vm.sh"

## Cleanup for 06_running_analysis
sudo apt remove git --yes
rm -rf ~/CLASS-Examples

