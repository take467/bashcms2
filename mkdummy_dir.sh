#!/bin/bash

#echo {a..z}{a..z}{a..z} | tr ' ' '\n' | sed 's;^;dummy_contents/posts/dummy_;' | xargs mkdir -p 

for d in `echo {a..z}{a..z}{a..z}`
do
	#echo  "dummy_contents/posts/dummy_$d"
	mkdir -p  dummy_contents/posts/dummy_$d
done
