#/bin/sh

#sudo apt-get install libmysqlclient-dev
sed -i "s/'HOST': 'localhost'/'HOST': 'sng.ces9zlqxeeow.eu-central-1.rds.amazonaws.com'/g" aqhorajuega/settings.py
sed -i 's/^\(python-apt==\|pygobject==\|ufw==\)/#\1/g' req.txt
sudo pip3 install -r req.txt
python3 manage.py collectstatic
