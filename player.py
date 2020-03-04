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
		self.speed = 4;

	def update(self, key):
		self.prev_x = self.x;
		self.prev_y = self.y;
		if key == 'KEY_UP':
			if self.y <= self.speed:
				speed_save = self.speed
				while self.y <= self.speed and self.speed > 1:
					self.speed -= 1
				self.y -= self.speed;
				self.speed = speed_save
			else:self.y -= self.speed;
		elif key == 'KEY_RIGHT':
			if self.x >= 27-2*self.speed:
				speed_save = self.speed
				while self.x > 27-2*self.speed and self.speed > 1:
					self.speed -= 1
				self.x += 2*self.speed;
				self.speed = speed_save
			else:self.x += 2*self.speed;
		elif key == 'KEY_DOWN':
			if self.y >= 8-self.speed:
				speed_save = self.speed
				while self.y > 8-self.speed and self.speed > 1:
					self.speed -= 1
				self.y += self.speed;
				self.speed = speed_save
			else:self.y += self.speed;
		elif key == 'KEY_LEFT':
			if self.x <= 2*self.speed:
				speed_save = self.speed
				while self.x <= 2*self.speed and self.speed > 1:
					self.speed -= 1
				self.x -= 2*self.speed;
				self.speed = speed_save
			else:self.x -= 2*self.speed;
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
