
echo "sayi1 girin:"
read a
echo "sayi2 girin:"
read b
echo " islem sec: 1-and 2-or 3-not"
read k
if [ $k -eq '1' ];then
	echo $((a&&b))
elif [ $k -eq '2' ];then
	echo $((a||b))
elif [ $k -eq '3' ];then
	echo " islem sec: 1-and 2-or 3-sayi1 4-sayi2"
	read kk
	if [ $kk -eq '1' ];then
		echo $((!(a&&b)))
	elif [ $kk -eq '2' ];then
		echo $((!(a||b)))
	elif [ $kk -eq '3' ];then
		echo $((!(a)))
	elif [ $kk -eq '4' ];then
		echo $((!(b)))
	fi
fi
