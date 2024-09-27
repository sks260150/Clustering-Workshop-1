#!/bin/bash

ext_key=".key"
ext_csr=".csr"
ext_crt=".crt"
ext_pfx=".pfx"


if [ $# -eq 0 ]; then
	echo -e "Usage: $0 <filename>\n"
	exit 1
else
	echo -e "Generating certificate files with the name: $1\n\n"
	echo -e "Generating Key: $1$ext_key"
	openssl genrsa -out "$1$ext_key" 4096
	echo -e "\n\nGenerating Certificate Request: $1$ext_csr"
	openssl req -new -key "$1$ext_key" -out "$1$ext_csr"
	echo -e "\n\nGenerating Auto Signed Certificate: $1$ext_crt"
	openssl x509 -req -days 3650 -in "$1$ext_csr" -signkey "$1$ext_key" -out "$1$ext_crt"
	echo -e "\n\nExporting Keys in .pfx format: $1$ext_pfx"
	openssl pkcs12 -keypbe PBE-SHA1-3DES -certpbe PBE-SHA1-3DES -export -in "$1$ext_crt" -inkey "$1$ext_key" -out "$1$ext_pfx" -name "$1"
	echo -e "\n\nCertificate Generation Complete"
	echo -e "$(ls -al | grep "$1")"
fi