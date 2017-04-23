from flask import Blueprint

main = Blueprint(
    'site',
    __name__,
    template_folder='templates',
    static_folder='static',
)

from . import views
