#experimental
import sys
import time
import random
import climage
import inquirer
from blessed import Terminal
CDHit1 = True
CDHit2 = True
CDHit3 = True
CDBarrageDMG = True
CDDMG = True
CDDMG2 = True
HP = 100
ThugHP = 100
Rage = 1
Pain = 1
Venom = 1
RageCD = 2
PainCD = 0
PainSens = 1
RageCount = 1

term = Terminal()

def RageUse():
  global Rage
  global RageCD
  global CDHit1
  global CDHit2
  global CDHit3
  global CDDMG
  global CDDMG2
  global CDBarrageDMG
  global RageCount
  if Rage < 2 and RageCD > 1:
    CDHit1 *= 1
    CDHit2 *= 1
    CDHit3 *= 1
    CDDMG *= 1
    CDDMG2 *= 1
    CDBarrageDMG *= 1
  elif Rage >= 2 and RageCD > 0:
    Rage = 2
    CDHit1 *= 2
    CDHit2 *= 2
    CDHit3 *= 2
    CDDMG *= 2
    CDDMG2 *= 1
    CDBarrageDMG *= 2
  elif Rage >= 2 and RageCD <= 0:
    Rage = 1
    RageCD = 10

def Rageis2():
  global Rage
  if Rage >= 2:
    Rage = 2

def Venomis8():
  global Venom
  if Venom >= 8:
    Venom = 8

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
  ThugHP -= CDHit1
  Rage += .05
  Rageis2()
  print(term.red("-" + str(round(CDHit1, 2))))
  time.sleep(0.5)
  ThugHP -= CDHit2
  Rage += .05
  Rageis2()
  print(term.red("-" + str(round(CDHit2, 2))))
  time.sleep(0.5)
  ThugHP -= CDHit3
  Rage += .05
  Rageis2()
  print(term.red("-" + str(round(CDHit3, 2))))
  time.sleep(0.5)
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.5)
  if Rage >= 2 and RageCD <= 2 and CDHit1 >= 10 or CDHit2 >= 10 or CDHit3 >= 10:
    RageCD -= 1
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)
  if RageCD <= 0:
    RageCD = 10
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")
  time.sleep(1)

def barrage_CD():
  global ThugHP
  global Rage
  global RageCD
  global CDBarrageDMG
  for a in range(20):
    CDBarrageDMG = round(random.uniform(0.5, 0.75), 3)
    if Rage >= 2 and RageCD > 0:
      CDBarrageDMG *= 2
    ThugHP -= CDBarrageDMG
    print(term.red("-" + str(round(CDBarrageDMG, 3))))
    time.sleep(0.1)
  time.sleep(1)
  if Rage < 2 and RageCD > 2:
    ThugHP -= 3.75
    Rage += 0.02
    print(term.red("-3.75"))
  elif Rage < 2 and RageCD <= 2:
    ThugHP -= 3.5
    Rage += 0.02
    print(term.red("-3.75"))
  elif Rage >= 2 and RageCD <= 2:
    ThugHP -= 7.5
    Rage += 0.04
    print(term.red("-7.5"))
    RageCD -= 1
  Rage += 0.3
  Rageis2()
  time.sleep(1)
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(1)
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)
  if RageCD <= 0:
    RageCD = 10
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")

def bearing_shot():
  global ThugHP
  global Rage
  global RageCD
  global BulletOdds
  global CDDMG
  global CDDMG2
  print("The bullet fires!")
  time.sleep(0.5)
  RageUse()
  BulletOdds = random.randint(1,3)
  if BulletOdds != 3:
    CDDMG = round(random.uniform(7, 14), 2)
    if Rage < 2 and RageCD >= 2:
      CDDMG *= 1
      Rage += 0.075
    elif Rage >= 2 and RageCD <= 2:
      CDDMG *= 2
    ThugHP -= round(CDDMG, 2)
    Rageis2()
    print(term.red("-" + str(round(CDDMG, 2))))
    print(term.orange("Your rage is ", str(round(Rage, 2))))
  else:
    print("The bullet missed!")
  time.sleep(1)
  print("The bullet comes back!")
  time.sleep(1)
  CDDMG2 = round(random.uniform(3.75, 14), 2)
  if Rage < 2 and RageCD > 2:
    CDDMG2 *= 1
  elif Rage >= 2 and RageCD <= 2:
    CDDMG2 *= 2
    RageCD -= 1
  ThugHP -= round(CDDMG2, 2)
  Rage += 0.8
  Rageis2()
  print(term.red("-" + str(round(CDDMG2, 2))))
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  RageUse()
  time.sleep(1)
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)
  time.sleep(1)
  if RageCD <= 0:
    RageCD = 10
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")

