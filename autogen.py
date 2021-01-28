import os

allowedClasses = ['Fighter', 'Ranger', 'Paladin', 'Wizard', 'Mage', 'Illusionist', 'Priest', 'Cleric', 'Druid', 'Thief', 'Bard', 'Fighter/Thief', 'Fighter/Cleric', 'Fighter/Druid', 'Fighter/Mage', 'Fighter/Illusionist', 'Fighter/Mage/Cleric', 'Fighter/Mage/Cleric', 'Fighter/Mage/Druid', 'Fighter/Mage/Thief', 'Cleric/Illusionist', 'Cleric/Mage', 'Cleric/Thief', 'Cleric/Ranger', 'Illusionist/Thief', 'Mage/Thief', 'Druid/Mage']
allowedRaces = ['Human', 'Elf', 'Half-Elf', 'Dwarf', 'Halfling', 'Gnome', 'Half-Orc']
allowedLevels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
programName = '2E_character_generator.py'

for characterLevel in allowedLevels:
    commandStringLevelDirectory = 'Pregenerated_Player_Characters_Level-' + characterLevel
    os.system('mkdir ' + commandStringLevelDirectory)
    for characterRace in allowedRaces:
        for characterClass in allowedClasses:
            commandString = 'python ' + programName + ' -c ' + characterClass + ' -l ' + characterLevel + ' -r ' + characterRace + ' -n 200'
            os.system(commandString)
            commandString = 'move 2E_Character_Sheets ' + commandStringLevelDirectory + '\/Level_' + characterLevel + '_' + characterRace.upper() + '_' + characterClass.replace('/','-')
            os.system(commandString)