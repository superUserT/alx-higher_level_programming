#!/bin/bash
#get body size of a request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
