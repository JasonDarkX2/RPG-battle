from classes.game  import  Person, bcolors
from classes.enemy import Enemy
from classes.player import Player
from classes.magic import Spell
from classes.inventory import Item
import random

# Instantiating black magic
fire= Spell("Fire",10, 160,"Black Magic")
thunder= Spell("Thunder",30, 100,"Black Magic")
blizzard= Spell("Blizzard",30, 100,"Black Magic")
meteor= Spell("Meteor",40, 200,"Black Magic")
quake= Spell("Quake",14, 140,"Black Magic")

# Instantiating white magic
cure= Spell("Cure",52,120,"White Magic",)
cura= Spell("Cura",38,200, "White Magic",)

#instantiating items
potion= Item( "Potion","potion", "heals 50 HP", 50)
highPotion= Item("High Potion","potion", "heals 100 HP", 100)
superPotion= Item(" Super Potion","potion", "heals 500 HP", 500)
elixer= potion= Item("Elixer","elixer", " Fully restore one party member  HP/MP", 50000)
highElixer= Item(" High elixer","elixer", " Fully restore  partys  HP/MP", 90000)
grenade = Item("Grenade", "attack", "deals 500 damage", 500)
sentry = Item("Sentry", "attack", "deals 800 damage", 800)

# Instantiating people
enemy_magic=[fire,thunder,blizzard,meteor]
player_magic = [fire,thunder,blizzard,meteor,cura]
player_item =[{"item":potion,"qty": 15},{"item":highPotion, "qty":5},
                          {"item": superPotion, "qty": 5}, {"item":elixer,"qty": 5},
                          {"item":highElixer, "qty":5},{"item":grenade, "qty": 2}
                         ]
enemy_item=[{"item":grenade, "qty": 1},
                            {"item":sentry, "qty":1}
                        ]
player1 =Player("Player1 ",1000,2,600,340,player_magic,[])
player2 =Player("Player2 ",4600,188,60,34,player_magic,player_item)
player3 =Player("Player3 ",4600,174,60,34,player_magic,player_item)
players= [player1]
enemy1=Enemy("Dragon1",1250,130,560,325,enemy_magic,enemy_item)
enemy2=Enemy("Dragon2 ",1200,100,20,25,enemy_magic,enemy_item)
enemy3=Enemy("Dragon3",1250,130,560,325,enemy_magic,enemy_item)
enemies=[enemy1,enemy2]



running =True
i=0
print(bcolors.FAIL +bcolors.BOLD + "An enemy Attacks!" +bcolors.ENDC)
for enemy in enemies:
    enemy.get_enemy_stats()
while running:
     print("===============")
     print(
         "NAME                       HP                                                                MP")
     for player in players:
         player.get_stats()
     for player in players:
         if len(enemies)==0:
             running=False
             break
         if player.get_hp()==0:
             continue
         else:
             invalid=True
             while invalid :
                 player.choose_action()
                 choice = inputt = input("     choose Action :")
                 index= int(choice)  - 1
                 if index ==0:
                     player.player_atk(enemies)
                     invalid=False
                 elif  index  ==1 :
                     if player.get_mp()<player.lowest_mp_cost():
                         print(bcolors.FAIL + "    Not enough Magic points" + bcolors.ENDC)
                         invalid=True
                     else:
                         player.player_magic(enemies)
                         invalid=False
                 elif index == 2:
                     if len (player.item)==0:
                         print(bcolors.FAIL + "    No items in inventory" + bcolors.ENDC)
                         invlaid=True
                     else:
                         player.player_item(enemies)
                         invalid=False
     print("______________________________________")

     if len(enemies)>0:
         enemy_choice= random.randrange(0,2)
         for enemy in enemies:
             if enemy_choice == 0:
                 enemy.enemy_atk(players)
             elif enemy_choice ==1:
                enemy.enemy_Spell(players)
             elif enemy_choice== 2:
                 enemy.enemy_item(players)



         for enemy in enemies:
             enemy.get_enemy_stats()
     ## player win
     if len(enemies) == 0:
         print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
         running = False
      ## player lose
     defeated_players = 0
     for player in players:
         if player.get_hp() == 0:
             defeated_players += 1
         if defeated_players == len(players):
             print(bcolors.FAIL + "You  have been defeated >.<" + bcolors.ENDC)
             running = False





