#!/bin/bash
egrep -C1 -i supplement $1 | grep -i material | cut -d. -f1 | sort -u | wc
