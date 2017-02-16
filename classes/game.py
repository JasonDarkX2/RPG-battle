import random

class bcolors:
        HEADER = '\033[95m'
        OKBLUE= '\033[94m'
        OKGREEN= '\033[92m'
        WARNING= '\033[93m'
        FAIL= '\033[91m'
        ENDC= '\033[0m'
        BOLD= '\033[1m'
        UNDERLINE= '\033[4m'


class Person:
    def __init__(self, name,hp,mp,atk,df,magic, items):
            self.name=name
            self.maxhp=hp
            self.hp=hp
            self.maxmp=mp
            self.mp=mp
            self.atkl=atk - 10
            self.atkh= atk + 10
            self.df=df
            self.magic=magic
            self.item= items
            self.actions =["Attack","Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)



    def take_damage(self,dmg):
            self.hp-=dmg
            if(self.hp<0):
                    self.hp = 0
                    return self.hp

    def get_hp(self):
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp>self.maxhp:
            self.hp= self.maxhp



    def get_mp(self):
        return self.mp

    def get_max_hp(self):
        return self.maxhp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]

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
    def get_enemy_stats(self):
        hp_bar = ""
        hpfill = "█"
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        while bar_ticks  > 0:
            hp_bar += "█"
            bar_ticks-=1
        hpbar_diff = 50 - len(hp_bar) + 1
        if hpbar_diff== 51:
            hpbar_diff=160
            hpfill = " "
            hp_bar=""
        hpts_diff = len(str(self.maxhp)) - len(str(self.hp)) + 3
        alignment= 111
        print(
            "________________________________________________________________".rjust(alignment," "))
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
            + "|".rjust(hpbar_diff, hpfill) )

    def enemy_Spell(self,players):

        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_spell_damage()
        if self.mp==0:
            self.enemy_atk(players)
            return False
        if self.mp < spell.cost:
            self.enemy_Spell()
        else:
            self.mp-= spell.cost
            target = random.randrange(0, len(players))
            players[target].take_damage(magic_dmg)
            print(self.name,  spell.name +" attack dealt ", magic_dmg, " points of damage to ", players[target].name)

    def enemy_item(self,players):
        if len(self.item)==0:
            self.enemy_atk(players)
        else:
            item_choice=random.randrange(0, len(self.item))
            if self.item[item_choice]["qty"] == 0:
                del self.item[item_choice]
                self.enemy_item()
            target=random.randrange(0, len(players))
            item=self.item[item_choice]['item']
            dmg=item.prop
            players[target].take_damage(dmg)
            self.item[item_choice]["qty"]-=1
            print(self.name,  item.name+ " dealt", str(dmg), "points of damage to ", players[target].name)




    def enemy_atk(self,players):
        target = random.randrange(0, len(players))
        enemy_dmg = self.generate_damage()
        players[target].take_damage(enemy_dmg)
        print(self.name, " attack dealt", enemy_dmg, "points of damage to ", players[target].name)