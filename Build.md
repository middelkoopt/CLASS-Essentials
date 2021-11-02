# Book Build Instructions

To build the book for local development run
```
./build-book.sh
```

To copy results to the `gh-pages` branch and push run
```
./push-book.sh
```

## GCP

Using Jupyter launched from a remote Visual Code Studio session inside GCP Cloud-Shell requires some local settings stored in `local.sh`, use the following as a template replacing the project and email with the proper vaules:
```
gcloud config set account student31@class.internet2.edu
export GOOGLE_CLOUD_PROJECT=just-armor-301114
export DEVSHELL_PROJECT_ID=$GOOGLE_CLOUD_PROJECT
gcloud config set project $GOOGLE_CLOUD_PROJECT
```
