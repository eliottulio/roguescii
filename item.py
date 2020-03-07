class Item:
    def __init__(self, x, y, appearance):
        self.x = x;
        self.y = y;
        self.appearance = appearance;

    def render(self, window):
        window.addstr(self.y, self.x, self.appearance);

class HealItem(Item):
    def __init__(self, x, y, appearance, hp_healed):
        super(HealItem, self).__init__(x, y, appearance);
        self.hp_healed = hp_healed;

class ArmorPiece(Item):
    def __init__(self, x, y, appearance, armor_val, armor_slot):
        super(ArmorPiece, self).__init__(x, y, appearance);
        self.armor_val = armor_val;
        self.armor_slot = armor_slot;
