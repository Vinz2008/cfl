#!/usr/bin/bash

full_path=$(realpath $0)
Path=$(dirname $full_path)
rm $Path/main.py
touch $Path/main.py
cat $Path/files/*.py >> main.py
echo "SUCESS"
echo "The operations have been added"
