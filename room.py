class room:
	def __init__(self, doors):
		self.closed = False;
		self.doors = doors; # Top, Right, Bottom, Left

	def update(self, player_pos, room_pos):
		if (player_pos[0] == 0):
			if not self.doors[3]:
				player_pos[0] = 1;
			else:
				if player_pos[1] >= 3 and player_pos[1] <= 6:
					player_pos[0] = 28;
					room_pos[0] -= 1;
				else:
					player_pos[0] = 1;
		elif (player_pos[0] == 29):
			if not self.doors[1]:
				player_pos[0] = 28;
			else:
				if player_pos[1] >= 3 and player_pos[1] <= 6:
					player_pos[0] = 1;
					room_pos[0] += 1;
				else:
					player_pos[0] = 28;

		if (player_pos[1] == 0):
			if not self.doors[0]:
				player_pos[1] = 1;
			else:
				if player_pos[0] >= 11 and player_pos[0] <= 18:
					player_pos[1] = 8;
					room_pos[1] -= 1;
				else:
					player_pos[1] = 1;
		elif (player_pos[1] == 9):
			if not self.doors[2]:
				player_pos[1] = 8;
			else:
				if player_pos[0] >= 11 and player_pos[0] <= 18:
					player_pos[1] = 1;
					room_pos[1] += 1;
				else:
					player_pos[1] = 8;

		return player_pos, room_pos;



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
