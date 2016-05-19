#!/bin/bash
egrep 'https?://' raw-text/*.txt | egrep -v 'youtube.com|books.google.com|doi.org|((doi|dl).acm.org)' 
