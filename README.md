# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- Rozpoczynając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedynczej aplikacji w python-ie:

  # Tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  ```
  $ python3 -m venv .venv

# Aktywowanie hermetycznego środowiska
```
$ source .venv/bin/activate

$ pip install -r requirements.txt

$ pip install -r test_requirements.txt

```
# Uruchamianie applikacji:

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
  lub komendą:
  $ make test

  ```


# Deaktywacja virtualenv
  $ deactivate
  

# Statuscake
```
Test appki Heroku:
- Odpalany co 5 minut
- Test HTTP
```


# Pomocnicze

# Ubuntu

- Instalacja python virtualenv i virtualenvwrapper:

  ```
  $ sudo pip install virtualenv
  $ sudo pip install virtualenvwrapper
  ```

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


# Travis Status

[![Build Status](https://travis-ci.org/HBCDresden/se_hello_printer_app.svg?branch=master)](https://travis-ci.org/HBCDresden/se_hello_printer_app)

# Statuscake uptime
![Website Status Monitoring](https://app.statuscake.com/button/index.php?Track=hTsFYZ0rzF&Days=1&Design=2)