#!/bin/bash

if swiftc main.swift; then
    ./main < input.txt
else
    exit 1
fi