def Heal():
  global ThugHP
  ThugHP = 100
  print("Dude, do you are have the stupid?\nYou just healed the thug back to 100 HP.")
  time.sleep(2.5)
  if ThugHP > 0:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)
  else:
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))

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
  GEHit1 = round(random.uniform(5, 8), 1)
  GEHit2 = round(random.uniform(5, 8), 1)
  GEHit3 = round(random.uniform(5, 8), 1)
  GEHit1 *= Pain
  ThugHP -= GEHit1
  print(term.red("-" + str(round(GEHit1, 1))))
  time.sleep(0.5)
  GEHit2 *= Pain
  ThugHP -= GEHit2
  print(term.red("-" + str(round(GEHit2, 1))))
  time.sleep(0.5)
  GEHit3 *= Pain
  ThugHP -= GEHit3
  print(term.red("-" + str(round(GEHit3, 1))))
  time.sleep(0.5)
  if PainCD > 0:
   PainCD -= 1
  if ThugHP <= 0:
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    PainCD = 0
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)

def barrage_GE():
  global ThugHP
  global PainCD
  if PainCD < 10:
    Pain = 1
  else:
    Pain = 1.5
  for a in range (20):
    GEBarrageDMG = round(random.uniform(0.5, 1.25), 2)
    GEBarrageDMG *= Pain
    ThugHP -= GEBarrageDMG
    print(term.red("-" + str(round(GEBarrageDMG, 3))))
    time.sleep(0.1)
  time.sleep(1)
  if Pain == 1:
    ThugHP -= 3.75
    print(term.red("-3.75"))
  elif Pain == 1.5:
    ThugHP -= 5.5
    print(term.red("-5.5"))
  time.sleep(1)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    PainCD = 1
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)

def Sand_Ant_Spray():
  global ThugHP
  global DMG
  global PainCD
  if PainCD < 10:
    Pain = 1
  else:
    Pain = 1.5
  print("You throw the sand")
  time.sleep(1)
  print("It turns into ants")
  time.sleep(1)
  print("The ants bite")
  time.sleep(1)
  GEDMG = round(random.uniform(11,22), 1)
  GEDMG *= Pain
  ThugHP -= GEDMG
  print(term.red("-" + str(round(GEDMG, 2))))
  time.sleep(1)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print("He has HP 0 left")
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    PainCD = 1
    time.sleep(2)
  else:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)

def Pain_Sens():
  if PainCheck() == True:
    global ThugHP
    global GEDMG
    global PainTime
    global Pain
    global PainCD
    print("You punch the enemy")
    time.sleep(1)
    ThugHP -= 7.5
    print(term.red("-7.5"))
    time.sleep(1)
    Pain = 1.5
    print("Damage has been increased")
    time.sleep(1)
    if PainCD == 0:
     PainCD = 10
    if ThugHP <= 0:
      print("He has HP 0 left")
      print(term.webgreen("You had ", str(round(HP)), "HP left"))
      PainCD = 0 
      time.sleep(2)
    else:
      print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
      time.sleep(2)
  else:
    print("You have", str(PainCD) + " moves left")

