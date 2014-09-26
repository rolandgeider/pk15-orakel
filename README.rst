PK15 Orakel
===========

pk15 Orakel ist eine einfache Webanwendung, die bei einem Geocachingspiel der
Firma Intevation verwendet wurde.


Installation
------------------------------


1) Abhängigkeiten installieren

::

 $ sudo apt-get install python-dev python-virtualenv
 $ virtualenv venv-django
 $ source venv-django/bin/activate

2) Anwendung klonen und starten

::

 $ git clone https://github.com/rolandgeider/pk15-orakel.git
 $ cd pk15-orakel
 $ pip install -r requirements.txt
 $ cp pk15/settings_sample.py pk15/settings.py  
 $ vim pk15/settings.py 
 $ python manage.py migrate
 $ python manage.py runserver 8003


Lizenz
======

pk15 Orakel steht unter der Affero GNU General Public License (AGPL) Version 3+
und darf ohne Restriktionen (unter den Bedingungen der Lizenz) benutzt,
verändert und (geändert) weitergegeben werden.
