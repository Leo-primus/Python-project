#!/bin/bash
which_script=1
if [ $which_script -eq 1 ]; then
    python3 ./src/email_validator.py
elif [ $which_script -eq 2 ]; then
    python3 ./src/email_validator_optimized.py
elif [ $which_script -eq 3 ]; then
    python3 ./src/create_fake_emails.py
elif [ $which_script -eq 4 ]; then
    python3 ./src/create_fake_emails_optimize.py
elif [ $which_script -eq 5 ]; then
    python3 ./src/calculator.py
fi
