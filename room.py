class room:
	def __init__(self, doors, ennemies):
		self.closed = False;
		self.visited = False;
		self.doors = doors; # Top, Right, Bottom, Left
		self.ennemies = ennemies;

	def is_open(self):
		return not self.closed and len(self.ennemies) == 0;

	def update(self, player):
		self.visited = True;

		if player.x <= 0:
			if not self.doors[3] or not self.is_open():
				player.restore_pos();
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 27;
					player.room_x -= 1;
				else:
					player.restore_pos();
		elif player.x >= 28:
			if not self.doors[1] or not self.is_open():
				player.restore_pos();
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 1;
					player.room_x += 1;
				else:
					player.restore_pos();

		if player.y <= 0 :
			if not self.doors[0]or not self.is_open():
				player.restore_pos();
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 8;
					player.room_y -= 1;
				else:
					player.restore_pos();
		elif player.y >= 9:
			if not self.doors[2] or not self.is_open():
				player.restore_pos();
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 1;
					player.room_y += 1;
				else:
					player.restore_pos();


		for ennemy in self.ennemies:
			ennemy.update(player);
			if (ennemy.prev_x, ennemy.prev_y) == (player.x, player.y):
				player.restore_pos();
				ennemy.get_hit(player.damage);
				if ennemy.hp <= 0:
					self.ennemies.remove(ennemy);
					continue;
			if (ennemy.x, ennemy.y) == (player.x, player.y):
				ennemy.restore_pos();
				player.get_hit(ennemy.damage);
				if player.hp <= 0:
					exit();


		return player;



	def render(self, window):
		self.render_base(window);
		self.render_doors(window);
		for ennemy in self.ennemies:
			ennemy.render(window);

	def render_base(self, window):

		try:
			window.addstr(0, 0, '┌────────────────────────────┐');
			for i in range(1, 9):
				window.addstr(i, 0, '│                            │');
			window.addstr(9, 0, '└────────────────────────────┘');
		except:
			pass;

	def render_doors(self, window):
		if not self.is_open():
			return;

		if self.doors[0]:
			window.addstr(0, 10, '┘        └');
		if self.doors[1]:
			window.addch(2, 29, '└');
			for i in range(3, 7):
				window.addch(i, 29, ' ');
			window.addch(7, 29, '┌');
		if self.doors[2]:
			window.addstr(9, 10, '┐        ┌');
		if self.doors[3]:
			window.addch(2, 0, '┘');
			for i in range(3, 7):
				window.addch(i, 0, ' ');
			window.addch(7, 0, '┐');

		return;
