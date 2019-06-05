import peewee, os 
db = peewee.SqliteDatabase('animalia.db')


class Aluno(peewee.Model):
    nome = peewee.CharField()
    turma = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return self.nome+","+self.turma


class Eventos(peewee.Model):
    ano = peewee.Charfield()
    local = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return self.ano +"do evento e "+ self.local


class Area_Atuacao(peewee.Model):
    nome = peewee.Charfield()
    onde_publicar = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return "o evento "+self.nome+"acontecerá no(a)"+ self.onde_publicar


class Docente(peewee.Model):
    nome = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return "O nome do docente é "+self.nome


class Periodico(Publicação):
    editora = peewee.Charfield()
    issn = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return "Editora de publicação, "+self.editora +"o issn é, " +self.issn


class Projeto_Integrador(peewee.Model):
    titulo = peewee.Charfield()
    ano = peewee.Charfield()
    alunos = peewee.ForeignKeyField(Aluno)
    orientadores = peewee.ForeignKeyField(Docente)
class Meta:
    database = db
def __str__(self):
    return "Título de PI, "+self.titulo +"ano de criação, " +self.ano +"alunos do PI, " +self.alunos +"orientadores do PI, " +self.orientadores


class Publicação(peewee.Model):
    titulo = peewee.Charfield()
    sigla = peewee.Charfield()
class Meta:
    database = db
def __str__(self):
    return "Título da publicação, "+self.etitulo +"sigla, " +self.sigla

    


