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
CDDMG2 = True
Pain = True
RageCD = 1
PainCD = 1
HP = 100
ThugHP = 100
Rage = 1
PainSens = 1

term = Terminal()

def RageAmp():
  global Rage
  global RageCD
  global CDHit1
  global CDHit2
  global CDHit3
  global CDDMG
  global CDDMG2
  global CDBarrageDMG
  if Rage < 2 and RageCD > 1:
    CDHit1 *= 1
    CDHit2 *= 1
    CDHit3 *= 1
    CDDMG *= 1
    CDDMG2 *= 1
    CDBarrageDMG *= 1
    RageCD -= 1
  elif Rage < 2 and RageCD == 1:
    CDHit1 *= 1
    CDHit2 *= 1
    CDHit3 *= 1
    CDDMG *= 1
    CDDMG2 *= 1
    CDBarrageDMG *= 1
  elif Rage >= 2 and RageCD != 1:
    CDHit1 *= 1
    CDHit2 *= 1
    CDHit3 *= 1
    CDDMG *= 1
    CDDMG2 *= 1
    CDBarrageDMG *= 1
    Rage = 2
  elif Rage >= 2 and RageCD <= 1:
    Rage = 2
    CDHit1 *= 1.5
    CDHit2 *= 1.5
    CDHit3 *= 1.5
    CDDMG *= 2
    CDDMG2 *= 2
    CDBarrageDMG *= 2
    Rage = 2
    RageCD -= 1
  else:
    pass

def RageCheck():
  global Rage
  global RageCD
  if Rage >= 2 and RageCD <= 0:
    Rage = 1
    RageCD = 5
  else:
    pass

def Rageis2():
  global Rage
  if Rage >= 2:
    Rage = 2
  else:
    pass

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

#CD
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
  RageAmp()
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
  RageCheck()
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(0.5)
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    time.sleep(1)
  if RageCD <= 0:
    RageCD = 5
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")
  else:
    pass
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
  else:
    pass
  Rage += 0.35
  Rageis2()
  time.sleep(1)
  RageCheck()
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(1)
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    time.sleep(1)
  if RageCD <= 0:
    RageCD = 5
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")
  else:
    pass
  time.sleep(1)

def bearing_shot():
  global ThugHP
  global Rage
  global RageCD
  global BulletOdds
  global DMG
  global DMG2
  print("The bullet fires!")
  DMG = round(random.uniform(7, 14), 2)
  DMG2 = round(random.uniform(3.75, 14), 2)
  RageAmp()
  time.sleep(0.5)
  BulletOdds = random.randint(1,3)
  if BulletOdds != 3:
    Rage += 0.075
    Rageis2()
    ThugHP -= round(DMG, 1)
    print(term.red("-" + str(round(DMG, 1))))
    print(term.orange("Your rage is ", str(round(Rage, 2))))
  else:
    print("The bullet missed!")
  time.sleep(1)
  print("The bullet comes back!")
  time.sleep(1)
  ThugHP -= round(DMG2, 2)
  print(term.red("-" + str(round(DMG2, 2))))
  Rage += 0.8
  Rageis2()
  print(term.orange("Your rage is ", str(round(Rage, 2))))
  time.sleep(1)
  if ThugHP <= 0:
    Rage = 1
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    time.sleep(2)
  else:
    time.sleep(2)
  time.sleep(1)
  if RageCD <= 0:
    RageCD = 5
  if ThugHP >= 0:
    print("You need to do", str(RageCD) + " more move(s) with rage to reset your rage and its cooldown")
  else:
    pass

def Heal():
  global ThugHP
  ThugHP = 100
  print("Dude, do you are have the stupid?\nYou just healed the thug back to 100 HP.")
  time.sleep(2.5)
  if ThugHP > 0:
    time.sleep(2)
  else:
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))

#GE
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
  else:
    pass
  time.sleep(1)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print(term.yellow("He has 0 HP left"))
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    PainCD = 1
    time.sleep(2)
  else:
    time.sleep(2)

def Sand_Ant_Spray():
  global ThugHP
  global GEDMG
  global PainCD
  print("You throw the sand")
  time.sleep(0.5)
  print("It turns into ants")
  time.sleep(0.5)
  print("The ants bite")
  time.sleep(0.5)
  GEDMG = round(random.uniform(15,25), 1)
  if Pain == 1.5:
    GEDMG *= Pain
  else:
    pass
  ThugHP -= GEDMG
  print(term.red("-" + str(round(GEDMG, 1))))
  time.sleep(1)
  if PainCD > 0:
    PainCD -= 1
  if ThugHP <= 0:
    print("He has HP 0 left")
    print(term.webgreen("You had ", str(round(HP)), "HP left"))
    PainCD = 1
    time.sleep(2)
  else:
    time.sleep(2)

