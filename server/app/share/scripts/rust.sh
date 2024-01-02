#!/bin/bash

if rustc main.rs; then
    ./main < input.txt
else
    exit 1
fi
