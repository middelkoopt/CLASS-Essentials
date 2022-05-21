#!/bin/bash

if [ -r ./local.sh ] ; then
  . ./local.sh
fi

echo "=== jupyterlab.sh Install and run JupyterLab locally"

echo "+++ installing jupyter"
python3 -m venv .venv
. .venv/bin/activate

ln -sfv /usr/lib/python3/dist-packages .venv/lib/python3.*/ # simulate VM behavior for apt-get install python3-rasterio

python3 -m pip install pip --upgrade
python3 -m pip install --upgrade jupyterlab

python3 -m pip install --upgrade bash_kernel
python3 -m bash_kernel.install

python3 -m pip install --upgrade jupyterlab-spellchecker

echo "+++ run jupyter"
jupyter-lab --port=8081
