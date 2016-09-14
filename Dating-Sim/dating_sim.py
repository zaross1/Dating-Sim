#####################################
#   Jason Mortensen
#
#   This program runs in CodeSkulptor. 
# 
#
#####################################

import random
import simplegui
import math
sound_links = ["https://dl.dropboxusercontent.com/u/14028449/06.%20Jia%20Peng%20Fang%20-%20Playing%20Love%20(La%20Leggenda%20Del%20Pianista%20Sull'Oceano).mp3", "https://dl.dropboxusercontent.com/u/14028449/gameoptionsound.mp3", "https://dl.dropboxusercontent.com/u/14028449/combatabilitysound.mp3", "https://dl.dropboxusercontent.com/u/14028449/The%20Last%20Encounter%20(90s%20RPG%20Version)%20Short%20Loop.mp3"]
character_image_links = ["https://dl.dropboxusercontent.com/u/14028449/candy.png", "https://dl.dropboxusercontent.com/u/14028449/aoi.png", "https://dl.dropboxusercontent.com/u/14028449/kono.png", "https://dl.dropboxusercontent.com/u/14028449/kane.png", "https://dl.dropboxusercontent.com/u/14028449/taba.png", "https://dl.dropboxusercontent.com/u/14028449/cookie.png"]
icon_image_links = ["https://dl.dropboxusercontent.com/u/14028449/Valentine-day-27.png", "https://dl.dropboxusercontent.com/u/14028449/Valentine-day-04.png"]
candy_img = simplegui.load_image(character_image_links[0])
aoi_img = simplegui.load_image(character_image_links[1])
kono_img = simplegui.load_image(character_image_links[2])
kane_img = simplegui.load_image(character_image_links[3])
taba_img = simplegui.load_image(character_image_links[4])
cookie_img = simplegui.load_image(character_image_links[5])
heartkey = simplegui.load_image(icon_image_links[0])
heart = simplegui.load_image(icon_image_links[1])

starting_music = simplegui.load_sound(sound_links[0])
starting_music.set_volume(.4)

option_click_sound = simplegui.load_sound(sound_links[1])
option_click_sound.set_volume(.7)

combat_sound = simplegui.load_sound(sound_links[2])
combat_sound.set_volume(.7)

combat_music = simplegui.load_sound(sound_links[3])
combat_music.set_volume(.7)




class Ability(object):
    def __init__(self, name, mana_cost, stamina_cost, health_cost, bonus, attack_message, image):
        self.name = name
        self.image = image
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost
        self.health_cost = health_cost
        self.bonus = bonus
        self.attack_message = attack_message
        

            
               


images = [candy_img, aoi_img, kono_img, kane_img, taba_img, cookie_img]

basic_attacks = [Ability("Penny Toss", 0, 5, 0, 0, "tosses a penny at ", "image"), Ability("Tap Dance", 3, 3, 0, 0, "tap dances with", "image"),
                 Ability("Lick", 0, 4, 3, 1, " licks ", "image"), Ability("Insult", 3, 5, 4, 2, " insults ", "image")]

ability1_attacks = [Ability("Strong Kick", 0, 10, 2, 10, " strong kicks ", "image"), Ability("Flare", 15, 5, 5, 5, " casts flare on ", "image"), Ability("Slide", 15, 2, 5, 10, " slides into ", "image"), Ability("Acid Puddle", 10, 7, 8 , 13, " spills an acid puddle on ", "image")]

ability2_attacks = [Ability("Lightning Strike", 25, 5, 10, 15, " calls a lightning strike on ", "image"), Ability("Grope", 2, 20, 15, 20, " gropes ", "image"),
                    Ability("Fondle", 15, 8, 10, 18, " fondles ", "image"), Ability("Panty Slip", 10, 10, 8 , 19, " panty slips ", "image")]
                    
ability3_attacks = [Ability("Strip", 20, 20, -20, 20, " strips for ", "image"), Ability("Sexy Sox", 0, 15, -15, 13, " slips a sexy sox off for ", "image"),
                    Ability("Cheeky", 10, -20, 5, 10, " turns a cheek toward ", "image"), Ability("Topless", 20, 20, -30, 35, " rips shirt off for ", "image")]                    
 
        
        
            


