import random
from datetime import datetime as dt
from datetime import timedelta as td
import pytz
from rich import print

print("""[bold dark_magenta]

 _                 _______ _________ ______  
( \      |\     /|(  ____ \\\__   __/(  __  \ 
| (      | )   ( || (    \/   ) (   | (  \  )
| |      | |   | || |         | |   | |   ) |
| |      | |   | || |         | |   | |   | |
| |      | |   | || |         | |   | |   ) |
| (____/\| (___) || (____/\___) (___| (__/  )
(_______/(_______)(_______/\_______/(______/ 
[/bold dark_magenta]                                              
-----------------------------------------------
Welcome to LUCID!
-----------------------------------------------
[bold dark_magenta]by qis[/bold dark_magenta] 
""")

now = dt.now(pytz.timezone('Asia/Kuala_Lumpur'))

def score(d):
  if d.score > 100:
    d.score = 100

def check(ans, d = None, ft = "stats", sd = "y", td = "n"):
  temp = ans
  while True:
    if temp == ft:
      print(d)
      temp = input("\n(y or n)\n")
      ft = None
    if temp == sd or temp == td:
      return temp
    else: temp = input("\ninvalid answer \n")

def enter():
  while input("") != "":
    pass

class Dream:
  def __init__(self, effect, descrip):
    self.effect = effect
    self.descrip = descrip

a = Dream(-25, "You consciously slip into a dream. \nYou find yourself in a vacant house and perform some martial arts movements to get a feel of your body. (+30 lp) \nYou decide to explore the house and spot a mirror in a room. \nYou run towards it and pass right through, falling into a disorienting abyss of mirrored illusions. (-55 lp)")
b =  Dream(-20, "You've previously filled out a university's application form. By the time you decide to submit it, you discover that the deadline has passed. \nYou blame yourself for such carelessness. (-20 lp)")
c = Dream(20, "You're being chased by the government. \nYou take an unusual turn that leads to a dead end. You achieve lucidity and call a friend for help. (+20 lp)")
d = Dream(10, "You're skiing on a piste and notice that something feels off. \nYou try to take control of the dream with minimal success. (+10 lp)")
e = Dream(45, "You decide to take a drive alone in CHERRYBOMB. \nThe traffic ahead distracts you and you crash into a child. \nYou achieve lucidity while talking to someone outside regarding the car accident and you reverse the scenario. (+45 lp)")
f = Dream(30, "You are flying in the air and notice that the view is bland. \nYou achieve lucidity and transform it into Riyadh's city skyline at dusk. (+30 lp)")
g = Dream(-50, "You are on a video call with your lover. \nYou walk towards a window and notice them on the other side. The video call ends as they notice you too, \nYou are entranced by their appeal. (-50 lp)")
h = Dream(-30, "You're looking at your skin on a mirror. You notice that that your acne is getting worse and your pores are opening up despite your best efforts at taking care of your skin. \nThis frustrates you to the point of anger. (-30 lp)")
dreams = [a, b, c, d, e, f, g, h, "d1", "d2", "d3"]

class Technique:
  def __init__(self, name, effect, rate):
    self.name = name
    self.effect = effect
    self.rate = rate

  def __repr__(self):
    return "{} \nsuccess rate: {} \n+{} lp if successful\n".format(self.name, self.rate, self.effect)
  
  def success(self):
    if random.choice(range(1, 101)) <= self.rate:
      return True
    else: return False

