import sys
import time
import random
import inquirer
from blessed import Terminal
LeftArm = False
RightArm = False
LeftLeg = False
RightLeg = False
Torso = False
Head = False
CDHit1 = True
CDHit2 = True
CDHit3 = True
CDBarrageDMG = True
CDDMG = True
Pain = True
RageCD = 2
PainCD = 1
HP = 100
ThugHP = 100
Melt = 0
Rage = 1
PainSens = 1
RageCount = 1

term = Terminal()

def RageCDCheck():
  global RageCD
  global CDHit1
  global CDHit2
  global CDHit3
  if RageCD > 2 and Rage >= 2:
    if CDHit1 > 17:
      CDHit1 /= 2
    if CDHit2 > 17:
      CDHit2 /= 2
    if CDHit3 > 17:
      CDHit3 /= 2

def RageCDRemoval():
  global RageCD
  if Rage == 0:
    RageCD = 10
  elif RageCD > 2 and Rage >= 2:
    RageCD -= 1
  elif RageCD == 2 and Rage < 2:
    RageCD = 2
  elif RageCD == 1 and Rage < 2:
    RageCD = 10

def RageUse():
  global Rage
  global RageCD
  global CDHit1
  global CDHit2
  global CDHit3
  global CDDMG
  global CDBarrageDMG
  global RageCount
  if Rage < 2 and RageCD > 1:
    CDHit1 *= 1
    CDHit2 *= 1
    CDHit3 *= 1
    CDDMG *= 1
    CDBarrageDMG *= 1
  elif Rage >= 2 and RageCD > 1:
    Rage = 2
    CDHit1 *= 2
    CDHit2 *= 2
    CDHit3 *= 2
    CDDMG *= 2
    CDBarrageDMG *= 2
    RageCount += 1
  elif Rage >= 2 and RageCD == 2:
    Rage = 2
    CDHit1 *= 2
    CDHit2 *= 2
    CDHit3 *= 2
    CDDMG *= 2
    CDBarrageDMG *= 2
    RageCount += 1
  elif Rage >= 2 and RageCD == 0:
    Rage = 1

def RageDivide():
  if RageCount >= 3:
    CDHit1 /= RageCount
    CDHit2 /= RageCount
    CDHit3 /= RageCount
    CDDMG /= RageCount

def PainCheck():
  global PainCD
  if PainCD == 0:
    return True
    PainCD = 0
  if PainCD > 0:
    return False
    PainCD -= 1

def ask(message, choices):
  global HP
  return inquirer.prompt([inquirer.List('',message,choices)])[""]

def punch_combo_CD():
  global HP
  global ThugHP
  global Rage
  global RageCD
  global CDHit1
  global CDHit2
  global CDHit3
  CDHit1 = round(random.uniform(5, 8.5), 1)
  CDHit2 = round(random.uniform(5, 8.5), 1)
  CDHit3 = round(random.uniform(5, 8.5), 1)
  RageUse()
  RageCDCheck()
  ThugHP -= CDHit1
  Rage += .05
  RageUse()
  print(term.red("-" + str(round(CDHit1, 2))))
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.5)
  if Rage < 2 and RageCD < 10:
    print("You need to do", str(RageCD) + " more move(s)")
  elif Rage >= 2 and RageCD == 10:
    RageCD -= 1
    RageCDCheck()
  ThugHP -= CDHit2
  Rage += .05
  RageUse()
  print(term.red("-" + str(round(CDHit2, 2))))
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.5)
  if Rage < 2 and RageCD < 10:
    CDHit3 *= 1
  elif Rage >= 2 and RageCD == 10:
    RageCDCheck()
  ThugHP -= CDHit3
  Rage += .05
  RageUse()
  print(term.red("-" + str(round(CDHit3, 2))))
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.25)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
  print("You need to do", str(RageCD) + " more move(s)")
  RageCDRemoval()

