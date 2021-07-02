#!/bin/bash
COMPRESS_SCRIPT="compress.py"
CURRENT_DIR=$(pwd)

if [ ! -f "$COMPRESS_SCRIPT" ]; then # check if the compress script file is found
    echo -e "Can not find the ${COMPRESS_SCRIPT} script"
    exit 1 # it will exit if the compress script file is not found
fi

# checks if the script is executed as root
if [ "$EUID" -ne 0 ]; then # if not it will tell the user and exit
    echo -e "Please run the script as root!"
    echo -e "do: sudo bash $0"
    exit 1
fi

chmod +x $CURRENT_DIR/$COMPRESS_SCRIPT

ln -svf $CURRENT_DIR/$COMPRESS_SCRIPT /bin/$COMPRESS_SCRIPT

echo "You can now use the script anywhere with: ${COMPRESS_SCRIPT}"
