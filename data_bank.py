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
	pause_count = 2;
	if self.current_frame == 0:
		self.appearence = '😶';
		x = player.x - self.x;
		y = player.y - self.y;
		if abs(x) > abs(y):
			self.x += int(x / abs(x)) * 2;
		else:
			self.y += int(y / abs(y)) if y != 0 else 0;
	elif self.current_frame == pause_count + 1:
		self.appearence = '😡';
	self.current_frame = (self.current_frame + 1) % (pause_count + 2);


ennemies = {
'skull': 		lambda x, y: ennemy.ennemy('💀', (x, y), 1, 50, skull_ai),
'alien': 		lambda x, y: ennemy.ennemy('👾', (x, y), 2, 1, alien_ai),
'mouthless': 	lambda x, y: ennemy.ennemy('😶', (x, y), 1, 1, mouthless_ai)
}




rooms = {
(False, False, False, True):
[
room.room((False, False, False, True), [ennemies['skull'](27, 1), ennemies['skull'](27, 8)])
],

(False, False, True, False):
[
room.room((False, False, True, False), [ennemies['mouthless'](27, 1), ennemies['mouthless'](1, 1)])
],

(False, False, True, True):
[
room.room((False, False, True, True), [ennemies['skull'](27, 1)])
],

(False, True, False, False):
[
room.room((False, True, False, False), [ennemies['mouthless'](1, 1), ennemies['mouthless'](1, 8)])
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
room.room((True, False, False, False), [ennemies['skull'](1, 8), ennemies['skull'](27, 8)])
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
