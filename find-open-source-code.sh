#!/bin/bash
egrep -i '(open(-| )?source)|(source(-| )?code)' raw-text/*.txt | cut -d: -f1 | sort -u
