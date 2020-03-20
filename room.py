import curses;

class room:
	def __init__(self, doors, ennemies, items):
		self.closed = False;
		self.visited = False;
		self.doors = doors; # Top, Right, Bottom, Left
		self.ennemies = ennemies;
		self.items = [i for i in items];
		self.cells_pointed_at = [];

	def signal(self, x, y):
		self.cells_pointed_at += [(x, y)];

	def is_open(self):
		return not self.closed and len(self.ennemies) == 0;

	def update(self, player):
		self.visited = True;

		# CHANGING ROOMS : LEFT
		if player.x <= 0:
			if not self.doors[3] or not self.is_open():
				player.restore_pos();
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 27;
					player.room_x -= 1;
				else:
					player.restore_pos();

		# CHANGING ROOMS : RIGHT
		elif player.x >= 28:
			if not self.doors[1] or not self.is_open():
				player.restore_pos();
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 1;
					player.room_x += 1;
				else:
					player.restore_pos();

		# CHANGING ROOMS : DOWN
		if player.y <= 0 :
			if not self.doors[0]or not self.is_open():
				player.restore_pos();
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 8;
					player.room_y -= 1;
				else:
					player.restore_pos();

		# CHANGING ROOMS : UP
		elif player.y >= 9:
			if not self.doors[2] or not self.is_open():
				player.restore_pos();
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 1;
					player.room_y += 1;
				else:
					player.restore_pos();

		# UPDATING ITEMS
		for item in self.items[::-1]:
			if (item.x, item.y) == (player.x, player.y):
				player.pickup_item(item, self);
				self.items.remove(item)

		# UPDATING PLAYER HITTING ENNEMIES
		for ennemy in self.ennemies[::-1]:
			if (ennemy.x, ennemy.y) == (player.x, player.y):
				player.restore_pos();
				ennemy.get_hit(player.damage);
				if ennemy.hp <= 0:
					self.ennemies.remove(ennemy);
					curses.beep();
					continue;
		# UPDATING ENNEMIES HITTING PLAYER AND ENNEMY COLLISION
		for ennemy in self.ennemies[::-1]:
			ennemy.update(player, self);
			for ennemy2 in self.ennemies[::-1]:
				if ennemy is ennemy2:
					pass;
				elif (ennemy.x, ennemy.y) == (ennemy2.x, ennemy2.y):
					ennemy.restore_pos();
			if ennemy.x <= 0 or ennemy.x >= 29 or ennemy.y <= 0 or ennemy.y >= 9:
				ennemy.restore_pos();
			if (ennemy.x, ennemy.y) == (player.x, player.y):
				ennemy.restore_pos();
				player.get_hit(ennemy.damage);
				if player.hp <= 0:
					exit();

		return player;



	def render(self, window, player):
		self.render_base(window);
		self.render_doors(window);
		for item in self.items:
			if (item.x, item.y) != (player.x, player.y):
				item.render(window);
		for ennemy in self.ennemies:
			ennemy.render(window);
		for i, j in self.cells_pointed_at:
			window.chgat(j, i, 2, curses.color_pair(1));
		self.cells_pointed_at = [];

	def render_base(self, window):

		try:
			window.addstr(0, 0, '┌────────────────────────────┐');
			for i in range(1, 9):
				window.addch(i, 0, '│');
				window.addch(i, 29, '│');
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

	def add_item(self, item):
		self.items.append(item)
