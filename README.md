# ProductCatalog
Simple Django project to practice. Creates list of products with ability to create/delete/modify list items.

### Running

* Install a relatively fresh version of Python. I used Python 3.6.8.
* Clone the repo or download the sources as ZIP.
* Create venv and install packages:

Linux:
```bash
# Ubuntu/Debian need installation of package for venv creation
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Windows:
```bash
python3 -m venv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

* Apply migrations: `python manage.py migrate`
* Run Django-server: `python manage.py runserver 127.0.0.1:8000`

### License
ProductCatalog is released under the terms of the MIT license. See MIT and LICENSE for more information.