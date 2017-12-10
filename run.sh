#!/bin/sh

. ./bin/activate
./get_posts.py
./main.py > hinabitter.txt
