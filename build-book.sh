#!/bin/bash

python3 -m venv .venv

. .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -U jupyter-book sphinx_inline_tabs

jupyter-book build content/