class Player:
  def __init__(self, name):
    self.name = name
    self.minutes = td(hours = 0, minutes = 0)
    self.score = 0
    self.counter = 0
    self.lucid = False
    self.experience = False
    self.log = False
    self.awake = False
  def __repr__(self):
    return "\nname: {} \nlucidity score: {}".format(self.name, self.score)

  def time(self):
    time = dt(1970, 1, 1) + self.minutes
    return time.strftime("%H hours and %M minutes")

  def perf_tech(self, tech):
    if tech.success() is True:
      self.score += tech.effect
      print("\nThe technique was successful. \n+{} lp".format(tech.effect))
    else: print("\nThe technique was unsuccessful")
    enter()

  def sp(self):
    if self.score <= 0:
      print("\nyour lucidity score has plunged \nyou are currently undergoing sleep paralysis\n")
      if self.experience == True:
        print("fortunately, your sleep is uninterrupted by reason of prior experience")
        self.score = 0
        enter()
      else: 
        self.awake = True
        print(dt.strftime(now + self.minutes, ("%H:%M\n")))
        print("your sleep paralysis demon assaults you. \nyou wake in fright, too petrified to return to sleep")
        print("\n" + "time slept:", self.time() + "\n\nlucid dreams:", self.counter)

  def success(self):
    if random.choice(range(1, 101))<=self.score:
      return True
    else: return False

  def singledream(self, dream):
    self.score += dream.effect
    if dream.effect > 0 or dream == a: 
      self.lucid = True
      self.counter += 1
    self.minutes += td(minutes = 15)
    self.score += 10
    print("\n" + dream.descrip + "\n\n+10 lp\n")
    score(self)
    return True

  def say(self, dreamer):
    temp = input("\n" + self.name + " says: ")
    while True:
      temp = input("\n" + dreamer.name + " says: ")
      if temp == "end": break
      temp = input("\n" + self.name + " says: ")
      if temp == "end": break
    self.score += 30
    self.score += 30
    print("\n{a} +30 lp \n{b} +30 lp".format(a = self.name, b = dreamer.name))
    enter()

  def dualdream(self, dream, dreamer):
    if dream == "d1":
      self.score += 20
      dreamer.score += 20
      score(self)
      score(dreamer)
      print("\nYou're learning acrobatic gymnastics with {b}. They repeatedly shapeshift into a little girl and back while performing twists in the air with you. You achieve lucidity when you both land and notice a sense of clarity in {b}'s eyes. \n{a} +20 lp\n\n{b} +20 lp \nTo your surprise, they ask, \"are you dreaming too?\"".format(a = self.name, b = dreamer.name))
      print("\n\n" + dreamer.name)
      enter()
      q = check(input("\nwould you like to answer? \n(y, n, stats) \n"), dreamer)
      if q == "y": 
        print("\ntype \"end\" to end the dialogue")
        dreamer.say(self)

    if dream == "d2":
      self.score += 10
      dreamer.score += 10
      score(self)
      score(dreamer)
      print("\nYou're driving {b}'s car to Dallas, away from adolescence. You stop at a 7-11 and the both of you start planning your weekend together. \n{a} +10 lp\n{b} +10 lp \n\nAfter a while, you ask, \"How is it living with your parents?\"".format(a = self.name, b = dreamer.name))
      print("\n\n" + dreamer.name)
      enter()
      q = check(input("\nwould you like to answer? \n(y, n, stats) \n"), dreamer)
      if q == "y": 
        print("\ntype \"end\" to end the dialogue")
        dreamer.say(self)

    if dream == "d3":
      self.score += 30
      dreamer.score += 30
      score(self)
      score(dreamer)
      print("\nYou fly to Paris with {b} on a private plane, pretending to be like Jackie Onassis and wearing big glasses because you're both overdramatic and the world is ending. \n{a} +30 lp\n{b} +30 lp".format(a = self.name, b = dreamer.name))
      q = check(input("\nwould you like to start a conversation? \n(y, n, stats) \n"), self)
      if q == "y": 
        print("\ntype \"end\" to end the dialogue")
        input("\n" + dreamer.name + " says: ")
        self.say(self)

    self.counter += 1
    dreamer.counter += 1
    self.minutes += td(minutes = 15)
    dreamer.minutes += td(minutes = 15)
  
    self.score += 10
    dreamer.score += 10
    print("\n{} +10 lp \n{} +10 lp".format(self.name, dreamer.name))
    self.lucid = True
    dreamer.lucid = True
    score(self)
    score(dreamer)
    return True

  def dream(self, d):
    if self.success() is False or len(dreams) == 0: 
      print("\nyou fail to achieve lucidity and dream as per usual")
      self.minutes += td(minutes = 15)
      self.score += 10
    else:
      dream = dreams.pop(dreams.index(random.choice(dreams)))
      if dream == "d1" or dream == "d2" or dream == "d3":
        if d.awake:
          while dream == "d1" or dream == "d2" or dream == "d3":
            dreams.append(dream)
            dream = dreams.pop(dreams.index(random.choice(dreams)))
          return self.singledream(dream)
        return self.dualdream(dream, d)
      else: 
        return self.singledream(dream)

  def wake(self):
    self.awake = True
    msg = ("you wake up ")
    if self.log == True: msg += "and begin logging your dreams"
    dt.strftime(now + self.minutes, ("%H:%M"))
    time = now + self.minutes
    print("\n" + self.name + dt.strftime(time, ("\n\n%H:%M")) + "\n\n" + msg + "\n\ntime slept:", self.time() + "\n\nlucid dreams:", self.counter, "\n")

A = Technique("climbing up a rope", 25, 50)
B = Technique("riding on a train through a tunnel", 30, 40)

def qis():
  print("\ngreetings, your grace\n+30 lp")
  enter()
  dreamer = Player("qis")
  dreamer.score += 30
  dreamer.experience = True
  dreamer.log = True
  return dreamer

def new(name):
  dreamer = Player(name)
  q = check(input("\ndo you have prior experience in lucid dreaming? \n(y or n) \nthere is a probability of undergoing sleep paralysis if you have no experience, proceed with caution \n"), ft = None)
  if q == "y": 
    dreamer.score += 10
    print("+10 lp")
    dreamer.experience = True
  q = check(input("\ndo you perform reality checks? \n(y or n) \n"), ft = None)
  if q == "y": 
    dreamer.score += 10
    print("+10 lp")
  q = check(input("\ndo you log your dreams? \n(y or n) \n"), ft = None)
  if q == "y":
    dreamer.log = True
    dreamer.score += 10
    print("+10 lp")
  return dreamer

