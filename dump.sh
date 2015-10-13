#!/bin/bash

for i in {1..20..1}
do
	python client.py 127.0.0.1 2222
	sleep 1
done
