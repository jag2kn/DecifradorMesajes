#!/bin/bash
for i in `seq 1 50`;
do
        wget -c https://primes.utm.edu/lists/small/millions/primes$i.zip -O Primos/primes$i.zip --no-check-certificate
done

find Primos -name '*.zip' -exec sh -c 'unzip -d Primos "$1"' _ {} \;
