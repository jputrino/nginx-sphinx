import os
from os import path

def get_html_theme_path():
    """Return the html theme path for this template library.
    :returns: List of directories to find template files in
    """
    curdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return [curdir]

def setup(app):
    """Set up the theme for distribution as a python package
    :return: Adds nginx-sphinx to the html_themes path in Sphinx
    """
    app.add_html_theme('nginx_sphinx', path.abspath(path.dirname(__file__)))
