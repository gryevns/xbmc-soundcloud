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
BASE_URL    = "plugin://plugin.audio.soundcloud2"

def get_menu(params):
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + "favorites/", listitem=ListItem("Likes"), isFolder=True)
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=URL + "playlists/", listitem=ListItem("Playlists"), isFolder=True)
    xbmcplugin.endOfDirectory(handle=HANDLE, succeeded=True)

def get_username():
    username = xbmcplugin.getSetting(HANDLE, u"username")
    if not username:
        __addon__.openSettings()
        return
    return username 

def get_favorites(params):
    username = get_username()
    client = SoundCloudClient(username)
    tracks = client.get_favorites()
    for track in tracks:
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
    #TODO
    Pattern(r"^/playlists/$", None)
]

page = URL[len(BASE_URL):]
for pattern in patterns:
    if pattern.match(page): break