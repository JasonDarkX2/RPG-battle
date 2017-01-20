from classes.game  import  Person, bcolors
magic =[{"name": "Fire","cost": 10, "dmg":160},
                {"name": "Thunder", "cost": 12, "dmg": 124},
                {"name": "Bilizzard", "cost": 10, "dmg": 100}]

player =Person(460,65,60,34,magic)
enemy=Person(1200,65,45,25,magic)

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
            magic_dmg= player.generate_spell_damage(magic_choice)
            spell=player.get_spell_name(magic_choice)
            cost=player.get_spell_cost(magic_choice)
            current_mp= player.get_mp()
            if cost > current_mp:
                print(bcolors.FAIL +"\n N ot enough Magic points" +bcolors.ENDC)
                continue

            player.reduce_mp(cost)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell + " deals " + str(magic_dmg), " points of damage" + bcolors.ENDC)



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





