# run these commands on local
# scp -r deploy himanshu:
# ssh himanshu 'bash deploy/uberspace/install.sh'

cd deploy/uberspace

set -e

# create folders
mkdir -p ~/repos
git init --bare ~/repos/stockdata.git
cp post-receive ~/repos/stockdata.git/hooks/post-receive
chmod +x ~/repos/stockdata.git/hooks/post-receive
mkdir -p ~/webapps/stockdata
touch ~/ENV
ln -s /home/himanshu/ENV ~/webapps/stockdata/.env

# https://lab.uberspace.de/guide_django.html
# install uwsgi
pip3.9 install uwsgi --user
cp uwsgi.ini ~/etc/services.d/uwsgi.ini
mkdir -p ~/uwsgi/apps-enabled
touch ~/uwsgi/err.log
touch ~/uwsgi/out.log

supervisorctl reread
supervisorctl update
supervisorctl status

# configure web server
uberspace web domain add www.example.com
uberspace web backend set www.example.com --http --port 8000

# create deamon
mkdir -p ~/uwsgi/apps-enabled/
cp django-app.ini ~/uwsgi/apps-enabled/

# configure static servers
uberspace web backend set www.example.com/static --apache
uberspace web backend set www.example.com/media --apache

# add nginx headers
uberspace web header set www.example.com/static/ expires 7d
uberspace web header set www.example.com/favicon.ico root /var/www/virtual/himanshu/html/static/favicons
uberspace web header set www.example.com/favicon.ico expires 7d

uberspace web header set www.example.com/static gzip on
uberspace web header set www.example.com/static gzip_comp_level 6
uberspace web header set www.example.com/static gzip_types "text/plain text/css text/xml application/json application/javascript application/xml+rss application/atom+xml image/svg+xml"


# instructions to setup git push
echo "Remote setup done"
echo "Run these on local"
echo "git remote add live himanshu:repos/stockdata.git"
echo "git push live"
echo "ssh himanshu"
echo "vi ENV"
echo "python3.9 manage.py createsuperuser --settings=stockdata.settings.production"
