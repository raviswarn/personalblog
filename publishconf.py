#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'http://michaeltoth.me'
FAVICON = SITEURL + '/images/favicon.ico' # Make this a favicon of your profile picture
RELATIVE_URLS = False

FEED_ALL_ATOM =	'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = 'michaeltoth'
GOOGLE_ANALYTICS = 'UA-35477329-1'
