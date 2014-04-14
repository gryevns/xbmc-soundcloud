class Track:
	"""
	SoundCloud track object
	"""
	def __init__(self, data, client_param):
		self.client_param = client_param
		self.id = data['id']
		self.created_at = data['created_at']
		self.user_id = data['user_id']
		self.title = data['title'].encode('utf-8', 'replace')
		self.uri = data['uri']
		self.artwork_url = data['artwork_url']
		self.genre = data['genre']
		self.streamable = data['streamable']
		self.stream_url = data['stream_url']

	def __repr__(self):
		return self.title

	def get_id(self):
		return self.id

	def get_title(self):
		return self.title

	def get_genre(self):
		return self.genre

	def get_artwork_url(self):
		return self.artwork_url

	def get_stream_url(self):
		return self.stream_url + self.client_param