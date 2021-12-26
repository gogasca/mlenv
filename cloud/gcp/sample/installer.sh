#!/bin/bash

jupyter labextension install @jupyterlab/git
pip install jupyterlab-git
jupyter server extension enable --py jupyterlab_git