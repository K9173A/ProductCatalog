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

### Deployment on Heroku

Note! Heroku requires `requirements.txt` in the root directory even if we have separate files for
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
