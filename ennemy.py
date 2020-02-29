class ennemy:
	def __init__(self, appearence, pos, hp, damage, pattern):
		self.prev_x = pos[0];
		self.prev_y = pos[1];
		self.x = pos[0];
		self.y = pos[1];
		self.dir = 'E'
		self.appearence = appearence;
		self.pattern = pattern;
		self.hp = hp;
		self.damage = damage;
		self.current_frame = 0;

	def update(self, player):
		self.prev_x, self.prev_y = self.x, self.y;
		self.pattern(player, self);
		#DIRECTION
		dx = (self.x-self.prev_x)/2
		dy = self.y-self.prev_y
		if abs(dx) >= abs(dy):
			if dx > 0:
				self.dir = 'E'
			elif dx < 0:
				self.dir = 'W'
		else:
			if dy > 0:
				self.dir = 'S'
			else: #dy < 0
				self.dir = 'N'

	def restore_pos(self):
		self.x, self.y = self.prev_x, self.prev_y;

	def get_hit(self, damage):
		self.hp -= damage;

	def render(self, window):
		window.addstr(self.y, self.x, self.appearence);
