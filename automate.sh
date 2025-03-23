#!/bin/bash

# Run the python script
if [ "$1" == "test_db" ]; then
    # Move to the db directory
    cd "$(dirname "$0")/db"
    python3 main.py
elif [ "$1" == "test_backend" ]; then
    # Move to the backend directory
    cd "$(dirname "$0")/backend"
    uvicorn main:app --reload
else
    echo "Invalid argument. Please use 'test_db' or 'test_backend'."
    exit 1
fi

exit 0