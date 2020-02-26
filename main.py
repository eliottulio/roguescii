import time, random, curses
import room
import player as player_
import map as map_

def main(sc):
	curses.nl();
	gameplay_window = curses.newwin(10, 30, 0, 0);
	map_window = curses.newwin(10, 10, 0, 35);
	gameplay_window.keypad(True);
	curses.curs_set(0);



	player = player_.player((13, 4), (0, 0));
	map = map_.map(5, 6);



	running = True;

	def render_all():
		map.rooms[player.room_y][player.room_x].render(gameplay_window)
		player.render(gameplay_window);
		map.render(map_window, player);

		sc.refresh();
		gameplay_window.refresh();
		map_window.refresh();

	render_all();

	while running:
		key = gameplay_window.getkey();

		if key == ' ':
			gameplay_window.addstr(2, 8, "Do you really");
			gameplay_window.addstr(3, 5, "want to quit (y/n) ?");
			gameplay_window.refresh();
			k = gameplay_window.getkey();
			if k == 'y':
				running = False;
			render_all();
			continue;

		player.update(key);
		player = map.rooms[player.room_y][player.room_x].update(player);

		render_all();

	curses.curs_set(2);
	gameplay_window.keypad(False);
	curses.nonl();

curses.wrapper(main);
