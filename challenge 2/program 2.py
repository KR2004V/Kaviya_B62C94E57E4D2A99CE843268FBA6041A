#create objects of both theBatsman and Bowler classes and call the play method for each object
class player:
  def play(self):
    print("The player is play cricket")
class Batsman(player):
  def play(self):
    print("The batsman is batting")
class Bowler (player):
  def play(self):
    print("The bowler is bowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()