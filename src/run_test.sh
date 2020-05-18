set -e

virtualenv pip3_test_env
. ./pip3_test_env/bin/activate

# Install Python dependencies
pip3 install -r 'requirements.txt'

cp test_verify_temp_hours.py SeleniumBase/examples/test_event_firing.py

cd SeleniumBase/examples/

python3 -m pytest test_event_firing.py