def punch_combo_GE():
  global HP
  global ThugHP
  global GEHit1
  global GEHit2
  global GEHit3
  global PainCD
  if PainCD < 10:
    Pain = 1
  else:
    Pain = 1.5
  GEHit1 = round(random.uniform(4, 7), 1)
  GEHit2 = round(random.uniform(4, 7), 1)
  GEHit3 = round(random.uniform(4, 7), 1)
  GEHit1 *= Pain
  ThugHP -= GEHit1
  print("-" + str(round(GEHit1, 1)))
  time.sleep(0.5)
  GEHit2 *= Pain
  ThugHP -= GEHit2
  print("-" + str(round(GEHit2, 1)))
  time.sleep(0.5)
  GEHit3 *= Pain
  ThugHP -= GEHit3
  print("-" + str(round(GEHit3, 1)))
  time.sleep(0.5)
  if PainCD > 0:
   PainCD -= 1
  if ThugHP <= 0:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    PainCD = 0
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)

def Shoot():
  global ThugHP
  global ShotChance1
  global Shot1DMG
  global Shot2DMG
  ShotChance1 = random.randint(1,10)
  Shot1DMG = round(random.uniform(3, 3.8), 1)
  Shot2DMG = round(random.uniform(3, 3.8), 1)
  if ShotChance1 == (1, 2):
    LeftLeg = True
    ThugHP -= Shot1DMG
    print("-" + str(round(Shot1DMG, 1)))
  elif ShotChance1 == (3, 4):
    RightLeg = True
    ThugHP -= Shot1DMG
    print("-" + str(round(Shot1DMG, 1)))
  elif ShotChance1 == (5, 6):
    LeftArm = True
    ThugHP -= Shot1DMG
    print("-" + str(round(Shot1DMG, 1)))
  elif ShotChance1 == (7, 8):
    RightArm = True
    ThugHP -= Shot1DMG
    print("-" + str(round(Shot1DMG, 1)))
  elif ShotChance1 == 9:
    Torso = True
    Shot1DMG *= 1.5
    ThugHP -= Shot1DMG
    print("-" + str(round(Shot1DMG, 1)))
  else:
    Head = True
    ThugHP = 0
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)

def barrage_CD():
  global ThugHP
  global Rage
  global RageCD
  global PainCD
  global CDBarrageDMG
  for a in range(20):
    CDBarrageDMG = round(random.uniform(0.5, 0.75), 3)
    RageUse()
    ThugHP -= CDBarrageDMG
    print(term.red("-" + str(round(CDBarrageDMG, 3))))
    Rage += 0.015
    RageUse()
    time.sleep(0.1)
  time.sleep(0.5)
  if Rage < 2:
    RageCDCheck()
    ThugHP -= 3.75
    Rage += 0.02
    print(term.red("-3.75"))
  else:
    RageCDCheck()
    ThugHP -= 7.5
    Rage += 0.04
    print(term.red("-7.5"))
  RageUse()
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.5)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
  if RageCD == 0:
    RageCD = 10
  print("You need to do", str(RageCD) + " more move(s)")
  RageCDRemoval()

def barrage_GE():
  global ThugHP
  global PainCD
  if PainCD < 10:
    Pain = 1
  else:
    Pain = 1.5
  for a in range (18):
    GEBarrageDMG = round(random.uniform(0.5, 1), 1)
    GEBarrageDMG *= Pain
    ThugHP -= GEBarrageDMG
    print("-" + str(round(GEBarrageDMG, 3)))
    time.sleep(0.1)
  time.sleep(0.5)
  if Pain == 1:
    ThugHP -= 3.75
    print("-3.75")
  elif Pain == 1.5:
    ThugHP -= 5.5
    print("-5.5")
  time.sleep(0.5)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    PainCD = 1
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)

