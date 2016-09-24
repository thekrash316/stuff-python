#!/bin/bash
set -e

python doctest_try.py -v
python unittest_try.py

