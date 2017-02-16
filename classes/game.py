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

