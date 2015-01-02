#/bin/env sh

cut -d , -f -1 KEN_ALL_nkf_w.CSV | sort | uniq | wc 

