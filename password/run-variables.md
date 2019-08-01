export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1

pip install dnspython
pip install flask-pymongo
apt-get install python3-flask