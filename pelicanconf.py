#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raveendra Swarna'
SITENAME = u"Swarna's's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Data Scientist, Python, R Programmer'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings on Statistics, Data Science, Programming, and Economics' % AUTHOR
SITEURL = 'https://swarna.info'
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico' 

ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2017


THEME = u"../Flex"
PATH = 'content'
STATIC_PATHS = ['images', 'figures']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM =	'feeds/all.atom.xml'

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Social widget
SOCIAL = (('twitter', 	'https://twitter.com/swarnaravi'),
	 ('github', 	'https://github.com/swarnaravi'),
	 ('linkedin',   'https://www.linkedin.com/in/swarnaravi'))

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
	    ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10
