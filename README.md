# ProductCatalog
Simple Django project to practice. Creates list of products with ability to create/delete/modify list items.
Deployed on Heroku:  https://murmuring-ravine-49991.herokuapp.com/

### Running locally

* Install a relatively fresh version of Python. I used Python 3.6.8.
* Clone the repo or download the sources as ZIP.
* Create venv and install packages:

Linux:
```bash
# Ubuntu/Debian need installation of package for venv creation
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
```
Windows:
```bash
python3 -m venv venv
venv/Scripts/activate.bat
pip install -r requirements/development.txt
```

* Apply migrations: `python manage.py migrate`
* Run Django-server: `python manage.py runserver 127.0.0.1:8000`

### Local deployment
#### Getting started

Used OS:
* Host OS: Windows 10 Professional
* Guest OS: Ubuntu 18.04 Server

Used software:
* VirtualBox (Host OS) - software for VM management.
* Vagrant (Host OS) - useful tool to create VMs from config files (e.g. Vagrantfiles) . I used [this](https://github.com/K9173A/vagrantfiles/tree/master/ubuntu-18.04-server-amd) configuration.
* Gunicorn (Guest OS) - HTTP WSGI server for Python (based on Ruby's Unicorn server). Hidden "behind" Nginx server: gets requests and responses to nginx, but does not communitate with clients directly. Nginx takes care of that.
* Nginx (Guest OS) - reverse proxy-server which is being used to enhance speed of request handling.
* Supervisor (Guest OS) - tool which is being used to restart Nginx if it crashes for some reason.

**Note!** Deployment algorithm can vary from one OS to another, so be careful when trying to copy-paste my implementation.

#### Preparations

* Check interfaces possible for bridged connection:
```
cd C:/Program Files/Oracle/VirtualBox
VBoxManage list bridgedifs
```
* Go to Vagrantfile and place selected interface after the `bridge`. For instance:
```
config.vm.network "public_network", bridge: "Intel(R) Ethernet Connection (2) I219-V"
```
* Run: `vagrant run`. You will notice the following information: `Adapter 1: nat` and `Adapter 2: bridged`. Vagrant sets `eth0` as NAT - this is fundamental requirement as noted [here](https://github.com/hashicorp/vagrant/issues/2093). So `eth1` will be bridged interface.
* Login. Login: `vagrant`. Password: `vagrant`.
* Add `PROD_LOCAL` environment variable in the `.bashrc`, so Django will import correct settings needed for local deployment: `sudo nano ~/.bashrc`.
* Clone the repo: `git clone https://github.com/K9173A/ProductCatalog.git`
* Create virtual enviroment:
```
cd ProductCatalog
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/production-local.txt
```

#### Netplan

* Go to the `01-netcfg.yaml`:
```
cd /etc/netplan
sudo nano 01-netcfg.yaml
```
* Paste the following config. We manually set static IP and switch off DHCP on `eth1`.
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth1:
      dhcp4: no
      dhcp6: no
      addresses: [192.168.0.98/24]
      gateway4: 192.168.0.1
      nameservers:
        addresses: [8.8.8.8, 192.168.0.1]
```
* Apply settings: `sudo netplan apply`
* Check the IP: `ifconfig -a`. It should be `192.168.0.98`.

#### PostgreSQL

* Check Postgres activity: `sudo systemctl status postgresql`. It should be active.
* Enter the psql: `sudo -u postgres psql`.
* Create a new database:
```sql
CREATE DATABASE productcatalog;
CREATE USER admin with PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE geekplanner TO admin;
ALTER ROLE admin SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE admin SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE admin SET TIME ZONE 'Europe/Moscow';
```
* Go to the `pb_hba.conf`:
```
cd /etc/postgresql/10/main
sudo nano pg_hba.conf
```
* Add `host all all 192.168.0.0/24 md5` after `IPv4 local connections` line.
* Go to the `postgresql.conf`:
```
cd /etc/postgresql/10/main
sudo nano postgresql.conf
```
* Find title `CONNETIONS AND AUTHENTICATION` and set: `listen_addresses = '*'`
* Restart PostgreSQL and check its status:
```
sudo systemctl restart postgresql
sudo systemctl status postgresql
```

#### Nginx

* Go to `default` file:
```
sudo nano /etc/nginx/sites-available/default
```
* Paste the following settings:
```
server {
  listen 80;
  server_name 192.168.0.98;
  access_log /var/log/nginx/example.log;

  location / {
    include proxy_params;
    proxy_pass http://127.0.0.1:8000;
  }

  location /static/ {
    root /home/vagrant/ProductCatalog;
  }
}
```
* Restart Nginx and check its status: 
```
sudo systemctl restart nginx
sudo systemctl status nginx
```
* Check configuration file: `sudo nginx -t`.
* Enable FireWall and  add a rule for Nginx:
```
sudo ufw enable
sudo ufw allow 'Nginx Full'
```

#### Supervisor

* Create Supervisor config:
```
cd /etc/supervisor/conf.d/
touch productcatalog.conf
sudo nano productcatalog.conf
```
* Paste the following settings:
```
[program:productcatalog]
command=/home/vagrant/ProductCatalog/venv/bin/gunicorn ProductCatalog.wsgi:application -c /home/vagrant/ProductCatalog/deploy/gunicorn.conf.py
directory=/home/vagrant/ProductCatalog
user=vagrant
autorestart=true
redirect_stderr=true
```
* Enable and start Supervisor:
```
sudo update-rc.d supervisor enable
sudo service supervisor start
```

#### Migrations
* Apply migrations:
```
cd ProductCatalog/
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```
* Now you can test website from the host OS: `http://192.168.0.98/`.

### Deployment on Heroku

**Note!** Heroku requires `requirements.txt` in the root directory even if we have separate files for
development and production environment. Hence, we need `requirements.txt` to point to the right
file (`requirements/production-heroku.txt`) if we want build to succeed.

* Install Heroku: `sudo snap install heroku --classic`.
* Login: `heroku login`.
* Clone the repo: `git clone https://github.com/K9173A/ProductCatalog`.
* Go to the root folder: `cd ProductCatalog`.
* Install and create virtual environment with requirements (@see "Running Locally").
* Create Heroku app: `heroku create`.
* Install PostgreSQL addon: `heroku addons:create heroku-postgresql:hobby-dev`.
* Push data to Heroku: `git push heroku master`.
* Apply migrations: `heroku run python manage.py migrate --no-input`.
* Create superuser: `heroku run python manage.py createsuperuser`.

### License
ProductCatalog is released under the terms of the MIT license.  See [MIT](https://opensource.org/licenses/MIT) and [LICENSE](https://github.com/K9173A/ProductCatalog/blob/master/LICENSE) for more information.
