#!/bin/bash
set -e

pip3 install -r 'requirements.txt'
git clone https://github.com/seleniumbase/SeleniumBase.git
cd SeleniumBase/
pip install -r requirements.txt
python setup.py install

seleniumbase install chromedriver
