I crawled the papers with pubCrawler2 from my pubMunch collection.

I originally thought about grepping the filtText.tsv file but almost all files 
had matches to the regex used for the HCI papers '(open(-| )?source)|(source(-| )?code)|supplement'

So instead I opened all PDFs and searched manually. The input pdf files are in the directory "pdf/"
the manual annotation are in the file manualAnnotation.tsv. When the source code is clearly there, 
it's annotated with "OK", when a program is freely available and it looks like the source code is 
there, it's annotated with "OK?", otherwise "NO".

Max
