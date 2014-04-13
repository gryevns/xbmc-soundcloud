class Track:
	"""
	SoundCloud track object
	"""
	def __init__(self, data):
		self.id = data['id']
		self.created_at = data['created_at']
		self.user_id = data['user_id']
		self.title = data['title']
		self.uri = data['uri']
		self.artwork_url = data['artwork_url']
		self.genre = data['genre']
		self.streamable = data['streamable']
		self.stream_url = data['stream_url']

	def __repr__(self):
		return "%s" % self.title

	def get_id(self):
		return self.id

	def get_title(self):
		return self.title

	def get_artwork_url(self):
		return self.artwork_url

	def get_stream_url(self):
		return self.stream_url