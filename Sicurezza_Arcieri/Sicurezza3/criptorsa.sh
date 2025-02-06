if [ "$1" == "1" ]
then
    echo "Comando cripta file lungo"
    openssl rand -out password.dat 32
    openssl enc -e -in $2 -out $2.enc -kfile password.dat -aes256
    openssl pkeyult -encrypt -inkey $3 -pubin -in password.dat -out password.dat.enc
    zip $2.zip password.dat.enc $2.enc
    rm password.dat $2.enc password.dat.enc
fi
if [ "$1" == "2" ]
then
    echo "Comando decripta file lungo"
    unzip $2
fi