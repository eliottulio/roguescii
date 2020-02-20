class room:
	def __init__(self, doors):
		self.closed = False;
		self.doors = doors; # Top, Right, Bottom, Left

	def update(self, player):
		if (player.x == 0):
			if not self.doors[3]:
				player.x = 1;
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 28;
					player.room_x -= 1;
				else:
					player.x = 1;
		elif (player.x == 29):
			if not self.doors[1]:
				player.x = 28;
			else:
				if player.y >= 3 and player.y <= 6:
					player.x = 1;
					player.room_x += 1;
				else:
					player.x = 28;

		if (player.y == 0):
			if not self.doors[0]:
				player.y = 1;
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 8;
					player.room_y -= 1;
				else:
					player.y = 1;
		elif (player.y == 9):
			if not self.doors[2]:
				player.y = 8;
			else:
				if player.x >= 11 and player.x <= 18:
					player.y = 1;
					player.room_y += 1;
				else:
					player.y = 8;

		return player;



	def render(self, window):
		self.render_base(window);
		self.render_doors(window);

	def render_base(self, window):

		try:
			window.addstr(0, 0, '┌────────────────────────────┐');
			for i in range(1, 9):
				window.addstr(i, 0, '│                            │');
			window.addstr(9, 0, '└────────────────────────────┘');
		except:
			pass;

	def render_doors(self, window):
		if self.closed:
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
