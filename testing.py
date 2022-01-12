import sys
import time
import random
import inquirer
Hit1 = None
Hit2 = None
Hit3 = None
DMG = None
Pain = True
HP = 100
ThugHP = 100
Melt = 0
Rage = 1
PainSens = 1
if Rage > 2:
  Rage = 2
  RageTime = time.time() + 10
  while time.time() < RageTime:
    CDHit1 /= Rage
    CDHit2 /= Rage
    CDHit3 /= Rage
    CDDMG /= Rage
  while time.time() < RageTime:
    CDHit1 *= 2
    CDHit2 *= 2
    CDHit3 *= 2
    CDDMG *= 2
def ask(message, choices):
  global HP
  return inquirer.prompt([inquirer.List('',message,choices)])[""]
def punch_combo_CD():
  global HP
  global ThugHP
  global Rage
  global CDHit1
  global CDHit2
  global CDHit3
  CDHit1 = round(random.uniform(1,1), 1)
  CDHit2 = round(random.uniform(1,1), 1)
  CDHit3 = round(random.uniform(1,1), 1)
  CDHit1 *= Rage
  ThugHP -= CDHit1
  print("-" + str(round(CDHit1, 1)))
  Rage += .05
  time.sleep(0.5)
  CDHit2 *= Rage
  ThugHP -= CDHit2
  print("-" + str(round(CDHit2, 1)))
  Rage += .05
  time.sleep(0.5)
  CDHit3 *= Rage
  ThugHP -= CDHit3
  print("-" + str(round(CDHit3, 1)))
  Rage += .05
  time.sleep(0.25)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 1), "HP left")
    time.sleep(1)
def punch_combo_GE():
  global HP
  global ThugHP
  global GEHit1
  global GEHit2
  global GEHit3
  GEHit1 = round(random.uniform(1,1), 2)
  GEHit2 = round(random.uniform(1,1), 2)
  GEHit3 = round(random.uniform(1,1), 2)
  GEHit1 *= Pain
  ThugHP -= GEHit1
  print("-" + str(round(GEHit1, 2)))
  time.sleep(0.5)
  GEHit2 *= Pain
  ThugHP -= GEHit2
  print("-" + str(round(GEHit2, 2)))
  time.sleep(0.5)
  GEHit3 *= Pain
  ThugHP -= GEHit3
  print("-" + str(round(GEHit3, 2)))
  time.sleep(0.5)
  if ThugHP <= 0:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
def barrage_CD():
  global ThugHP
  global Rage
  for a in range (20):
    CDBarrageDMG = round(random.uniform(0.01,0.01), 2)
    CDBarrageDMG *= Rage
    ThugHP -= CDBarrageDMG
    print("-" + str(round(CDBarrageDMG, 2)))
    Rage += 0.01
    time.sleep(0.1)
  time.sleep(0.5)
  ThugHP -= 1
  print("-1")
  Rage += 0.03
  time.sleep(0.5)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
def barrage_GE():
  global ThugHP
  for a in range (18):
    GEBarrageDMG = round(random.uniform(0.01, 0.01), 2)
    GEBarrageDMG *= Pain
    ThugHP -= GEBarrageDMG
    print("-" + str(round(GEBarrageDMG, 2)))
    time.sleep(0.1)
  time.sleep(0.5)
  if Pain == 1:
    ThugHP -= 1
    print("-1")
  elif Pain == 1.5:
    ThugHP -= 1.5
    print("-1.5")
  time.sleep(0.5)
  if ThugHP <= 0:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
def bearing_shot():
  global ThugHP
  global Rage
  global BulletOdds
  global CDDMG
  print("The bullet fires!")
  time.sleep(0.25)
  BulletOdds = random.randint(1,4)
  if BulletOdds != 4:
    CDDMG = round(random.randint(1, 1), 1)
    Rage += 0.07
    CDDMG *= Rage
    ThugHP -= round(CDDMG, 1)
    print("-" + str(round(CDDMG, 1)))
  else:
    print("The bullet missed!")
  time.sleep(0.5)
  print("The bullet comes back!")
  time.sleep(0.5)
  CDDMG = round(random.randint(1,1), 1)
  CDDMG *= Rage
  ThugHP -= round(CDDMG, 1)
  print("-" + str(round(CDDMG, 1)))
  Rage += 0.08
  time.sleep(0.5)
  if ThugHP <= 0:
    Rage = 1
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 1), "HP left")
    time.sleep(1)
