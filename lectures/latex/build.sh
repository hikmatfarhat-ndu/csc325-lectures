#!/bin/bash
args="--output-directory=../pdf --aux-directory=../auxilary"
pdflatex $args $1
