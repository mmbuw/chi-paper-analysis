for line in $(cat $1 | grep ea | cut -d/ -f7- | cut -d'&' -f1-2 | sort -u) ; do
	target=$(echo $line | cut -d'?' -f1)
	id=$(echo $line | cut -d= -f3)
	src=$(find . -name "*$id*")
	echo $target $id $src
	mv -n $src $target
done
