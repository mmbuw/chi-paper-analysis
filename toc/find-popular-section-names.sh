#!/bin/bash
cat $1 | sort -fi | uniq -ci | sort -n -k1
