import random
import room

class map:
	def __init__(self, h, w):
		self.width = w;
		self.height = h;
		visited_rooms = [];
		self.rooms = [];
		for i in range(h):
			visited_rooms += [[]]
			self.rooms += [[]]
			for j in range(w):
				visited_rooms[i] += [False]
				self.rooms[i] += [room.room([False, False, False, False])]

		stack = [];
		current_x = 0
		current_y = 0
		while True:
			print(len(stack));
			neighbors = [];
			if current_x != 0 and not visited_rooms[current_y][current_x - 1]:
				neighbors += [(current_y, current_x - 1)];
			if current_y != 0 and not visited_rooms[current_y - 1][current_x]:
				neighbors += [(current_y - 1, current_x)];
			if current_x != w - 1 and not visited_rooms[current_y][current_x + 1]:
				neighbors += [(current_y, current_x + 1)];
			if current_y != h - 1 and not visited_rooms[current_y + 1][current_x]:
				neighbors += [(current_y + 1, current_x)];

			visited_rooms[current_y][current_x] = True;
			if len(neighbors) == 0:
				if len(stack) == 0:
					break;
				current_y, current_x = stack[-1];
				stack.pop();
			else:
				stack += [(current_y, current_x)];
				new_y, new_x = random.choice(neighbors);
				if new_y == current_y + 1:
					self.rooms[current_y][current_x].doors[2] = True;
					self.rooms[new_y][new_x].doors[0] = True;
				elif new_y == current_y - 1:
					self.rooms[current_y][current_x].doors[0] = True;
					self.rooms[new_y][new_x].doors[2] = True;
				elif new_x == current_x + 1:
					self.rooms[current_y][current_x].doors[1] = True;
					self.rooms[new_y][new_x].doors[3] = True;
				elif new_x == current_x - 1:
					self.rooms[current_y][current_x].doors[3] = True;
					self.rooms[new_y][new_x].doors[1] = True;
				current_y, current_x = new_y, new_x;

	def render(self, window):
		for i in range(self.height):
			for j in range(self.width):
				doors = self.rooms[i][j].doors;
				try:
					if doors[0]:
						if doors[1]:
							if doors[2]:
								if doors[3]:
									window.addch(i, j, '┼');
								else:
									window.addch(i, j, '├');
							else:
								if doors[3]:
									window.addch(i, j, '┴');
								else:
									window.addch(i, j, '╰');
						else:
							if doors[2]:
								if doors[3]:
									window.addch(i, j, '┤');
								else:
									window.addch(i, j, '│');
							else:
								if doors[3]:
									window.addch(i, j, '╯');
								else:
									window.addch(i, j, '╵');
					else:
						if doors[1]:
							if doors[2]:
								if doors[3]:
									window.addch(i, j, '┬');
								else:
									window.addch(i, j, '╭');
							else:
								if doors[3]:
									window.addch(i, j, '─');
								else:
									window.addch(i, j, '╶');
						else:
							if doors[2]:
								if doors[3]:
									window.addch(i, j, '╮');
								else:
									window.addch(i, j, '╷');
							else:
								if doors[3]:
									window.addch(i, j, '╴');
								else:
									window.addch(i, j, '·');
				except:
					pass;
