# Book Build Instructions

## Building and Publishing the Book

All the build scripts must be run from the top of the repository.

To build the book for local development run
```
./scripts/build-book.sh
```
This will create a local Python venv environment in `.venv/`, install Jupyter Book and dependcies and build it. The Jupyter Book content is located in `content/`.  The build process does not reevaluate the Jupyter Notbooks due to the complexity of building across all the providers in a single run.  Development for each provider should be done in a branch (`gcp-dev`, `aws-dev` and `azure-dev` branch).

The resulting book is a set of static html pages found in [`content/_build/html/`](content/_build/html/).  If development is being done remotly these pages can be exposed on port 8080 by running.
```
./scripts/preview-book.html
```
This runs a local http server enabling the "preview" feature of the Cloud Shell to view the rendered book. Visual Cloud Studio, when used in a remote shell, will also redirect this port to the local developmen machine and the previw can be found on [localhost:8080](http://localhost:8080).

To use GitHub pages to preview or publish run
```
./scripts/push-book.sh
```
THis will copy rendered content to the `gh-pages` branch and push to the `private` remote.  

To publish to the `gh-pages` of the `origin` (or other) remote run.
```
./scripts/push-book.sh origin
```

This copies the contents of `content/_build/html/` to `docs/` so GitHub Pages will render the document.  GitHub pages should be set to the `gh-pages` and `docs/` folder.  The script pushes a new branch overwriting the old branch and will not track changes.


## GCP

Using Jupyter launched from a remote Visual Code Studio session inside GCP Cloud-Shell requires some local settings stored in `local.sh`, use the following as a template replacing the project and email with the proper vaules:
```
gcloud config set account student31@class.internet2.edu
export GOOGLE_CLOUD_PROJECT=just-armor-301114
export DEVSHELL_PROJECT_ID=$GOOGLE_CLOUD_PROJECT
gcloud config set project $GOOGLE_CLOUD_PROJECT
```
