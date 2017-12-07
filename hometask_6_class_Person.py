class Person():

    def __init__(self, age, first_name, second_name, birthday_month):
         self.age = age
         self.first_name = first_name.title()
         self.second_name = second_name.title()
         self.birthday_month = birthday_month
    
    def f_name(self):

        return self.first_name + " " + self.second_name
        
      
    def email(self):
        
        return self.first_name + "." + self.second_name + "@email.com"
        

    def season_of_birth(self):
        
        winter = ["January","Fabruary","December"]
        spring = ["March","April","May"]
        summer = ["June","July","August"]
        autumn = ["September","October","November"]
        seasons = ["winter", "spring", "summer", "autumn"]
        for s in seasons:
            if self.birthday_month in winter:
                return "winter"
            elif self.birthday_month in spring:
                return "spring"
            elif self.birthday_month in summer:
                return "summer"
            elif self.birthday_month in autumn:
                return "autumn"
            else:
                return"Error : Input correct month"




body = Person(age = '18', first_name = 'PEDRO', second_name = 'VILLIALOBOS', birthday_month = 'March')
print body.age, body.first_name, body.second_name, body.birthday_month
print body.f_name()
print body.email()
print body.season_of_birth()
"""
Person has atributes:

body = Person(age='18', first_name='Pedro', second_name='Villalobos', birthday_month='Marth')
body.age
18
body. first_name
'Pedro'
body. second_name
'Villalobos'
birthday_month.wage
'Marth'

Person has methods:

body.full_name()
'Pedro Villalobos' """