class Character(object):

    def __init__(self, name, archtype, strength, dexterity, agility, intelligence, wisdom, default_attack, ability1, ability2, ability3, image):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.agility = agility
        self.default_attack = default_attack
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.name = name
        self.archtype = archtype
        self.level = 1
        self.image = image

        self.health = (100 * self.level) + (10 * self.strength)
        self.mana = 10 + (20 * self.wisdom)
        self.stamina = 50 + (20 * self.strength)
        
        self.current_health = self.health
        self.current_stamina = self.stamina
        self.current_mana = self.mana
        self.armor = (5 * self.level) + (.2 * self.strength)
        self.crit = .5 * self.dexterity
        self.crit_def = .5 * self.dexterity
        self.dodge = .1 * self.agility
        self.miss = 5 - (.11 * self.dexterity)
        
        if archtype == "caster":
            self. damage = (3 * self.intelligence)
        elif archtype == "melee":
            self. damage = (3 * self.strength) 
            
        self.experience_to_level = 200

    def use(self, ability):
            self.current_health -= ability.health_cost
            self.current_mana -= ability.mana_cost
            self.current_stamina -= ability.stamina_cost
    

def attack(attacker, defender, ability):
    global message
    if combat_toggle == True:
        attacker.use(ability)
        if (defender.current_health > 0) and (attacker.current_health > 0):
            miss_roll = random.randrange(1, 100)
            dodge_roll = random.randrange(1, 100)
            if miss_roll <= attacker.miss:
                message = attacker.name + " misses"
            elif dodge_roll <= defender.dodge:
                message = defender.name + " dodges " + attacker.name
            else:
                ran = random.randrange(1, 10) 
                damage = int( (ran / 10.0) * (attacker.damage + ability.bonus) - defender.armor)
                if damage <= 0:
                    damage = 2    
                defender.current_health -= damage
                message = attacker.name + ability.attack_message + defender.name + " for " + str(damage) + " points of damage."

            display_text(message, text1)
        combat_resolution()
def combat_resolution():
        global combat_toggle, combatover_toggle
        if player1.current_health <= 0:
            player1.current_health = 0
            combat_toggle = False
            combatover_toggle = True
            combat_music.pause()
            display_text(" ", text1)
            message = player1.name + " has been slain by " + enemy.name
            display_text(message, text1)
        elif enemy.current_health <= 0:
            combat_toggle = False
            combatover_toggle = True
            combat_music.pause()
            enemy.current_health = 0
            display_text(" ", text1)
            message = player1.name + " is victorious!"
            player1.experience_to_level -= 50
            display_text(message, text1)
            if player1.experience_to_level <= 0:
                level_up()
                
def level_up():
        player1.level += 1
        message = player1.name + " is now level " + str(player1.level)
        player1.strength += 3
        player1.stamina += 3
        player1.intelligence += 3
        player1.dexterity += 3
        player1.agility += 3
        player1.wisdom += 3
        
        if player1.archtype == "caster":
            player1.mana += 100
            player1.health += 50
        else:
            player1.mana += 25
            player1.health += 125
        display_text(" ", text1)
        display_text(message, text1)
        player1.experience_to_level = (200 * player1.level)

def clear_text(text):
    global clear_text1, clear_text2
    for x in range(len(text)):
        text[x] = ""


text1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
text2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

player1 = ""

text1_toggle = False
text2_toggle = False
title = ""
combat_toggle = False
stats_toggle = False
player_info_toggle = False
new_game_toggle = False
choose_character_toggle = False

candy_toggle = False
kane_toggle = False
taba_toggle = False
cookie_toggle = False
kono_toggle = False
aoi_toggle = False

combatover_toggle = False

show_enemy_toggle = False

select_flirt_fight_toggle = False

fight_text_toggle = False

character_chosen = False

character_info_toggle = False

player_main_options_toggle = False

characters_array = []
player1_attacks = []
enemy1_attack = []


def display_text(message, text):
    global text1, text2
    
    if (text[0] != "") and (text[1] != "") and (text[2] != "") and (text[3] != "") and (text[4] != "") and (text[5] != "") and (text[6] != " ") and (text[7] != "") and (text[8] != "") and (text[9] != "") and (text[10] != "") and (text[11] != "") and (text[12] != "") and (text[13] != ""):
        for x in range(len(text) - 1):
            text[x] = text[x + 1]
        text[-1] = message                     
    else:
        for x in range(len(text)):
            if text[x] == "":
                text[x] = message
                break 
                


                 

candy_bio = ["Candy has an extremely bubbly personality, and  she never holds back.", "When she's not smashing faces with a lacrosse racket, she plays the piano.", "In keeping with her rebellious spirit, while she's at home she strongly prefers ", "to wear nothing but her sensual and silky cat panties.",
             "The last few weeks have been very confusing for Candy. She's always been", "drawn to the strong, rugged types, but recently her dreams have featured boys", "with soft hands, and a soft gaze. She has begun to wonder if it has anything", "to do with the mysterious boy who transferred into her class recently.", "Candy wants to be a doctor when she grows up more than anything. So, when ", "the old doctor who she's been seeing on and off since she was a child offers", " her an internship, she's ecstatic. However, she is beginning to wonder if he", "has alterior motives. She thought she would do anything to become a doctor,", "but what if the doctor wants...something she isn't willing to give up?!?"]

