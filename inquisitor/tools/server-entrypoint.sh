ENV_DIR='.venv'
python3 -m venv $ENV_DIR
source $ENV_DIR/bin/activate
pip install -r requirements.txt

# Last command
tail -f /dev/null