from peewee import *

db=SqliteDatabase('cat.sqlite')

class Cat(Model):
    name =CharField()
    color=CharField()
    age= IntegerField()


    class Meta:
        database=db



    def __str__(self):
        return f'{self.name} is a {self.color}  cat and is {self.age} years old.'


db.connect()
db.create_tables([Cat])


Zoe = Cat(name='zoe',color='Ginger',age=3).save()
Holly = Cat(name='Holly',color='Tabby',age=2).save()
Fluffy = Cat(name='Fluffy ',color='Black',age=7).save()

print('\n findall cats ')

print(*Cat.select())
