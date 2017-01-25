from classes.game  import  Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
# Instantiating black magic
fire= Spell("Fire",10, 160,"Black Magic")
thunder= Spell("Thunder",10, 100,"Black Magic")
blizzard= Spell("Blizzard",10, 100,"Black Magic")
meteor= Spell("Meteor",20, 200,"Black Magic")
quake= Spell("Quake",14, 140,"Black Magic")

# Instantiating white magic
cure= Spell("Cure",12,120,"White Magic",)
cura= Spell("Cura",18,200, "White Magic",)

#instantiating items
potion= Item("Potion","potion", "heals 50 HP", 50)
highPotion= Item("High Potion","potion", "heals 100 HP", 100)
superPotion= Item(" Super Potion","potion", "heals 500 HP", 500)
elixer= potion= Item("Elixer","elixer", " Fully restore one party member   HP/MP", 50000)
highElixer= Item(" High elixer","elixer", " Fully restore  partys   HP/MP", 90000)
grenade = Item("Grenade", "attack", "deals 500 damage", 500)

# Instantiating people
player_magic = [fire,thunder,blizzard,meteor,cura]
player_item =[potion,highPotion,superPotion, elixer, highElixer,grenade]
player =Person(460,65,60,34,player_magic,player_item)
enemy=Person(1200,65,45,25,[],[])



running =True
i=0
print(bcolors.FAIL +bcolors.BOLD + "An enemy Attacks!" +bcolors.ENDC)

while running:
     print("===============")
     player.choose_action()
     choice = inputt = input("choose action :")
     index= int(choice)  - 1
     if index ==0:
            dmg=player.generate_damage()
            enemy.take_damage(dmg)
            print ("Your attacked deals", dmg, "points of damage.")
     elif  index  ==1 :
            player.choose_magic()
            magic_choice= int(input("Choose Magic:"))  - 1
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
                print(bcolors.OKBLUE + "\n" + spell.name +" heals  " + str(magic_dmg) + "  HP " + bcolors.ENDC )
            elif spell.type ==  "Black Magic":
                player.reduce_mp(spell.cost)
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), " points of damage" + bcolors.ENDC)
     elif index == 2:
         player.choose_item()
         item_choice= int(input( "choose item:" ))  - 1
         if item_choice == -1:
             continue
         item= player.item[item_choice]
         if item.type =="potion":
             player.heal(item.prop)
             print (bcolors.OKGREEN +"\n" + item.name + " heals " + str(item.prop) + "HP" + bcolors.ENDC)
         elif item.type == "elixer":
             player.hp= player.maxhp
             player.mp =player.maxmp
             print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
         elif item.type =="attack":
             enemy.take_damage(item.prop)
             print(bcolors.FAIL + "\n" + item.name + "  deals ",str(item.prop) , "points of damage"+ bcolors.ENDC)





     enemy_choice = 1
     enemy_dmg = enemy.generate_damage()
     player.take_damage(enemy_dmg)
     print("Enemy attack dealt", enemy_dmg, "points of damage" )
     print("------------------------------------")
     print("Enemy HP", bcolors.FAIL +  str(enemy.get_hp()) + "/" + str(enemy.get_max_hp() ) + bcolors.ENDC + "\n" )
     print("Your HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
     print("Your MP", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
     if enemy.get_hp() == 0:
         print(bcolors.OKGREEN +"You Win!!" +bcolors.ENDC)
         running=False
     elif player.get_hp() ==0:
         print(bcolors.FAIL + "You  have been defeated >.<" + bcolors.ENDC)
         running= False





