for link in $(cat links) ; do

	file=${link#http://dl.acm.org/}
	echo $link $file

	wget -U Mozilla $link
	sleep $(($RANDOM/400))

	pdf=$(grep FullTextPDF $file | cut -d'"' -f6)
	echo $pdf
	wget -U Mozilla http://dl.acm.org/$pdf
	sleep $(($RANDOM/400))

done
