s/<img src="\(.*\)" title="\(.*\)" width="\(.*\)" height="\(.*\)" \/>/\![\2](\1){ width=\3 height=\4}/g
s/<img src="\(.*\)" title="\(.*\)" width="\(.*\)" \/>/\![\2](\1){ width=\3}/g
s/<img src="\(.*\)" title="\(.*\)" \/>/\![\2](\1)/g