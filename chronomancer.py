#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Wizard                             #
#                                     #
# Adds Wizard abilities to randomly   #
#  generated character                #
#######################################

import random, csv, os

#--------------------------------------
# Return the amount of experience
#  points a character has based on
#  level
#--------------------------------------
def getChronomancer_XP(my_level):
    wizard_table = [0,3000,6000,12000,24000,48000,72000,105000,160000,285000,425000,\
        850000,1235000,1610000,1985000,2370000,2755000,3140000,3525000,3910000]

    my_xp = chronomancer_table[my_level - 1]

    return my_xp

def getTemporalRaider_XP(my_level):
    temporalraider_table = [0,3500,7000,14000,28000,55000,110000,220000,400000,840000,1280000,\
        1720000,2160000,2600000,3040000,3480000,3920000,4360000,4800000,5240000]

    my_xp = temporalraider_table[my_level - 1]

    return my_xp

def getTemporalChampion_XP(my_level):
    temporalchampion_table = [0,4000,8000,16000,30000,60000,120000,200000,350000,700000,1000000,\
        1500000,2000000,25000000,3000000,4000000,45000000,5000000,5500000,6000000]

    my_xp = temporalchampion_table[my_level - 1]

    return my_xp

#--------------------------------------
# Return the casting level and number
#  of chronomancer spells a chronomancer has
#  based on level
#--------------------------------------
def Chronomancer_Spells(my_level):
    chronomancer_spell_table = [\
        # Level 1
        [1,0,0,0,0,0,0,0,0],\
        # Level 2
        [1,0,0,0,0,0,0,0,0],\ 
        # Level 3
        [1,1,0,0,0,0,0,0,0],\
        # Level 4
        [2,1,0,0,0,0,0,0,0],\
        # Level 5
        [3,1,1,0,0,0,0,0,0],\
        # Level 6
        [3,1,1,0,0,0,0,0,0],\
        # Level 7
        [3,2,1,1,0,0,0,0,0],\
        # Level 8
        [3,2,2,1,0,0,0,0,0],\
        # Level 9
        [3,2,2,1,1,0,0,0,0],\
        # Level 10
        [3,3,2,1,1,0,0,0,0],\
        # Level 11
        [3,3,3,2,2,0,0,0,0],\
        # Level 12
        [3,3,3,3,3,1,0,0,0],\
        # Level 13
        [4,4,4,3,3,1,0,0,0],\
        # Level 14
        [4,4,4,3,3,1,1,0,0],\
        # Level 15
        [4,4,4,4,4,1,1,0,0],\
        # Level 16
        [4,4,4,4,4,2,1,1,0],\
        # Level 17
        [4,4,4,4,4,2,2,1,0],\
        # Level 18
        [4,4,4,4,4,2,2,1,1],\
        # Level 19
        [4,4,4,4,4,2,2,2,1],\
        # Level 20
        [4,4,4,4,4,3,2,2,1]]
    
    return chronomancer_spell_table[my_level - 1]

def TemporalRaider_Spells(my_level):
    temporal-raider_spell_table = [\
        # Level 1
        [1,0,0,0,0,0,0,0,0],
        # Level 2
        [1,0,0,0,0,0,0,0,0],\ 
        # Level 3
        [1,1,0,0,0,0,0,0,0],\
        # Level 4
        [2,1,0,0,0,0,0,0,0],\
        # Level 5
        [3,1,1,0,0,0,0,0,0],\
        # Level 6
        [3,1,1,0,0,0,0,0,0],\
        # Level 7
        [3,2,1,1,0,0,0,0,0],\
        # Level 8
        [3,3,2,1,1,0,0,0,0],\
        # Level 9
        [3,2,2,1,1,0,0,0,0],\
        # Level 10
        [3,3,2,1,1,0,0,0,0],\
        # Level 11
        [3,3,3,2,2,1,0,0,0],\
        # Level 12
        [3,3,3,3,3,1,0,0,0],\
        # Level 13
        [4,4,4,3,3,1,0,0,0],\
        # Level 14
        [4,4,4,3,3,1,1,0,0],\
        # Level 15
        [4,4,4,4,4,1,1,0,0],\
        # Level 16
        [4,4,4,4,4,2,1,1,0],\
        # Level 17
        [4,4,4,4,4,2,2,1,0],\
        # Level 18
        [4,4,4,4,4,2,2,1,1],\
        # Level 19
        [4,4,4,4,4,2,2,2,1],\
        # Level 20
        [4,4,4,4,4,3,2,2,1]]
    
    return temporal-raider_spell_table[my_level - 1]

