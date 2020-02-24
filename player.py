class player:
	def __init__(self, pos, room_pos):
		self.x = pos[0];
		self.y = pos[1];
		self.room_x = room_pos[0];
		self.room_y = room_pos[1];

	def update(self, key):
		if key == 'KEY_UP':
			self.y -= 1;
		elif key == 'KEY_RIGHT':
			self.x += 1;
		elif key == 'KEY_DOWN':
			self.y += 1;
		elif key == 'KEY_LEFT':
			self.x -= 1;

	def render(self, window):
		window.addch(self.y, self.x, '🤖');
