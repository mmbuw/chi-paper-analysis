#!/bin/bash
egrep -i '(open(-| )?source)|(source(-| )?code)|supplement' raw-text/*.txt | cut -d: -f1 | sort -u
#egrep -l -z -i '(open(-|[[:space:]])?source)|(source(-|[[:space:]])?code)' raw-text/*.txt | cut -d: -f1 | sort -u
