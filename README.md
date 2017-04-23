# Flask application template

Minimal working application template for Flask projects.

## Usage

### Using the template project

1. Copy-paste this whole `template-flask` directory and rename it the name of your project, e.g. `flaskproject`. Also rename the `flaskproject/yourapp` and `flaskproject/yourapp/yourapp` folders to, for instance, `flaskapp`.

2. Using your favorite text editor's find/replace functionality on the whole `flaskproject` directory with case sensitivity enabled, replace occurences of `yourapp` and `YOURAPP` with `flaskapp` and `FLASKAPP` respectively.

3. After activating your `env`, you can `pip install -e flaskapp`.

### Running your application

1. Define the `FLASK_APP` environment variable: `export FLASK_APP=flaskapp`
2. `flask run`.

You may then open your favorite web browser at `localhost:5000` and see a "Hello World!" web page: if so, everything worked as expected !

## Contents

### Directory structure

```
yourapp
├── setup.py
└── yourapp
    ├── __init__.py
    ├── static
    │   └── style.css
    ├── template
    │   └── index.html
    └── views.py
```

### Default files & details

- `yourapp/static`: folder for your static files, containing an empty `style.css` CSS file.
- `yourapp/template/index.html`: HTML template that loads Bootstrap and jQuery for your application as well as the default CSS custom style.
- `yourapp/views.py`: views file containing a boilerplate "Hello World!" index view.
- `setup.py` defines the `setuptools` configuration file used when installing your application inside your `virtualenv`.
