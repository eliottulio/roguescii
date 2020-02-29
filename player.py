class player:
	def __init__(self, pos, room_pos):
		self.prev_x = pos[0];
		self.prev_y = pos[1];
		self.x = pos[0];
		self.y = pos[1];
		self.dir = 'E'
		self.room_x = room_pos[0];
		self.room_y = room_pos[1];
		self.hp = 8;
		self.damage = 1;

	def update(self, key):
		self.prev_x = self.x;
		self.prev_y = self.y;
		if key == 'KEY_UP':
			self.y -= 1;
		elif key == 'KEY_RIGHT':
			self.x += 2;
		elif key == 'KEY_DOWN':
			self.y += 1;
		elif key == 'KEY_LEFT':
			self.x -= 2;
		#DIRECTION
		dx = self.x-self.prev_x
		dy = self.y-self.prev_y
		if dx == 2:
			self.dir = 'E'
		elif dx == -2:
			self.dir = 'W'
		elif dy == 1:
			self.dir = 'S'
		elif dy == -1:
			self.dir = 'N'
			

	def get_hit(self, damage):
		self.hp -= damage;

	def restore_pos(self):
		self.x, self.y = self.prev_x, self.prev_y;

	def render(self, window, stats_window):
		window.addstr(self.y, self.x, '°°');
		stats_window.addstr('<3' * (self.hp // 2) + '-3' * (self.hp % 2));
