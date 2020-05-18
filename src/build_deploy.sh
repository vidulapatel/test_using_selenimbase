#!/bin/bash
set -e

pip3 install -r 'requirements.txt'
git clone https://github.com/seleniumbase/SeleniumBase.git
cd SeleniumBase/
pip3 install -r requirements.txt
python3 setup.py install

seleniumbase install chromedriver
