#!/bin/sh -l

echo "EXECUTING PYTHON SCRIPT..."
python3 /main.py

echo "ls -lah"
ls -lah

echo "pwd"
pwd

echo "ls -lah /github/workspace/.github/actions/action_1.2/.githab"
ls -lah /github/workspace