def bearing_shot():
  global ThugHP
  global Rage
  global RageCD
  global BulletOdds
  global CDDMG
  print("The bullet fires!")
  time.sleep(0.25)
  BulletOdds = random.randint(1,3)
  if BulletOdds != 3:
    CDDMG = round(random.uniform(7, 14), 2)
    Rage += 0.075
    RageUse()
    if Rage < 2 and RageCD > 1:
      CDDMG *= 1
    elif Rage >= 2 and RageCD == 2:
      Rage = 2
    elif Rage >= 2 and RageCD == 0:
      CDDMG *= 2
      RageCD == 10
    RageCDCheck()
    ThugHP -= round(CDDMG, 2)
    print(term.red("-" + str(round(CDDMG, 2))))
    print(term.orange("Your rage is ", str(round(Rage, 2))))
  else:
    print("The bullet missed!")
  time.sleep(0.5)
  print("The bullet comes back!")
  time.sleep(0.5)
  CDDMG = round(random.uniform(3.75, 14), 2)
  RageUse()
  if Rage < 2:
    CDDMG *= 1
  else:
    if RageCD == 10:
      CDDMG *= 2
      RageCDCheck()
      RageCD -= 1
  ThugHP -= round(CDDMG, 2)
  Rage += 0.1
  print(term.red("-" + str(round(CDDMG, 2))))
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  RageUse()
  time.sleep(0.5)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
  RageCD -= 1
  if RageCD == 0:
    RageCD = 10
  print("You need to do", str(RageCD) + " more move(s)")
  RageCDRemoval()

def Sand_Ant_Spray():
  global ThugHP
  global DMG
  global PainCD
  if PainCD < 10:
    Pain = 1
  else:
    Pain = 1.5
  print("You throw the sand")
  time.sleep(0.5)
  print("It turns into ants")
  time.sleep(0.5)
  print("The ants bite")
  time.sleep(0.5)
  GEDMG = round(random.uniform(10,20), 1)
  GEDMG *= Pain
  ThugHP -= GEDMG
  print("-" + str(round(GEDMG, 2)))
  time.sleep(0.5)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print("He has HP 0 left")
    print("You had", round(HP, 1), "HP left")
    PainCD = 1
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)

def Heal():
  global ThugHP
  ThugHP = 100
  print("Dude, do you are have the stupid?\nYou just healed the thug back to 100 HP.")
  time.sleep(2.5)
  if ThugHP > 0:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
  else:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")

def Pain_Sens():
  if PainCheck() == True:
    global ThugHP
    global GEDMG
    global PainTime
    global Pain
    global PainCD
    print("You punch the enemy")
    time.sleep(0.5)
    ThugHP -= 4.5
    print(term.red("-4.5"))
    time.sleep(0.5)
    Pain = 1.5
    print("Damage has been increased")
    time.sleep(0.5)
    if PainCD == 0:
     PainCD = 10
    if ThugHP <= 0:
      print("He has HP 0 left")
      print("You had", round(HP, 1), "HP left")
      PainCD = 0 
      time.sleep(1)
    else:
      print("He has", round(ThugHP, 2), "HP left")
      time.sleep(1)
  else:
    print("You have", str(PainCD) + " moves left")
  
thugshot = ['HeadBonk', 'Hit']

def Thugshot():
  global ThugHP
  global HP
  global Rage
  global RageCount
  shot = random.choice(thugshot)
  print("The thug goes for the kill")
  time.sleep(0.5)
  if shot == 'HeadBonk':
    HP -= 20
    print("The bat hits your head")
    time.sleep(0.5)
    print(term.red("-20"))
    time.sleep(0.5)
    Rage += 0.15
    RageUse()
    if ability == 'CD':
      print(term.orange("Your rage is ", str(round(Rage, 2))))
    if HP > 0:
      print("You have", round(HP, 1), "HP left")
      time.sleep(0.5)
    else:
      print("Y O U  D I E D")
      time.sleep(1)
      sys.exit()
  if shot == 'Hit':
    for a in range(2):
      ThugDMG = round(random.uniform(7.5, 12))
      HP -= ThugDMG
      Rage += 0.07
      RageUse()
      print(term.red("-" + str(round(ThugDMG, 2))))
      if ability == 'CD':
        print(term.orange("Your rage is ", str(round(Rage, 2))))
      time.sleep(0.5)
    if HP > 0:
      print("You have", round(HP, 1), "HP left")
      time.sleep(0.5)
    else:
      print("Y O U  D I E D")
      time.sleep(1)
      sys.exit()

power = ['CD', 'GE', ] 

