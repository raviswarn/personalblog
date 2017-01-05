#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Toth'
SITENAME = u"Michael Toth's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Data Scientist'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico' 

ROBOTS = 'index, follow'

STATIC_PATHS = ['figure', 'images']

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2016

THEME = u"../Flex"
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM =	'feeds/all.atom.xml'

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Plugin Setup
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['rmd_reader']
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}

LINKS = (('R-Bloggers',  'https://www.r-bloggers.com'),)

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/michaelttoth'),
          ('github', 	'https://github.com/michaeltoth'),
	  ('facebook', 	'https://www.facebook.com/tothmt'),
	  ('twitter', 	'https://twitter.com/Michael_Toth'),
          ('google', 	'https://plus.google.com/+MichaelToth2/'),
	  ('rss', 	'/feeds/all.atom.xml'),)
          #('quora', 	'https://www.quora.com/Michael-Toth-1'),)

MENUITEMS = (('Archives', '/archives.html'),
	     ('Categories', '/categories.html'),
	     ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
