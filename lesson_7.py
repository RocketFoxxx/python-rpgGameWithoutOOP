import random

def rpg():

    # player template
    player = {
    "name": "",
    "xp": 0,
    "lvl": 0,
    "hp": 50,
    "mana": 25,
    "attack": 10,
    "defense": 2,
    "gold": 0,
    "inventory": {"HP Potion": 1,
                  "Mana Potion": 1,
                  "Gauntlets of Void": 1}
}  

    # enemy template
    enemies = [
    {"name": "Goblin", "hp": 30, "attack": 6, "gold": 10, "xp": 8},
    {"name": "Orc", "hp": 45, "attack": 8, "gold": 20, "xp": 10},
    {"name": "Slime", "hp": 20, "attack": 3, "gold": 5, "xp": 5},
]   
    
    # invt of merchant
    merchant_invt = {
        "HP Potion": {"amount": 56, "price": 20},
        "Mana Potion": {"amount": 32, "price": 30},
        "Shield of Knights": {"amount": 56, "price": 181},
        "Helmet of Winged Hussar": {"amount": 1, "price": 436},
}
    
    merchant_dialogues = ["Greetings traveler.", 
                          "You look tired… need potions?", 
                          "Business is business."]


    def show_stats():
        for k, v in player.items():
            print(k.capitalize(), "->", v)
    
    # user wants to continue(like imagine we also have db, so its imitation) or new hero with default stats
    def new_or_continue():
        while True:
            print("==== Welcome to DND v1.0 ====")
            print("1. Continue")
            print("2. New Game")

            action = input("You choice: ")

            if action == "1":
                print("Loading your character.")
                player["name"] = "emilo"
                player["hp"] = 3
                player["gold"] = 700
                player['xp'] = 33
                break
        
            elif action == "2":
                hero_name = input("Welcome, hero! Enter your name: ")
                player["name"] = hero_name
                break

            else:
                print("Try again.")

    # level system and boosting some stats by lvl uping
    def get_level():
        level_barrier = [0, 10, 50, 100, 300, 500, 1000, 1800]
        lvl = len([s for s in level_barrier if player["xp"] > s])
        player["lvl"] = lvl
        if lvl > 0:
            player["attack"] += int(lvl * 1.5)
            player["hp"] += int(lvl * 2)
        else:
            pass
    
    new_or_continue()
    get_level()

    # invt, amount checks
    # check if item is in invt
    def get_item(invt, text):
        item = input(text)
        if item not in invt:
            print("No such item.")
            return None
        return item
            
    # checking item amount, if its <= 0 then del it
    def get_amount(invt, item_name):
        invt[item_name] -= 1
        if invt[item_name] <= 0:
            del invt[item_name]
        else:
            pass

    # checker for merchant
    def get_amount_merch(invt, item , amount):
        invt[item]["amount"] -= amount
        if invt[item]["amount"] <= 0:
            del invt[item]
        else:
            pass
    
    def percentage(part, whole):
        return (part * whole) / 100
    
    def get_att():
        return player["attack"]
    

    '''
    def get_choice_of_att(att_type):
        while True:
            choice = input(att_type)

            player_dmg = get_att()

            if choice == "1":
                break
            elif choice == "2":
                print("qui")
                player_dmg = 2
                break
            elif choice == "3":
                print("hea")
                break
            elif choice == "4":
                print("def")
                break
            else:
                print("Try again.")

            player["attack"]
    
    
    def get_miss_or_hit(choice):
        chances = [1, 21]
        missed = False
        rand = random.randint(chances)
        if choice == "1":
            if rand <= 15:
                pass
            else:
                print("You missed.")
    '''

    def get_crit():
        crit = random.randint(1, 11)
        if crit <= 6:
            return True
        else:
            return False
    
    def get_limit_hp():
        max_hp = 100
        if player["hp"] > max_hp:
            print("You reached max hp.")
            player["hp"] = max_hp
        else:
            pass

    def get_game_over():
        print("YOU DIED")
        print("I am weak...")
        print("But...")
        print("I have a chance to continue.")
        print("1. CONTINUE or 2. EXIT")

        choice = input("Your choice: ")

        while True:
            if choice == "1":
                rpg()

            elif choice == "2":
                quit()
            
            else:
                print("Try again.")
        

    while True:
        print("=== MENU ===")
        print("1. Explore")
        print("2. Inventory")
        print("3. Shop")
        print("4. Show stats")
        print("5. Exit")

        action = input("Your choice: ")

        get_limit_hp()

        # 1. EXPLORE
        if action == "1":
            # getting random enemy from enemies
            enemy = random.choice(enemies)

            enemy_hp = enemy["hp"]
            # assigning values from enemies like hp and gold, OLDER LOGIC
            #enemy_name = enemy["name"]
            #enemy_gold = enemy["gold"]

            # check, is player tried to escape or not
            tried_to_escape = False

            print("A wild", enemy["name"].lower(), "appears!")

            print("You: ", player["hp"], "HP")
            print(enemy["name"], ": ", enemy_hp, "HP")

            while True:
                print("1. Attack")
                print("2. Run")

                battle_action = input("Choose: ")

                if battle_action == "1":
                    print(f"1. Regular attack === regular damage, 25% chance to miss")
                    print(f"2. Quick Slash === 75% damage but guaranteed hit")
                    print(f"3. Heavy Strike === double damage, 50% chance to miss")
                    print(f"4. Guard === +50% defense for 1 turn")

                    choice = input("Your choice: ")

                    # variables for battle, to avoid changing in dict const stats
                    battle_dmg = player["attack"]

                    battle_def = player["defense"]

                    missed = False

                    skip = False

                    # 20 part chance sys, so n = 5%
                    miss_or_hit = random.randint(1, 21)

                    while True:
                        if choice == "1":
                            if miss_or_hit >= 15:
                                pass
                            else:
                                missed = True
                            break
                    
                        elif choice == "2":
                            temp_dmg = percentage(75, battle_dmg)
                            battle_dmg = int(temp_dmg)
                            break

                        elif choice == "3":
                            if miss_or_hit <= 10:
                                temp_dmg = percentage (200, battle_dmg)
                                battle_dmg = int(temp_dmg)
                            else:
                                missed = True
                            break
                    
                        elif choice == "4":
                            temp_def = percentage(150, battle_def)
                            battle_def = int(temp_def)
                            skip = True
                            break

                        else:
                            print("Try again.")

                    # adding crit if its TRUE
                    crit = get_crit()
                    if crit == True:
                        battle_dmg = int(battle_dmg * 1.5)
                    else:
                        pass
                    
                    if missed == False and skip == False:
                        enemy_hp -= battle_dmg
                        print("You deal ", battle_dmg, "damage!")

                        # calc player hp
                        player["hp"] -= enemy["attack"] - battle_def
                        print(enemy["name"],"deals ", enemy["attack"] - battle_def, "damage!")

                    elif missed == True:
                        print("You missed!")

                        # calc player hp
                        player["hp"] -= enemy["attack"] - battle_def
                        print(enemy["name"],"deals ", enemy["attack"] - battle_def, "damage!")
                    
                    elif skip == True:
                        print("You focused on your defense!")

                        # calc player hp
                        player["hp"] -= enemy["attack"] - battle_def
                        print(enemy["name"],"deals ", enemy["attack"] - battle_def, "damage!")

                elif battle_action == "2":
                    if tried_to_escape != True:
                        print("You're trying to escape!")
                        escape = random.randint(1,2)
                        if escape == 1:
                            print("Luck is on your side, hero. You escaped.")
                            break
                        else:
                            # myb tried_escape = true?, and if its true then this option is not even possible +++smartness from me
                            # idk how to make to player had only one chance to escape, bc now every turn player has chance to escape(its realistic, but still)
                            tried_to_escape = True
                            player["hp"] -= enemy["attack"]
                            print(enemy["name"],"deals ", enemy["attack"], "damage!")

                            print("You failed to escape. Fight!")
                    elif tried_to_escape != False:
                        print("You can't escape.")
                
                # end of the battle, player or enemy hp <= 0
                if player["hp"] <= 0:
                    get_game_over()

                elif enemy_hp <= 0:
                    print("Enemy defeated! You found ", enemy["gold"],"gold.")
                    print("You gained ", enemy["xp"], "XP.")

                    # adding gold and xp to player
                    player["gold"] += enemy["gold"]
                    player["xp"] +=enemy["xp"]

                    break
        
        # 2. INVENTORY
        elif action == "2":
            # assigning to invt, bc then its easier to make iteration etc.
            invt = player["inventory"]
            
            while True:
                print("====", player["name"], " inventory ====")
                # like python for its dynamic, like if dict is empty then it becomes false and I can easily use it
                if bool(invt) == False:
                        print("Your inventory is empty")
                else:
                    for k, v in invt.items():
                        print("Item name: ", k, ", Amount: ", v)

                get_limit_hp()

                print("1. Use item")
                print("2. Equip Item")
                print("2. Leave inventory")

                action = input("Your choice: ")

                if action == "1":
                    # there also could be check like is it sword, shield(like uneatable thing), so player
                    # cant use this kind of items
                    item_name = get_item(invt, "Enter item name that you want to use: ")
                    if not item_name: continue

                    # check if item is usable
                    if item_name not in ["HP Potion", "Mana Potion"]:
                        print("You can't use this item.")
                        continue

                    # checking what potion, and updating hp or mana
                    if item_name == "HP Potion":
                        player["hp"] += 10

                    elif item_name == "Mana Potion":    
                        player["mana"] += 10

                    get_amount(invt, item_name)

                elif action == "2":
                    item_name = get_item(invt, "Enter item name that you want to equip: ")
                    if not item_name: continue

                    if item_name not in ["HP Potion", "Mana Potion"]:
                        get_amount(invt, item_name)

                        if item_name == "Gauntlets of Void":
                            player["defense"] += 5

                        elif item_name == "Helmet of Winged Hussars":
                            player["defense"] += 8

                    else:
                        print("You can't use this item.")
                        continue
                
                elif action == "3":
                    break
                else:
                    print("Try again.")
        
        # 3. SHOP
        elif action == "3":
            dialogue = random.choice(merchant_dialogues)
            print("Merchant:", dialogue)
            print("Merchant: Take a look, traveler.")
            print("==== Merchant inventory ====")
            for x, obj in merchant_invt.items():
                print("Item name: ", x)
                for y in obj:
                    print(y.capitalize(), ": ", obj[y])

            while True:

                print("1. Buy item")
                print("2. Leave merchant")

                action = input("Your choice: ")

                if action == "1":
                    item_name = get_item(merchant_invt, "Enter item name that you want to buy: ")
                    if not item_name: continue

                    amount = int(input("Enter amount: "))

                    if merchant_invt[item_name]["amount"] >= amount:

                        total_cost = merchant_invt[item_name]["price"] * amount

                        if total_cost <= player["gold"]:
                            print("You will buy ", item_name, ", amount: ", amount,", it will cost you: ", total_cost, " gold.")
                        
                            # check amount in merchant inv
                            get_amount_merch(merchant_invt, item_name, amount)

                            cart = {item_name:amount}
                            player["inventory"].update(cart)
                            player["gold"] -= total_cost
                            print("Deal was succesfull.")
                            break
                        else:
                            print("You don't have enough money.")
                    else:
                        print("Merchant don't have enough amount.")


                elif action == "2":
                    break
                
                else:
                    print("Try again.")

        # 4. STATS
        elif action == "4":
            show_stats()
        
        # 5. EXIT
        elif action == "5":
            break

        else:
            print("Try again.")

rpg()

# add dialogues for merchant with random, make unusable items in inv, finish shop
# , and chatgpt recommendation like special moves, crit