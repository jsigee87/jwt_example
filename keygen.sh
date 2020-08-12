#!/bin/bash

if [ -z $1 ];
then
    echo "Usage: bash keygen.sh <keyname>\nNote <keyname> should end in .key"
    exit 1
fi

# Pass in name of key
ssh-keygen -t rsa -b 4096 -P "" -f $1

# Reformat public key to PEM
openssl rsa -in $1 -pubout -outform PEM -out $1.pub
