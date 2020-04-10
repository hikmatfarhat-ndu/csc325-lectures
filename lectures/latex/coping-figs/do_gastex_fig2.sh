#/bin/sh
file=${1%.tex}
rm -f $file.pdf $file.eps
latex $file
dvips -o $file.ps $file.dvi
ps2eps --loose $file.ps

