#!/bin/bash

# Function to locate and modify the neofetch config
modify_neofetch_config() {
    DEFAULT_CONFIG_PATH="${HOME}/.config/neofetch/config.conf"
    echo "Searching for Neofetch config file..."

    # Find the actual location of the neofetch config file
    CONFIG_PATH=$(find ${HOME} -type f -name "config.conf" 2>/dev/null | grep -m 1 'neofetch')

    if [[ -z "$CONFIG_PATH" ]]; then
        echo "Neofetch config file not found. Please ensure Neofetch is installed."
        exit 1
    else
        echo "Neofetch config file found at: $CONFIG_PATH"
    fi

    # Check if the config file is writable
    if [[ -w "$CONFIG_PATH" ]]; then
        sed -i 's/# info "Disk"/info "Disk"/' "$CONFIG_PATH"
        sed -i 's/# info "Local IP"/info "Local IP"/' "$CONFIG_PATH"
        sed -i 's/# info "Public IP"/info "Public IP"/' "$CONFIG_PATH"
        sed -i 's/# info "Users"/info "Users"/' "$CONFIG_PATH"
        echo "Neofetch config modified successfully."
    else
        echo "Insufficient permissions to modify the neofetch config."
        exit 1
    fi
}

# Function to display neofetch on SSH login
display_neofetch_ssh() {
    # Check if .bashrc is writable
    if [[ -w "${HOME}/.bashrc" ]]; then
        echo 'neofetch' >> "${HOME}/.bashrc"
        echo "Neofetch will be displayed on SSH login."
    else
        echo "Insufficient permissions to modify .bashrc for SSH login display."
        exit 1
    fi
}

# Main script execution
modify_neofetch_config
display_neofetch_ssh