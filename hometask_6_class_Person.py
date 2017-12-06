class Person():

    def __init__(self, age, first_name, second_name, birthday_month):
         self.age = age
         self.first_name = first_name
         self.second_name = second_name
         self.birthday_month = birthday_month
    
    def f_name(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

        summ = first_name + " " + second_name
        return summ
      


body = Person(age = '18', first_name = 'Pedro', second_name = 'Villalobos', birthday_month = 'Marth')
print body.age, body.first_name, body.second_name, body.birthday_month
print body.f_name("Pedro", "Villalobos")
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

