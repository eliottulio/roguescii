import time, random, curses
import room
import player as player_

def main(sc):
	curses.nl();

	gameplay_window = curses.newwin(10, 30, 0, 0);
	gameplay_window.keypad(True);
	curses.curs_set(0);



	player = player_.player((14, 4), (1, 1));

	rooms = [	[room.room((0, 1, 1, 0)), room.room((0, 0, 1, 1)), room.room((0, 0, 1, 0))],
				[room.room((1, 0, 1, 0)), room.room((1, 1, 0, 0)), room.room((1, 0, 1, 1))],
				[room.room((1, 0, 0, 0)), room.room((0, 1, 0, 0)), room.room((1, 0, 0, 1))]];



	running = True;

	gameplay_window.mvwin(player.room_y * 10, player.room_x * 30);
	rooms[player.room_y][player.room_x].render(gameplay_window)
	player.render(gameplay_window);

	while running:
		key = gameplay_window.getkey();

		if key == ' ':
			running = False;

		player.update(key);
		player = rooms[player.room_y][player.room_x].update(player);


		gameplay_window.mvwin(player.room_y * 10, player.room_x * 30);
		rooms[player.room_y][player.room_x].render(gameplay_window)
		player.render(gameplay_window);

		sc.clear();
		sc.refresh();
		gameplay_window.refresh();

	curses.curs_set(2);
	gameplay_window.keypad(False);
	curses.nonl();


curses.wrapper(main);
