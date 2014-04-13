import re

class Pattern:
	"""
	URL pattern matcher
	"""
	def __init__(self, pattern, function):
		self.pattern = pattern
		self.function = function

	def __str__(self):
		return "%s" % self.pattern

	def match(self, url):
		m = re.match(self.pattern, url)
		if m is not None:
			self.function(m.groupdict())
		return False