#'SPTW', 'CUSTOMPOWER', 'CUSTOMPOWER2', 'LIMBLOSS','ICEMELT', 'MIH', 'CUSTOMSPEED', 'CUSTOMSPEED2', 'GERKC'
print("Not Finished, I just want to make a good game")
name = input('My name is ')
print("I,", name + """, have a dream. My dream is to kill bossu. Someone that sells drugs to anyone who pays. Don't do drugs kids. \nOr else you might join the Italian Mafia.""")
print("""\nWoah what a weird house, doesn't look like anyone will shoot me with an arrow that looks golden.
Oh look, I got shot with an arrow that's golden.""")
ability = random.choice(power)
if ability == 'CD':
  print("\nLiterally God himself: You now have the ability to heal or fix anything else but yourself, including objects.")
elif ability == 'GE':
  print("\nLiterally God himself: You can now grow organic materials out of inorganic materials and heal yourself.")
elif ability == 'CUSTOMHEAL':
  print("\nLiterally God himself: You can now shoot a venom dart that when it hits, the limb that is hit loses function and loses blood \nto that limb and can ricochet until it hits its target. \nYou can also now heal yourself, but after a cooldown for a healing syrum dart.")
#elif ability == 'SPTW':
#  print("\nLiterally God himself: You can now stop time for five relative seconds and use it to your advantage with extreme core power.")
#elif ability == 'CUSTOMPOWER':
#  print("\nLiterally God himself: You can expose others to concentrated and immedeate radiation effects and fine radioactive sand. \nThe radiation can be healed overtime if there is no exposure after 30 seconds.")
#elif ability == 'CUSTOMPOWER2':
#  print("\nLiterally God himself: You can now form objects using your imagination that is also limited by the will of your fighting spirit.")
#elif ability == 'LIMBLOSS':
#  print("\nLiterally God himself: Whenever you touch an opponent's limb, you can control it in any way you want, \nyou can even make their limb lose function and blood.")
#elif ability == 'ICEMELT':
#  print("\nLiterally God himself: The closer opponents are to you, the more your opponents melt until they are dead.")
#elif ability == 'MIH':
#  print("\nLiterally God himself: Travel at almost infinite speed at an infinite acceleration rate. You have limited core power, though.")
#elif ability == 'CUSTOMSPEED':
#  print("\nLiterally God himself: Make others travel at a high speed (100mph to 300 mph) uncontrollably if you touch them.")
#elif ability == 'CUSTOMSPEED2':
#  print("\nLiterally God himself: You can only control objects near you to travel at the speed of a bullet to your opponent.")
#elif ability == 'GERKC':
#  print("\nLiterally God himself: You can revert time by at most 24 hours and skip time by at most 10 minutes.")
print("\nSo apparently some guy wants to beat you down, because you've been crippled by the arrow. Don't question.")
if ability == 'CD':
  def CD():
    global HP
  while ThugHP > 0:
    moves = ask('What do you want to do?', ['Punch Combo', 'Barrage', 'Double Bearing Shot', 'Heal?'])
    if moves == 'Punch Combo':
      punch_combo_CD()
      RageUse()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Barrage':
      barrage_CD()
      RageUse()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Double Bearing Shot':
      bearing_shot()
      RageUse()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Heal?':
      Heal()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    if ThugHP <= 0:
      print("And then there's thug, he's dead.\n\nDK. THE THUG IS DEAD.")
elif ability == 'GE':
  def GE():
    global HP
  while ThugHP > 0:
    moves = ask('What do you want to do?', ['Punch Combo', 'Barrage', 'Sand-Ant Spray', 'Pain Sensitivity'])
    if moves == 'Punch Combo':
      punch_combo_GE()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Barrage':
      barrage_GE()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Sand-Ant Spray':
      Sand_Ant_Spray()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Pain Sensitivity':
      if PainCD == 0:
        Pain_Sens()
        PainCD = 10
        if ThugHP > 0:
          Thugshot()
      else:
        PainCheck()
        print("You have", str(PainCD) + " moves left")
        time.sleep(1)
        GE()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
elif ability == 'CUSTOMHEAL':
  def CUSTOMHEAL():
    global HP
  print("WIP (and nae nae)")