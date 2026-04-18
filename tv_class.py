# Task 4: Create a TV class to control channel and volume settings.
class TV:
  def __init__(self):
    self.channel = 1
    self.volume = 1
    self.on = False

  def turnOn(self):
    self.on = True
  
  def turnOff(self):
    self.on = False
  
  def channelUp(self):
    if self.on:
      if self.channel < 120:
        self.channel += 1
  
  def channelDown(self):
    if self.on:
      if self.channel > 0:
        self.channel -= 1
      
  def volumeUp(self):
    if self.on:
      if self.volume < 7:
        self.volume += 1
  
  def volumeDown(self):
    if self.on:
      if self.volume > 0:
        self.volume -= 1
  
  def setChannel(self, x):
    if self.on:
      if 1 <= x <= 120:
        self.channel = x
      
tv = TV()

tv.turnOn()
tv.channelUp()
tv.channelUp()
tv.channelDown()
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeDown()
tv.setChannel(18)

print(tv.channel)  
print(tv.volume)  