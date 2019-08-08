#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Abhilash Sarwade'
SITENAME = 'abhilash_sw'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = [".ipynb_checkpoints"]

#theme
THEME = '/home/abhilash/Abhilash/my_blog/pelican-themes/clean-blog'
COLOR_SCHEME_CSS = 'darkly.css'

SOCIAL = (('github', 'https://github.com/leme-cosmo'),
          ('facebook','https://facebook.com/leme.cosmo'),
          ('envelope','mailto:pythonabhilash@gmail.com'),
          ('reddit','https://reddit.com/u/leme16'))