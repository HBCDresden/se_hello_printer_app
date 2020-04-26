# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- Rozpoczynając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedynczej aplikacji w python-ie:

  ```


  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
$ python3 -m venv .venv

# aktywowanie hermetycznego środowiska
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r test_requirements.txt
  ```

  Sprawdź: [documentację virtualenvwrappera](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)s oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test  --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  $ source /usr/local/bin/virtualenvwrapper.sh # nie trzeba, jeśli już w .bashrc
  $ workon wsb-simple-flask-app

  ...

  # deaktywacja virtualenv
  $ deactivate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  ```


# Pomocnicze

## Ubuntu

- Instalacja python virtualenv i virtualenvwrapper:

  ```
  $ sudo pip install virtualenv
  $ sudo pip install virtualenvwrapper
  ```

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

# Materiały

- https://virtualenvwrapper.readthedocs.io/en/latest/



Modyfikacja readme bla bla