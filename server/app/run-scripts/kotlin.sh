#!/bin/bash

kotlinc main.kt -include-runtime -d main.jar

kotlin main.jar 