def TemporalChampion_Spells(my_level):
    temporal-champion_spell_table = [\
        # Level 1
        [1,0,0,0,0,0,0,0,0],
        # Level 2
        [1,0,0,0,0,0,0,0,0],\ 
        # Level 3
        [1,1,0,0,0,0,0,0,0],\
        # Level 4
        [2,1,0,0,0,0,0,0,0],\
        # Level 5
        [2,1,1,0,0,0,0,0,0],\
        # Level 6
        [2,1,1,0,0,0,0,0,0],\
        # Level 7
        [2,2,1,1,0,0,0,0,0],\
        # Level 8
        [2,2,2,1,0,0,0,0,0],\
        # Level 9
        [2,2,2,1,1,0,0,0,0],\
        # Level 10
        [2,2,2,1,1,0,0,0,0],\
        # Level 11
        [2,2,2,2,2,0,0,0,0],\
        # Level 12
        [2,2,2,2,2,1,0,0,0],\
        # Level 13
        [3,3,3,2,2,1,0,0,0],\
        # Level 14
        [3,3,3,2,2,1,1,0,0],\
        # Level 15
        [3,3,3,3,3,1,1,0,0],\
        # Level 16
        [3,3,3,3,3,2,1,1,0],\
        # Level 17
        [3,3,3,3,3,2,2,1,0],\
        # Level 18
        [3,3,3,3,3,2,2,1,1],\
        # Level 19
        [3,3,3,3,3,2,2,2,1],\
        # Level 20
        [3,3,3,3,3,2,2,2,1]]
    
    return temporal-champion_spell_table[my_level - 1]

#--------------------------------------
# Randomly assign a specialist school
#  for a wizard
#--------------------------------------
def Chronomancer_Specialist(my_race, scores):
    specialist_table = [['Abjurer','Abjuration','Alteration and Illusion'],\
        ['Conjurer','Conjuration/Summoning','Greater Divination and Invocation'],\
        ['Diviner','Greater Divination','Conjuration/Summoning'],\
        ['Enchanter','Enchantment/Charm','Invocation/Evocation and Necromancy'],\
        ['Illusionist','Illusion','Necromancy, Invocation/Evocation, and Abjuration'],\
        ['Invoker','Invocation/Evocation','Enchantment/Charm and Conjuration/Summoning'],\
        ['Necromancer','Necromancy','Illusion and Enchantment/Charm'],\
        ['Transmuter','Alteration','Abjuration and Necromancy']]
    
    my_specialist_table = []

    if my_race == 'Human':
        if scores[4] > 14:
            my_specialist_table.append(specialist_table[0])
        if scores[1] > 15:
            my_specialist_table.append(specialist_table[4])
        if scores[2] > 15:
            my_specialist_table.append(specialist_table[5])
        if scores[4] > 15:
            my_specialist_table.append(specialist_table[6])
    if my_race == 'Half-Elf' or my_race == 'Human':
        if scores[2] > 14:
            my_specialist_table.append(specialist_table[1])
        if scores[1] > 14:
            my_specialist_table.append(specialist_table[7])
    if my_race == 'Elf' or my_race == 'Half-Elf' or my_race == 'Human':
        if scores[4] > 15:
            my_specialist_table.append(specialist_table[2])
    if my_race == 'Elf' or my_race == 'Half-Elf' or my_race == 'Human':
        if scores[5] > 15:
            my_specialist_table.append(specialist_table[3])        

    if not my_specialist_table:
        return ['Mage','General','None']
    else:
        return random.choice(my_specialist_table)

