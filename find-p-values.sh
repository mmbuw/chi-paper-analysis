#!/bin/bash
LC_ALL=C egrep -io 'p *= *[0-9.]*' raw-text/*.txt | cut -d= -f2 | sed '/^\s*$/d' | LC_ALL=C sort -n > numbers.tmp
gnuplot p-values.gpl
