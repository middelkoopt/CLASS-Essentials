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

## Google Cloud

Google Cloud development is split between the Cloud Shell episodes (04_intro_to_cli and 05_cli_storage) and the VM episodes.  Although the Cloud Shell episodes *should* work on the VM the prompt responses are slightly different.

The Jupyter notebook is forwarded to http://localhost:8080 and the preview on http://localhost:8081.  Use the links in the output of the script for Jupyter to login with the proper authentication key.

First setup the Google Cloud SDK and login to the account and project that you are going to use for development.

Verify the active project and account with
```bash
gcloud config configurations list
```

### Google Cloud Shell Development

The project is located in a hidden directory (`.essentials`) to hide the output from Jupyter and the students.  To start Cloud Shell run `./scripts/gcp-cloudshell.sh` to open the shell with the agent and ports 8081 and 8080 forwarded (Jupyter and preview respectively) and run the following commands to setup the Cloud Shell (this needs to be done only once).  Be sure to check the project and account values.

```bash
git clone git@github.internet2.edu:/CLASS/CLASS-Essentials.git .essentials
( cd .essentials/ ; git checkout -b gcp-dev --track origin/gcp-dev )

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

### Google Virtual Machine Development

If you manually create a with the instructions in the 06_running_analysis episode you must use the `us-west2-c` zone or delete it and let the script create it.

Workflow
  * Create and configure a new VM with `./scripts/gcp-create.sh`
  * Open Jupiter link shown in the output of the `gcp-create.sh` script.
  * Delete the vm when done (don't forget to commit and push!) with `./scripts/gcp-delete.sh`


## AWS

Expect that `aws` is installed locally.  A ssh-key named 'learner' is required to access the account.

## Azure

Expect that `az` is installed and configured locally.  It will utilize your ~/.ssh/id_rsa.pub key.

## Jupyter Book Tags

You can control the rendering of the book by adding "Tags" to the cells.  To access tags select a cell then click the gears box on the top right of the browser tab to open up the properties. 

Tags
  * To hide a cell add the tag `remove-cell`.

## Bugs and Fixes

The bash kernel and Python do not like the new "bracketed paste" mode of the new bash/readline.  To fix you can disable "bracketed paste" mode by doing
```bash
echo "set enable-bracketed-paste off" > ~/.inputrc
```
Note, this removes some copy/paste protection and recommended only for disposable VM's.

