from django.db import models \\importa o módulo "models" do Django, que é responsável por fornecer um conjunto de classes de modelo de banco de dados

class Dogs(models.Model): \\ Essa função está criando uma classe "Dogs" que herda todos os atributos da classe base "(models.Model)"
  title= models.CharField(max_length=50) \\atribuindo um campo que possua um máximo de 50 caracteres e definido como title (que seria para o nome do chachorro)
  raca= models.CharField(max_length=30) \\atribuindo um campo que possua um máximo de 30 caracteres, para botar a raça do cachorro
  idade= models.CharField(max_length=30) \\atribuindo um campo que possua um máximo de 30 caracteres, para botar a idade do cachorro
  adoção= models.DateField() \\atribuindo um campo de data, para inserir a data de adoção

class Metas(models.Model):  \\ Essa função está criando uma classe "Metas" que herda todos os atributos da classe base "(models.Model)"
  title = models.CharField(max_length = 50) \\atribuindo um campo que possua um máximo de 50 caracteres e definido como title, para botar o título da meta
  description = models.TextField() \\atribuindo um campo que possua uma área maior para a escrita, para que seja adicionada uma descrição para a meta 
  place= models.CharField(max_length = 50) \\atribuindo um campo que possua um máximo de 50 caracteres, para inserir o lugar que a meta tem que ser cumprida
  done=models.BooleanField() \\define um campo de modelo chamado "done" que representa um valor booleano (True ou False), para identificar o estado de conclusão da meta