def technique(d):
    q = check(input("\nwould you like to opt for a technique? \n(y, n, stats) \n"), d)
    if q == "y": 
      q = check(input("\n\ntechniques: \n\nA: " + repr(A) + "\n" + "B: " + repr(B) + "\nchoose an option \nA or B\n"), None, None, "A", "B")
      if q == "A": d.perf_tech(A)
      else: d.perf_tech(B)

print("\n" + dt.strftime(now, ("%H:%M")), "\n\n2 dreamers fall asleep")

name = input("\nplayer 1 \nwhat is your dreamer name? \n")
while name.strip() == "": 
  name = input("\nthe name can't be blank\n")
if name.strip() == "qis": dreamer1 = qis()
else: dreamer1 = new(name)
print(dreamer1)
enter()
name = input("\nplayer 2 \nwhat is your dreamer name? \n")
while name.strip() == dreamer1.name or name.strip() == "": 
  if name.strip() == "":
    name = input("\nthe name can't be blank\n")
  elif name.strip() == dreamer1.name:
    name = input("\n1 player can't dream for 2\n")
if name.strip() == "qis": dreamer2 = qis()
else: dreamer2 = new(name)
print(dreamer2)
enter()

def session1(d1, d2): 
  if d1.awake is False:
    print("\n" + d1.name)
    enter()
    d1.lucid = False
    if d1.dream(d2):
      d1.sp()
    else: 
      d1.minutes += td(minutes = 15)
      d1.score += 10
      score(d1)
      print("+20 lp")
    print(d1)
    enter()

def session2(d1, d2):
  if d1.awake is False:
    if d1.lucid is True and d1.score != 100:
      print(d1.name)
      enter()
      technique(d1)
    if d1.dream(d2):
      d1.sp()
    print(d1)
    enter()

print(dt.strftime(now + td(hours = 1, minutes = 47), ("\n%H:%M")))
dreamer1.minutes += td(hours = 1, minutes = 47)
dreamer2.minutes += td(hours = 1, minutes = 47)
enter()

if td(hours = 1, minutes = 47) == dreamer1.minutes:
  session1(dreamer1, dreamer2)
if td(hours = 2, minutes = 2) == dreamer1.minutes:
  session2(dreamer1, dreamer2)
if td(hours = 2, minutes = 17) == dreamer1.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer1.minutes = td(hours = 3, minutes = 39)
if td(hours = 1, minutes = 47) == dreamer2.minutes:
  session1(dreamer2, dreamer1)
if td(hours = 2, minutes = 2) == dreamer2.minutes:
  session2(dreamer2, dreamer1)
if td(hours = 2, minutes = 17) == dreamer2.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer2.minutes = td(hours = 3, minutes = 39)

print(dt.strftime(now + td(hours = 3, minutes = 39), ("\n%H:%M")))
enter()

if td(hours = 3, minutes = 39) == dreamer1.minutes:
  session1(dreamer1, dreamer2)
if td(hours = 3, minutes = 54) == dreamer1.minutes:
  session2(dreamer1, dreamer2)
if td(hours = 4, minutes = 9) == dreamer1.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer1.minutes = td(hours = 5, minutes = 1)
if td(hours = 3, minutes = 39) == dreamer2.minutes:
  session1(dreamer2, dreamer1)
if td(hours = 3, minutes = 54) == dreamer2.minutes:
  session2(dreamer2, dreamer1)
if td(hours = 4, minutes = 9) == dreamer2.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer2.minutes = td(hours = 5, minutes = 1)

print(dt.strftime(now + td(hours = 5, minutes = 1), ("\n%H:%M")))
enter()

if td(hours = 5, minutes = 1) == dreamer1.minutes:
  session1(dreamer1, dreamer2)
if td(hours = 5, minutes = 16) == dreamer1.minutes:
  session2(dreamer1, dreamer2)
if td(hours = 5, minutes = 31) == dreamer1.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer1.minutes = td(hours = 6, minutes = 18)
if td(hours = 5, minutes = 1) == dreamer2.minutes:
  session1(dreamer2, dreamer1)
if td(hours = 5, minutes = 16) == dreamer2.minutes:
  session2(dreamer2, dreamer1)
if td(hours = 5, minutes = 31) == dreamer2.minutes:
  print("\ndeep sleep begins")
  enter()
  dreamer2.minutes = td(hours = 6, minutes = 18)

print(dt.strftime(now + td(hours = 6, minutes = 18), ("\n%H:%M")))
enter()

if td(hours = 6, minutes = 18) == dreamer1.minutes:
  session1(dreamer1, dreamer2)
if td(hours = 6, minutes = 33) == dreamer1.minutes:
  session2(dreamer1, dreamer2)
if td(hours = 6, minutes = 48) == dreamer1.minutes:
  dreamer1.minutes = td(hours = 7, minutes = 23)
  dreamer1.wake()
if td(hours = 6, minutes = 18) == dreamer2.minutes:
  session1(dreamer2, dreamer1)
if td(hours = 6, minutes = 33) == dreamer2.minutes:
  session2(dreamer2, dreamer1)
if td(hours = 6, minutes = 48) == dreamer2.minutes:
  dreamer2.minutes = td(hours = 7, minutes = 55)
  dreamer2.wake()

print("\nthe end\n")