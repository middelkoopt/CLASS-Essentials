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

## VM Development Setup

Have your ~/.ssh/config source the file the *-create.sh scripts create. This is a one-time per machine setup.

```
echo "include ~/.ssh/essentials.config" >> ~/.ssh/config
```

Verify your name and email are correct (locally) as they are copied over to the VM
```
git config user.name
git config user.email
```

## GCP

Checkout the project so it is not seen by the students.  Run `./scripts/gcp-cloudshell.sh` to open the shell with the agent and ports 8080 and 8081 forwarded and run the following commands (onetime setup).  Be sure to check the project and account values.

```bash
git clone git@github.internet2.edu:/CLASS/CLASS-Essentials.git .essentials
cd .essentials/
git checkout -b gcp-dev --track origin/gcp-dev

ACCOUNT=learner@class.internet2.edu
PROJECT=essentials-learner
cat > .essentials/local.sh <<EOF
gcloud config set account $ACCOUNT
export GOOGLE_CLOUD_PROJECT=$PROJECT
export DEVSHELL_PROJECT_ID=$PROJECT
gcloud config set project $PROJECT
EOF
```

Then run the following from your local machine (Make sure to shutdown from the web-gui as ctrl-c is not managed properly):
```bash
./scripts/gcp-cloudshell-jupyter-lab.sh
```
## AWS

Expect that `aws` is installed locally.  A ssh-key named 'learner' is required to access the account.

## Azure

Expect that `az` is installed and configured locally.  It will utilize your ~/.ssh/id_rsa.pub key.
