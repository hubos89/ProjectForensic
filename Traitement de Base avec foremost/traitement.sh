#!/bin/bash
echo "debut zip \n" >> $1/avance.txt
foremost -t zip -i /dev/sda -o $1/zip/zip
echo "zip fini debut xlsx \n" >> $1/avance.txt
foremost -t xlsx -i /dev/sda -o $1/xlsx
echo "xlsx fini debut xls \n" >> $1/avance.txt
foremost -t xls -i /dev/sda -o $1/xls
echo "xls fini debut wmv \n" >> $1/avance.txt
foremost -t wmv -i /dev/sda -o $1/wmv
echo "wmv fini debut wav \n" >> /$1/avance.txt
foremost -t wav -i /dev/sda -o $1/vis
echo "wav fini debut sxw \n" >> $1/avance.txt
foremost -t sxw -i /dev/sda -o $1/sxw
echo "sxw fini debut rif \n" >> $1/avance.txt
foremost -t rif -i /dev/sda -o $1/rif
echo "rif fini debut rar \n" >> $1/avance.txt
foremost -t rar -i /dev/sda -o $1/rar/rar
echo "rar fini debut pptx \n" >> $1/avance.txt
foremost -t pptx -i /dev/sda -o $1/pptx
echo "pptx fini debut ppt \n" >> $1/avance.txt
foremost -t ppt -i /dev/sda -o $1/ppt
echo "ppt fini debut png \n" >> $1/avance.txt
foremost -t png -i /dev/sda -o $1/png
echo "png fini debut pdf \n" >> $1/avance.txt
foremost -t pdf -i /dev/sda -o $1/pdf
echo "pdf fini debut ole \n" >> $1/avance.txt
foremost -t ole -i /dev/sda -o $1/ole
echo "ole fini debut mpg \n" >> $1/avance.txt
foremost -t mpg -i /dev/sda -o $1/mpg
echo "mpg fini debut mp4 \n" >> $1/avance.txt
foremost -t mp4 -i /dev/sda -o $1/mp4
echo "mp4 fini debut mov \n" >> $1/avance.txt
foremost -t mov -i /dev/sda -o $1/mov
echo "mov fini debut jpg \n" >> $1/avance.txt
foremost -t jpg -i /dev/sda -o $1/jpg
echo "jpg fini debut htm \n" >> $1/avance.txt
foremost -t htm -i /dev/sda -o $1/htm
echo "htm fini debut gif \n" >> $1/avance.txt
foremost -t gif -i /dev/sda -o $1/gif
echo "gif fini debut exe \n" >> $1/avance.txt
foremost -t exe -i /dev/sda -o $1/exe
echo "exe fini debut docx \n" >> $1/avance.txt
foremost -t docx -i /dev/sda -o $1/docx
echo "docx fini debut doc \n" >> $1/avance.txt
foremost -t doc -i /dev/sda -o $1/doc
echo "doc fini debut bmp \n" >> $1/avance.txt
foremost -t bmp -i /dev/sda -o $1/bmp
echo "bmp fini debut avi \n" >> $1/avance.txt
foremost -t avi -i /dev/sda -o $1/avi
echo "avi fini \n" >> $1/avance.txt
echo "FIN TRAITEMENT \n" >> $1/avance.txt
echo "END OF PROCESS"
