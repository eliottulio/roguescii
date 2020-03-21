import time, random, curses
import room
import player as player_
import map as map_

def main(sc):
	curses.nl();
	gameplay_window = curses.newwin(10, 30, 0, 0);
	map_window = curses.newwin(5, 10, 0, 35);
	stats_window = curses.newwin(5, 10, 5, 35);
	gameplay_window.keypad(True);
	curses.curs_set(0);
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)



	player = player_.player((13, 4), (0, 0));
	map = map_.map(5, 6);



	running = True;

	def render_all():
		stats_window.clear();
		gameplay_window.clear();
		player.render(gameplay_window, stats_window);
		map.rooms[player.room_y][player.room_x].render(gameplay_window, player)
		map.render(map_window, player);

		sc.refresh();
		gameplay_window.refresh();
		map_window.refresh();
		stats_window.refresh();

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
		player = map.rooms[player.room_y][player.room_x].update(player, gameplay_window);

		render_all();

	curses.curs_set(2);
	gameplay_window.keypad(False);
	curses.nonl();

curses.wrapper(main);
