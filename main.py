from classes.game  import  Person, bcolors
from classes.magic import Spell
# Instantiating black magic
fire= Spell("Fire",10, 160,"black")
thunder= Spell("Thunder",10, 100,"black magic")
blizzard= Spell("Blizzard",10, 100,"black magic")
meteor= Spell("Meteor",20, 200,"black magic")
quake= Spell("Quake",14, 140,"black magic")

# Instantiating white magic
cure= Spell("Cure",12,120,"White")
cura= Spell("Cura",18,200, "White Magic")
# Instantiating people
player =Person(460,65,60,34,[fire,thunder,blizzard,meteor,cura])
enemy=Person(1200,65,45,25,[])



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
            spell=  player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()


            current_mp= player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL +"\n N ot enough Magic points" +bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), " points of damage" + bcolors.ENDC)



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





