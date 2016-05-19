#!/bin/bash
for file in *.pdf ; do echo $file ; pdftotext -layout -nopgbrk -raw $file ; done
