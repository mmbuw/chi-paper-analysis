#!/bin/bash
egrep 'https?://' *.txt | egrep -v 'youtube.com|books.google.com|doi.org|((doi|dl).acm.org)' 