def Shoot():
  global ThugHP
  global ShotChance1
  global ShotChance2
  global Shot1DMG
  global Shot2DMG
  global Venom
  ShotChance1 = random.randint(1,20)
  ShotChance2 = random.randint(1,20)
  Shot1DMG = round(random.uniform(3, 3.8), 1)
  Shot2DMG = round(random.uniform(3, 3.8), 1)
  if ShotChance2 >= 1 and ShotChance2 <= 8:
    #Left Leg
    Shot1DMG *= Venom
    ThugHP -= Shot1DMG
    Venom += 0.25
    Venomis8()
    print(term.red("-" + str(round(Shot1DMG, 1))))
  elif ShotChance2 >= 9 and ShotChance2 <= 16:
    #Left Arm
    Shot1DMG *= Venom
    ThugHP -= Shot1DMG
    Venom += 0.375
    Venomis8()
    print(term.red("-" + str(round(Shot1DMG, 1))))
  elif ShotChance1 >= 17 and ShotChance1 <= 19:
    #Torso
    Shot1DMG *= Venom
    Shot1DMG *= 1.5
    ThugHP -= Shot1DMG
    Venom += 0.75
    Venomis8()
    print(term.red("-" + str(round(Shot1DMG, 1))))
  else:
    #Head
    Shot1DMG *= Venom
    ThugHP = 0
    print(term.red("Headshot!"))
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
  time.sleep(0.5)
  if ShotChance1 != 20:
    if ShotChance2 >= 1 and ShotChance2 <= 8:
      #Legs
      Shot2DMG *= Venom
      ThugHP -= Shot2DMG
      Venom += 0.25
      Venomis8()
      print(term.red("-" + str(round(Shot2DMG, 1))))
    elif ShotChance2 >= 9 and ShotChance2 <= 16:
      #Arms
      Shot2DMG *= Venom
      ThugHP -= Shot2DMG
      Venom += 0.375
      Venomis8()
      print(term.red("-" + str(round(Shot2DMG, 1))))
    elif ShotChance2 == 17 or ShotChance2 == 18 or ShotChance2 == 19:
      #Torso
      Shot2DMG *= Venom
      Shot2DMG *= 1.5
      ThugHP -= Shot2DMG
      Venom += 0.75
      Venomis8()
      print(term.red("-" + str(round(Shot2DMG, 1))))
    else:
      #Head
      ThugHP = 0
      print(term.red("Headshot!"))
      print(term.yellow("He has 0 HP left"))
      print(term.webgreen("You had ", str(round(HP)), "HP left"))
  time.sleep(1)
  if ThugHP > 0:
    print(term.yellow("He has ", str(round(ThugHP, 2)), "HP left"))
    time.sleep(2)

thugshot = ['HeadBonk', 'Hit']

def Thugshot():
  global ThugHP
  global HP
  global Rage
  global RageCount
  shot = random.choice(thugshot)
  print("The thug goes for the kill")
  time.sleep(1)
  if shot == 'HeadBonk':
    HP -= 20
    print("The bat hits your head")
    time.sleep(1)
    print(term.red("-20"))
    time.sleep(1)
    Rage += 0.15
    Rageis2()
    if ability == 'CD':
      print(term.orange("Your rage is ", str(round(Rage, 2))))
    if HP > 0:
      print(term.webgreen("You have ", str(round(HP, 1)), "HP left"))
      time.sleep(1)
    else:
      print("Y O U  D I E D")
      time.sleep(2)
      sys.exit()
  if shot == 'Hit':
    for a in range(2):
      ThugDMG = round(random.uniform(7.5, 12))
      HP -= ThugDMG
      Rage += 0.07
      Rageis2()
      print(term.red("-" + str(round(ThugDMG, 2))))
      if ability == 'CD':
        print(term.orange("Your rage is ", str(round(Rage, 2))))
      time.sleep(1)
    if HP > 0:
      print(term.webgreen("You have ", str(round(HP, 1)), "HP left"))
      time.sleep(1)
    else:
      print("Y O U  D I E D")
      time.sleep(2)
      sys.exit()

power = ['CUSTOMHEAL'] 

