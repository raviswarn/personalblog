#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Toth'
SITENAME = u"Michael Toth's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Data Scientist'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = 'https://qph.is.quoracdn.net/main-thumb-7362250-200-ugpksvyqbzsktznpdworrsucakndefsk.jpeg' # Change to http://michaeltoth.me/img/profile.png
SITEURL = 'http://localhost:8000'
FAVICON = SITEURL + '/images/favicon.ico' # Make this a favicon of your profile picture

THEME = u"../Flex"
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
#OG_LOCALE = u'en_US'
#LOCALE = u'en_US'

FEED_ALL_ATOM =	'feeds/all.atom.xml'

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

#LINKS = ()

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
