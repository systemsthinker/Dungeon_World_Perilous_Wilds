# Perilous Wil Region Name Generator version 1
# Thomas Roberts 10-17-15

# Imports :   Dice for die rolling
import dice

# class and function defs

# function takes a list and rolls a result from that list
def dice_roller(table_list,num_dice=1):
    table_item_cnt = int(len(table_list))
    if num_dice is None:
        num_dice=1
    try:
        die_to_roll= str(num_dice) +"d" + str(table_item_cnt)
        #print(die_to_roll)
    except:
        print("dice_roller helper failed ")
        return None
    roll_real = int(dice.roll(die_to_roll)) - 1
    while roll_real > table_item_cnt-1:
        roll_real = int(dice.roll(die_to_roll)) - 1
        #print(roll_real)
    return roll_real



#helper functions
def contains_word(source, word):
    return (' ' + word + ' ') in (' ' + source + ' ')


def place(n):
    # schema
    PLACE_NAME = ["The " + PLACE_TYPE[r(PLACE_TYPE)],
                  "The " + PLACE_ADJECTIVE[dice_roller(PLACE_ADJECTIVE)] + " " + PLACE_TYPE[dice_roller(PLACE_TYPE)],
                  "The " + PLACE_ADJECTIVE[dice_roller(PLACE_ADJECTIVE)] + " " + PLACE_TYPE[dice_roller(PLACE_TYPE)],
                  "The " + PLACE_TYPE[dice_roller(PLACE_TYPE)] + " of " + PLACE_NOUN[dice_roller(PLACE_NOUN)],
                  "The " + PLACE_TYPE[dice_roller(PLACE_TYPE)] + " of " + PLACE_NOUN[dice_roller(PLACE_NOUN)],
                  PLACE_NOUN[dice_roller(PLACE_NOUN)] + "'s " + PLACE_TYPE[dice_roller(PLACE_TYPE)],
                  PLACE_TYPE[dice_roller(PLACE_TYPE)] + " of the " + PLACE_ADJECTIVE[dice_roller(PLACE_ADJECTIVE)] + " " + PLACE_NOUN[
                      dice_roller(PLACE_NOUN)],
                  PLACE_TYPE[dice_roller(PLACE_TYPE)] + " of the " + PLACE_ADJECTIVE[dice_roller(PLACE_ADJECTIVE)] + " " + PLACE_NOUN[
                      dice_roller(PLACE_NOUN)], "The " + PLACE_ADJECTIVE[dice_roller(PLACE_ADJECTIVE)] + " " + PLACE_NOUN[dice_roller(PLACE_NOUN)]]
    # print()

    i = 0
    while True:
        if i < n:
            i = i + 1
            try:
                print("   AREA")
                PLACE = PLACE_NAME[dice_roller(PLACE_NAME)]
                REGION_TAGS = (TERRAIN_TYPE[dice_roller(TERRAIN_TYPE)]) + ", " + (SAFETY_LEVEL[dice_roller(SAFETY_LEVEL)]) + ", " + (
                ALIGNMENT[dice_roller(ALIGNMENT)]) + ", "
                if contains_word(PLACE, "Village"):
                    print("     " + PLACE)
                    print("     " + VILLAGE)
                    print("     " + "Villiage Complications: ---- ")
                    print()
                else:
                    print("     " + PLACE)
                    print("     " + REGION_TAGS)
            except:
                print("error on itt PLACE")
        else:

            PLACE = []
            return None


def region():
    print("-----REGION-----")
    # todo get better random namer
    AREA_NAME = [ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)],
                 ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)],
                 ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)],
                 ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)], TERRAIN[dice_roller(TERRAIN)] + " of The " + NOUN[dice_roller(NOUN)],
                 TERRAIN[dice_roller(TERRAIN)] + " of The " + NOUN[dice_roller(NOUN)],
                 "The " + TERRAIN[dice_roller(TERRAIN)] + " " + ADJECTIVE[dice_roller(ADJECTIVE)],
                 "The " + TERRAIN[dice_roller(TERRAIN)] + " " + ADJECTIVE[dice_roller(ADJECTIVE)],
                 NOUN[dice_roller(NOUN)] + " " + TERRAIN[dice_roller(TERRAIN)], NOUN[dice_roller(NOUN)] + " " + TERRAIN[dice_roller(TERRAIN)],
                 "The " + NOUN[dice_roller(NOUN)] + "'s " + ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)],
                 "The " + ADJECTIVE[dice_roller(ADJECTIVE)] + " " + TERRAIN[dice_roller(TERRAIN)] + " of " + NOUN[dice_roller(NOUN)]]
    REGION_TITLE = (AREA_NAME[dice_roller(AREA_NAME)])
    REGION_TAGS = (TERRAIN_TYPE[dice_roller(TERRAIN_TYPE)]) + ", " + (SAFETY_LEVEL[dice_roller(SAFETY_LEVEL)]) + ", " + (
    ALIGNMENT[dice_roller(ALIGNMENT)]) + ", "
    print(REGION_TITLE)
    print(REGION_TAGS)

    return None


# function iteratates 5 times
def iterator_region(n):
    i = 0

    while True:
        if i < n:
            i = i + 1
            try:

                region()

                place(COUNT[dice_roller(COUNT)])
            except:
                print("error on itt regg")
        else:
            print("---------------------")
            return None


# Main loop of program
def main():
    iterator_region(10)