def Pain_Sens():
  if PainCheck() == True:
    global ThugHP
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
    PainCheck()
    if ThugHP <= 0:
      print("He has HP 0 left")
      print(term.webgreen("You had ", str(round(HP)), "HP left"))
      PainCD = 0 
      time.sleep(2)
    else:
      time.sleep(2)
  else:
    print("You have ", str(PainCD) + "moves left")

thugshot = ['HeadBonk', 'Hit']

def Thugshot():
  global ThugHP
  global HP
  global Rage
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
      time.sleep(1)
    if ability == 'CD':
      print(term.orange("Your rage is ", str(round(Rage, 2))))
    if HP > 0:
      print(term.webgreen("You have ", str(round(HP, 1)), "HP left"))
      time.sleep(1)
    else:
      print("Y O U  D I E D")
      time.sleep(2)
      sys.exit()

power = ['CD', 'GE', ] 

#'SPTW', 'CUSTOMPOWER', 'CUSTOMPOWER2', 'LIMBLOSS','ICEMELT', 'MIH', 'CUSTOMSPEED', 'CUSTOMSPEED2', 'GER'
print("Not Finished, I just want to make a good game. Use the up and down keys to select attacks.")
name = input('My name is ')
print("I,", name + """, have a dream. My dream is to kill bossu.
Someone that sells drugs to anyone who pays. Don't do drugs kids.
Or else you might join the Italian Mafia.""")
print("""\nWoah what a weird house, doesn't look like anyone will shoot me with an arrow that looks golden.
Oh look, I got shot with an arrow that's golden.""")
ability = random.choice(power)
if ability == 'CD':
  print("""\nLiterally God himself: You now have the ability to heal or fix anything else BUT yourself, including objects.
  This affects your abilities.
  
  Rage is a meter that can double your damage when it is at 2, choose your attack wisely.""")
elif ability == 'GE':
  print("""\nLiterally God himself: You can now grow organic materials out of inorganic materials and heal yourself.
  This affects your abilities.
  
  Pain is a damage multiplier for one move when activated, choose your attack wisely.""")
elif ability == 'CUSTOMHEAL':
  print("""\nLiterally God himself: You can now shoot venom darts that can ricochet until it hits its target. 
  You can also now heal yourself with them, but after a cooldown.
  This affects your abilities.
  
  Venom is a damage amplifier. The more you shoot, the higher, the better.""")
#elif ability == 'SPTW':
#  print("""\nLiterally God himself: You can now stop time for a few seconds and use it to your advantage with extreme strength.
# This affects your abilities.""")
#elif ability == 'CUSTOMPOWER':
#  print("""\nLiterally God himself: You can expose others to radiation effects and fine radioactive sand.
# The radiation can be healed overtime if there is no exposure after 30 seconds.
# This affects your abilities.""")
#elif ability == 'CUSTOMPOWER2':
#  print("""\nLiterally God himself: You can now form objects using your imagination that is also limited by the will of your fighting spirit.
# This affects your abilities.""")
#elif ability == 'LIMBLOSS':
#  print("""\nLiterally God himself: Whenever you touch an opponent's limb, you can control it in any way you want,
# you can even make their limb lose function and blood.
# This affects your abilities.""")
#elif ability == 'ICEMELT':
#  print("""\nLiterally God himself: The closer opponents are to you, the more your opponents melt until they are dead.
# This affects your abilities.""")
#elif ability == 'MIH':
#  print("""\nLiterally God himself: Travel at almost infinite speed at an infinite acceleration rate. You have limited strength, though.
# This affects your abilities.""")
#elif ability == 'CUSTOMSPEED':
#  print("""\nLiterally God himself: Make others travel at a high speed (100mph to 300 mph) uncontrollably if you touch them.
# This affects your abilities.""")
#elif ability == 'CUSTOMSPEED2':
#  print("""\nLiterally God himself: You can only control objects near you to travel at the speed of a bullet to your opponent.
# This affects your abilities.""")
#elif ability == 'GER':
#  print("""\nLiterally God himself: You can revert time by at most 24 hours.
# This affects your abilities.""")
print("\nSo apparently some guy wants to beat you down, because you've been crippled by the arrow. Don't question.")
if ability == 'CD':
  def CD():
    global HP
  while ThugHP > 0:
    moves = ask('What do you want to do?', ['Punch Combo', 'Barrage', 'Double Bearing Shot', 'Heal?'])
    if moves == 'Punch Combo':
      punch_combo_CD()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
    elif moves == 'Barrage':
      barrage_CD()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(2)
        sys.exit()
    elif moves == 'Double Bearing Shot':
      bearing_shot()
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
  print("WIP")