kane_bio = ["Kane is the student council president, and he is ranked first at his school in", "every subject. The girls think he's dreamy, and all the teachers say he's got a", "great future ahead of him. But when it comes to Kane, things are darker and", "more complicated than they might initially seem.", "All Kane's ever wanted was a friend. But the girls are intimdated by his beauty", "and the other guys call him 'pretty boy' and 'tart' behind his back. Along with", "a deeply rooted sadness, Kane has a dark secret, something that keeps him up", "nights, and closes him off emotionally. ", "During the day he's just another high performing student, but when the sun", "goes down, he transforms into 'Stroker', a high class stripper at Cat Lounge.", "He hates it, but his brother has debts to the Yakuza, and without all that money", "Kane's brother is a dead man. He's so tired of the leering women and just wants it to", "stop. Kane is beginning to wonder if his brother is worth it.", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio"]

kono_bio = ["When Kono was younger the other kids called her 'bug eyes' and 'rabbit lover' ", "because of her large eyes and the stuffed rabbit she used to carry everywhere.", "But now no one teases her anymore because they're afraid of her. She's the", "school's kendo champion, and won't hesitate to resort to violence.", "She scorns all the boys in her grade, but she has a crush on Mr. Miyagi, the", "high school science teacher who has always had kind words for her. She has", "taken to following him home at night, and hiding in the bush outside while he", "and his wife eat dinner in their homely kitchen.", "She knows Kyako, his wife, doesn't appreciate him. She just shops all day, and", "complains all the time about being poor. But Kono has a plan. She knows she's", "right for him, but he's never going to realize it while he's with that witch. So, ", "this weekend, when Mr. Miyagi goes away for a conference, she plans to pay", "his wife a visit, and she's bringing her stick.", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio"]

taba_bio = ["Taba has street smarts his peers can only dream of. He used to live in the", "alleys of Tokyo with his sister, after his parents mysteriously disappeared", "one autumn day when Taba was six. When he's not in school, he manages and", "trains his sister,'tough-as-nails Tia', who fights in an underground fight ring.", "Although they really need the money, Taba is wondering whether he should try", "to convince Tia to give it up once and for all. But it's not just Taba's feelings", "about fighting that are starting to change. His sister is the most precious person", "in the world to him. ", "the only thing is... he's started to tread dangerous ground. His dreams used to", "be full of busty blonde euro dancers, but now when he wakes up to damp,", "sticky sheets, it's an image of Tia that lingers in his mind. And when they train", "together, his eyes are inexorably drawn to her svelte form, and generous", "breasts. His mind knows it's wrong, but his body is saying something else.", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio"]

aoi_bio = ["Aoi loves to ride her horse, Sable, around the secluded race track behind her", "family's ancestral home. When the new school year starts, Aoi is worried about", "not making any friends. She knows she's shy, but she vows to make seven",  "friends before the cherry blossoms fall.", "During a chemistry lab, Aoi partners with Cookie, the most popular and pretty",  "girl in the whole school,  and with uncharacteristic boldness, Aoi asks Cookie", "if she wants to ride Sable. Aoi is delighted and a little surprised that Cookie is", "so quick to agree.", "Aoi is a little nervous as they climb onto her horse - she doesn't want Cookie", "to fall and get hurt. But once Cookie's long legs are wrapped around Sable, she", "relaxes into Cookie's arms. She soon becomes aware of how very firm and ", "substantial Cookie's breasts feel against her back, and the way her hair slides",  "like liquid silk across Aoi's cheeks. Aoi wants to stay like this forever. ", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio"]

cookie_bio = ["Since freshman year, Cookie has been claiming to be dating a boy at another", "school. But it's all a lie. Cookie was embarrassed to admit that - among all her",  "friends -- she was the only one who hadn't made out with a boy. Of course, no", "one doubted her -- she was gorgeous, and everyone raved about her hair", "her legs, and breasts, purple eyes like nothing else in this world. But now", "she has her sights set on Eric, Aoi's handsome and studious brother. When Aoi", "invites Cookie for some horse riding, she's astonished at her good fortune.", "She's tired of lying, and it would be great to not have to worry about her parents", "finding her vibrator. As far as Cookie could tell, Eric had never had a girlfriend before.", "Which was perfect for her. Now, if she could figure out a way to get Aoi away", "from the house for a few hours, she could be alone with Eric. She had some", "new heels and a miniskirt that clung in all the right places she wanted to show", "him.", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio", "bio"]


def new_game():
    global character_chosen, combat_toggle, choose_character_toggle, player_main_options_toggle, show_enemy_toggle, select_flirt_fight_toggle, fight_text_toggle, text1, player_info_toggle, stats, title, new_game_toggle, chosen_character_toggle, starting_music
    title = "Click on a character to learn more."
    new_game_toggle = True
    choose_character_toggle = True
    character_info_toggle = True
    starting_music.rewind()
    starting_music.play()
    starting_music.set_volume(.7)
    toggle_off()
    combat_music.pause()
   
    
    select_flirt_fight_toggle = False
    show_enemy_toggle = False
    fight_text_toggle = False
    player_info_toggle = False
    stats_toggle = False
    player_main_options_toggle = False
    character_chosen = False
    combat_toggle = False
    
    

        



def mouse_handler(position):
    global combatover_toggle, combat_toggle, fight_text_toggle, select_flirt_fight_toggle, show_enemy_toggle, player_main_options_toggle, title, character_chosen, choose_character_toggle, character_info_toggle, candy_toggle, kono_toggle, aoi_toggle, taba_toggle, cookie_toggle, kane_toggle
    if character_chosen == False:
        for x in range(3):
            if ( position[0] >= (100 + (250 * x) )  and position[0] <= (300 + (250 * x) ) ) and (position[1] >= 100 and position[1] <= 300):
                    if x == 0:
                        candy_toggle = True


                    elif x == 1:
                        aoi_toggle = True

                    elif x == 2:
                        kono_toggle = True

                    choose_character_toggle = False
                    character_info_toggle = True
                    option_click_sound.rewind()
                    option_click_sound.play()
        for x in range(3):
            if ( position[0] >= (100 + (250 * x) )  and position[0] <= (300 + (250 * x) ) ) and (position[1] >= 350 and position[1] <= 550):
                    if x == 0:
                            kane_toggle = True
                    elif x == 1:
                            taba_toggle = True
                    elif x == 2:
                            cookie_toggle = True

                    choose_character_toggle = False
                    character_info_toggle = True
                    option_click_sound.rewind()
                    option_click_sound.play()

    if character_info_toggle and character_chosen == False:
        if ( (position[0] >= 550) and (position[0] <= 1000) ) and ( (position[1] >= 10) and (position[1] <= 75) ) :
            character_info_toggle = False
            choose_character_toggle = True
            toggle_off()
            title = "Click on a character to learn more."
            option_click_sound.rewind()
            option_click_sound.play()
        elif ( (position[0] >= 550) and (position[0] <= 900) ) and ( (position[1] >= 510) and (position[1] <= 570) ) :
            character_info_toggle = False
            choose_character_toggle = False
            character_creation()
            character_chosen = True
            player_main_options_toggle = True
            option_click_sound.rewind()
            option_click_sound.play()
            
    if player_main_options_toggle == True:
        if ( (position[0] >= 100) and (position[0] <= 350) )  and ( (position[1] >= 200) and (position[1] <= 260) ):
            travel_yes("science_lab")
            player_main_options_toggle = False
            show_enemy_toggle = True
            select_flirt_fight_toggle = True
         
        elif ( (position[0] >= 100) and (position[0] <= 350) )  and ( (position[1] >= 300) and (position[1] <= 360) ):
            travel_yes("arcade")
            player_main_options_toggle = False
            show_enemy_toggle = True 
            select_flirt_fight_toggle = True
           
        elif ( (position[0] >= 400) and (position[0] <= 580) )  and ( (position[1] >= 205) and (position[1] <= 255) ):
            travel_yes("cat_cafe")
            player_main_options_toggle = False
            show_enemy_toggle = True 
            select_flirt_fight_toggle = True
          
        elif ( (position[0] >= 400) and (position[0] <= 660) )  and ( (position[1] >= 300) and (position[1] <= 360) ):
            travel_yes("train_tracks")
            player_main_options_toggle = False
            show_enemy_toggle = True 
            select_flirt_fight_toggle = True
           
        elif ( (position[0] >= 250) and (position[0] <= 400) )  and ( (position[1] >= 410) and (position[1] <= 460) ):
            travel_yes("arcade")
            player_main_options_toggle = False
            select_flirt_fight_toggle = True
            show_enemy_toggle = True
           
            
            
    if select_flirt_fight_toggle == True:
            if ( (position[0] >= 385) and (position[0] <= 520) )  and ( (position[1] >= 150) and (position[1] <= 220) ): 
                fight_text_toggle = True
                select_flirt_fight_toggle = False
                clear_text(text1)
                combat_toggle = True
                combat_timer1.start()
                combat_restore_timer.start()
                option_click_sound.rewind()
                option_click_sound.play()
                combat_music.rewind()
                combat_music.play()
            elif ( (position[0] >= 400) and (position[0] <= 530) )  and ( (position[1] >= 65) and (position[1] <= 100) ):  
                combat_toggle = False
                fight_text_toggle = False
                player_main_options_toggle = True
                select_flirt_fight_toggle = False
                combat_timer1.stop()
                show_enemy_toggle = False
                option_click_sound.rewind()
                option_click_sound.play()
                
    if fight_text_toggle == True and combat_toggle == True :
        starting_music.pause()
        starting_music.rewind()
        if ( (position[0] >= 600) and (position[0] <= 750) )  and ( (position[1] >= 70) and (position[1] <= 100) ):
            if player1.default_attack.mana_cost >= player1.current_mana: 
                text = player1.name + " doesn't have enough mana to use " + player1.default_attack.name
                display_text(text, text1)
            elif player1.default_attack.stamina_cost >= player1.current_stamina:
                text = player1.name + " doesn't have enough stamina to use " + player1.default_attack.name
                display_text(text, text1)
            elif player1.default_attack.health_cost >= player1.current_health:
                text = player1.name + " doesn't have enough health to use " + player1.default_attack.name
                display_text(text, text1)
            else:
                attack(player1, enemy, player1.default_attack)
            combat_sound.rewind()
            combat_sound.play()
        elif ( (position[0] >= 600) and (position[0] <= 750) )  and ( (position[1] >= 110) and (position[1] <= 135) ): 
            if player1.ability1.mana_cost >= player1.current_mana: 
                text = player1.name + " doesn't have enough mana to use " + player1.ability1.name
                display_text(text, text1)
            elif player1.ability1.stamina_cost >= player1.current_stamina:
                text = player1.name + " doesn't have enough stamina to use " + player1.ability1.name
                display_text(text, text1)
            elif player1.ability1.health_cost >= player1.current_health:
                text = player1.name + " doesn't have enough health to use " + player1.ability1.name
                display_text(text, text1)
            else:
                attack(player1, enemy, player1.ability1)
            combat_sound.rewind()
            combat_sound.play()
        elif ( (position[0] >= 600) and (position[0] <= 750) )  and ( (position[1] >= 145) and (position[1] <= 175) ): 
            if player1.ability2.mana_cost >= player1.current_mana: 
                text = player1.name + " doesn't have enough mana to use " + player1.ability2.name
                display_text(text, text1)
            elif player1.ability2.stamina_cost >= player1.current_stamina:
                text = player1.name + " doesn't have enough stamina to use " + player1.ability2.name
                display_text(text, text1)
            elif player1.ability2.health_cost >= player1.current_health:
                text = player1.name + " doesn't have enough health to use " + player1.ability2.name
                display_text(text, text1)
            else:
                attack(player1, enemy, player1.ability2)
            combat_sound.rewind()
            combat_sound.play()
        elif ( (position[0] >= 600) and (position[0] <= 750) )  and ( (position[1] >= 180) and (position[1] <= 205) ):
            if player1.ability3.mana_cost >= player1.current_mana: 
                text = player1.name + " doesn't have enough mana to use " + player1.ability3.name
                display_text(text, text1)
            elif player1.ability3.stamina_cost >= player1.current_stamina:
                text = player1.name + " doesn't have enough stamina to use " + player1.ability3.name
                display_text(text, text1)
            elif player1.ability3.health_cost >= player1.current_health:
                text = player1.name + " doesn't have enough health to use " + player1.ability3.name
                display_text(text, text1)
            else:
                attack(player1, enemy, player1.ability3)
            combat_sound.rewind()
            combat_sound.play()   
    if combatover_toggle == True:
        starting_music.play()
        if ( (position[0] >= 400) and (position[0] <= 530) )  and ( (position[1] >= 60) and (position[1] <= 105) ):
            option_click_sound.rewind()
            option_click_sound.play()
            combatover_toggle = False
            fight_text_toggle = False
            show_enemy_toggle = False
            player_main_options_toggle = True
            combat_restore_timer.stop()
            reset_hp_all()

def travel_yes(location):
    global enemy, player1
    random_number = random.randrange(0, 4)
    enemy = characters_array[random_number]
   
    reset_hp_all()
    clear_text(text1)
     
    option_click_sound.rewind()
    option_click_sound.play()
   
    
    
    
    
    
def creation(name):
    global cookie, taba, candy, kono, player1, aoi, kane
    character_array = ["Cookie", "Taba", "Candy", "Kono", "Aoi", "Kane"]
    character_array1 = ["Cookie", "Taba", "Candy", "Kono", "Aoi", "Kane"]
    cookie = ""
    taba = ""
    candy = ""
    kono = ""
    player1 = ""
    aoi = ""
    kane = ""

    for x in character_array:
        if x == name:
            if name == "Cookie":
                player1_img = cookie_img
            elif name == "Taba":
                player1_img = taba_img
            elif name == "Aoi":
                player1_img = aoi_img
            elif name == "Kane":
                player1_img = kane_img
            elif name == "Candy":
                player1_img = candy_img
            elif name == "Kono":
                player1_img = kono_img
            player1 = Character(name, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), player1_img)
            character_array1.remove(name)
            for x in character_array1:
                if x == "Cookie":
                    cookie = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), cookie_img)
                    characters_array.append(cookie)
                elif x == "Taba":
                    taba = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), taba_img)
                    characters_array.append(taba)
                elif x == "Candy":
                    candy = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), candy_img)
                    characters_array.append(candy)
                elif x == "Kane":
                    kane = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), kane_img)
                    characters_array.append(kane)
                elif x == "Kono":
                    kono = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), kono_img)
                    characters_array.append(kono)
                elif x == "Aoi":
                    aoi = Character(x, "melee", random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.randrange(3, 10), random.choice(basic_attacks), random.choice(ability1_attacks), random.choice(ability2_attacks), random.choice(ability3_attacks), aoi_img)
                    characters_array.append(aoi)
 




                    
                    


