import ennemy, room, item, random

def skull_ai(player, self, room):
	self.current_frame = (self.current_frame + 1) % 1;

def alien_ai(player, self, room):
	if self.current_frame == 1:
		self.y += 1;
	elif self.current_frame == 3:
		self.y -= 1;
	self.current_frame = (self.current_frame + 1) % 4;

def mouthless_ai(player, self, room):
	if self.current_frame == 0:
		dx = self.x - player.x;
		dy = self.y - player.y;
		self.x -= dx//abs(dx)*2 if (dx != 0 and abs(dy) <= abs(dx/2)) else 0
		self.y -= dy//abs(dy) if (dy != 0 and abs(dx) < abs(dy*2)) else 0
		self.appearance = '¤¤'
		self.current_frame = 1
	else:
		self.appearance = '**'
		self.current_frame = 0

def genie_ai(player, self, room):
	if self.current_frame == 0:
		dist2 = (self.x / 2 - (player.x / 2)) ** 2 + (self.y - player.y) ** 2;
		if dist2 < 8:
			self.appearance = '%%';
			self.next_x = player.x if player.x != self.x else player.prev_x;
			self.next_y = player.y if player.y != self.y else player.prev_y;
			room.signal(self.next_x, self.next_y);
			self.current_frame = 1;
	else:
		self.x = self.next_x;
		self.y = self.next_y;
		self.appearance = '§§';
		self.current_frame = 0;

def backstabber_ai(player, self, room):
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
			room.signal(self.x, self.y - 1);
			room.signal(self.x, self.y - 2);
		elif player.dir == 'S':
			self.x = player.x;
			self.y = player.y - 1;
			room.signal(self.x, self.y + 1);
			room.signal(self.x, self.y + 2);
		elif player.dir == 'E':
			self.x = player.x - 2;
			self.y = player.y;
			room.signal(self.x + 2, self.y);
			room.signal(self.x + 4, self.y);
		elif player.dir == 'W':
			self.x = player.x + 2;
			self.y = player.y;
			room.signal(self.x - 2, self.y);
			room.signal(self.x - 4, self.y);
		self.current_frame += 1
	elif self.current_frame == 3:
		if self.x == player.x or self.y == player.y:
			self.x = player.x
			self.y = player.y
		else:
			self.x = player.prev_x
			self.y = player.prev_y
		self.current_frame -= 1

def ogre_ai(player, self, room):
	if 0 <= self.current_frame < 3:
		self.appearance = '||'
		if self.current_frame == 2:
			self.appearance = ']['
		self.current_frame += 1

	elif self.current_frame == 3:
		dx = self.x - player.x
		dy = self.y - player.y
		self.x -= dx//abs(dx)*2 if dx != 0 else 0
		self.y -= dy//abs(dy) if dy != 0 else 0
		dx = (self.x - player.x)/2
		dy = self.y - player.y
		if dx**2 + dy**2 <= 4:
			self.appearance = '{}'
			self.current_frame += 1
		else:self.appearance = ']['

	elif 3 < self.current_frame < 8:
		dx = abs((self.x - player.x)/2)
		dy = abs(self.y - player.y)
		if (dx == 0 and dy <= 2) or (dy == 0 and dx <= 2):
			room.signal(self.x - 2, self.y) if self.x >= 3 else '';
			room.signal(self.x - 4, self.y) if self.x >= 5 else '';
			room.signal(self.x + 2, self.y) if self.x <= 27 else '';
			room.signal(self.x + 4, self.y) if self.x <= 25 else '';
			room.signal(self.x, self.y - 1) if self.y >= 2 else '';
			room.signal(self.x, self.y - 2) if self.y >= 3 else '';
			room.signal(self.x, self.y + 1) if self.y <= 8 else '';
			room.signal(self.x, self.y + 2) if self.y <= 7 else '';
			self.x = player.x
			self.y = player.y
			self.current_frame = 0
			self.appearance = '||'
		else:
			dx = self.x - player.x
			dy = self.y - player.y
			self.x -= dx//abs(dx)*2 if (dx != 0 and abs(dy) <= abs(dx/2)) else 0
			self.y -= dy//abs(dy) if (dy != 0 and abs(dx) < abs(dy*2)) else 0
		self.current_frame += 1
		if self.current_frame == 8:
			self.current_frame = 0
			self.appearance = '||'

ennemies = {
'skull': 		lambda x, y: ennemy.ennemy('00', (x, y), 1, 50, skull_ai),
'alien': 		lambda x, y: ennemy.ennemy(')(', (x, y), 2, 1, alien_ai),
'mouthless': 	lambda x, y: ennemy.ennemy('¤¤', (x, y), 1, 1, mouthless_ai),
'genie': 		lambda x, y: ennemy.ennemy('§§', (x, y), 2, 2, genie_ai),
'backstabber':	lambda x, y: ennemy.ennemy('FℲ', (x, y), 3, 3, backstabber_ai),
'ogre':			lambda x, y: ennemy.ennemy('||', (x, y), 4, 5, ogre_ai)
}

