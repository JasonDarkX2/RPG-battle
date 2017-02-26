from classes. game import Person, bcolors
import random

class Enemy(Person):

    def __int__(self):
        Person.__init__(self)

    def get_enemy_stats(self):
        hp_bar = ""
        hpfill = "█"
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        hpbar_diff = 50 - len(hp_bar) + 1
        if hpbar_diff == 51:
            hpbar_diff = 160
            hpfill = " "
            hp_bar = ""
        hpts_diff = len(str(self.maxhp)) - len(str(self.hp)) + 3
        alignment = 112
        print(
            "______________________________________________________________________________________".rjust(alignment, " "))
        print(
            self.name
            + bcolors.BOLD
            + "         "
            + str(self.hp).rjust(hpts_diff, ' ')
            + "/"
            + str(self.maxhp)
            + bcolors.ENDC +
            "|"
            + bcolors.FAIL
            + hp_bar
            + bcolors.ENDC
            + "|".rjust(hpbar_diff, hpfill))

    def enemy_Spell(self, players):

        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_spell_damage()
        if self.mp == 0:
            self.enemy_atk(players)
            return False
        if self.mp < spell.cost:
            self.enemy_Spell()
        else:
            self.mp -= spell.cost
            target = random.randrange(0, len(players))
            players[target].take_damage(magic_dmg)
            print(self.name, spell.name + " attack dealt ", magic_dmg, " points of damage to ", players[target].name)

    def enemy_item(self, players):
        if len(self.item) == 0:
            self.enemy_atk(players)
        else:
            item_choice = random.randrange(0, len(self.item))
            if self.item[item_choice]["qty"] == 0:
                del self.item[item_choice]
                self.enemy_item()
            target = random.randrange(0, len(players))
            item = self.item[item_choice]['item']
            dmg = item.prop
            players[target].take_damage(dmg)
            self.item[item_choice]["qty"] -= 1
            print(self.name, item.name + " dealt", str(dmg), "points of damage to ", players[target].name)

    def enemy_atk(self, players):
        target = random.randrange(0, len(players))
        enemy_dmg = self.generate_damage()
        players[target].take_damage(enemy_dmg)
        print(self.name, " attack dealt", enemy_dmg, "points of damage to ", players[target].name)




