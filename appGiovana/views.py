from django.shortcuts import render, redirect
from .models import Dogs
from .models import Metas

# A função home é chamada quando a página inicial é acessada
# Ela faz uma busca no banco de dados de cães e metas e retorna todos os objetos criados de cada um, que após isso são renderizados no home.html (página inicial)
def home(request): 
  meta = Metas.objects.all()
  dog = Dogs.objects.all()
  context = { "dog": dog, "meta": meta}
  return render(request, "home.html",context=context)

#Essa função é chamada quando o usuário deseja criar um novo registro de dogs
#Se a requisição for uma solicitação do tipo POST, a função cria um novo objeto "Dogs" com os dados enviados pelo usuário e salva-o no banco de dados. Em seguida, redireciona o usuário para a página inicial 
#Se a requisição for uma solicitação do tipo GET, a função simplesmente redireciona para o formulário de criação de um novo "Dog"
def create_dogs(request):
  if request.method=="POST":
    Dogs.objects.create(
    title=request.POST["nome"],
    raca=request.POST["raça"],
    idade=request.POST["idade"],
    adoção=request.POST["adoção"]
    )
    return redirect("home")  
  return render(request, "dogs_forms.html")

#Essa função tem o mesmo funcionamento da função acima, porém para criar um novo registro de metas
#Porém ela verifica se quando a função foi requisitada no metodo POST o done foi selecionado ou não, para que apareça apareça se a meta ja foi concluída ou não
def create_metas(request):
  if request.method=="POST":
    if "done" not in request.POST:
      done = False
    else:
      done = True
    Metas.objects.create(
    title=request.POST["titulo"],
    description=request.POST["descrição"],
    place=request.POST["lugar"],
    done=done
    )
    return redirect("home") 
  return render(request, "metas_forms.html")

#Essa função atualiza uma meta existente no banco de dados com base no ID da meta fornecido
#Primeiro, a função obtém a meta do banco de dados com o ID fornecido 
#Em seguida, verifica se a requisição é um método POST
#Se for um método POST, a função atualiza as informações da meta com base nos dados enviados pelo usuário no formulário 
def update_metas(request, meta_id):
  meta=Metas.objects.get(id=meta_id)
  if request.method=="POST":
    meta.title = request.POST["titulo"]
    meta.description = request.POST["descrição"]
    meta.place = request.POST["lugar"]
    if "done" not in request.POST:
      meta.done = False
    else:
      meta.done = True
    meta.save()
    return redirect("home")
  return render(request, "metas_forms.html", context={"meta": meta})

#Essa função é responsável por deletar uma meta específica do banco de dados
#Se a requisição for do tipo POST e o usuário confirmar a exclusão da meta, a função apaga a meta do banco de dados 
#Em seguida, a função redireciona o usuário para a página inicial 
def delete_metas(request, meta_id):
  meta=Metas.objects.get(id=meta_id)
  if request.method =="POST":
    if "confirm" in request.POST:
      meta.delete()
    return redirect("home")
  return render(request, "deleteMetas_forms.html", context={"meta":meta})

#Essa função tem o meesmo funcionamento do update_metas, mas para atualizar ou criar um novo cachorro
def update_dogs(request, dog_id):
  dog=Dogs.objects.get(id=dog_id)
  dog.adocao = dog.adoção.strftime('%Y-%m-%d')
  if request.method=="POST":
    dog.title = request.POST["nome"]
    dog.raca = request.POST["raça"]
    dog.idade = request.POST["idade"]
    dog.adocao = request.POST["adoção"]
    dog.save()
    return redirect("home")
  return render(request, "dogs_forms.html", context={"dog": dog})

#Essa funçao tem o mesmo funcionamento do delete_metas, mas para deletar um dog
def delete_dogs(request, dog_id):
  dog=Dogs.objects.get(id=dog_id)
  if request.method =="POST":
    if "confirm" in request.POST:
      dog.delete()
    return redirect("home")
  return render(request, "deleteDogs_forms.html", context={"dog":dog})
