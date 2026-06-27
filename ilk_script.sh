echo ">"
read s1
echo ">"
read s2

top=$((s1+s2))
echo $top

echo ">"
read s1
echo ">"
read s2

carp=$((s1*s2))
echo $carp

while true; do
echo "hangi işlemden hesap makinesini kulanacaksınız"
echo "(+) (-) (*) (/)"
read a


if [ "$a" = "+" ] ; then
    echo "yapacagınız işleme göre sayi giriniz" 

read s1
read s2


toplam=$((s1+s2))
echo $toplam
fi

if [ "$a" = "-" ]; then

    echo "yapacagınız işleme göre sayi giriniz" 
read a1
read a2

eks=$((a1-a2))
echo $eks
    
fi

if [ "$a" = "*" ]; then
echo "işlem seçin"
read s1
read s2
times_sign=$((s1*s2))
echo $times_sign
fi

if [ "$a" = "/" ]; then
    echo "işlem seçdiginize göre sayi girin"
read s1 
read s2
slash=$((s1/s2))
echo $slash
fi

done