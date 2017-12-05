class Boxer():
    # put your code here
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
    def kick(self):
        return "I'll kill you!"
    def pull_ups(self):
        return "I can make 50 pull_ups!!!"

Vasiliy = Boxer(height = '150', weight = '100', age = '22')
print Vasiliy.height, Vasiliy.weight, Vasiliy.age
print Vasiliy.kick()
print Vasiliy.pull_ups()
  


""" vasily = Boxer()
vasily.age
22
vasily.weight
100
vasily.height
150



vasily.kick()
"I'll kill you!!!"
vasily.pull_ups()
"I can make 50 pull-ups!!!" """