def character_creation():
        global player_info_toggle
  
   
        if cookie_toggle:
            name = "Cookie"
        if taba_toggle:
            name = "Taba"
        elif kane_toggle:
            name = "Kane"
        elif candy_toggle:
            name = "Candy"
        elif kono_toggle:
            name = "Kono"
        elif aoi_toggle:
            name = "Aoi"
        creation(name)
        player_info_toggle = True
        toggle_off()


def draw_handler(canvas):
    
        if combatover_toggle == True:
             canvas.draw_text("Travel", [400, 100], 50, "White")
             canvas.draw_text("Flirt", [600, 100], 50, "White")
            
    
        if fight_text_toggle == True:
            for x in range(len(text1)):
                canvas.draw_text(str(text1[x]), [500, 300 + (20 * x)], 12, "gold")
        if text2_toggle == True:
            for x in range(len(text2)):
                canvas.draw_text(str(text2[x]), [50, 300 + (20 * x)], 12, "gold")
            
            
        if fight_text_toggle == True and combat_toggle == True:
            canvas.draw_text(player1.default_attack.name, [600, 100], 30, "White")
            canvas.draw_text(player1.ability1.name, [600, 135], 30, "White")
            canvas.draw_text(player1.ability2.name, [600, 170], 30, "White")
            canvas.draw_text(player1.ability3.name, [600, 205], 30, "White")
           
            
    
        if player_main_options_toggle == True:
            
            canvas.draw_text("Travel", [250, 100], 70, "Blue")
            canvas.draw_text("Science Lab", [100, 250], 50, "White")
            canvas.draw_text("Cat Cafe", [400, 250], 50, "White")
            canvas.draw_text("Aquarium", [100, 350], 50, "White")
            canvas.draw_text("Train Tracks", [400, 350], 50, "White")
            canvas.draw_text("Arcade", [250, 450], 50, "White")
            
            
    
        if stats_toggle == True:
        
            canvas.draw_text( ("Strength: " + str(player1.strength)), [920, 20], 12, "Cyan")
            canvas.draw_text( ("Intelligence: " + str(player1.intelligence)), [920, 35], 12, "Cyan")
            canvas.draw_text(  ( "Wisdom: " + str(player1.wisdom) ), [920, 50], 12, "Cyan")
            canvas.draw_text( ( "Agility: " + str(player1.agility) ), [920, 65], 12, "Cyan")
            canvas.draw_text( ( "Dexterity: " + str(player1.dexterity) ), [920, 80], 12, "Cyan")
            canvas.draw_text( ( "Class: " + str(player1.archtype) ), [920, 95], 12, "Cyan")


        canvas.draw_text(title, [150, 50], 40, "Blue")
        
        
        
        if show_enemy_toggle == True:
            canvas.draw_image(enemy.image, (enemy.image.get_width() / 2, enemy.image.get_height() / 2), (enemy.image.get_width(), enemy.image.get_height() ), (50, 50), (100, 100) )
            canvas.draw_text( ("Name: " + enemy.name), [15, 140], 20, "Gold")
            canvas.draw_text( ("Health: " + str(enemy.current_health) + "/" + str(enemy.health)), [15, 160], 20, "Green")
            canvas.draw_text( ("Mana: " + str(enemy.current_mana) + "/" + str(enemy.mana) ), [15, 180], 20, "Blue")
            canvas.draw_text( ("Stamina: " + str(enemy.current_stamina) + "/" + str(enemy.stamina) ), [15, 200], 20, "Yellow")
            canvas.draw_text( ("Level: " + str(enemy.level) ), [15, 220], 20, "Cyan")
        
        
        if select_flirt_fight_toggle == True: 
            canvas.draw_text("Travel", [400, 100], 50, "White")
            canvas.draw_text("Fight", [400, 200], 50, "White")
            canvas.draw_text("Flirt", [400, 300], 50, "White")
           

        
        if player_info_toggle == True:
            canvas.draw_image(player1.image, (player1.image.get_width() / 2, player1.image.get_height() / 2), (player1.image.get_width(), player1.image.get_height() ), (850, 50), (100, 100) )
            canvas.draw_text( ("Name: " + player1.name), [800, 140], 20, "Gold")
            canvas.draw_text( ("Health: " + str(player1.current_health) + "/" + str(player1.health)), [800, 160], 20, "Green")
            canvas.draw_text( ("Mana: " + str(player1.current_mana) + "/" + str(player1.mana) ), [800, 180], 20, "Blue")
            canvas.draw_text( ("Stamina: " + str(player1.current_stamina) + "/" + str(player1.stamina) ), [800, 200], 20, "Yellow")
            canvas.draw_text( ("Level: " + str(player1.level) ), [800, 220], 20, "Cyan")
            canvas.draw_text( ("Exp to next level: " + str(player1.experience_to_level) ), [800, 240], 20, "Purple")
            

        if new_game_toggle == False:
            canvas.draw_text("Click on the 'New Game' button to begin a new game.", [100, 300], 40, "White")

        if choose_character_toggle == True:
             for x in range(len(images) - 3):
                    canvas.draw_image(images[x], (images[x].get_width() / 2, images[x].get_height() / 2), (images[x].get_width(), images[x].get_height() ), ( (200 + (250 * x)), 200), (200, 200) )


             for x in range(len(images) - 3):
                    canvas.draw_image(images[x + 3], (images[x + 3].get_width() / 2, images[x + 3].get_height() / 2), (images[x + 3].get_width(), images[x + 3].get_height() ), ( (200 + (250 * x)), 450), (200, 200) )



        if character_info_toggle == True:
            if candy_toggle:
                info("Candy Legrue", "17", "Lacrosse", candy_bio[0], candy_bio[1], candy_bio[2], candy_bio[3], candy_bio[4], candy_bio[5], candy_bio[6], candy_bio[7], candy_bio[8], candy_bio[9], candy_bio[10], candy_bio[11], candy_bio[12], images[0], canvas)

            elif kane_toggle:
                info("Kane Grundan", "17", "Basketball", kane_bio[0], kane_bio[1], kane_bio[2], kane_bio[3], kane_bio[4], kane_bio[5], kane_bio[6], kane_bio[7], kane_bio[8], kane_bio[9], kane_bio[10], kane_bio[11], kane_bio[12], images[3], canvas)


            elif taba_toggle:
                info("Taba Otto", "16", "Soccer", taba_bio[0], taba_bio[1], taba_bio[2], taba_bio[3], taba_bio[4], taba_bio[5], taba_bio[6], taba_bio[7], taba_bio[8], taba_bio[9], taba_bio[10], taba_bio[11], taba_bio[12], images[4], canvas)
            elif aoi_toggle:
                info("Aoi Notoko", "15", "Horse Riding", aoi_bio[0], aoi_bio[1], aoi_bio[2], aoi_bio[3], aoi_bio[4], aoi_bio[5], aoi_bio[6], aoi_bio[7], aoi_bio[8], aoi_bio[9], aoi_bio[10], aoi_bio[11], aoi_bio[12], images[1], canvas)
            elif kono_toggle:
                info("Kono Mayoko", "17", "Kendo", kono_bio[0], kono_bio[1], kono_bio[2], kono_bio[3], kono_bio[4], kono_bio[5], kono_bio[6], kono_bio[7], kono_bio[8], kono_bio[9], kono_bio[10], kono_bio[11], kono_bio[12], images[2], canvas)
            elif cookie_toggle:
                 info("Cookie", "15", "baking", cookie_bio[0], cookie_bio[1], cookie_bio[2], cookie_bio[3], cookie_bio[4], cookie_bio[5], cookie_bio[6], cookie_bio[7], cookie_bio[8], cookie_bio[9], cookie_bio[10], cookie_bio[11], cookie_bio[12],  images[5], canvas)

