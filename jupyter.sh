#!/bin/bash

if [ -r ./local.sh ] ; then
  . ./local.sh
fi

echo "=== Install and run JupyterLab locally"

echo "+++ installing jupyter"
python3 -m venv .venv
. .venv/bin/activate

python3 -m pip install pip --upgrade
python3 -m pip install --upgrade jupyterlab

python3 -m pip install --upgrade bash_kernel
python3 -m bash_kernel.install

python3 -m pip install  --upgrade jupyterlab-spellchecker

jupyter-lab --port=8080
