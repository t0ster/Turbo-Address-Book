Installation and Setup
======================

Create and activate virtualenv.

Install ``Turbo-Address-Book`` using the setup.py script::

    $ cd Turbo-Address-Book
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Go to http://localhost:8000

* Login: manager
* Password: managepass
