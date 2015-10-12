#!/bin/bash

for i in {0..10..1}
do
	python client.py 127.0.0.1 2223
	sleep 3
done
