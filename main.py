from classes.game  import  Person, bcolors
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
sentry = Item("Sentry", "attack", "deals 500 damage", 1000)

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
player1 =Person("Player1 ",1000,132,600,340,player_magic,player_item)
player2 =Person("Player2 ",4600,188,60,34,player_magic,player_item)
player3 =Person("Player3 ",4600,174,60,34,player_magic,player_item)
players= [player1,player2,player3]
enemy1=Person("Dragon1",1250,130,560,325,enemy_magic,enemy_item)
enemy2=Person("Dragon2 ",1200,100,20,25,enemy_magic,enemy_item)
enemy3=Person("Dragon3",1250,130,560,325,enemy_magic,enemy_item)
enemies=[enemy1,enemy2,enemy3]



running =True
i=0
print(bcolors.FAIL +bcolors.BOLD + "An enemy Attacks!" +bcolors.ENDC)
for enemy in enemies:
    enemy.get_enemy_stats()
while running:
     print("===============")
     print(
         "NAME                               HP                                                                                                    MP")
     for player in players:
         player.get_stats()
     for player in players:
         if len(enemies)==0:
             running=False
             break
         if player.get_hp()==0:
             continue
         else:
             player.choose_action()
             choice = inputt = input("     choose Action :")
             index= int(choice)  - 1
             if index ==0:
                    dmg=player.generate_damage()
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(dmg)
                    print (player.name+" attack deals", dmg, "points of damage to "+ enemies[enemy].name)
                    if enemies[enemy].get_hp() ==0:
                        print( enemies[enemy].name.replace(" ","") +"has been defeated")
                        del  enemies[enemy]
             elif  index  ==1 :
                    player.choose_magic()
                    magic_choice= int(input("    Choose Magic:"))  - 1
                    if magic_choice == -1:
                        continue
                    spell=  player.magic[magic_choice]
                    magic_dmg = spell.generate_spell_damage()


                    current_mp= player.get_mp()
                    if spell.cost > current_mp:
                        print(bcolors.FAIL +"\n Not enough Magic points" +bcolors.ENDC)
                        continue

                    if spell.type  == "White Magic":
                        player.heal(magic_dmg)
                        player.reduce_mp(spell.cost)
                        print(bcolors.OKBLUE + player.name + spell.name +" heals  " + str(magic_dmg) + "  HP " + bcolors.ENDC )
                    elif spell.type ==  "Black Magic":
                        player.reduce_mp(spell.cost)
                        enemy = player.choose_target(enemies)
                        enemies[enemy].take_damage(magic_dmg)
                        print(bcolors.OKBLUE +   player.name+ spell.name + " deals " + str(magic_dmg), " points of damage to " + enemies[enemy].name+ bcolors.ENDC)
                        if enemies[enemy].get_hp() == 0:
                            print(enemies[enemy].name.replace(" ", "") + "has been defeated")
                            del enemies[enemy]
             elif index == 2:
                 player.choose_item()
                 item_choice= int(input( "choose item:" ))  - 1
                 if item_choice == -1:
                     continue
                 item= player.item[item_choice]["item"]
                 if player.item[item_choice]["qty"] <=0:
                     print(bcolors.FAIL+ "\n"+" None Left....."+bcolors.ENDC)
                     continue
                 player.item[item_choice]["qty"] -= 1
                 if item.type =="potion":
                     player.heal(item.prop)
                     print (bcolors.OKGREEN +"\n" + item.name + " heals " + str(item.prop) + "HP" + bcolors.ENDC)
                 elif item.type == "elixer":
                     player.hp= player.maxhp
                     player.mp =player.maxmp
                     print(bcolors.OKGREEN + player.name + item.name + " fully restores HP/MP" + bcolors.ENDC)
                 elif item.type =="attack":
                     enemy = player.choose_target(enemies)
                     enemies[enemy].take_damage(item.prop)
                     print(bcolors.FAIL +player.name+ item.name + "  deals ",str(item.prop) , "points of damage to "+ enemies[enemy].name + bcolors.ENDC)
                     if enemies[enemy].get_hp() == 0:
                         print(enemies[enemy].name.replace(" ", "") + "has been defeated")
                         del enemies[enemy]
             print("______________________________________")

     if len(enemies)>0:
         enemy_choice= 2 ##random.randrange(0,2)
         for enemy in enemies:
             if enemy_choice == 0:
                 target = random.randrange(0, 3)
                 enemy.enemy_atk(players)
             elif enemy_choice ==1:
                 spell=enemy.enemy_Spell()
                 target = random.randrange(0, 3)
                 players[target].take_damage(spell[1])
                 print(enemy.name,  spell[0].name+ " spell dealt", spell[1], "points of damage to ", players[target].name)
             elif enemy_choice ==2:
                 if len(enemy.item)!=0:
                     item_choice=enemy.enemy_item()
                     target = random.randrange(0, 3)
                     if(item_choice==False):
                         enemy.enemy_atk(players)
                     else:
                         players[target].take_damage(item_choice[1])
                         print(enemy.name,  item_choice[0].name+ " dealt", item_choice[1], "points of damage to ", players[target].name)
                         enemy.item[item_choice[2]]["qty"] -= 1
             else:
                 enemy.enemy_atk(players)

         for enemy in enemies:
             enemy.get_enemy_stats()
     else:

            ## player win
            print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
            running = False
#check if players lost
defeated_players =0
for player in players:
        if player.get_hp() ==0:
            defeated_players +=1
        if defeated_players ==2:
             print(bcolors.FAIL + "You  have been defeated >.<" + bcolors.ENDC)
             running= False