randc = lambda axis: (1, 27)[random.randint(0, 1)] if axis == 'x' else (1, 8)[random.randint(0, 1)]

rand = lambda x,y: random.randint(x, y)

armor_loot_tables = 	[lambda: item.ArmorPiece(randc('x'), randc('y'), *leather_armorset[rand(0,3)]),
						lambda: item.ArmorPiece(randc('x'), randc('y'), *chainmail_armorset[rand(0,3)]),
						lambda: item.ArmorPiece(randc('x'), randc('y'), *iron_plate_armorset[rand(0,3)]),
						lambda: item.ArmorPiece(randc('x'), randc('y'), *steel_plate_armorset[rand(0,3)])]

leather_armorset = [	('^^', 1, 'helm'),
						('][', 2, 'chest'),
						('::', 1.5, 'legs'),
						(',,', .5, 'boots')]

chainmail_armorset = [	('**', 2, 'helm'),
						('##', 4, 'chest'),
						('##', 3, 'legs'),
						('¤¤', 1, 'boots')]

iron_plate_armorset = [	('¤¤', 3, 'helm'),
						('[]', 6, 'chest'),
						('||', 4.5, 'legs'),
						('**', 1.5, 'boots')]

steel_plate_armorset = [('╭╮', 4, 'helm'),
						('§§', 8, 'chest'),
						('!!', 6, 'legs'),
						(';;', 2, 'boots')]

heal_loot_tables = [lambda: item.HealItem(randc('x'), randc('y'), *basic_heal_items[rand(0, 2)]),
					lambda: item.HealItem(randc('x'), randc('y'), *better_heal_items[rand(0, 2)]),
					lambda: item.HealItem(randc('x'), randc('y'), *best_heal_items[rand(0, 1)])]

basic_heal_items = [(' Ò', 1),('-<', 2),('<3', 3)]

better_heal_items = [('@ ', 4), ('∴ ', 5), ('∞', 6)]

best_heal_items = [('Θ~',9), ('♡!', 10)]

rooms = {
(False, False, False, True):
lambda: [
room.room((False, False, False, True), [ennemies['genie'](5, 1), ennemies['mouthless'](7, 1), ennemies['genie'](9, 1),
										ennemies['genie'](5, 8), ennemies['mouthless'](7, 8), ennemies['genie'](9, 8)],
										[armor_loot_tables[3](), heal_loot_tables[2]()])
],

(False, False, True, False):
lambda: [
room.room((False, False, True, False), [ennemies['ogre'](27, 1), ennemies['mouthless'](1, 1), ennemies['alien'](27, 8)],
										[armor_loot_tables[3](), armor_loot_tables[2]()])
],

(False, False, True, True):
lambda: [
room.room((False, False, True, True), [ennemies['mouthless'](27, 1), ennemies['backstabber'](1,1), ennemies['alien'](21, 5)],
										[armor_loot_tables[2](), heal_loot_tables[1]()])
],

(False, True, False, False):
lambda: [
room.room((False, True, False, False), [ennemies['mouthless'](1, 1), ennemies['genie'](1, 8), ennemies['alien'](27, 1)],
										[armor_loot_tables[1](), heal_loot_tables[0]()])
],

(False, True, False, True):
lambda: [
room.room((False, True, False, True), [ennemies['mouthless'](13, 1), ennemies['genie'](13, 8)],
										[heal_loot_tables[0]()])
],

(False, True, True, False):
lambda: [
room.room((False, True, True, False), [ennemies['genie'](1, 1)], [])
],

(False, True, True, True):
lambda: [
room.room((False, True, True, True), [ennemies['backstabber'](13, 1), ennemies['ogre'](13, 4)], [])
],

(True, False, False, False):
lambda: [
room.room((True, False, False, False), [ennemies['genie'](1, 8), ennemies['mouthless'](27, 8)], [])
],

(True, False, False, True):
lambda: [
room.room((True, False, False, True), [ennemies['ogre'](27, 8),ennemies['ogre'](13, 6)], [])
],

(True, False, True, False):
lambda: [
room.room((True, False, True, False), [ennemies['skull'](1, 5), ennemies['skull'](27, 5)], [])
],

(True, False, True, True):
lambda: [
room.room((True, False, True, True), [ennemies['skull'](27, 1), ennemies['skull'](27, 8)], [])
],

(True, True, False, False):
lambda: [
room.room((True, True, False, False), [ennemies['skull'](1, 5)], [])
],

(True, True, False, True):
lambda: [
room.room((True, True, False, True), [ennemies['skull'](13, 8)], [])
],

(True, True, True, False):
lambda: [
room.room((True, True, True, False), [ennemies['skull'](1, 1), ennemies['skull'](1, 8)], [])
],

(True, True, True, True):
lambda: [
room.room((True, True, True, True), [ennemies['skull'](13, 5)], [])
]
};
