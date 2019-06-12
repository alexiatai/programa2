import os
from peewee import *

class Produto (BaseModel):
    nome = CharField()

class Carrinho(BaseModel):
    nome = CharField()

class Item (BaseModel):
    produto =  ForeignKeyField (Produto)
    Carrinho = ForeignKeyField (Carrinho)

class BaseModel(Model):
    class = Meta:
        database = db

melancia = Produto.create(nome = "Melancia")
carrinho = Carrinho.create(nome = "Carrinho")
item = Item.create(produto=melancia, carrinho = carrinho)
