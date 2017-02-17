from classes. game import Person, bcolors
import random

class Player(Person):

    def __int__(self):
        Person.__init__(self)

    def choose_target(self,enemies):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print ("         "+ str(i) + ".", enemy.name)
                i+=1
        choice =input("    Choose Target:")
        return int(choice) -1


    def choose_action(self):
        i = 1
        print( "     "+bcolors.BOLD +self.name + bcolors.ENDC + "\n"+ bcolors.OKBLUE +  bcolors.BOLD + "     ACTION" + bcolors.ENDC)
        for item in self.actions:
            print("         "+ str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("     "+bcolors.BOLD +self.name + bcolors.ENDC + "\n"+  bcolors.OKBLUE +"      MAGIC" +bcolors.ENDC)
        for spell in self.magic:
            print("         "+str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
    def choose_item(self):
        i = 1
        print( "     "+bcolors.BOLD +self.name + bcolors.ENDC + "\n"+ bcolors.OKGREEN + "      ITEMS" + bcolors.ENDC)
        for item in self.item:
            print("         "+str(i) + ":", item["item"].name, ":", item["item"].description, "(x"+str(item["qty"])+ ")")
            i += 1
    def get_stats( self):
        hp_bar=""
        mp_bar=""
        bar_ticks = (self.hp/ self.maxhp) * 100 / 4
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        while bar_ticks  > 0:
            hp_bar += "█"
            bar_ticks-=1
        while mp_ticks  > 0:
            mp_bar += "█"
            mp_ticks-=1
        hpbar_diff=25-len(hp_bar)+1
        hpfill='█'
        if hpbar_diff ==26:
            hpbar_diff=75
            hpfill = ' '
            hp_bar = ' '
        mpbar_diff= 10- len(mp_bar)+1
        mpfill= '█'
        if mpbar_diff ==11:
            mpbar_diff=50
            mpfill=''
            mp_bar=''
        hpts_diff = len(str(self.maxhp)) - len(str(self.hp))+3
        mpts_diff = len(str(self.maxmp)) - len(str(self.mp)) + 3
        alignment= (len(str(self.maxhp))*2)+len(self.name)
        print(
        "                                             ________________________________                                _____________")
        print(
                    self.name
                    + bcolors.BOLD
                    + "         "
                    +str(self.hp).rjust(hpts_diff,' ')
                    +"/"
                    + str(self.maxhp)
                    + bcolors.ENDC +
                    "|"
                    + bcolors.OKGREEN
                    + hp_bar
                    + bcolors.ENDC
                    + "|".rjust(hpbar_diff, hpfill) +
                    bcolors.BOLD
                    + "               "
                    + str(self.mp).rjust(mpts_diff,' ')+
                    "/"
                    + str(self.maxmp)
                    + bcolors.ENDC
                    + "|"
                    +bcolors.OKBLUE
                    + mp_bar
                    + bcolors.ENDC
                    + "|".rjust(mpbar_diff, mpfill)
                    )
    def player_atk(self, enemy):
        dmg = self.generate_damage()
        target = self.choose_target(enemy)
        enemy[target].take_damage(dmg)
        print(self.name + " attack deals", dmg, "points of damage to " + enemy[target].name)
        if enemy[target].get_hp() == 0:
            print(enemy[target].name.replace(" ", "") + "has been defeated")
            del enemy[target]

    def player_magic(self, enemy):
        self.choose_magic()
        spell=""
        magic_choice = int(input("    Choose Magic:")) - 1
        if magic_choice == -1:
            self.player_magic(enemy)
        else:
            spell = self.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()

            current_mp = self.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + "Not enough Magic points" + bcolors.ENDC)
                self.player_magic(enemy)

            if spell.type == "White Magic":
                self.heal(magic_dmg)
                self.reduce_mp(spell.cost)
                print(bcolors.OKBLUE + self.name + spell.name + " heals  " + str(magic_dmg) + "  HP " + bcolors.ENDC)
            elif spell.type == "Black Magic":
                self.reduce_mp(spell.cost)
                target = self.choose_target(enemy)
                enemy[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + self.name + spell.name + " deals " + str(magic_dmg),
                      " points of damage to " + enemy[target].name + bcolors.ENDC)
                if enemy[target].get_hp() == 0:
                    print(enemy[target].name.replace(" ", "") + "has been defeated")
                    del enemy[target]

    def player_item(self,enemy):
            self.choose_item()
            item_choice = int(input("choose item:")) - 1
            if item_choice == -1:
                self.player_item(enemy)
            item = self.item[item_choice]["item"]
            if self.item[item_choice]["qty"] <= 0:
                print(bcolors.FAIL  + " None Left....." + bcolors.ENDC)
            else:
                self.item[item_choice]["qty"] -= 1
                if item.type == "potion":
                    self.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals " + str(item.prop) + "HP" + bcolors.ENDC)
                elif item.type == "elixer":
                    self.hp = self.maxhp
                    self.mp = self.maxmp
                    print(bcolors.OKGREEN + self.name + item.name + " fully restores HP/MP" + bcolors.ENDC)
                elif item.type == "attack":
                    target = self.choose_target(enemy)
                    enemy[target].take_damage(item.prop)
                    print(bcolors.FAIL + self.name + item.name + "  deals ", str(item.prop),
                          "points of damage to " + enemy[target].name + bcolors.ENDC)
                    if enemy[target].get_hp() == 0:
                        print(enemy[target].name.replace(" ", "") + "has been defeated")
                        del enemy[target]

