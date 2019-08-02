import os 
from peewee import *

arq = receitas.db
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Ingrediente(BaseModel):
    nomeing = CharField()

class Receita(BaseModel):
    nomerec = CharField()

class IngredienteDaReceita(BaseModel):
    nomeing = ForeignKey(Ingrediente)
    nomerec = ForeignKey(Receita)
    quantidade = FloatField()
    unidade = CharField()

    def listar_receita_ingrediente()
        for rec in Receita.select():
            print("=>" +rec.nomeing)
            ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == rec)
            print("Ingredientes:")
            for ingrediente in ings: 
                print(ingrediente.ingrediente.nomeing)