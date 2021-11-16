#!/bin/bash

echo "[1] Installing mypy...."
python3 -m pip install mypy

echo "[2] Running mypy static code analyzer...."
mypy_static_code_analyzer=$(mypy --ignore-missing-imports flask_my_form.py)
echo $mypy_static_code_analyzer

echo "[3] Running unittesting function tests...."
python testscript.py
unittest_testing=$? #Exit code of last command stored in $?

if [[ $unittest_testing = 0 ]] && [[ $mypy_static_code_analyzer = 'Success: no issues found in 1 source file' ]]
then
	echo "Static code analyzer and unittesting scripts were successful, Starting Up server...."
        python flask_my_form.py 
else
	echo "There was an error in either the static code analyzer or unnitesting scripts, unable to start server - Please see error above...."
fi
