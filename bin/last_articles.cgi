#!/bin/bash

source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

num=$(tr -dc '0-9' <<< ${QUERY_STGING})
[ -z "$num" ] && num=10

echo -e 'Content-Type: text/html\n'
tac "$datadir/post_list" |
	head -n "$num"	|
	awk '{print $3}' |
	xargs -I@ cat "$datadir/@/link_date" |
	sed 's;$;<br />;'
#awk '{print $3}' "$datadir/post_list" | xargs -I@ cat "$datadir/@/link"
