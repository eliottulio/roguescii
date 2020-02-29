import ennemy, room

def skull_ai(player, self):
	self.current_frame = (self.current_frame + 1) % 1;

def alien_ai(player, self):
	if self.current_frame == 1:
		self.y += 1;
	elif self.current_frame == 3:
		self.y -= 1;
	self.current_frame = (self.current_frame + 1) % 4;

def mouthless_ai(player, self):
	pause_count = 0;
	if self.current_frame == 0:
		self.appearence = '¤¤';
		x = player.x - self.x;
		y = player.y - self.y;
		if abs(x) > abs(y):
			self.x += int(x / abs(x)) * 2;
		else:
			self.y += int(y / abs(y)) if y != 0 else 0;
	elif self.current_frame == pause_count + 1:
		self.appearence = '**';
	self.current_frame = (self.current_frame + 1) % (pause_count + 2);

def genie_ai(player, self):
	if self.current_frame == 0:
		dist2 = (self.x / 2 - (player.x / 2)) ** 2 + (self.y - player.y) ** 2;
		if dist2 < 8:
			self.appearence = '%%';
			self.next_x = player.x if player.x != self.x else player.prev_x;
			self.next_y = player.y if player.y != self.y else player.prev_y;
			self.current_frame = 1;
	else:
		self.x = self.next_x;
		self.y = self.next_y;
		self.appearence = '§§';
		self.current_frame = 0;

def backstabber_ai(player, self):
	if self.current_frame == 0:
		dx = self.x - player.x
		dy = self.y - player.y
		if dy == 0:
			if dx < 0 and player.dir == 'W':
				self.current_frame += 1
			elif dx > 0 and player.dir == 'E':
				self.current_frame += 1
		elif dx == 0:
			if dy < 0 and player.dir == 'N':
				self.current_frame += 1
			elif dy > 0 and player.dir == 'S':
				self.current_frame += 1
	elif self.current_frame == 1:
		dx = self.x - player.x
		dy = self.y - player.y
		self.x -= dx//abs(dx)*2 if dx != 0 else 0
		self.y -= dy//abs(dy) if dy != 0 else 0
		self.current_frame += 1
	elif self.current_frame == 2:
		if player.dir == 'N':
			self.x = player.x;
			self.y = player.y + 1;
		elif player.dir == 'S':
			self.x = player.x;
			self.y = player.y - 1;
		elif player.dir == 'E':
			self.x = player.x - 2;
			self.y = player.y;
		elif player.dir == 'W':
			self.x = player.x + 2;
			self.y = player.y;
		self.current_frame += 1
	elif self.current_frame == 3:
		if self.x == player.x or self.y == player.y:
			self.x = player.x
			self.y = player.y
		else:
			self.x = player.prev_x
			self.y = player.prev_y
		self.current_frame -= 1

ennemies = {
'skull': 		lambda x, y: ennemy.ennemy('00', (x, y), 1, 50, skull_ai),
'alien': 		lambda x, y: ennemy.ennemy(')(', (x, y), 2, 1, alien_ai),
'mouthless': 	lambda x, y: ennemy.ennemy('¤¤', (x, y), 1, 1, mouthless_ai),
'genie': 		lambda x, y: ennemy.ennemy('§§', (x, y), 2, 2, genie_ai),
'backstabber':	lambda x, y: ennemy.ennemy('FℲ', (x, y), 3, 3, backstabber_ai)
}




rooms = {
(False, False, False, True):
[
room.room((False, False, False, True), [ennemies['genie'](5, 1), ennemies['mouthless'](7, 1), ennemies['genie'](9, 1),
										ennemies['genie'](5, 8), ennemies['mouthless'](7, 8), ennemies['genie'](9, 8)])
],

(False, False, True, False):
[
room.room((False, False, True, False), [ennemies['backstabber'](27, 1), ennemies['mouthless'](1, 1), ennemies['alien'](27, 8)])
],

(False, False, True, True):
[
room.room((False, False, True, True), [ennemies['skull'](27, 1)])
],

(False, True, False, False):
[
room.room((False, True, False, False), [ennemies['mouthless'](1, 1), ennemies['genie'](1, 8), ennemies['alien'](27, 1)])
],

(False, True, False, True):
[
room.room((False, True, False, True), [ennemies['skull'](13, 1), ennemies['skull'](13, 8)])
],

(False, True, True, False):
[
room.room((False, True, True, False), [ennemies['skull'](1, 1)])
],

(False, True, True, True):
[
room.room((False, True, True, True), [ennemies['skull'](13, 1)])
],

(True, False, False, False):
[
room.room((True, False, False, False), [ennemies['genie'](1, 8), ennemies['mouthless'](27, 8)])
],

(True, False, False, True):
[
room.room((True, False, False, True), [ennemies['skull'](27, 8)])
],

(True, False, True, False):
[
room.room((True, False, True, False), [ennemies['skull'](1, 5), ennemies['skull'](27, 5)])
],

(True, False, True, True):
[
room.room((True, False, True, True), [ennemies['skull'](27, 1), ennemies['skull'](27, 8)])
],

(True, True, False, False):
[
room.room((True, True, False, False), [ennemies['skull'](1, 5)])
],

(True, True, False, True):
[
room.room((True, True, False, True), [ennemies['skull'](13, 8)])
],

(True, True, True, False):
[
room.room((True, True, True, False), [ennemies['skull'](1, 1), ennemies['skull'](1, 8)])
],

(True, True, True, True):
[
room.room((True, True, True, True), [ennemies['skull'](13, 5)])
]
};