#--------------------------------------
# Randomly select spells for a wizard,
#  taking into account specialization
#  if assigned
#--------------------------------------
def getWizardSpells(my_class, school, spellsByLevel):
    # If a wizard of some type, randomly select and print out spells
    #   only allocating the number it is possible to cast at their level,
    #   not allocating all they could possibly know (max spells per level, etc.)
    if "Mage" in my_class or my_class == 'Bard':
        # Read random spells from PH, stored in wizard_spells.csv, put in list
        with open("wizard_spells.csv") as f:
            reader = csv.reader(f, delimiter=",")
            spells = list(reader)
        # Randomly select spells from list, minding max number of spells allowed
        #   to memorize, by level, and store to new list
        my_spells = []
        count = spellsByLevel[0]
        while count > 0: # 1st level spells
            spell_pick = random.randint(1,45)    # 45 possible 1st level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(1,45)
            my_spells.append(spells[spell_pick])
            count -= 1
        count = spellsByLevel[1]
        while count > 0: # 2nd level spells
            spell_pick = random.randint(46,88)    # 43 possible 2nd level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(46,88)
            my_spells.append(spells[spell_pick])
            count -= 1
        count = spellsByLevel[2]
        while count > 0: # 3rd level spells
            spell_pick = random.randint(89,124)    # 36 possible 3rd level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(89,124)
            my_spells.append(spells[spell_pick])
            count -= 1
        count = spellsByLevel[3]
        while count > 0: # 4th level spells
            spell_pick = random.randint(125,166)    # 42 possible 4th level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(126,167)
            my_spells.append(spells[spell_pick])
            count -= 1
        count = spellsByLevel[4]
        while count > 0: # 5th level spells
            spell_pick = random.randint(167,206)    # 40 possible 5th level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(167,206)
            my_spells.append(spells[spell_pick])
            count -= 1
        count = spellsByLevel[5]
        while count > 0: # 6th level spells
            spell_pick = random.randint(207,246)    # 40 possible 6th level spells, pick 1
            while spells[spell_pick] in my_spells: # Don't pick already picked spell
                spell_pick = random.randint(208,247)
            my_spells.append(spells[spell_pick])
            count -= 1
        if "Mage" in my_class:
            count = spellsByLevel[6]
            while count > 0: # 7th level spells
                spell_pick = random.randint(247,272)    # 26 possible 7th level spells, pick 1
                while spells[spell_pick] in my_spells: # Don't pick already picked spell
                    spell_pick = random.randint(248,273)
                my_spells.append(spells[spell_pick])
                count -= 1
            count = spellsByLevel[7]
            while count > 0: # 8th level spells
                spell_pick = random.randint(273,294)    # 22 possible 8th level spells, pick 1
                while spells[spell_pick] in my_spells: # Don't pick already picked spell
                    spell_pick = random.randint(273,294)
                my_spells.append(spells[spell_pick])
                count -= 1
            count = spellsByLevel[8]
            while count > 0: # 9th level spells
                spell_pick = random.randint(295,312)    # 18 possible 9th level spells, pick 1
                while spells[spell_pick] in my_spells: # Don't pick already picked spell
                    spell_pick = random.randint(295,312)
                my_spells.append(spells[spell_pick])
                count -= 1
        
    if "Illusionist" in my_class or my_class == "Wizard":
            # Read random spells from PH, stored in wizard_spells.csv, put in list
            with open("wizard_spells.csv") as f:
                reader = csv.reader(f, delimiter=",")
                spells = list(reader)
            # Randomly select spells from list, minding max number of spells allowed
            #   to memorize and school of magic, by level, and store to new list
            # Prefer spells from own school and disallow spells from opposition school
            my_spells = []
            count = spellsByLevel[0]
            spec_spells = 0
            for i in range(1,45):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 1st level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(1,45)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(1,45)    # 45 possible 1st level spells, pick 1
                    this_school = spells[spell_pick][2]  # Store current spell school
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(1,45)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[1]
            spec_spells = 0
            for i in range(46,88):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 2nd level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(46,88)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(46,88)    # 43 possible 2nd level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(46,88)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[2]
            spec_spells = 0
            for i in range(89,124):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 3rd level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(89,124)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(89,124)    # 36 possible 3rd level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(89,124)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[3]
            spec_spells = 0
            for i in range(125,166):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 4th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(125,166)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(125,166)    # 42 possible 4th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(125,166)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[4]
            spec_spells = 0
            for i in range(167,206):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 5th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(167,206)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(167,206)    # 40 possible 5th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(167,206)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[5]
            spec_spells = 0
            for i in range(207,246):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 6th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(207,246)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(207,246)    # 40 possible 6th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(207,246)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[6]
            spec_spells = 0
            for i in range(247,272):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 7th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(247,272)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(247,272)    # 26 possible 7th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(247,272)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[7]
            spec_spells = 0
            for i in range(273,294):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 8th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(273,294)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(273,294)    # 22 possible 8th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(274,295)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
            count = spellsByLevel[8]
            spec_spells = 0
            for i in range(295,312):   # find number of specialist school spells available
                if school[1] in spells[i][2]:
                    spec_spells += 1
            while count > 0: # 9th level spells
                if spec_spells > 0: # pick from specialist school if spells available
                    r = random.randint(295,312)
                    if school[1] in spells[r][2]:
                        if spells[r] not in my_spells:
                            my_spells.append(spells[r])
                            spec_spells -= 1
                            count -= 1
                else:
                    spell_pick = random.randint(295,312)    # 18 possible 9th level spells, pick 1
                    this_school = spells[spell_pick][2]
                    # Don't pick already picked spell or a spell in the opposition school
                    while spells[spell_pick] in my_spells or school[2] in this_school:
                        spell_pick = random.randint(295,312)
                        this_school = spells[spell_pick][2]
                    my_spells.append(spells[spell_pick])
                    count -= 1
    return my_spells

