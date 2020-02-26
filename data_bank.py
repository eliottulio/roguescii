import ennemy, room

def poop_ai(player, self):
	return;

ennemies = {
'poop': lambda x, y: ennemy.ennemy('💩', (x, y), 1, 50, poop_ai)
}




rooms = {
(False, False, False, True):
[
room.room((False, False, False, True), [ennemies['poop'](27, 1), ennemies['poop'](27, 8)])
],

(False, False, True, False):
[
room.room((False, False, True, False), [ennemies['poop'](27, 1), ennemies['poop'](1, 1)])
],

(False, False, True, True):
[
room.room((False, False, True, True), [ennemies['poop'](27, 1)])
],

(False, True, False, False):
[
room.room((False, True, False, False), [ennemies['poop'](1, 1), ennemies['poop'](1, 8)])
],

(False, True, False, True):
[
room.room((False, True, False, True), [ennemies['poop'](13, 1), ennemies['poop'](13, 8)])
],

(False, True, True, False):
[
room.room((False, True, True, False), [ennemies['poop'](1, 1)])
],

(False, True, True, True):
[
room.room((False, True, True, True), [ennemies['poop'](13, 1)])
],

(True, False, False, False):
[
room.room((True, False, False, False), [ennemies['poop'](1, 8), ennemies['poop'](27, 8)])
],

(True, False, False, True):
[
room.room((True, False, False, True), [ennemies['poop'](27, 8)])
],

(True, False, True, False):
[
room.room((True, False, True, False), [ennemies['poop'](1, 5), ennemies['poop'](27, 5)])
],

(True, False, True, True):
[
room.room((True, False, True, True), [ennemies['poop'](27, 1), ennemies['poop'](27, 8)])
],

(True, True, False, False):
[
room.room((True, True, False, False), [ennemies['poop'](1, 5)])
],

(True, True, False, True):
[
room.room((True, True, False, True), [ennemies['poop'](13, 8)])
],

(True, True, True, False):
[
room.room((True, True, True, False), [ennemies['poop'](1, 1), ennemies['poop'](1, 8)])
],

(True, True, True, True):
[
room.room((True, True, True, True), [ennemies['poop'](13, 5)])
]
};
