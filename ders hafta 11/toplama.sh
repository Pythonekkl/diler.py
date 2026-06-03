echo "Sayi1 Gir"
read sayi1
echo "Sayi2 Gir"
read sayi2
echo "islem türü gir + - * /"
read islem
if [ "$islem" -eq 1 ]; then
	sayi3=$((sayi1+sayi2))
	echo "$sayi3"    
elif [ "$islem" -eq 2 ]; then
	sayi3=$((sayi1-sayi2))
	echo "$sayi3"
elif [ "$islem" -eq 3 ]; then
	sayi3=$((sayi1*sayi2))
	echo "$sayi3"
elif [ "$islem" -eq 4 ]; then
	sayi3=$((sayi1/sayi2))
	echo "$sayi3"
else
	echo "Hatalı operator"
fi
