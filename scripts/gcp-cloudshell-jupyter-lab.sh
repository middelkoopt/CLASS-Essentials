#!/bin/bash

gcloud cloud-shell ssh --authorize-session --ssh-flag=-A --ssh-flag=-L8080:localhost:8080 --ssh-flag=-L8081:localhost:8081 \
    --command="cd .essentials && ./scripts/jupyter-lab.sh"
