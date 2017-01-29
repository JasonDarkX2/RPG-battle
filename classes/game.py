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
        while len(mp_bar) < 10:
                mp_bar += " "
        bar_diff=25-len(hp_bar)
        fill='█'
        if bar_diff ==25:
            bar_diff=75
            fill = ' '
            hp_bar = ' '
        print(bar_diff)

        hpts_diff = len(str(self.maxhp)) - len(str(self.hp))+3
        print(
        "                                         ________________________________                               _____________")
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
                    + "|".rjust(bar_diff, fill) +
                    bcolors.BOLD
                    + "               "
                    + str(self.mp)+"/"
                    + str(self.maxmp) + bcolors.ENDC
                    + "|" + bcolors.OKBLUE
                    + mp_bar
                    + bcolors.ENDC + "|")


