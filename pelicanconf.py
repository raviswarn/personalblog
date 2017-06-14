#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Toth'
SITENAME = u"Michael Toth's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Data Scientist, R Programmer'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings on Statistics, Data Science, Programming, and Economics' % AUTHOR
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico' 

ROBOTS = 'index, follow'

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2017


THEME = u"../Flex"
PATH = 'content'
STATIC_PATHS = ['images', 'figures']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM =	'feeds/all.atom.xml'

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Social widget
SOCIAL = (('twitter', 	'https://twitter.com/Michael_Toth'),
	 ('github', 	'https://github.com/michaeltoth'),
	 ('linkedin',   'https://www.linkedin.com/in/michaelttoth'))

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
	    ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10
