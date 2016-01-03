# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import time

here = os.path.abspath(os.path.dirname(__file__))

# plugins
PLUGIN_PATHS = [ os.path.abspath(os.path.join(here, os.pardir, os.pardir, 'plugins')) ]
PLUGINS = ["chameleontemplates", "rstreader", "sitemap"] 
    #"gzip_cache"]

THEME = "./themes/gogrinder"

AUTHOR = u'Mark Fink'

COPYRIGHT_YEAR = time.strftime("%Y")

# SITECONFIG
OUTPUT_PATH = 'output'
LOCALPORT = 8000
GOOGLE_ANALYTICS = 'UA-6201xxx-1'
#SITEURL = 'http://www.gogrinder.io'
SITEURL = 'http://localhost:8000'
SITENAME = u'www.gogrinder.io website'

S3_CACHE_EXPIRES = [('**', 7), ('*', 7), ('theme/**', 100)]
DEFAULT_S3_CACHE_EXPIRES = 700
S3_BUCKET = 'www.gogrinder.io'
CF_DISTRIBUTION = 'E1GOHK80XYZUV'

DATE_FORMATS = {
    'en': ('en_US.utf8', '%B %d, %Y'),
    'de': ('de_DE.utf8', '%d. %B %Y'),
}

# paths
PATH = 'content'
PAGE_PATHS = ['']
ARTICLE_PATHS = []  # this website currently has no articles

# A list of files to copy from the source to the destination
STATIC_PATHS = [
    'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'save_as': 'robots.txt'},
}

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = False

DOCUTILS_SETTINGS = {'cloak_email_addresses': 1}

GZIP_CACHE_OVERWRITE = True

# DIRECT_TEMPLATES
#DIRECT_TEMPLATES = ['index', 'nochmal']   

# URLs
CATEGORY_SAVE_AS = ''  # disable category pages
CATEGORIES_SAVE_AS = ''  # disable
PAGE_URL= '{slug}.html' # this is necessary if you do not want to move pages to pages folder
PAGE_SAVE_AS = '{slug}.html'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'tags': 0.3
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'tags': 'daily'
    }
}

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Set to True if you want local URLs when developing
LOCAL_URLS = False
