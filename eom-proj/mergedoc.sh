#!/bin/bash

cat PREFACE.md */README.md > README.md
pandoc -f markdown -t docx --lua-filter=./pagebreak.lua README.md -o README.docx
rm -f README.md
