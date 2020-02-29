class ennemy:
	def __init__(self, appearence, pos, hp, damage, pattern):
		self.prev_x = pos[0];
		self.prev_y = pos[1];
		self.x = pos[0];
		self.y = pos[1];
		self.appearence = appearence;
		self.pattern = pattern;
		self.hp = hp;
		self.damage = damage;
		self.current_frame = 0;

	def update(self, player):
		self.prev_x, self.prev_y = self.x, self.y;
		self = self.pattern(player, self);

	def restore_pos(self):
		self.x, self.y = self.prev_x, self.prev_y;

	def get_hit(self, damage):
		self.hp -= damage;

	def render(self, window):
		window.addstr(self.y, self.x, self.appearence);