def Sand_Ant_Spray():
  global ThugHP
  global DMG
  print("You throw the sand")
  time.sleep(0.5)
  print("It turns into ants")
  time.sleep(0.5)
  print("The ants bite")
  time.sleep(0.5)
  GEDMG = round(random.uniform(1,1), 1)
  GEDMG *= Pain
  ThugHP -= GEDMG
  print("-" + str(round(GEDMG, 2)))
  time.sleep(0.5)
  if ThugHP <= 0:
    print("He has HP 0 left")
    print("You had", round(HP, 1), "HP left")
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
    print("He has", round(ThugHP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has 0 HP left")
    print("You had", round(HP, 1), "HP left")
def Pain_Sens():
  global ThugHP
  global GEDMG
  global PainTime
  global Pain
  ThugHP -= 1
  print("You punch the enemy")
  time.sleep(0.5)
  print("-1")
  time.sleep(0.5)
  PainTime = time.time() + 4.5
  while time.time() < PainTime:
    Pain = 1.5
    print("Damage has been increased")
  time.sleep(0.5)
  if ThugHP <= 0:
    print("He has HP 0 left")
    print("You had", round(HP, 1), "HP left")
    time.sleep(1)
  else:
    print("He has", round(ThugHP, 2), "HP left")
    time.sleep(1)
thugshot = ['HeadBonk', 'Hit']
def Thugshot():
  global ThugHP
  global HP
  global Rage
  shot = random.choice(thugshot)
  print("The thug goes for the kill")
  time.sleep(0.5)
  if shot == 'HeadBonk':
    HP -= 1
    print("The bat hits your head")
    time.sleep(0.5)
    print("-1")
    time.sleep(0.5)
    Rage += 0.2
    if HP > 0:
      print("You have", round(HP, 1), "HP left")
      time.sleep(0.5)
    else:
      print("Y O U  D I E D")
      time.sleep(1)
      sys.exit()
  if shot == 'Hit':
    for a in range(2):
      ThugDMG = round(random.uniform(1,1))
      HP -= ThugDMG
      print("-" + str(round(ThugDMG, 2)))
      Rage += 0.07
      time.sleep(0.5)
    if HP > 0:
      print("You have", round(HP, 1), "HP left")
      time.sleep(0.5)
    else:
      print("Y O U  D I E D")
      time.sleep(1)
      sys.exit()
power = ['CD', 'GE'] 
#'CUSTOMHEAL', 'SPTW', 'CUSTOMPOWER', 'CUSTOMPOWER2', 'LIMBLOSS','ICEMELT', 'MIH', 'CUSTOMSPEED', 'CUSTOMSPEED2', 'GERKC'
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
#elif ability == "CUSTOMHEAL":
#  print("\nLiterally God himself: You can now shoot a venom dart that when it hits, #the limb that is hit loses function and loses blood \nto that limb and can ricochet #until it hits its target. \nYou can also now heal yourself, but after a cooldown for a #healing syrum dart.")
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
print("\nSo apparently some guy wants to beat you down")
if ability == 'CD':
  def CD():
    global HP
  while ThugHP > 0:
    moves = ask('What do you want to do?', ['Punch Combo', 'Barrage', 'Double Bearing Shot', 'Heal?'])
    if moves == 'Barrage':
      barrage_CD()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Double Bearing Shot':
      bearing_shot()
      if ThugHP > 0:
        Thugshot()
      if HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()
    elif moves == 'Punch Combo':
      punch_combo_CD()
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
      Pain_Sens()
      if ThugHP > 0:
        Thugshot()
      elif HP <= 0:
        print("Y O U  D I E D")
        time.sleep(1)
        sys.exit()