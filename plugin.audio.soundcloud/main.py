import xbmc
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from utils.pattern import Pattern

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')

HANDLE  	= int(sys.argv[1])
URL 		= sys.argv[0]
BASE_URL 	= 'plugin://plugin.audio.soundcloud2'

def get_menu(params):
	xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + 'likes/', listitem=ListItem('Likes'), isFolder=True)
	xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + 'playlists/', listitem=ListItem('Playlists'), isFolder=True)
	xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

def get_likes(params):
	xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + '2/', listitem=ListItem('1'), isFolder=True)
	xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + '1/', listitem=ListItem('2'), isFolder=True)
	xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

patterns = [
	Pattern(r'^/$', get_menu),
	Pattern(r'^/likes/$', get_likes),
	Pattern(r'^/likes/(?P<id>\d+)/$', None),
	Pattern(r'^/tracks/(?P<id>\d+)/$', None),
	Pattern(r'^/playlists/$', None)
]


page = URL[len(BASE_URL):]
for pattern in patterns:
	if pattern.match(page):break

#DEBUG
print "URL: %s" % sys.argv[0]
print "PARAMS: %s" % sys.argv[2]