import urllib2
import json
from track import Track
from playlist import Playlist

class SoundCloudClient:
	"""
	SoundCloud client API wrapper
	"""
	_client_key = "7f34ba13d0bc2c4ee34ce6b6a35607fc"
	_url_favorites = "http://api.soundcloud.com/users/%s/favorites.json"
	_url_playlists = "http://api.soundcloud.com/users/%s/playlists.json"
	_url_playlist  = "http://api.soundcloud.com/playlists/%s.json"

	def __init__(self, username):
		self.username = username

	def get_username(self):
		return self.username

	def get_client_id_param(self, first=False):
		param = "client_id=%s" % self._client_key
		return ("?" + param) if first else ("&" + param)

	def get_favorites(self):
		url = (self._url_favorites % self.username) + self.get_client_id_param(True)
		u = urllib2.urlopen(url)
		response = json.load(u)
		tracks = []
		for track in response:
			tracks.append(Track(track, self.get_client_id_param(True)))
		u.close()
		return tracks

	def get_playlists(self):
		url = (self._url_playlists % self.username) + self.get_client_id_param(True)
		u = urllib2.urlopen(url)
		response = json.load(u)
		playlists = []
		for playlist in response:
			playlists.append(Playlist(playlist, self.get_client_id_param(True)))
		u.close()
		return playlists

	def get_playlist(self, id):
		url = (self._url_playlist % id) + self.get_client_id_param(True)
		u = urllib2.urlopen(url)
		response = json.load(u)
		u.close()
		return Playlist(response, self.get_client_id_param(True))