#--------------------------------------
# Print Wizard Spells to screen
#--------------------------------------
def printWizardSpells(my_class,my_spells):

    print('\n------------------------\nWizard Spells:\n\n')
    print('1st Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '1':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    print('\n\n2nd Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '2':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    print('\n\n3rd Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '3':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    print('\n\n4th Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '4':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    print('\n\n5th Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '5':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    print('\n\n6th Level:')
    for i in range(0,len(my_spells)):
        if my_spells[i][0] == '6':
            print('\n\n' + str(my_spells[i][1]))
            print('\n(' + str(my_spells[i][2]) + ')\n')
            print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
            print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
            print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
            print('\n' + str(my_spells[i][9]))
    if "Bard" not in my_class:
        print('\n\n7th Level:')
        for i in range(0,len(my_spells)):
            if my_spells[i][0] == '7':
                print('\n\n' + str(my_spells[i][1]))
                print('\n(' + str(my_spells[i][2]) + ')\n')
                print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
                print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
                print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
                print('\n' + str(my_spells[i][9]))
        print('\n\n8th Level:')
        for i in range(0,len(my_spells)):
            if my_spells[i][0] == '8':
                print('\n\n' + str(my_spells[i][1]))
                print('\n(' + str(my_spells[i][2]) + ')\n')
                print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
                print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
                print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
                print('\n' + str(my_spells[i][9]))
        print('\n\n9th Level:')
        for i in range(0,len(my_spells)):
            if my_spells[i][0] == '9':
                print('\n\n' + str(my_spells[i][1]))
                print('\n(' + str(my_spells[i][2]) + ')\n')
                print('Range: ' + str(my_spells[i][3]) + '\tComponents: ' + str(my_spells[i][4]))
                print('Duration: ' + str(my_spells[i][5]) + '\tCasting Time: ' +str(my_spells[i][6]))
                print('Area of Effect: ' + str(my_spells[i][7]) + '\tSaving Throw: ' + str(my_spells[i][8]))
                print('\n' + str(my_spells[i][9]))
        print('\n\n')

#--------------------------------------
# Print Wizard Spells to CSV
#--------------------------------------
def csvWizardSpells(my_spells,my_name,my_level):

    # Print spell list to character sheet directory
    my_dir = 'Level_' + str(my_level) + '_2E_Character_Sheets'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, my_dir)
    try:
        os.makedirs(path, exist_ok= True)
    except OSError as error:
        print("Directory '%s' can not be created.\n" % my_dir)

    name2 = os.path.join(path, my_name)

    with open(name2 + '_Wizard_Spell_List.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Level","Name","School","Range","Components","Duration","Casting Time",\
            "Area of Effect","Saving Throw","Description"])
        writer.writerows(my_spells)
