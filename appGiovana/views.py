from django.shortcuts import render, redirect
from .models import Dogs
from .models import Metas

def home(request):
  meta = Metas.objects.all()
  dog = Dogs.objects.all()
  context = { "dog": dog, "meta": meta}
  return render(request, "home.html",context=context)

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

def delete_metas(request, meta_id):
  meta=Metas.objects.get(id=meta_id)
  if request.method =="POST":
    if "confirm" in request.POST:
      meta.delete()
    return redirect("home")

  return render(request, "deleteMetas_forms.html", context={"meta":meta})

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

def delete_dogs(request, dog_id):
  dog=Dogs.objects.get(id=dog_id)
  if request.method =="POST":
    if "confirm" in request.POST:
      dog.delete()
    return redirect("home")

  return render(request, "deleteDogs_forms.html", context={"dog":dog})