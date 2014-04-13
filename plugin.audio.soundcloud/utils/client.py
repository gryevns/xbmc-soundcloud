import urllib2
import json

class SoundCloudClient:
	"""
	SoundCloud client API wrapper
	"""
	__client_key = "7f34ba13d0bc2c4ee34ce6b6a35607fc"
	__url_favorites = "http://api.soundcloud.com/users/%s/favorites.json"
	__url_playlists = "http://api.soundcloud.com/users/%s/playlists.json"

	def __init__(self, username):
		self.username = username

	def get_username(self):
		return self.username

	def get_client_id_param(self, first=False):
		param = "client_id=%s" % self.__client_key
		return ("?" + param) if first else ("&" + param)

	def get_favorites(self):
		url = (self.__url_favorites % self.username) + self.get_client_id_param(True)
		u = urllib2.urlopen(url)
		response = json.load(u)
		tracks = []
		for track in response:
			tracks.append(Track(track))
		u.close()
		return tracks

	def get_playlists(self):
		url = (self.__url_playlists % self.username) + self.get_client_id_param(True)
		u = urllib2.urlopen(url)
		response = json.load(u)
		playlists = []
		for playlist in response:
			playlists.append(Playlist(response))
		u.close()
		return playlists

	def get_playlist(self, id):
		return None