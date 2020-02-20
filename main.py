import time, random, curses
import room
import player as player_
import map as map_

def main(sc):
	curses.nl();

	gameplay_window = curses.newwin(10, 30, 0, 0);
	map_window = curses.newwin(5, 4, 0, 120);
	gameplay_window.keypad(True);
	curses.curs_set(0);



	player = player_.player((14, 4), (0, 0));
	map = map_.map(5, 4);



	running = True;

	gameplay_window.mvwin(player.room_y * 10, player.room_x * 30);
	map.rooms[player.room_y][player.room_x].render(gameplay_window)
	player.render(gameplay_window);
	map.render(map_window);

	gameplay_window.refresh();
	map_window.refresh();

	while running:
		key = gameplay_window.getkey();

		if key == ' ':
			running = False;

		player.update(key);
		player = map.rooms[player.room_y][player.room_x].update(player);

		gameplay_window.mvwin(player.room_y * 10, player.room_x * 30);
		map.rooms[player.room_y][player.room_x].render(gameplay_window)
		player.render(gameplay_window);
		map.render(map_window);

		sc.clear();
		sc.refresh();
		gameplay_window.refresh();
		map_window.refresh();

	curses.curs_set(2);
	gameplay_window.keypad(False);
	curses.nonl();


curses.wrapper(main);
