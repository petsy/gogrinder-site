# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import time

here = os.path.abspath(os.path.dirname(__file__))

# plugins
PLUGIN_PATHS = [ os.path.abspath(os.path.join(here, os.pardir, os.pardir, 'plugins')) ]
PLUGINS = ["chameleontemplates", "rstreader", "markdownreader", "htmlreader", "sitemap"] 
    #"gzip_cache"]

THEME = "./themes/gogrinder"

AUTHOR = u'Mark Fink'
#AUTHOR_IMAGE = 'markfink.png'
#AUTHOR_BIO = 'Software Engineer. Test-Automation expert. Microcontroller enthusiast. Creator of buccaneer.'

COPYRIGHT_YEAR = time.strftime("%Y")

# SITECONFIG
OUTPUT_PATH = 'output'
LOCALPORT = 8000
GOOGLE_ANALYTICS = 'UA-6201xxx-1'
SITEURL = 'http://www.gogrinder.io'
#SITEURL = 'http://localhost:8000'
SITENAME = u'www.gogrinder.io website'
COVER_IMAGE = 'cover.png'
S3_CACHE_EXPIRES = [('**', 7), ('*', 1), ('drafts/**', 0), ('articles/**', 1), 
    ('tags/**', 3), ('theme/**', 100)]
DEFAULT_S3_CACHE_EXPIRES = 700
S3_BUCKET = 'www.gogrinder.io'
CF_DISTRIBUTION = 'E1GOHK80XYZUV'

DATE_FORMATS = {
    'en': ('en_US.utf8', '%B %d, %Y'),
    'de': ('de_DE.utf8', '%d. %B %Y'),
}

# paths
PATH = 'content'
# use all subfolders of PATH for articles/categories but extra
ARTICLE_PATHS = [d for d in os.walk(os.path.abspath(os.path.join(here, PATH))).next()[1]
    if d != 'extra']
#ARTICLE_EXCLUDES = ['']
PAGE_PATHS = ['']
#PAGE_EXCLUDES = []
FINDMEDIA = {
    'images': ['.png', '.jpg'],
    'slides': ['.pdf'],
}

# parse the date and slug from the folder that contains the article
# the regexp that will be used to extract any metadata from the filename.
# all named groups that are matched will be set in the metadata object.
PATH_METADATA = 'articles/(?P<date>\d{8})_.*/.*'

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
DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5

DOCUTILS_SETTINGS = {'cloak_email_addresses': 1}

GZIP_CACHE_OVERWRITE = True

# URLs
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = os.path.join('drafts', '{slug}.html')
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
CATEGORY_SAVE_AS = ''  # disable category pages
CATEGORIES_SAVE_AS = ''  # disable
PAGE_URL= '{slug}.html' # this is necessary if you do not want to move pages to pages folder
PAGE_SAVE_AS = '{slug}.html'

# configure the tag cloud
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_STEPS = 5

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

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Set to True if you want local URLs when developing
LOCAL_URLS = False
