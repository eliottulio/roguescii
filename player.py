import math
import item as item_
class player:
	def __init__(self, pos, room_pos):
		self.prev_x = pos[0];
		self.prev_y = pos[1];
		self.x = pos[0];
		self.y = pos[1];
		self.dir = 'E'
		self.room_x = room_pos[0];
		self.room_y = room_pos[1];

		self.damage = 1;
		self.speed = 1;

		self.hp = 10;
		self.hp_max = 10;

		self.armor = {'helm' : item_.ArmorPiece(0, 0, '  ', 0, 'helm'),\
					 'chest' : item_.ArmorPiece(0, 0, '  ', 0, 'helm'),\
					 'legs' : item_.ArmorPiece(0, 0, '  ', 0, 'helm'),\
					 'boots' : item_.ArmorPiece(0, 0, '  ', 0, 'helm')};

		self.armor_val = sum(item.armor_val for item in self.armor.values());

	def update(self, key):
		self.prev_x = self.x;
		self.prev_y = self.y;
		if key == 'KEY_UP':
			if self.y <= self.speed:
				speed_save = self.speed
				while self.y <= self.speed and self.speed > 1:
					self.speed -= 1
				self.y -= self.speed;
				self.speed = speed_save
			else:self.y -= self.speed;
		elif key == 'KEY_RIGHT':
			if self.x >= 27-2*self.speed:
				speed_save = self.speed
				while self.x > 27-2*self.speed and self.speed > 1:
					self.speed -= 1
				self.x += 2*self.speed;
				self.speed = speed_save
			else:self.x += 2*self.speed;
		elif key == 'KEY_DOWN':
			if self.y >= 8-self.speed:
				speed_save = self.speed
				while self.y > 8-self.speed and self.speed > 1:
					self.speed -= 1
				self.y += self.speed;
				self.speed = speed_save
			else:self.y += self.speed;
		elif key == 'KEY_LEFT':
			if self.x <= 2*self.speed:
				speed_save = self.speed
				while self.x <= 2*self.speed and self.speed > 1:
					self.speed -= 1
				self.x -= 2*self.speed;
				self.speed = speed_save
			else:self.x -= 2*self.speed;
		#DIRECTION
		dx = self.x-self.prev_x
		dy = self.y-self.prev_y
		if dx == 2:
			self.dir = 'E'
		elif dx == -2:
			self.dir = 'W'
		elif dy == 1:
			self.dir = 'S'
		elif dy == -1:
			self.dir = 'N'

	def pickup_item(self, item, room):
		if isinstance(item, item_.HealItem):
			self.hp += item.hp_healed;
			if self.hp > self.hp_max:
				self.hp = self.hp_max;
		else: # item is an ArmorPiece
			if self.armor[item.armor_slot].appearance != '  ':
				self.armor[item.armor_slot].x = self.x
				self.armor[item.armor_slot].y = self.y
				room.add_item(self.armor[item.armor_slot])
			self.armor[item.armor_slot] = item
		self.armor_val = sum(item.armor_val for item in self.armor.values());

	def get_hit(self, damage):
		damage = math.ceil(damage * (1-self.armor_val/25));
		self.hp -= damage;

	def restore_pos(self):
		self.x, self.y = self.prev_x, self.prev_y;

	def render(self, window, stats_window):
		window.addstr(self.y, self.x, '°°');
		stats_window.addstr('<3' * (self.hp // 2) + '-3' * (self.hp % 2));
		stats_window.addstr(1, 0, self.armor['helm'].appearance)
		stats_window.addstr(1, 2, self.armor['chest'].appearance)
		stats_window.addstr(1, 4, self.armor['legs'].appearance)
		stats_window.addstr(1, 6, self.armor['boots'].appearance)
