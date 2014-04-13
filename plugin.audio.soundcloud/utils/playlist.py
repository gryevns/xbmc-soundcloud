class Playlist:
	"""
	SoundCloud playlist object
	"""
	def __init__(self, data):
		self.id = data['id']
		self.created_at = data['created_at']
		self.title = data['title']
		self.uri = data['uri']
		self.artwork_url = data['artwork_url']
		self.tracks = []
		print "..."
		for track in data.tracks:
			self.tracks.append(Track(track))

	def get_id(self):
		return self.id

	def get_title(self):
		return self.title

	def get_artwork_url(self):
		return self.artwork_url

	def get_tracks(self):
		return self.tracks