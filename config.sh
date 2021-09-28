apt update
apt -y install libffi-dev libnacl-dev python3-dev
apt -y install ffmpeg

yes | pip3 install -r requirements.txt