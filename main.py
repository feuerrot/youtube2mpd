#!/usr/bin/env python3
import os
import urllib.request

download = {
		'bottle.py' : 'https://raw.github.com/defnull/bottle/d7780fd5d5c2baeb0152864138adbbdfcf83e6e4/bottle.py',
		'youtube-dl' : 'https://yt-dl.org/downloads/2014.03.04.2/youtube-dl'
}

for elem in download:
	if not os.path.isfile(elem):
		urllib.request.urlretrieve(download[elem], elem)

import bottle
