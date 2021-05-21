# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
  package_data={'nginx_sphinx': [
    'theme.conf',
    '*.html',
    'includes/*.html',
    'static/fonts/*/*.*',
    'static/images/*.*',
    'static/images/icons/*.*',
    'static/*.*',
    'static/css/*.css',
    'static/js/*.js',
    'static/js/*/*.js',
    ]
  },
  include_package_data = True,
  entry_points = {
        'sphinx.html_themes': [
            'nginx_sphinx = nginx_sphinx',
        ]
    },
  install_requires = [
  'sphinx>=3.5.4',
  ],
)

