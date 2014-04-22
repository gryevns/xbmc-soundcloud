from track import Track

class Playlist:
	"""
	SoundCloud playlist object
	"""
	def __init__(self, data, client_param):
		self.id = data['id']
		self.created_at = data['created_at']
		self.genre = data['genre']
		self.title = data['title']
		self.uri = data['uri']
		self.artwork_url = data['artwork_url']
		self.tracks = []
		for track in data['tracks']:
			self.tracks.append(Track(track, client_param))

	def get_id(self):
		return self.id

	def get_title(self):
		return self.title

	def get_artwork_url(self):
		return self.artwork_url

	def get_tracks(self):
		return self.tracks

	def get_genre(self):
		return self.genre