#'SPTW', 'CUSTOMPOWER', 'CUSTOMPOWER2', 'LIMBLOSS','ICEMELT', 'MIH', 'CUSTOMSPEED', 'CUSTOMSPEED2', 'GERKC'
print("Not Finished, I just want to make a good game")
name = input('My name is ')
print("I,", name + """, have a dream. My dream is to kill bossu. \nSomeone that sells drugs to anyone who pays. Don't do drugs kids. \nOr else you might join the Italian Mafia.""")
print("""\nWoah what a weird house, doesn't look like anyone will shoot me with an arrow that looks golden.
Oh look, I got shot with an arrow that's golden.""")
ability = random.choice(power)
if ability == 'CD':
  print("\nLiterally God himself: You now have the ability to heal or fix anything else but yourself, including objects.\nThis affects your abilities.")
elif ability == 'GE':
  print("\nLiterally God himself: You can now grow organic materials out of inorganic materials and heal yourself.\nThis affects your abilities.")
elif ability == 'CUSTOMHEAL':
  print("\nLiterally God himself: You can now shoot a venom dart that when it hits, the limb that is hit loses function and loses blood \nto that limb and can ricochet until it hits its target. \nYou can also now heal yourself, but after a cooldown for a healing syrum dart. \nThis affects your abilities.")
#elif ability == 'SPTW':
#  print("\nLiterally God himself: You can now stop time for five relative seconds and use it to your advantage with extreme core power.\nThis affects your abilities.")
#elif ability == 'CUSTOMPOWER':
#  print("\nLiterally God himself: You can expose others to concentrated and immedeate radiation effects and fine radioactive sand. \nThe radiation can be healed overtime if there is no exposure after 30 seconds.\nThis affects your abilities.")
#elif ability == 'CUSTOMPOWER2':
#  print("\nLiterally God himself: You can now form objects using your imagination that is also limited by the will of your fighting spirit.\nThis affects your abilities.")
#elif ability == 'LIMBLOSS':
#  print("\nLiterally God himself: Whenever you touch an opponent's limb, you can control it in any way you want, \nyou can even make their limb lose function and blood.\nThis affects your abilities.")
#elif ability == 'ICEMELT':
#  print("\nLiterally God himself: The closer opponents are to you, the more your opponents melt until they are dead.\nThis affects your abilities.")
#elif ability == 'MIH':
#  print("\nLiterally God himself: Travel at almost infinite speed at an infinite acceleration rate. You have limited core power, though.\nThis affects your abilities.")
#elif ability == 'CUSTOMSPEED':
#  print("\nLiterally God himself: Make others travel at a high speed (100mph to 300 mph) uncontrollably if you touch them.\nThis affects your abilities.")
#elif ability == 'CUSTOMSPEED2':
#  print("\nLiterally God himself: You can only control objects near you to travel at the speed of a bullet to your opponent.\nThis affects your abilities.")
#elif ability == 'GERKC':
#  print("\nLiterally God himself: You can revert time by at most 24 hours and skip time by at most 10 minutes.\nThis affects your abilities.")
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
        time.sleep(2)
        sys.exit()
    elif moves == 'Barrage':
      barrage_CD()
      RageUse()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
    elif moves == 'Double Bearing Shot':
      bearing_shot()
      RageUse()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
    elif moves == 'Heal?':
      Heal()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
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
        time.sleep(2)
        sys.exit()
    elif moves == 'Barrage':
      barrage_GE()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
    elif moves == 'Sand-Ant Spray':
      Sand_Ant_Spray()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
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
        time.sleep(2)
        GE()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
  if ThugHP <= 0:
    print("And then there's thug, he's dead.\n\nDK. THE THUG IS DEAD.")
elif ability == 'CUSTOMHEAL':
  def CUSTOMHEAL():
    global HP
  while ThugHP > 0:
    moves = ask('What do you want to do?', ['Shoot'])
    if moves == 'Shoot':
      Shoot()
      if ThugHP > 0:
        Thugshot()
  if ThugHP <= 0:
    print("And then there's thug, he's dead.\n\nDK. THE THUG IS DEAD.")