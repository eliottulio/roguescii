import time, random, curses
import room

def main(sc):
	curses.nl();

	gameplay_window = curses.newwin(10, 30, 0, 0);
	gameplay_window.keypad(True);
	curses.curs_set(0);

	player_x = 14;
	player_y = 4;
	room_x = 1;
	room_y = 1;

	rooms = [	[room.room((0, 0, 0, 0)), room.room((0, 0, 1, 0)), room.room((0, 0, 0, 0))],
				[room.room((0, 0, 0, 0)), room.room((1, 1, 0, 0)), room.room((0, 0, 0, 1))],
				[room.room((0, 0, 0, 0)), room.room((0, 0, 0, 0)), room.room((0, 0, 0, 0))]];

	running = True;
	while running:
		key = gameplay_window.getkey();
		if key == 'KEY_UP':
			player_y -= 1;
		elif key == 'KEY_RIGHT':
			player_x += 1;
		elif key == 'KEY_DOWN':
			player_y += 1;
		elif key == 'KEY_LEFT':
			player_x -= 1;
		elif key == ' ':
			running = False;

		(player_x, player_y), (room_x, room_y) = rooms[room_y][room_x].update([player_x, player_y], [room_x, room_y]);



		rooms[room_y][room_x].render(gameplay_window)

		gameplay_window.addch(player_y, player_x, '0');

		gameplay_window.refresh();

	curses.curs_set(2);
	gameplay_window.keypad(False);
	curses.nonl();


curses.wrapper(main);