def info(name, age, hobbies, bio, bio1, bio2, bio3, bio4, bio5, bio6, bio7, bio8, bio9, bio10, bio11, bio12, image, canvas):
    global title
    canvas.draw_text( ("Return to character select menu"), [600, 50], 30, "White")
    canvas.draw_image(heartkey, (heartkey.get_width() / 2, heartkey.get_height() / 2), (heartkey.get_width(), heartkey.get_height() ), (575, 40), (40, 40) )

    canvas.draw_text( ("Choose " + name), [600, 550], 30, "White")
    canvas.draw_image(heart, (heart.get_width() / 2, heart.get_height() / 2), (heart.get_width(), heart.get_height() ), (575, 540), (40, 40) )
    canvas.draw_text( ("About " + name), [500, 150], 40, "Blue")


    canvas.draw_text( ("Name: " + name), [100, 450], 20, "Blue")
    canvas.draw_text( ("Age: " + age), [100, 500], 20, "Blue")
    canvas.draw_text( ("Hobbies: " + hobbies), [100, 550], 20, "Blue")
    canvas.draw_image(image, (image.get_width() / 2, image.get_height() / 2), (image.get_width(), image.get_height() ), (200, 200), (300, 300) )
    title = ""
    canvas.draw_text( bio, [365, 195], 20, "Blue")
    canvas.draw_text( bio1, [365, 215], 20, "Blue")
    canvas.draw_text( bio2, [365, 235], 20, "Blue")
    canvas.draw_text( bio3, [365, 255], 20, "Blue")
    canvas.draw_text( bio4, [365, 295], 20, "Blue")
    canvas.draw_text( bio5, [365, 315], 20, "Blue")
    canvas.draw_text( bio6, [365, 335], 20, "Blue")
    canvas.draw_text( bio7, [365, 355], 20, "Blue")
    canvas.draw_text( bio8, [365, 395], 20, "Blue")
    canvas.draw_text( bio9, [365, 415], 20, "Blue")
    canvas.draw_text( bio10, [365, 435], 20, "Blue")
    canvas.draw_text( bio11, [365, 455], 20, "Blue")
    canvas.draw_text( bio12, [365, 475], 20, "Blue")


    
        

