#!/bin/bash

# Define the new sudoers file and entry
SUDOERS_FILE="/etc/sudoers.d/custom_user"
NEW_ENTRY="username ALL=(ALL) NOPASSWD:ALL"

# Create the file with the new entry
echo "$NEW_ENTRY" > "$SUDOERS_FILE"

# Set the correct permissions
chmod 0440 "$SUDOERS_FILE"

# Validate the sudoers file
visudo -cf "$SUDOERS_FILE"
if [ $? -eq 0 ]; then
    echo "Sudoers entry added successfully in $SUDOERS_FILE."
else
    echo "Failed to validate $SUDOERS_FILE. No changes applied."
    rm -f "$SUDOERS_FILE"
fi
