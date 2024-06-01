#!/bin/bash

# Activate the virtual environment
source myenv/Scripts/activate

# Run the ML pipeline
python src/mlp.py

# Deactivate the virtual environment
deactivate