def toggle_off():
    global player_info_toggle, candy_toggle, kane_toggle, taba_toggle, cookie_toggle, kono_toggle, aoi_toggle
    candy_toggle = False
    kane_toggle = False
    taba_toggle = False
    cookie_toggle = False
    kono_toggle = False
    aoi_toggle = False
    

def stats():
    global stats_toggle
    if character_chosen: 
        if stats_toggle == True:
            stats_toggle = False
        elif stats_toggle == False:
            stats_toggle = True
    
        
def enemy_combat():
    
    choice = random.choice([enemy.default_attack, enemy.ability1, enemy.ability2, enemy.ability3])
    for x in range(4):                       
        if (choice.mana_cost >= enemy.current_mana) or (choice.stamina_cost >= enemy.current_stamina) or (choice.health_cost >= enemy.current_health):    
            choice = random.choice([enemy.default_attack, enemy.ability1, enemy.ability2, enemy.ability3])
    if (choice.mana_cost >= enemy.current_mana) or (choice.stamina_cost >= enemy.current_stamina) or (choice.health_cost >= enemy.current_health):                               
        return  
    else:    
         attack(enemy, player1, choice)
                                   
def restoring(character):
    
    if (character.current_health < character.health) and character.current_health != 0:
        if (character.health - character.current_health) <= 8:
            character.current_health = character.health
        else:
            character.current_health += 8
    
    if (character.current_mana < character.mana) and character.current_health != 0:
        if (character.mana - character.current_mana) < 8:
            character.current_mana = character.mana
        else:
            character.current_mana += 8 
    if (character.current_stamina < character.stamina) and character.current_health != 0:
        if (character.stamina - character.current_stamina) < 8:
            character.current_stamina = character.stamina
        else:
            character.current_stamina += 8 
    if character.current_health >= character.health:
        character.current_health = character.health
    if character.current_mana >= character.mana:
        character.current_mana = character.mana
    if character.current_stamina >= character.stamina:
        character.current_stamina = character.stamina
                                   
def restore():
    restoring(enemy)
    restoring(player1)
    
def reset_hp(character):
    global player1, enemy
    character.current_health = character.health
    character.current_mana = character.mana
    character.current_stamina = character.stamina
    
def reset_hp_all():
    
    for x in characters_array:
        reset_hp(x)
    reset_hp(enemy)
    reset_hp(player1)
                                  
                                   
frame = simplegui.create_frame("Jason's Coursera Game Prototype", 1000, 600)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)
button1 = frame.add_button('New Game', new_game, 100)
character_stats_button = frame.add_button('Stats', stats, 100)
combat_timer1 = simplegui.create_timer(1500, enemy_combat)
combat_restore_timer = simplegui.create_timer(5000, restore)                                   
                                 

frame.start()

