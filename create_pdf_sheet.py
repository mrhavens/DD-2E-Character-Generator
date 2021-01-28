#######################################
# AD&D 2nd Edition                    #
# Random Character Generator:         #
#  Wizard                             #
#                                     #
# Adds Wizard abilities to randomly   #
#  generated character                #
#######################################

import random, sys, getopt, os
from _classData import *

def printMultiClassFighter(yPos):
            my_xp, S_Att_R, Att_R, followers = classData('Fighter', my_level, my_race, scores, my_armor)
            canvas.drawString(30,720,'Fighter Class')
            canvas.drawString(30,yPos-30,'Experience Points: ' + str(my_xp))
            canvas.drawString(30,yPos-60,'Specialist Attacks/Round:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(180,yPos-60,'Melee')
            canvas.drawString(215,yPos-60,'Light X-bow')
            canvas.drawString(285,yPos-60,'Heavy X-bow')
            canvas.drawString(355,yPos-60,'Thrown Dagger')
            canvas.drawString(425,yPos-60,'Thrown Dart')
            canvas.drawString(495,yPos-60,'Other Missiles(not bow)')
            canvas.drawString(180,yPos-75,str(S_Att_R[0]))
            canvas.drawString(215,yPos-75,str(S_Att_R[1]))
            canvas.drawString(285,yPos-75,str(S_Att_R[2]))
            canvas.drawString(355,yPos-75,str(S_Att_R[3]))
            canvas.drawString(425,yPos-75,str(S_Att_R[4]))
            canvas.drawString(495,yPos-75,str(S_Att_R[5]))
            canvas.setFont('Helvetica', 12)
            canvas.drawString(30,yPos-100,'Non-Specialist Attacks/Round: ' + str(Att_R))
            canvas.drawString(30,yPos-130,'Followers:')
            canvas.setFont('Helvetica', 8)
            canvas.drawString(40,yPos-145,'Leader:')
            canvas.drawString(130,yPos-145,str(followers[0]))
            canvas.drawString(40,yPos-165,'Troops (0th-level):')
            canvas.drawString(130,yPos-170,str(followers[1]))
            canvas.drawString(40,yPos-190,'Elite Units:')
            canvas.drawString(130,yPos-190,str(followers[2]))
            canvas.setFont('Helvetica', 12)
            canvas.line(30,yPos-200,580,yPos-200)
            return yPos-200