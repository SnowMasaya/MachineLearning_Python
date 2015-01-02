#/bin/env sh

cut -d , -f 2-2 KEN_ALL_nkf_w.CSV | sort -r | uniq -c 
sort -r -k2,2 KEN_ALL_nkf_w.CSV
