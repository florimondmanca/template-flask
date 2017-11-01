# Flask application template

Minimal working application template for Flask projects.

## Usage

### Using the template project

1. Clone this repo in your project folder, e.g. `flaskproject`. Also rename the `flaskproject/yourapp` and `flaskproject/yourapp/yourapp` folders, for instance `flaskapp`.

2. Create the virtual environment and install the dependencies:
```
$ virtualenv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

2. Using your favorite text editor's find/replace functionality on the whole `flaskproject` directory with case sensitivity enabled, replace occurences of `yourapp` and `YOURAPP` with `flaskapp` and `FLASKAPP` respectively.

### Running your application

```
flaskproject $ python3 flaskapp/run.py
```


## Contents

### Project structure

```
yourapp
├── config.py
├── instance
│   └── config.py
├── run.py
├── setup.py
└── yourapp
    ├── __init__.py
    ├── main
    │   ├── __init__.py
    │   ├── static
    │   ├── templates
    │   │   └── index.html
    │   └── views.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   ├── fonts
    │   └── js
    └── templates
        └── layout.html
```

### Blueprints

This template default a default blueprint called `main`. To see how to use blueprints in Flask applications, see some [tutorials](https://exploreflask.com/en/latest/blueprints.html). This template project uses **divisional organization** of blueprints.

### Database management

Database backend is offered through SQLAlchemy. Migrations are handled with Alembic (see [ExploreFlask](https://exploreflask.com/en/latest/storing.html) for details).

## References

This template project structure and contents are inspired by the [ExploreFlask](https://exploreflask.com/en/latest/) tutorials.
