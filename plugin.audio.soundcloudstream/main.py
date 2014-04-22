import xbmc
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem
from utils.pattern import Pattern
from utils.client import SoundCloudClient

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo("name")
__icon__        = __addon__.getAddonInfo("icon")

HANDLE      = int(sys.argv[1])
URL         = sys.argv[0]
BASE_URL    = "plugin://plugin.audio.soundcloudstream"

def get_menu(params):
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + "favorites/", listitem=ListItem("Likes"), isFolder=True)
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + "playlists/", listitem=ListItem("Playlists"), isFolder=True)
    xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

def get_favorites(params):
    client = SoundCloudClient(username)
    tracks = client.get_favorites()
    for track in tracks:
        artwork = track.get_artwork_url() if track.get_artwork_url() else ""
        li = ListItem(label=track.get_title())
        li.setInfo("music", { "title": track.get_title(), "genre": track.get_genre() })
        li.setIconImage(artwork)
        li.setThumbnailImage(artwork)
        li.setProperty("mimetype", "audio/mpeg")
        li.setProperty("IsPlayable", "true")
        url = track.get_stream_url()
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

def get_playlists(params):
    client = SoundCloudClient(username)
    playlists = client.get_playlists()
    for playlist in playlists:
        artwork = playlist.get_artwork_url() if playlist.get_artwork_url() else ""
        li = ListItem(label=playlist.get_title())
        li.setInfo("music", { "title": playlist.get_title(), "genre": playlist.get_genre() })
        li.setIconImage(artwork)
        li.setThumbnailImage(artwork)
        li.setProperty("IsPlayable", "false")
        url = "%s%d/" % (URL, playlist.get_id())
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

def get_playlist(params):
    client = SoundCloudClient(username)
    playlist = client.get_playlist(params['id'])
    for track in playlist.get_tracks():
        artwork = track.get_artwork_url() if track.get_artwork_url() else ""
        li = ListItem(label=track.get_title())
        li.setInfo("music", { "title": track.get_title(), "genre": track.get_genre() })
        li.setIconImage(artwork)
        li.setThumbnailImage(artwork)
        li.setProperty("mimetype", "audio/mpeg")
        li.setProperty("IsPlayable", "true")
        url = track.get_stream_url()
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

patterns = [
    Pattern(r"^/$", get_menu),
    Pattern(r"^/favorites/$", get_favorites),
    Pattern(r"^/playlists/$", get_playlists),
    Pattern(r"^/playlists/(?P<id>\d+)/$", get_playlist)
]

# Require username
username = xbmcplugin.getSetting(HANDLE, u"username")
if not username:
    __addon__.openSettings()

page = URL[len(BASE_URL):]
for pattern in patterns:
    if pattern.match(page):
        break