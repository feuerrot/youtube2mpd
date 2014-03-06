#!/usr/bin/env python3
import os
import urllib.request
import subprocess

# config
destination = '/tmp/'
# end config

html = {
	'top' : """<html>
			<head><title>youtube2mpd</title></head>
			<body>""",
	'main' : """
				<h1>youtube2mpd:</h1>
				<form action='/' method='post'>
					<input name='url' type='text' size='40'></br>
					<input name='addplaylist' type='checkbox' value='addplaylist'>Zur Playliste hinzufügen</br>
					<input type="submit" value="submit">
				</form>""",
	'done' : """
				<div>done</div>""",
	'bottom' : """
			</body>
		</html>"""
}
		

download = {
		'bottle.py' : 'https://raw.github.com/defnull/bottle/d7780fd5d5c2baeb0152864138adbbdfcf83e6e4/bottle.py',
		'youtube-dl' : 'https://yt-dl.org/downloads/2014.03.04.2/youtube-dl'
}

for elem in download:
	if not os.path.isfile(elem):
		urllib.request.urlretrieve(download[elem], elem)

from bottle import route, run, request, debug

@route('/')
@route('/', method='POST')
def route_main():
	if request.POST.get('url','').strip():
		url = request.POST.get('url','').strip()
		add = request.POST.get('addplaylist','').strip()
		subprocess.call(['./youtube-dl', '-o /tmp/%(title)s.%(ext)s', '--extract-audio', str(url)])
		rtn = html['top'] + html['main'] + html['done'] + html['bottom']
	else:
		rtn = html['top'] + html['main'] + html['bottom']
	return rtn

run(reloader=True)
					