# Lists
RESOURCE = ["Gold", "Tin", "Copper", "Lumber", "Fish", "Fur", "Rare Beast", "Silver", "Iron", "Stone"]
STEADING = ["Village", "Village", "Village", "Village", "Village" "Town", "Town", "Town", "Keep", "Keep", "City"]
VILLAGE = " TAGS - Poor, Steady,Milita, Resource - " + (RESOURCE[dice_roller(RESOURCE)]) + " OATH -"
TERRAIN = ["Woods", "Wasteland", "Waste", "Wall", "Upland", "Thicket", "Teeth", "Sweep", "Swamp", "Steppe", "Sound",
           "Slough", "Sea", "Scarps", "Savanna", "Sands", "Reach", "Range", "Quagmire", "Prairie", "Plains", "Peaks",
           "Mountains", "Mounds", "Morass", "Moor", "Meadows", "Marsh", "March", "Lowland", "Lake", "Jungle", "Hollows",
           "Hills", "Heights", "Heath", "Groves", "Forest", "Foothills", "Flats", "Fen", "Fells", "Expanse", "Dunes",
           "Downs", "Desert", "Cliffs", "Bog", "Bluffs", "Bay"]
ADJECTIVE = ["Yellow", "Wicked", "White", "Umber", "Silver", "Shining", "Shifting", "Shattered", "Shadow", "Sapphire",
             "Ruby", "Red", "Queen’s", "Perilous", "Light", "King’s", "Jagged", "Iron", "Holy", "Green", "Golden",
             "Ghost", "Frozen", "Forsaken", "Forgotten", "Fire", "Fell", "Far", "Fallen", "Endless", "Emerald", "Dun",
             "Dismal", "Diamond", "Devil’s", "Desolate", "Demon’s", "Deep", "Dead", "Dark", "Cursed", "Copper",
             "Burning", "Broken", "Blue", "Blighted", "Blessed", "Black", "Ashen", "Ageless"]
NOUN = ["Witch", "Troll", "Traitor", "Thunder", "Thorn", "Sun", "Storm", "Sorrow", "Snake", "Smoke", "Sky", "Skull",
        "Silver", "Shadow", "Savior", "Regret", "Refuge", "Rain", "Queen", "Pity", "Mist", "Lost", "Light", "Life",
        "King", "Horror", "Hope", "Honor", "Hero", "Hell", "Heaven", "Gold", "God", "Giant", "Ghost", "Fury", "Fire",
        "Fear", "Fate", "Dragon", "Doom", "Devil", "Despair", "Desolation", "Death", "Dead", "Darkness", "Bone", "Ash",
        "choose_name"]
SAFETY_LEVEL = ["SAFE", "SAFE", "SAFE", "UNSAFE", "UNSAFE", "PERILOUS", "PERILOUS", "PERILOUS", "PERILOUS", "PERILOUS"]
ALIGNMENT = ["Neutral", "Neutral", "Neutral", "Neutral", "Neutral", "Neutral", "Good", "Evil", "Chaotic", "Lawful",
             "Evil", "Chaotic Evil", "Chaotic"]
PLACE_TYPE = ["Wall", "Village", "Valley", "Vale", "Tree", "Town", "Tower", "Tomb", "Throne", "Temple", "Tangle",
              "Stone", "Spring", "Spire", "Shrine", "Ruin", "Rock", "Rise", "Ring", "Ridge", "Ridge", "Post", "Pit",
              "Pile", "Meadow", "Marsh", "Lake", "Keep", "Hut", "Hole", "Hill", "Grove", "Fort", "Field", "Fence",
              "Falls", "Door", "Ditch", "Den", "Crypt", "Crossing", "Crater", "Cliff", "City", "Circle", "Cave", "Camp",
              "Bowl", "Beach", "Barrier"]
PLACE_ADJECTIVE = ["Withered", "White", "Thundering", "Thorny", "Sunken", "Stoney", "Stalwart", "Silver", "Shrouded",
                   "Shivering", "Shining", "Shifting", "Shattered", "Sharp", "Screaming", "Red", "Petrified", "Near",
                   "Low", "Lost", "Jagged", "Iron", "High", "Hidden", "Grim", "Golden", "Gloomy", "Ghostly", "Frozen",
                   "Found", "Floating", "Fearsome", "Far", "Fallen", "Endless", "Doomed", "Dead", "Dark", "Cracked",
                   "Copper", "Clouded", "Burning", "Broken", "Bright", "Bright", "Blue", "Bloody", "Black", "Ashen",
                   "Ancient", ]
PLACE_NOUN = ["Wizard", "Water", "Troll", "Thief", "Sword", "Stone", "Spirit", "Spear", "Souls", "Smoke", "Skull",
              "Silver", "Sailor", "Queen", "Murder", "Mud", "Muck", "Maiden", "Knight", "Knave", "King", "Hope", "Hero",
              "Head", "Hand", "Gold", "God", "Goblin", "Giant", "Ghost", "Foot", "Fire", "Finger", "Fighter", "Fear",
              "Eyes", "Doom", "Devil", "Demon", "Dagger", "Crystal", "Courage", "Corpse", "Cleric", "Cinder", "Child",
              "Captain", "Ash", "Arm", "[Name]*", ]
CLIMATE = ["Frigid", "Temperate", "Temperate", "Temperate", "Hot Desert", "Jungle", "Coastal Warm", "Coastal Cool"]
TERRAIN_TYPE = ["Farmland", "Mountains", "Kingdom", "Barony", "Duchy", "Tribal Lands", "Unexplored", "Accursed",
                "Wasteland", "Forested"]
OTHER_REGION_TAGS = ["", "", "", "", "", "", "", "", "", "", "", "", "Barren", "Blighted", "Civilized", "Civilized",
                     "Contested", "Contested", "Contested", "Defensible", "Enchanted",
                     "Resource - " + (RESOURCE[dice_roller(RESOURCE)])]
COUNT = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]
# Call Main loop
main()
















