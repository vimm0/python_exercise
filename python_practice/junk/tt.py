import urwid as u

class game:
  count1 = 0
  count2 = 0
  def __init__(self,count1,count2):
      self.count1 = count1
      self.count2 = count2

  def count_one(self, count1):
    i = 0
    for x in range(1,count1):
      print(self.count1)
      i = i + 1

  def count_two(self, count2):
    j = 0
    for x in range(1,count2):
      print(self.count2)
      j = j + 1

#   def __init__(self, name, address):
#       self.name = name
#       self.address = address
#
#   def prnt_char(self):
#       print(self.name + self.address)
#
#reg1 = game('Sabita','Gothatar')
#reg2 = game('Ravina','Naya Thimi')
#
#reg1.prnt_char()

g = game(0,0)
g.count_one(0)
g.count_one(2)
g.count_one(3)
g.count_one(4)
g.count_one(5)
g.count_two(2)
